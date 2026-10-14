#!/usr/bin/env python3
"""Fetch Statable visitor counts for the trailing 7 days and all recorded days."""

from __future__ import annotations

import json
import os
import re
import sys
import tempfile
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SITE_ID = 3386330
QUERY_URL = "https://statable.com/api/v1/query"
SITES_URL = "https://statable.com/api/v1/sites"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "_data" / "statable_visitor_count.json"
MAX_EXPLICIT_RANGE_DAYS = 366
DATE_PATTERN = re.compile(r"\A\d{4}-\d{2}-\d{2}\Z")
COUNTRY_CODE_PATTERN = re.compile(r"\A[A-Z]{2}\Z")
COUNTRY_DIMENSION = "visit:country"
COUNTRY_LIMIT = 1000
OTHER_LOCATIONS = "Other locations"
UNKNOWN_COUNTRY_CODES = {"XX", "ZZ"}
UNKNOWN_COUNTRY_LABELS = {"", "(not set)", "n/a", "not available", "not set", "other", "unknown"}


def query_statable(api_key: str, query: dict[str, object]) -> dict[str, object]:
    body = json.dumps(query).encode("utf-8")
    request = Request(
        QUERY_URL,
        data=body,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise RuntimeError("Statable returned an unsuccessful response.")
            payload = json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"Statable request failed with HTTP {exc.code}.") from None
    except URLError:
        raise RuntimeError("Statable could not be reached.") from None
    except (TimeoutError, json.JSONDecodeError):
        raise RuntimeError("Statable returned an unreadable response.") from None

    if not isinstance(payload, dict):
        raise RuntimeError("Statable returned an unexpected response.")
    echoed_query = payload.get("query")
    if not isinstance(echoed_query, dict) or echoed_query.get("site_id") != SITE_ID:
        raise RuntimeError("Statable returned data for an unexpected site.")
    return payload


def parse_date_range(payload: dict[str, object]) -> list[str]:
    query = payload.get("query")
    date_range = query.get("date_range") if isinstance(query, dict) else None
    if (
        not isinstance(date_range, list)
        or len(date_range) != 2
        or any(not isinstance(day, str) or DATE_PATTERN.fullmatch(day) is None for day in date_range)
    ):
        raise RuntimeError("Statable returned an invalid reporting period.")
    return date_range


def parse_aggregate_count(payload: dict[str, object]) -> int:
    results = payload.get("results")
    if not isinstance(results, list) or len(results) != 1:
        raise RuntimeError("Statable returned an unexpected aggregate result.")
    metrics = results[0].get("metrics") if isinstance(results[0], dict) else None
    visitors = metrics.get("visitors") if isinstance(metrics, dict) else None
    if type(visitors) is not int or visitors < 0:
        raise RuntimeError("Statable returned an invalid visitor count.")
    return visitors


def payload_has_import(payload: dict[str, object]) -> bool:
    has_import = payload.get("has_import", False)
    if type(has_import) is not bool:
        raise RuntimeError("Statable returned invalid import metadata.")
    return has_import


def fetch_count(api_key: str, requested_range: str = "7d") -> tuple[int, list[str], bool]:
    payload = query_statable(
        api_key,
        {
            "site_id": SITE_ID,
            "metrics": ["visitors"],
            "date_range": requested_range,
        },
    )
    date_range = parse_date_range(payload)
    return parse_aggregate_count(payload), date_range, payload_has_import(payload)


