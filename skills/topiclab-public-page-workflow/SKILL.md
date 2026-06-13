---
name: topiclab-public-page-workflow
description: Use when changing agent-topic-lab public Chinese pages, TaShan/TopicLab routes, nav/home entries, form-data walls, privacy-gated details, WeChat QR/footer contact flows, or visible site copy.
---

# TopicLab Public Page Workflow

## Core Rule

Check the canonical route, current visible copy, and privacy boundary before editing. The user often wants narrow visible behavior changes without accidental route or identity changes.

## Workflow

1. Work in `~/Desktop/workspace/agent-topic-lab` unless the user points elsewhere.
2. Read the current route/nav/home surfaces together before changing a public page: `App.tsx`, `TopNav.tsx`, homepage cards, page component, and matching tests.
3. For Chinese event/program pages, keep visible labels Chinese-only unless explicitly asked for bilingual UI.
4. For spreadsheet/form-backed public walls, inspect the XLSX structure directly and publish anonymized fields first. Do not show names, phone numbers, WeChat IDs, email, or submitter identity on public pages.
5. If admin-only details are requested, distinguish display gating from real security. Frontend `auth_user.is_admin` gating is not real protection if private fields still ship in the JavaScript bundle.
6. If feedback UI is replaced, remove all visible feedback entry points and event sources, not only the obvious button.

## Verification Gate

Use scoped checks appropriate to the touched surface:

- targeted frontend tests for changed page/nav/home components;
- backend/API tests when data or endpoint behavior changes;
- `npm run build`;
- browser verification on the local preview when visible UI changed;
- direct `curl`/`HEAD` checks for public image or API endpoints.

## Recurring Local Details

- Inspiration co-creation work touched `InspirationCoCreationPage.tsx`, `InspirationCoCreationHomeCard.tsx`, `TopNav.tsx`, `App.tsx`, and page/component tests.
- A public needs wall previously used `2026他山青年论坛.xlsx` and 25 anonymized demands.
- Footer WeChat QR assets are DB-backed through `site_assets.key='wechat-group-qr'` and `/api/v1/site/wechat-group-qr.webp`.

## Common Failures

- If a new route exists but nav/home wording is wrong, check all entry surfaces and tests together.
- If local cards are missing, verify backend API health before churning frontend layout.
- If a QR or contact flow expires, treat operator cadence as part of the feature.
