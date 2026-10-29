[← Milestones](milestones.md)

## 2 · Reporting — the moment it becomes real

A hosted report at a URL they can send to a client or a boss. This is the
milestone that converts: it's the first time Porter produces something that
outlives the conversation.

| Step | How | What to ask |
|---|---|---|
| Build it | `draft_report_spec(intent=…, accounts_used=[…])` → adjust with a `patch` → `publish_report_spec(draft_id=…, patch=[…])`: the report as data, live in about a minute, in any design (theme, free layout, `viz` charts). `create_report` (a bundle you build) only for what the spec cannot express — `publish_report_spec` says so | "Want me to put this into a report you can share?" |
| Show it | `share_report(report_id, method="link")` | Send them the URL. Let them click it before you say anything else. |
| Adjust | `publish_report_spec(report_id=…, patch=[…])` (`edit_report` only for a built bundle) | "Anything you'd change?" — different metrics / only some campaigns / another date range / it's good |
| Start from an existing one | `duplicate_report` | For an agency doing the same report per client, this is the whole job. |
| Deliver it | `execute_action("report_email_schedule.create", …)` | "Want it in your inbox every Monday?" — weekly / monthly / not now |
| Move it to a client | `share_report(report_id, method="transfer", company_id=…)` | Built it in your own company but it belongs to the client (e.g. their custom domain 404s)? Owner only; the company's owner becomes owner, you stay admin. |

## What actually matters here

**A report nobody opened isn't a report.** Give them the link and stop. If they
come back with "can it show X" you've reached the milestone; if they say
nothing, ask what's missing rather than moving on.

**Check it renders before you send it.** `publish_report_spec` runs every chart
against real data and returns its preview; `preview_report` is for any other
report. Find an empty chart before the user does: a broken report shared with a
client costs more than the milestone was worth.

**The schedule is the sticky part.** A one-off report gets looked at once. One
that arrives every Monday makes Porter part of their week — the highest-value
single step in this flow.

**For an agency, `duplicate_report` is the pitch.** Build it once, clone it per
client, restyle. Say that out loud to anyone who answered "clients as an agency".

⚠️ The email schedule is an **action**, reached with `list_actions` →
`execute_action` — not a fixed tool. Same for the exports in
[Data Export](data-export.md). And when a report does need `create_report` (what
`publish_report_spec` cannot express), follow the build instructions it returns
rather than hand-authoring a bundle, which renders empty.

→ Next: [Data Transformation](data-transformation.md)
