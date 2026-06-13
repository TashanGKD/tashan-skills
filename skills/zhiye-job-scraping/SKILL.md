---
name: zhiye-job-scraping
description: Use when extracting job postings from BeiSen/Zhiye recruitment portals such as *.zhiye.com/jobs, campus hiring pages, internship lists, or pages backed by /api/Jobad/GetJobAdPageList.
---

# Zhiye Job Scraping

## Overview

BeiSen/Zhiye recruitment portals often render job lists from public JSON endpoints. Prefer the API over DOM scraping when the page exposes `BSGlobal` and `/api/Jobad/GetJobAdPageList`.

## Quick Workflow

1. Open the target jobs page in a browser and confirm the visible total count.
2. Fetch the HTML and extract `BSGlobal.PortalId` plus the page's `JobAdListSetting.ListItems`.
3. POST to:

```text
https://<host>/api/Jobad/GetJobAdPageList
```

Use headers:

```text
Content-Type: application/json
Accept: application/json
X-Requested-With: xmlhttprequest
langType: zh_CN
Referer: https://<host>/jobs
```

Core payload:

```json
{
  "PageIndex": 0,
  "PageSize": 200,
  "KeyWords": "",
  "SpecialType": 0,
  "PortalId": "<BSGlobal.PortalId>",
  "DisplayFields": ["Category", "Kind", "LocId", "DetailAddress", "Org", "HeadCount", "Station", "EndTime", "PostDate", "Salary", "Degree", "YearsOfWorking", "ClassificationOne", "ClassificationTwo"]
}
```

4. If `Count > PageSize`, paginate by increasing `PageIndex`.
5. Save raw JSON and a flattened CSV. Add a detail URL such as `https://<host>/jobs/detail?jobAdId=<JobAdId>`.
6. Verify `Code == 200`, fetched rows equal `Count`, and key fields such as `JobAdName`, `Duty`, `Require`, and `LocNames` are present.

## Bundled Script

Use the script for the common case:

```bash
python3 ~/.codex/skills/zhiye-job-scraping/scripts/scrape_zhiye_jobs.py \
  --url https://360campus.zhiye.com/jobs \
  --output-prefix ~/Desktop/workspace/360campus_jobs
```

It writes `<prefix>.json` and `<prefix>.csv`, reports count parity, and includes `DetailUrl` on each record.

## Field Notes

- `GetJobAdPageList` may already include detail fields (`Duty`, `Require`), so do not assume one request per detail page is necessary.
- `Category` often distinguishes `校园招聘`, `实习生招聘`, or social hiring.
- `Kind` usually distinguishes `全职` and `实习`.
- `Status: 1` indicates active positions in observed portals.
- Some portals use lowercase `/api/Jobad/...` for list endpoints and mixed-case `/api/JobAd/...` for detail/share endpoints.

## Common Mistakes

- Do not scrape visible cards first; the API is more complete and less brittle.
- Do not hard-code `PortalId`; parse it from the page.
- Do not treat the first page size as the total. Always compare fetched rows with `Count`.
- Do not strip multiline text fields; responsibilities and requirements often contain meaningful line breaks.
