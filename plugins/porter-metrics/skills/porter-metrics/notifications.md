[← Milestones](milestones.md)

## 6 · Notifications — it arrives without being asked for

The last milestone, and the one that decides whether Porter becomes a habit.
Everything up to here still needs someone to remember to open a chat.

| Step | How | What to ask |
|---|---|---|
| The report, on a schedule | `execute_action("report_email_schedule.create", …)` | "Want this in your inbox every Monday morning?" |
| The data, on a schedule | `execute_action("blend_export.create", …)` with a `cron_expression` | "Want the Sheet to refresh itself every morning?" |
| Email through their own account | `connect_account` for Gmail | Only if they want it sent from their address, or on to a client. |

## What actually matters here

**This is the highest-value step in the flow.** A scheduled delivery is the
difference between a tool someone tried and a tool someone uses. If you only get
one milestone past Reporting, make it this one.

**Match the cadence to the decision, not to the data.** Daily for someone
actively managing spend; Monday morning for a weekly review; first of the month
for a client report. Ask which of those they actually do.

**Send one now.** A schedule they can't see feels like a promise. Run it once so
they get the email in front of them, then leave the recurring one in place.

⚠️ Only email works end to end today. **Slack, Teams and SMS are not
available** — see [pending](pending.md) for what to offer instead. Don't promise
a Slack alert; email covers the same need, which is not having to remember to
look.

→ Next: [the daily routine](routine.md) — the step where Porter stops waiting
to be opened at all.

---

Don't announce completing a checklist; they never saw it. If they got here they
have live data, a report that shares itself and numbers that arrive on their
own. That's the moment to ask what else takes up their week.
