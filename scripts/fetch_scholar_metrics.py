#!/usr/bin/env python3
"""Refresh the public Google Scholar profile metrics used by the homepage."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


PROFILE_URLS = (
    "https://scholar.google.ca/citations?user=RS59rgIAAAAJ&hl=en",
    "https://scholar.google.com/citations?user=RS59rgIAAAAJ&hl=en",
    "https://scholar.google.co.uk/citations?user=RS59rgIAAAAJ&hl=en",
)
MIRROR_BASE_URL = "https://r.jina.ai/http://scholar.google.ca/citations?"
PROFILE_ID = "RS59rgIAAAAJ"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "_data" / "scholar_metrics.json"


class MetricsParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_metrics_table = False
        self.in_cell = False
        self.current_cell: list[str] = []
        self.current_row: list[str] = []
        self.rows: list[list[str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "table" and attributes.get("id") == "gsc_rsb_st":
            self.in_metrics_table = True
        elif self.in_metrics_table and tag == "td":
            self.in_cell = True
            self.current_cell = []

    def handle_endtag(self, tag: str) -> None:
        if not self.in_metrics_table:
            return
        if tag == "td" and self.in_cell:
            value = " ".join("".join(self.current_cell).split())
            self.current_row.append(value)
            self.in_cell = False
        elif tag == "tr":
            if self.current_row:
                self.rows.append(self.current_row)
            self.current_row = []
        elif tag == "table":
            self.in_metrics_table = False

    def handle_data(self, data: str) -> None:
        if self.in_metrics_table and self.in_cell:
            self.current_cell.append(data)


def read_profile_metrics(profile_url: str) -> dict[str, int]:
    request = Request(
        profile_url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; AcademicHomepageMetrics/1.0)"},
    )
    with urlopen(request, timeout=30) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        html = response.read().decode("utf-8", errors="replace")

    parser = MetricsParser()
    parser.feed(html)
    names = {"Citations": "citations", "h-index": "h_index", "i10-index": "i10_index"}
    metrics: dict[str, int] = {}
    for row in parser.rows:
        if len(row) < 2 or row[0] not in names:
            continue
        value = re.sub(r"[^0-9]", "", row[1])
        if not value:
            raise RuntimeError(f"invalid {row[0]} value")
        metrics[names[row[0]]] = int(value)
    expected = {"citations", "h_index", "i10_index"}
    if set(metrics) != expected:
        raise RuntimeError(f"incomplete metrics: {sorted(metrics)}")
    return metrics


def read_profile_metrics_through_reader() -> dict[str, int]:
    """Read the profile's public publication pages and derive its three metrics."""
    counts: list[int] = []
    seen_pages: set[tuple[int, ...]] = set()
    for start in range(0, 200, 20):
        query = urlencode({
            "user": PROFILE_ID,
            "hl": "en",
            "view_op": "list_works",
            "cstart": start,
            "pagesize": 20,
        })
        page_url = MIRROR_BASE_URL + query
        request = Request(page_url, headers={"User-Agent": "AcademicHomepageMetrics/1.0"})
        with urlopen(request, timeout=45) as response:
            if response.status != 200:
                raise RuntimeError(f"Reader HTTP {response.status}")
            page = response.read().decode("utf-8", errors="replace")
        if "Mengzhe Geng" not in page:
            raise RuntimeError("Reader response was not the requested Scholar profile")
        page_counts = tuple(
            int(value)
            for value in re.findall(
                r"(\d+)\]\(https?://scholar\.google\.(?:ca|com|co\.uk)/scholar\?",
                page,
            )
        )
        if not page_counts or page_counts in seen_pages:
            break
        seen_pages.add(page_counts)
        counts.extend(page_counts)
        if len(page_counts) < 20:
            break
    if not counts:
        raise RuntimeError("Reader returned no publication citation counts")
    ordered = sorted(counts, reverse=True)
    return {
        "citations": sum(counts),
        "h_index": sum(count >= rank for rank, count in enumerate(ordered, start=1)),
        "i10_index": sum(count >= 10 for count in counts),
    }


def main() -> None:
    metrics: dict[str, int] = {}
    source_url = ""
    last_error = ""
    if os.environ.get("SCHOLAR_METRICS_SOURCE") != "mirror":
        for profile_url in PROFILE_URLS:
            try:
                metrics = read_profile_metrics(profile_url)
                source_url = profile_url
                break
            except Exception as error:
                last_error = f"{profile_url}: {error}"

    if not metrics:
        try:
            metrics = read_profile_metrics_through_reader()
            source_url = MIRROR_BASE_URL + urlencode({"user": PROFILE_ID, "view_op": "list_works"})
        except Exception as error:
            last_error = f"{MIRROR_BASE_URL}: {error}"

    expected = {"citations", "h_index", "i10_index"}
    if set(metrics) != expected:
        raise RuntimeError(f"Could not read all Google Scholar metrics; last error: {last_error}")

    payload = {
        "updated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "citations": f"{metrics['citations']:,}",
        "h_index": metrics["h_index"],
        "i10_index": metrics["i10_index"],
    }
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Updated Google Scholar profile metrics from {source_url} at {payload['updated_at']}")


if __name__ == "__main__":
    main()
