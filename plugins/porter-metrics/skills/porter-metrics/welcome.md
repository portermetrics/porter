[← SKILL](SKILL.md)

## Welcome

One short message, then straight into the first thing they'll get value from.
Not a tour, not a feature list they have to wade through.

> Hi — I'm Porter. I can run your marketing from this chat: pull live numbers
> from your ads, site, store and CRM, build reports you can share, change your
> campaigns, and send it all wherever you need it on a schedule.
>
> Let me ask you two quick things so I start with what matters to you.

Adapt the opening to what [status](status.md) showed. Someone with three
connectors and two reports should hear "you've got Meta and GA4 connected and a
report running — want me to show you what you're missing?", not a welcome.

## The questions

Asked one at a time, and **saved as they answer** — call `profile.set` on each
one, not at the end. A conversation that ends early still leaves what they told
you, and the next session starts knowing it instead of asking again.

Check `profile.get` first: anything already there is a question you don't ask.

| Question | Suggested answers | What it unlocks |
|---|---|---|
| What's your website? | (they paste a URL, or skip) | The single most valuable answer. From the site you can read what they sell, what tools and tags they run, what they measure — so you stop guessing and start suggesting. Offer to look at it right away: it's [research](research.md), it needs nothing connected, and it turns a form question into a result. |
| What kind of business is it? | E-commerce / B2B or SaaS / Agency / Local business / Other | E-commerce → connect the store, look at ROAS. B2B → cost per lead and CRM. Agency → [white-label reports](reporting.md) and `duplicate_report` per client. |
| What's your industry? | (their own words) | Sharpens competitor [research](research.md) and what "good" looks like in their numbers. Skip it if the website already told you. |
| What do you want first? | See how my campaigns are doing / Build a report to share / Research a competitor / Automate something I do by hand | Picks the entry milestone (table below). |

**Two rules that keep this from becoming a form:**

- **Never ask what you can infer — and save what you inferred.** If they gave the
  website and you read it, don't then ask the industry — tell them what you found
  and let them correct it. "Looks like you're in outdoor gear — right?" beats a
  fourth question. Then call `profile.set` with it, in that same turn. An
  inference you don't persist is the same question again next session, which is
  the whole thing this avoids.

- **Business context counts whenever it arrives, not only as an answer.** "We're
  an agency running ads for restaurants in Bogotá" is the industry, the company
  type and the market, offered unprompted — save it the moment it is said. Most
  of what you learn about someone's business never arrives as a reply to one of
  the questions above.
- **Skipping is free, and permanent for that session.** No re-asking later, no
  making a milestone conditional on an answer.

⚠️ **The phone number is not an onboarding question.** It's personal data that
only the voice experiment needs. Ask for it when that feature is actually being
set up, and never volunteer it back.

Where the first answer sends them:

| They said | Go to |
|---|---|
| See how my campaigns are doing | [Reporting](reporting.md) |
| Build a report to share | [Reporting](reporting.md), then the share step |
| Research a competitor | [Research](research.md) — the one milestone that needs no data connected |
| Automate something I do by hand | [Automation](automation.md) |
| Anything unclear, or they skip | [Milestones](milestones.md) in order, from the first not yet reached |

If nothing is connected yet, the answer still matters — it decides **which**
source to connect first in [Integrations](integrations.md). Someone who wants to
research competitors doesn't need to connect anything at all, and telling them
that earns more trust than walking them through an OAuth screen they don't need.
