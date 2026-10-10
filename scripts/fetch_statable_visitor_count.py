#!/usr/bin/env python3
"""Fetch Statable's aggregate visitor count for the trailing 30 days."""

from __future__ import annotations

import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SITE_ID = 3386330
QUERY_URL = "https://statable.com/api/v1/query"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "_data" / "statable_visitor_count.json"
DATE_PATTERN = re.compile(r"\A\d{4}-\d{2}-\d{2}\Z")


def fetch_count(api_key: str) -> tuple[int, list[str]]:
    body = json.dumps(
        {
            "site_id": SITE_ID,
            "metrics": ["visitors"],
            "date_range": "30d",
        }
    ).encode("utf-8")
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
    query = payload.get("query")
    if not isinstance(query, dict) or query.get("site_id") != SITE_ID:
        raise RuntimeError("Statable returned data for an unexpected site.")
    date_range = query.get("date_range")
    if (
        not isinstance(date_range, list)
        or len(date_range) != 2
        or any(not isinstance(day, str) or DATE_PATTERN.fullmatch(day) is None for day in date_range)
    ):
        raise RuntimeError("Statable returned an invalid reporting period.")

    results = payload.get("results")
    if not isinstance(results, list) or len(results) != 1:
        raise RuntimeError("Statable returned an unexpected aggregate result.")
    metrics = results[0].get("metrics") if isinstance(results[0], dict) else None
    visitors = metrics.get("visitors") if isinstance(metrics, dict) else None
    if type(visitors) is not int or visitors < 0:
        raise RuntimeError("Statable returned an invalid visitor count.")

    return visitors, date_range


def write_count(visitors: int, date_range: list[str]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "visitors": visitors,
        "date_range": date_range,
        "refreshed_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
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
        visitors, date_range = fetch_count(api_key)
        write_count(visitors, date_range)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(f"Refreshed aggregate visitor count for {date_range[0]} through {date_range[1]}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
