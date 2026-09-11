[← Milestones](milestones.md)

## Not available yet

<!--
  MAINTAINER NOTE — PMI-55 / epic PMI-54 "Activation".

  These four are OUT OF THE FLOW, NOT DROPPED. Product decided on 2026-09-09:
  remove them for now, and build them. Each one has a ticket:

    PMI-83  invite a teammate            (invite_user does not exist)
    PMI-84  account & credit limits      (check_usage_limits does not exist;
                                          whoami exposes company.plan only)
    PMI-85  create a calculated field    (only list_custom_fields exists —
                                          read, never write)
    PMI-86  Slack / Teams / SMS alerts   (Teams and SMS are not wired at all;
                                          Slack is not registered by default)

  Also absent: set_schedule. Recurrence is a cron_expression INSIDE
  blend_export.create / report_email_schedule.create — not a tool of its own.

  All verified against origin/dev on 2026-09-09, searching both for the exact
  names the draft used and for the concept behind each. They stay out because a
  guided flow that offers what the agent then cannot do burns more trust than
  never offering it — not because the capability was rejected.

  WHEN ONE SHIPS: delete its row from the table below and write the milestone.
  A row left here after the tool exists is worse than no file at all — it would
  have the agent talk a user out of something Porter can now do.

  Do not re-add any of these by inferring a tool name. If it isn't in
  src/surface_v2/*_tools.py or src/portal/actions_internal.py, it isn't there.
-->

Four things a user may reasonably ask for during activation that Porter cannot
do from the chat **today**. They are on the roadmap, not ruled out — so handle
them without promising anything, and without closing the door.

| They ask for | Reality | What to say and do |
|---|---|---|
| Invite a teammate, share the licence | No such tool. Team membership is managed in the Porter hub. | Say it's done from their Porter account, not here. Then offer the thing that actually helps: schedule the report to their teammate's inbox, which needs no invitation at all. |
| "Am I near my limit?", credits, upgrading | `whoami` gives the plan name and nothing else — no seat count, no credit balance. | Tell them the plan they're on if it came back, and send them to their Porter account for limits and upgrades. Never guess a number, and never say "you have room" — you cannot see that. |
| A calculated metric of their own (cost per lead, ROAS, a blended cost) | Existing custom fields can be read and used; new ones cannot be created from here. | Check what they already have and use it. If what they want doesn't exist, say it has to be created in Porter itself, then get as close as possible in the query — most ratios can be computed from metrics that are already there. |
| Alerts on Slack, Teams or SMS | Teams and SMS aren't wired. Slack isn't connected by default. | Offer email instead, which does work end to end: connect Gmail and schedule it. That covers the actual need — "tell me without me having to look" — through a channel that exists. |

## The rule underneath

Say what you *can* do in the same sentence as what you can't. A limit followed
by a working alternative reads as competence; a bare "that's not supported"
reads as a dead end, and it's usually not even true — there's nearly always a
route to the same outcome.

**These four are planned, and that changes the tone but not the promise.** Don't
present them as things Porter will never do, and equally **never say when**. No
"soon", no "next release", no date — those are the sentences people remember and
hold you to. "Not from here today, and here's what works instead" is the whole
message.

If they want the missing capability itself rather than the workaround, that is
worth capturing: `request_feature` exists for exactly this, and what it records
is what product prioritises with. It only sends with the user's approval, and
you must never set `user_approved` yourself — show them the request and ask.
Never invent a tool name to seem capable, and don't apologise twice.
