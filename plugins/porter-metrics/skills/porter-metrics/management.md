[← Automation](automation.md)

## Management — changing things, not just reading them

The highest-value and highest-risk milestone. These calls spend real money and
publish to real audiences.

| They want to | Where to look |
|---|---|
| Pause, resume, rebudget or retarget a campaign | `facebook_ads.campaign_update`, `google_ads.campaign_update` / `budget_update`, and the same pattern for `linkedin_ads`, `tiktok_ads`, `microsoft_ads`, `apple_ads` |
| Launch something new | `facebook_ads.campaign_create` → `adset_create` → `ad_create` |
| Build an audience | `facebook_ads.customaudience_create`, `customaudience_add_users` |
| Capture leads | `facebook_ads.leadform_create` |
| Publish a post | `instagram_insights.media_publish`, `facebook_insights.post_create`, `linkedin_pages.post_create` |
| Update the CRM | `hubspot.contact_create` / `contact_update` / `deal_update`, `active_campaign.contact_sync` |
| Send an email or SMS campaign | `klaviyo.campaign_create` / `campaign_send`, `mailchimp.campaign_create` / `campaign_send` |

Find the exact one with `list_actions(task="…")` — the catalog is far larger
than this table and differs per connector.

## What actually matters here

**Confirm the specifics, every time.** Name the campaign, the current value and
the new one, then wait for a clear yes. "Pause the Black Friday - Retargeting
campaign, currently running at $340/day?" — not "shall I pause it?".

**One change per confirmation.** Never batch several writes behind a single
approval. If they want three things, that's three confirmations.

**Read back the result.** After the write, confirm the new state from Porter
instead of assuming. A call that returned without error is not proof the
platform applied it.

**The one exception — a new campaign on Meta Ads: one plan, one yes.** A Meta
campaign with its ad sets and ads is one decision, not ten. Do the lookups
first, then show the whole structure in one message — the campaign, every ad
set and ad, each budget in the account's own currency, everything created
paused — and ask once. After that yes, create it all without asking before each
step, one write at a time per ad account (Meta reads bursts as abuse and locks
the account), and read the result back once, at the end.

What that yes does not cover: turning anything on (that is when money starts
moving), deleting, and anything the client already had — each of those still
gets its own yes. If a step fails in a way that changes what they approved —
another objective, a bigger budget, a different structure — stop and ask again;
a technical fix that leaves the plan as it was does not need a new yes — retrying
the same call, a renamed or reformatted parameter, an ID you can look up. Anything
the user would see differently is not technical and needs a new yes: targeting,
placements, creatives, copy, budgets, schedule or the number of ad sets and ads. If you
cannot finish, stop and tell them exactly what was created (all of it paused)
and what was not, and ask whether to complete it or delete what is there —
never leave a half-built campaign without saying so. On every
other platform the two rules above still apply, one write and one yes at a time.

**Start with the reversible one.** For someone's first write, pausing something
is a far better demonstration than creating a campaign — they can undo it, and
that's what makes them willing to try the next one.
