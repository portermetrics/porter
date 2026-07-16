---
name: porter-metrics
description: >-
  Use the Porter Metrics connector correctly. Load this whenever the user
  mentions Porter, Porter Metrics, or wants marketing data from ad platforms
  (Meta/Facebook Ads, Google Ads, GA4, TikTok, LinkedIn, Shopify, …), saved
  blends, hosted reports, or write-back actions through Porter. Covers the
  right first steps (whoami, get_knowledge, connect an account), how to read
  data, and how to recover when no accounts or connectors show up.
---

# Using the Porter Metrics connector

Porter Metrics is a marketing-data platform. Through its MCP connector you can
pull live data from 25+ ad-platform and marketing connectors, save reusable
analyses ("blends") and scheduled exports, build hosted dashboards, and run
write actions on the connected platforms. The connector exposes 26 tools in
four groups; the sections below cover the ones a session actually starts from.

## The one habit that makes Porter work

`get_knowledge` is Porter's built-in manual — semantic search over its how-to
skills, error→fix patterns and FAQs. Consulting it at the right moments is what
separates a smooth session from one that guesses at tools and gives up:

- **Before the first data pull, blend, or report against a connector not yet
  used in this conversation** — it returns the field names, prerequisites and
  quirks that connector expects, so the first `query_data` succeeds.
- **On any unexpected error or empty result** — pass the error text as one of
  the `queries`; the KB pairs known errors with their fixes.
- **When the user asks what Porter can do, or how a Porter flow works.**

Pass `queries` as 3–5 rephrasings of the same intent (vary the verb, add
synonyms, mix English/Spanish) — they fuse into one ranked result set.

## Tool groups

- **Management** — `whoami` (who you are + company), `list_connectors` (every
  connector, destination and third-party app, with connection status),
  `list_accounts` (accounts for a connector), `connect_account` (returns an
  authorization URL the user opens in the browser), `disconnect_account`,
  `get_knowledge`, `prepare_upload` (signed URL for heavy payloads).
- **Analytics** — `list_fields`, `query_data` (live pull across accounts),
  `bigquery_join`, `query_blend`, and blend CRUD (`list_blends`, `get_blend`,
  `create_blend`, `update_blend`, `delete_blend`).
- **Reports** — hosted dashboards at `report.portermetrics.com/<id>`:
  `list_reports`, `get_report`, `preview_report`, `create_report`,
  `edit_report`, `duplicate_report`, `delete_report`, `share_report`.
- **Actions** — every write (ad-platform write-backs, blend exports, report
  email schedules, triggers, third-party app calls) is an *action* discovered
  by intent: `list_actions(task="…")` → pick one → `execute_action(action,
  account_id?, params)`.

## First run — nobody has connected anything yet

When `list_accounts` (or `list_connectors(connected_only=true)`) comes back
**empty, it means the user has connected nothing yet** — not that Porter has no
data or no connectors. An empty list is never a reason to conclude Porter is
broken. Do this instead:

1. `list_connectors` (no filter) to show the catalog. Slug connectors as it
   returns them: `facebook-ads`, `google-ads`, `google-analytics-4`,
   `tiktok-ads`, `shopify`, …
2. `connect_account(connector="facebook-ads")` → it returns an
   `authorization_url`. **Give that URL to the user and wait** — the OAuth
   happens in their browser; the connector cannot complete it for them.
3. After they confirm, `list_accounts(connector="facebook-ads")` lists their
   accounts. If it's still empty, wait a moment and retry once.

Each account carries a `connection_status`: `connected` (already used in
Porter) or `available` (the platform reports it, but Porter hasn't queried it
yet; billing starts on the first `query_data`). Pass the opaque `account_id`
verbatim into `query_data` and `execute_action` — never truncate or rebuild it.

## Reading data

`list_fields(connector=…)` gives the valid metric/dimension names, then run a
small `query_data` (e.g. last 7 days, 2–3 metrics, include `campaign_name` so
rows label themselves). Reply with the numbers in chat. For a recurring or
cross-connector analysis, save a **blend**; for a shareable dashboard URL,
create a **hosted report** (not a chat table).

## Recovering from errors

Every tool returns a plain object; on failure it carries `error_type`,
`message`, and a `hint` naming the next tool to call. Follow the `hint`.
`execute_action` failures also fill `knowledge` with related KB entries you can
open with `get_knowledge`. When a `hint` or error is unfamiliar, call
`get_knowledge` with the error text as one of the queries before retrying.

## Common intents → where to go

| The user wants… | Do this |
|---|---|
| "what can Porter do?" | `get_knowledge(queries=["what can Porter do","getting started"])` |
| "show my Facebook/Google spend" | `list_accounts` → `list_fields` → `query_data` |
| "I don't see any accounts" | First-run flow above: `list_connectors` → `connect_account` |
| "blend Facebook + Google daily" | `create_blend` (+ a scheduled export action) |
| "give me a shareable report" | `create_report` → `share_report` |
| "pause campaigns / write back" | `list_actions(task=…)` → `execute_action` |
