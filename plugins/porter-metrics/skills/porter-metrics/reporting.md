[← Milestones](milestones.md)

## 2 · Reporting — the moment it becomes real

A hosted report at a URL they can send to a client or a boss. This is the
milestone that converts: it's the first time Porter produces something that
outlives the conversation.

| Step | How | What to ask |
|---|---|---|
| Build it | `create_report(name=…, template=…)` — it returns the build instructions to author it | "Want me to put this into a report you can share?" |
| Show it | `share_report(report_id, method="link")` | Send them the URL. Let them click it before you say anything else. |
| Adjust | `edit_report` | "Anything you'd change?" — different metrics / only some campaigns / another date range / it's good |
| Start from an existing one | `duplicate_report` | For an agency doing the same report per client, this is the whole job. |
| Deliver it | `execute_action("report_email_schedule.create", …)` | "Want it in your inbox every Monday?" — weekly / monthly / not now |

## What actually matters here

**A report nobody opened isn't a report.** Give them the link and stop. If they
come back with "can it show X" you've reached the milestone; if they say
nothing, ask what's missing rather than moving on.

**Check it renders before you send it.** `preview_report` exists so you find an
empty chart before the user does. A broken report shared with a client costs
more than the milestone was worth.

**The schedule is the sticky part.** A one-off report gets looked at once. One
that arrives every Monday makes Porter part of their week — the highest-value
single step in this flow.

**For an agency, `duplicate_report` is the pitch.** Build it once, clone it per
client, restyle. Say that out loud to anyone who answered "clients as an agency".

⚠️ The email schedule is an **action**, reached with `list_actions` →
`execute_action` — not a fixed tool. Same for the exports in
[Data Export](data-export.md). And `create_report` returns build instructions:
follow them rather than hand-authoring a bundle, which renders empty.

→ Next: [Data Transformation](data-transformation.md)
