[← Milestones](milestones.md)

## 7 · The daily routine — Porter with a rhythm of its own

Every milestone before this one still waits for the user to open a chat. This is
the one where Porter stops waiting to be opened: a routine that runs on its own
each morning and has the work done — what actually changed, and what came of
what they did yesterday — before they ask for it.

⚠️ **Read the next section before you pitch it.** The work happens on its own;
the *delivery* is where the promise has to stay honest, and getting that wrong
leaves someone waiting for a message that never arrives.

| Step | How |
|---|---|
| Propose it | After they've seen a report or a scheduled delivery working — never before. The pitch is concrete: "want me to have this ready every morning before you start?" |
| Create it | `execute_action("create_trigger", {kind: "schedule", match: {cron: "0 8 * * 1-5", timezone: "<theirs>"}, action: {...}})` |
| Show it working | `list_trigger_runs` after the first fire, so they see it ran rather than trusting it did |
| Hand them the controls | `pause_trigger`, `resume_trigger`, `delete_trigger` — say these exist **when you create it**, not when they complain |

## Where it delivers — say this, do not imply it

A scheduled trigger runs in the background and **does not write into this chat
by itself**. There is no channel that pushes a message into a conversation on a
cron, so the two outputs that work end to end are:

* **email**, when the routine's action delivers one;
* **`list_trigger_runs`**, which the user goes and reads.

Slack, Teams and SMS are not wired. Do not offer them.

So say which one it will be, in the same message you create it.
**Never "I'll message you every morning"** — you only speak when the user
writes, and a routine cannot change that. And never end the turn on "it's under
way, I'll let you know": finish in this turn, with where to look.

This is a real limit of the platform and not a style note. Pitched as a message
that arrives on its own, the routine is a promise nothing can keep, and the user
finds out by waiting.

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
