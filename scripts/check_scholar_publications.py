#!/usr/bin/env python3
"""Report Google Scholar records that are not yet on the publications page."""

from __future__ import annotations

import html
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen


PROFILE_ID = "RS59rgIAAAAJ"
PROFILE_URL = "https://scholar.google.ca/citations"
PUBLICATIONS_DIR = Path(__file__).resolve().parents[1] / "_publications"


class ScholarWorksParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[dict[str, str]] = []
        self.in_row = False
        self.in_title = False
        self.in_year = False
        self.title_parts: list[str] = []
        self.year_parts: list[str] = []
        self.current: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        if tag == "tr" and "gsc_a_tr" in classes:
            self.in_row = True
            self.current = {"title": "", "href": "", "year": ""}
        elif self.in_row and tag == "a" and "gsc_a_at" in classes:
            self.in_title = True
            self.title_parts = []
            self.current["href"] = attributes.get("href") or ""
        elif self.in_row and tag == "span" and "gsc_a_h" in classes:
            self.in_year = True
            self.year_parts = []

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self.in_year:
            self.year_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self.in_title:
            self.current["title"] = " ".join("".join(self.title_parts).split())
            self.in_title = False
        elif tag == "span" and self.in_year:
            self.current["year"] = " ".join("".join(self.year_parts).split())
            self.in_year = False
        elif tag == "tr" and self.in_row:
            if self.current["title"] and self.current["href"]:
                self.rows.append(self.current)
            self.in_row = False


def record_id_from_url(url: str) -> str:
    value = parse_qs(urlparse(url).query).get("citation_for_view", [""])[0]
    profile_id, separator, record_id = value.partition(":")
    if not separator or profile_id != PROFILE_ID or not record_id:
        raise ValueError("publication link has no valid Scholar citation ID")
    return record_id


def normalized_title(title: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", html.unescape(title).casefold()))


def read_scholar_works() -> list[dict[str, str]]:
    works: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for start in range(0, 10000, 100):
        query = urlencode(
            {
                "user": PROFILE_ID,
                "hl": "en",
                "view_op": "list_works",
                "cstart": start,
                "pagesize": 100,
            }
        )
        url = f"{PROFILE_URL}?{query}"
        request = Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; AcademicHomepageMetrics/1.0)"},
        )
        with urlopen(request, timeout=30) as response:
            page = response.read().decode("utf-8", errors="replace")
        if PROFILE_ID not in page or "gsc_a_at" not in page:
            raise RuntimeError("Google Scholar did not return the requested profile works")

        parser = ScholarWorksParser()
        parser.feed(page)
        if not parser.rows:
            if start == 0:
                raise RuntimeError("Google Scholar returned no publication records")
            break

        for row in parser.rows:
            row["record_id"] = record_id_from_url(row["href"])
            if row["record_id"] in seen_ids:
                raise RuntimeError("Google Scholar repeated a publication page")
            seen_ids.add(row["record_id"])
            works.append(row)
        if len(parser.rows) < 100:
            break
    return works


def read_site_record_ids() -> tuple[set[str], set[str]]:
    ids: set[str] = set()
    pending_titles: set[str] = set()
    for path in sorted(PUBLICATIONS_DIR.glob("*.md")):
        source = path.read_text(encoding="utf-8")
        parts = source.split("---", 2)
        if len(parts) != 3:
            raise RuntimeError(f"publication file has no YAML front matter: {path.name}")
        frontmatter = parts[1]
        if re.search(r"(?mi)^scholar_pending:\s*true\s*$", frontmatter):
            title_match = re.search(r"(?m)^title:\s*(.*?)\s*$", frontmatter)
            if not title_match:
                raise RuntimeError(f"pending Scholar record has no title: {path.name}")
            title = title_match.group(1).strip()
            if len(title) >= 2 and title[0] == title[-1] and title[0] in "'\"":
                title = title[1:-1]
            normalized = normalized_title(title)
            if not normalized:
                raise RuntimeError(f"pending Scholar record has an invalid title: {path.name}")
            pending_titles.add(normalized)
            continue

        match = re.search(r"(?m)^scholarurl:\s*['\"]?(.+?)['\"]?\s*$", frontmatter)
        if not match:
            raise RuntimeError(f"publication file has no Scholar citation link: {path.name}")
        record_id = record_id_from_url(match.group(1).strip())
        if record_id in ids:
            raise RuntimeError(f"duplicate Scholar citation ID in publication files: {path.name}")
        ids.add(record_id)
    return ids, pending_titles


def markdown_label(value: str) -> str:
    escaped = html.escape(value, quote=False)
    for character in ("\\", "`", "*", "_", "[", "]"):
        escaped = escaped.replace(character, "\\" + character)
    return escaped


def citation_url(record_id: str) -> str:
    query = urlencode(
        {
            "view_op": "view_citation",
            "hl": "en",
            "user": PROFILE_ID,
            "citation_for_view": f"{PROFILE_ID}:{record_id}",
        }
    )
    return f"{PROFILE_URL}?{query}"


def write_summary(message: str) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write(message + "\n")
    else:
        print(message)


def main() -> int:
    try:
        works = read_scholar_works()
        site_ids, pending_titles = read_site_record_ids()
    except Exception as error:
        detail = " ".join(f"{type(error).__name__}: {error}".split())
        write_summary(
            "### Google Scholar publication check\n\n"
            "This run could not compare Scholar with the website. "
            f"`{detail}`\n"
        )
        print("::warning::Google Scholar publication check could not be completed.")
        return 0

    new_works = [
        work
        for work in works
        if work["record_id"] not in site_ids
        and normalized_title(work["title"]) not in pending_titles
    ]
    if not new_works:
        write_summary(
            "### Google Scholar publication check\n\n"
            f"All {len(works)} Scholar records are represented in the website source.\n"
        )
        print(f"Checked {len(works)} Scholar records; no new works found.")
        return 0

    lines = [
        "### New Google Scholar records\n",
        f"Scholar lists {len(new_works)} record(s) not yet on the website:\n",
    ]
    for work in new_works:
        label = markdown_label(work["title"])
        year = f" ({work['year']})" if work["year"] else ""
        lines.append(f"- [{label}]({citation_url(work['record_id'])}){year}")
    write_summary("\n".join(lines) + "\n")
    print(
        f"::warning::Google Scholar lists {len(new_works)} record(s) not yet on the website; "
        "see the workflow summary."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