def fetch_site_start_date(api_key: str) -> date:
    request = Request(
        SITES_URL,
        headers={"Accept": "application/json", "Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    try:
        with urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise RuntimeError("Statable returned an unsuccessful site-list response.")
            payload = json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"Statable site-list request failed with HTTP {exc.code}.") from None
    except URLError:
        raise RuntimeError("Statable could not be reached for site metadata.") from None
    except (TimeoutError, json.JSONDecodeError):
        raise RuntimeError("Statable returned unreadable site metadata.") from None

    sites = payload.get("sites") if isinstance(payload, dict) else None
    if not isinstance(sites, list):
        raise RuntimeError("Statable returned an unexpected site list.")
    matches = [site for site in sites if isinstance(site, dict) and site.get("site_id") == SITE_ID]
    if len(matches) != 1:
        raise RuntimeError("Statable did not return exactly one matching site.")
    start_value = matches[0].get("stats_start_date")
    if not isinstance(start_value, str) or DATE_PATTERN.fullmatch(start_value) is None:
        raise RuntimeError("Statable has no valid first-data date for this site.")
    try:
        return date.fromisoformat(start_value)
    except ValueError:
        raise RuntimeError("Statable returned an invalid first-data date.") from None


def fetch_all_time_count(api_key: str, end_value: str) -> tuple[int, list[str]]:
    start_date = fetch_site_start_date(api_key)
    try:
        end_date = date.fromisoformat(end_value)
    except ValueError:
        raise RuntimeError("Statable returned an invalid end date for the all-time count.") from None
    if start_date > end_date:
        raise RuntimeError("Statable's first-data date is later than the reporting end date.")

    # The API caps explicit ranges at 366 days. Sum disjoint ranges; this is exact
    # for native Statable data because its visitor identity resets every day.
    visitors_all_time = 0
    imported_data = False
    current_start = start_date
    while current_start <= end_date:
        current_end = min(current_start + timedelta(days=MAX_EXPLICIT_RANGE_DAYS - 1), end_date)
        requested_range = [current_start.isoformat(), current_end.isoformat()]
        payload = query_statable(
            api_key,
            {"site_id": SITE_ID, "metrics": ["visitors"], "date_range": requested_range},
        )
        if parse_date_range(payload) != requested_range:
            raise RuntimeError("Statable returned a different period for an all-time count segment.")
        visitors_all_time += parse_aggregate_count(payload)
        imported_data = imported_data or payload_has_import(payload)
        current_start = current_end + timedelta(days=1)

    if imported_data:
        raise RuntimeError("The all-time range overlaps imported data, so segment counts cannot be safely combined.")
    return visitors_all_time, [start_date.isoformat(), end_date.isoformat()]


def fetch_country_breakdown(api_key: str, date_range: list[str]) -> list[dict[str, int | str]]:
    rows: list[object] = []
    offset = 0
    total_rows: int | None = None

    while True:
        payload = query_statable(
            api_key,
            {
                "site_id": SITE_ID,
                "metrics": ["visitors"],
                "date_range": date_range,
                "dimensions": [COUNTRY_DIMENSION],
                "limit": COUNTRY_LIMIT,
                "offset": offset,
            },
        )
        if parse_date_range(payload) != date_range:
            raise RuntimeError("Statable returned a different reporting period for the location breakdown.")

        page_rows = payload.get("results")
        meta = payload.get("meta")
        if not isinstance(page_rows, list) or not isinstance(meta, dict):
            raise RuntimeError("Statable returned an unexpected location breakdown.")

        page_total = meta.get("total")
        page_limit = meta.get("limit")
        page_offset = meta.get("offset")
        has_more = meta.get("has_more")
        if (
            type(page_total) is not int
            or page_total < 0
            or type(page_limit) is not int
            or page_limit < 1
            or type(page_offset) is not int
            or page_offset != offset
            or type(has_more) is not bool
            or len(page_rows) > page_limit
        ):
            raise RuntimeError("Statable returned invalid location pagination metadata.")
        if total_rows is None:
            total_rows = page_total
        elif total_rows != page_total:
            raise RuntimeError("Statable changed the location breakdown while it was being read.")

        rows.extend(page_rows)
        if not has_more:
            break
        if not page_rows:
            raise RuntimeError("Statable returned an empty location page while more rows were expected.")
        offset += page_limit

    if total_rows != len(rows):
        raise RuntimeError("Statable returned an incomplete country breakdown.")

    country_counts: dict[str, dict[str, int | str]] = {}
    other_visitors = 0
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError("Statable returned an invalid country row.")
        dimensions = row.get("dimensions")
        labels = row.get("labels")
        metrics = row.get("metrics")
        code_value = dimensions.get(COUNTRY_DIMENSION) if isinstance(dimensions, dict) else None
        name_value = labels.get(COUNTRY_DIMENSION) if isinstance(labels, dict) else None
        visitors = metrics.get("visitors") if isinstance(metrics, dict) else None
        if type(visitors) is not int or visitors < 0:
            raise RuntimeError("Statable returned an invalid country visitor count.")

        code = code_value.strip().upper() if isinstance(code_value, str) else ""
        name = name_value.strip() if isinstance(name_value, str) else ""
        if code in {"CN", "HK", "MO", "TW"}:
            code = "CN"
            name = "China"
        unknown_location = (
            not COUNTRY_CODE_PATTERN.fullmatch(code)
            or code in UNKNOWN_COUNTRY_CODES
            or name.casefold() in UNKNOWN_COUNTRY_LABELS
        )
        if unknown_location:
            other_visitors += visitors
            continue

        if code not in country_counts:
            country_counts[code] = {"name": name, "visitors": 0}
        country_counts[code]["visitors"] = int(country_counts[code]["visitors"]) + visitors

    country_rows = list(country_counts.values())
    if other_visitors:
        country_rows.append({"name": OTHER_LOCATIONS, "visitors": other_visitors})
    country_rows.sort(key=lambda item: (-int(item["visitors"]), str(item["name"]).casefold()))

    largest_country_count = max((int(item["visitors"]) for item in country_rows), default=0)
    for item in country_rows:
        visitors = int(item["visitors"])
        item["bar_percent"] = (
            min(100, max(4, round(visitors * 100 / largest_country_count)))
            if largest_country_count and visitors
            else 0
        )
    return country_rows


def write_count(
    visitors_last_7_days: int,
    last_7_days_date_range: list[str],
    visitors_all_time: int | None,
    all_time_date_range: list[str] | None,
    countries: list[dict[str, int | str]],
    countries_available: bool,
) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "visitors_last_7_days": visitors_last_7_days,
        "last_7_days_date_range": last_7_days_date_range,
        "visitors_all_time": visitors_all_time,
        "all_time_date_range": all_time_date_range,
        "refreshed_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "countries_available": countries_available,
        "countries": countries,
    }
    temporary_path: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=OUTPUT_PATH.parent,
            prefix=".statable-visitor-count-",
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_path = temporary_file.name
            json.dump(record, temporary_file, separators=(",", ":"))
            temporary_file.write("\n")
        os.replace(temporary_path, OUTPUT_PATH)
    finally:
        if temporary_path and os.path.exists(temporary_path):
            os.unlink(temporary_path)


def main() -> int:
    api_key = os.environ.get("STATABLE_API_KEY", "").strip()
    if not api_key:
        print("STATABLE_API_KEY is not configured.", file=sys.stderr)
        return 2

    try:
        visitors_last_7_days, last_7_days_date_range, _ = fetch_count(api_key)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    visitors_all_time: int | None = None
    all_time_date_range: list[str] | None = None
    try:
        visitors_all_time, all_time_date_range = fetch_all_time_count(api_key, last_7_days_date_range[1])
    except RuntimeError as exc:
        print(f"::warning::Statable's all-time visitor count could not be refreshed: {exc}")

    countries_available = True
    try:
        countries = fetch_country_breakdown(api_key, last_7_days_date_range)
    except RuntimeError as exc:
        countries = []
        countries_available = False
        print(f"::warning::Statable's visitor location breakdown could not be refreshed: {exc}")

    write_count(
        visitors_last_7_days,
        last_7_days_date_range,
        visitors_all_time,
        all_time_date_range,
        countries,
        countries_available,
    )
    print(f"Refreshed 7-day and all-time visitor statistics through {last_7_days_date_range[1]}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
