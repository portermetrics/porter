[← Milestones](milestones.md)

## 7 · The daily routine — Porter with a rhythm of its own

Every milestone before this one still waits for the user to open a chat. This
is the one that flips it: a routine that runs on its own each morning, starts
their day with what actually changed, and closes the loop on what they did
about it.

It's the difference between a tool someone remembers to use and an assistant
that's already working when they sit down.

| Step | How |
|---|---|
| Propose it | After they've seen a report or a scheduled delivery working — never before. The pitch is concrete: "want me to have this ready every morning before you start?" |
| Create it | `execute_action("create_trigger", {kind: "schedule", match: {cron: "0 8 * * 1-5", timezone: "<theirs>"}, action: {...}})` |
| Show it working | `list_trigger_runs` after the first fire, so they see it ran rather than trusting it did |
| Hand them the controls | `pause_trigger`, `resume_trigger`, `delete_trigger` — say these exist **when you create it**, not when they complain |

## What actually matters here

**They create it, you only propose.** A routine that appears because the agent
thought it was a good idea is spam with a cron expression. Ask, wait for a yes,
and make the yes specific — what time, which days, what it should cover.

**Weekdays at their working hour, not 00:00 UTC.** Ask the timezone or infer it
from their account and say which one you used. A summary that lands at three in
the morning gets read as noise forever after.

**Make day three as useful as day one.** The trap is a routine that repeats the
same numbers every morning — that gets ignored within a week. Lead with what
*changed*: what moved since yesterday, what broke, what's newly worth attention.
If nothing changed, saying so briefly is better than padding.

**Close the loop, don't just report.** The second half of the routine is
feedback on the work: what they changed yesterday and what it did. That's what
makes it a colleague rather than a newsletter.

**Say how to stop it in the same breath you create it.** Nothing makes people
distrust automation faster than not knowing how to turn it off. It also makes
them far more willing to try it.

⚠️ Requires the trigger engine wired to the tools. If `create_trigger` is not
in the catalog for this deployment, **do not promise the routine** — offer the
scheduled report from [notifications](notifications.md) instead, which covers
part of the same need.

---

This is the last milestone, and it isn't an end: from here the conversation is
about what the routine should notice, which is a much better conversation than
"what can Porter do".
