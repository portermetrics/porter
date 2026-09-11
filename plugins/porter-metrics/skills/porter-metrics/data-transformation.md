[← Milestones](milestones.md)

## 3 · Data Transformation — answers, not dashboards

Where someone stops reading numbers per platform and starts asking questions
across all of them.

| Step | How | What to ask |
|---|---|---|
| First real question | `list_fields` then `query_data` | "What do you want to know?" — how are my campaigns doing / which creatives work best / where's the budget going / what's my return |
| Narrow it | `query_data` with `filters` | "Want to zoom into one campaign, country or device?" |
| Compare periods | `query_data` with `date_range` | "Against last month, or the same week last year?" |
| One view across sources | `create_blend`, then `query_blend` | "Want your ad spend from every platform in one table?" |

## What actually matters here

**`list_fields` first, always.** Guessing metric names is the single most common
way a first query fails. Pull the real field names for that connector, then
query.

**Start small.** Last 7 days, two or three metrics, and include `campaign_name`
so the rows label themselves. A wall of numbers with no labels reads as noise.

**The blend is the moment.** One table with Meta and Google side by side is
something they cannot get from either platform's own dashboard. That's the
argument for Porter, and it's worth making explicitly: "this is the bit neither
Meta nor Google will show you."

**Answer in chat first.** Reply with the numbers. Offer a report only if it's
something they'll want again — not everything needs to become a dashboard.

If they want a metric Porter doesn't carry — cost per lead, a blended ROAS —
existing custom fields can be read, but new ones can't be created from here. See
[pending](pending.md); most ratios can be computed from fields that already
exist.

→ Next: [Data Export](data-export.md)
