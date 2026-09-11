[← SKILL](SKILL.md)

## Status — read the room before you speak

Three calls, before the first message. They decide what you say and what you
skip: nothing is more deflating than being welcomed to a product you already set
up last month, or being offered a "first report" when you have eleven.

| What you need | How |
|---|---|
| Which data sources they have connected | `list_connectors(connected_only=true)` |
| How many accounts on each | the `accounts_count` on each connector returned |
| Whether they already build things | `list_reports` and `list_blends` |
| Who they are and on what plan | `whoami` → `user.email`, `company.name`, `company.plan` |
| What they told us about their business | `profile.get` — website, industry, company type |

Read the result as a position in the journey, not a checklist:

- **Nothing connected** — a genuine first run. Start at
  [Integrations](integrations.md); everything else needs data to exist first.
- **One source, nothing built** — the most common place people stall. They
  connected something, saw it worked, and stopped. Go to
  [Reporting](reporting.md): a live report is the moment Porter stops being a
  connector and starts being useful.
- **Reports or blends already exist** — do not walk them through basics. Skip to
  the first milestone they haven't reached, usually
  [Data Export](data-export.md) or [Automation](automation.md).

`profile.get` is what makes the second session better than the first: it comes
back with what they already answered, so you neither re-ask nor start generic.
Empty just means they are new — see [welcome](welcome.md).

⚠️ `company.plan` is best-effort. It is enriched from the subscription summary
and comes back `null` when that call fails, which is not the same as "no plan" —
never tell someone they are on a free plan because this field was empty.

An empty `list_accounts` is a first-run user, never a broken Porter. The
[first-run flow](SKILL.md) in the main skill file covers what to do about it.
