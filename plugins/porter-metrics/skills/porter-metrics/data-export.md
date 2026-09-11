[← Milestones](milestones.md)

## 4 · Data Export — out of Porter, into where they work

Some people live in a spreadsheet and always will. Meeting them there is worth
more than convincing them to open a dashboard.

| Step | How | What to ask |
|---|---|---|
| To a Google Sheet | `execute_action("blend_export.create", …)` with a Sheets destination | "Want this in a Sheet you can work with?" — once / refreshed weekly / refreshed daily |
| To BigQuery | same action, BigQuery destination | Only if they have a data team. Ask first: "does anyone on your side use a data warehouse?" |
| Run it now | `execute_action("blend_export.run", …)` | To show it working immediately instead of waiting for the first scheduled run. |

## What actually matters here

**Scheduling is not a separate step.** It's a `cron_expression` on the same
call. Offer "refreshed every morning" in the same breath as the export — a
one-off export is a file, a scheduled one is a process they stop thinking about.

**A blend has to exist first.** Exports run off a blend. If they haven't built
one, that's [Data Transformation](data-transformation.md), not this milestone.

**Don't offer BigQuery to everyone.** To a solo marketer it reads as noise and
makes Porter feel like it's not for them. To a team with an analyst it's the
reason they'd pay. The answer to "what do you work on" from
[welcome](welcome.md) usually tells you which one you're talking to.

**Run it once in front of them.** `blend_export.run` turns "it'll show up
tomorrow" into a Sheet they can open now.

→ Next: [Automation](automation.md)
