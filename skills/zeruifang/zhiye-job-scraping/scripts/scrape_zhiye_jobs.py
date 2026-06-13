#!/usr/bin/env python3
"""Scrape public job postings from BeiSen/Zhiye recruitment portals."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_DISPLAY_FIELDS = [
    "Category",
    "Kind",
    "LocId",
    "DetailAddress",
    "Org",
    "HeadCount",
    "Station",
    "EndTime",
    "PostDate",
    "Salary",
    "Degree",
    "YearsOfWorking",
    "ClassificationOne",
    "ClassificationTwo",
]

CSV_FIELDS = [
    "JobAdId",
    "JobAdName",
    "Category",
    "CategoryId",
    "Kind",
    "ClassificationOne",
    "ClassificationTwo",
    "LocNames",
    "Org",
    "Degree",
    "Salary",
    "HeadCount",
    "PostDate",
    "EndTime",
    "ChangeDate",
    "Status",
    "DetailUrl",
    "Duty",
    "Require",
]


def request_text(url: str, *, referer: str | None = None) -> str:
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "text/html,application/xhtml+xml"}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def request_json(url: str, payload: dict[str, Any], *, referer: str) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Requested-With": "xmlhttprequest",
            "langType": "zh_CN",
            "EagleEye-TraceID": "codex-zhiye-scrape",
            "Referer": referer,
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def extract_bsglobal(html: str) -> dict[str, Any]:
    match = re.search(r"var\s+BSGlobal\s*=\s*(\{.*?\})\s*;\s*</script>", html, re.S)
    if not match:
        raise ValueError("Could not find BSGlobal JSON in page HTML")
    return json.loads(match.group(1))


def infer_display_fields(bsglobal: dict[str, Any]) -> list[str]:
    fields: list[str] = []
    for page in bsglobal.get("Pages", []):
        if page.get("Code") not in {"jobs", "CampusList", "InternList", "SocialList"}:
            continue
        config_raw = page.get("Config") or ""
        if not config_raw:
            continue
        try:
            config = json.loads(config_raw)
        except json.JSONDecodeError:
            continue
        setting = config.get("extraBusinessSetting", {}).get("JobAdListSetting", {})
        for item in setting.get("ListItems", []):
            key = item.get("Key")
            if key and item.get("Select") and key not in fields:
                fields.append(key)
    merged = list(DEFAULT_DISPLAY_FIELDS)
    for field in fields:
        if field not in merged:
            merged.append(field)
    return merged


def detail_url_for(source_url: str, job_ad_id: Any) -> str:
    parsed = urllib.parse.urlparse(source_url)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, "/jobs/detail", "", f"jobAdId={job_ad_id}", ""))


def scrape(url: str, page_size: int) -> dict[str, Any]:
    parsed = urllib.parse.urlparse(url)
    base = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, "", "", "", ""))
    html = request_text(url)
    bsglobal = extract_bsglobal(html)
    portal_id = bsglobal["PortalId"]
    display_fields = infer_display_fields(bsglobal)
    api_url = base + "/api/Jobad/GetJobAdPageList"

    jobs: list[dict[str, Any]] = []
    reported_count: int | None = None
    page_index = 0
    while True:
        payload = {
            "PageIndex": page_index,
            "PageSize": page_size,
            "KeyWords": "",
            "SpecialType": 0,
            "PortalId": portal_id,
            "DisplayFields": display_fields,
        }
        data = request_json(api_url, payload, referer=url)
        if data.get("Code") != 200:
            raise RuntimeError(f"API returned non-200 Code: {data!r}")
        reported_count = int(data.get("Count") or 0)
        batch = data.get("Data") or []
        for job in batch:
            job["DetailUrl"] = detail_url_for(url, job.get("JobAdId"))
            job["SourceListUrl"] = url
        jobs.extend(batch)
        if len(jobs) >= reported_count or not batch:
            break
        page_index += 1

    return {
        "source": url,
        "portal_id": portal_id,
        "captured_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "api": api_url,
        "display_fields": display_fields,
        "count_reported": reported_count,
        "count_fetched": len(jobs),
        "jobs": jobs,
    }


def write_outputs(result: dict[str, Any], output_prefix: str) -> tuple[Path, Path]:
    json_path = Path(output_prefix).with_suffix(".json")
    csv_path = Path(output_prefix).with_suffix(".csv")
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for job in result["jobs"]:
            row = dict(job)
            row["LocNames"] = " / ".join(job.get("LocNames") or [])
            writer.writerow(row)
    return json_path, csv_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Zhiye jobs URL, for example https://360campus.zhiye.com/jobs")
    parser.add_argument("--output-prefix", required=True, help="Output path without extension")
    parser.add_argument("--page-size", type=int, default=200)
    args = parser.parse_args()

    result = scrape(args.url, args.page_size)
    json_path, csv_path = write_outputs(result, args.output_prefix)
    missing = {
        "Duty": sum(1 for job in result["jobs"] if not job.get("Duty")),
        "Require": sum(1 for job in result["jobs"] if not job.get("Require")),
        "LocNames": sum(1 for job in result["jobs"] if not job.get("LocNames")),
    }
    print(
        json.dumps(
            {
                "reported_count": result["count_reported"],
                "fetched_count": result["count_fetched"],
                "missing": missing,
                "json_path": str(json_path),
                "csv_path": str(csv_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if result["count_reported"] == result["count_fetched"] else 2


if __name__ == "__main__":
    sys.exit(main())
