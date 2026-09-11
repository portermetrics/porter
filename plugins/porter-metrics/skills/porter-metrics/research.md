[← Automation](automation.md)

## Research — intel on any brand, including the ones they compete with

The only milestone that needs **nothing connected**. Use it early with anyone
who hasn't committed yet: it produces something useful in one exchange.

Always ask for the target first — a website, a handle, a brand name — and say
it's optional. Without it you're guessing; with it the answer is about them.

| They want to know | Where to look | Ask for |
|---|---|---|
| What people search for, what a site ranks for | `seo.dataforseo_labs_google_keyword_overview`, `google_keywords_for_site`, `google_ranked_keywords` | Their site, or a competitor's |
| Who they're really competing with | `seo.dataforseo_labs_google_competitors_domain`, `google_serp_competitors` | Their domain |
| What a competitor is running on Meta | `meta_ads_research.run_audit`, then `enrich_creatives` for the breakdown | Brand name or Facebook page |
| Who's bidding on their keywords | `google_ads_research.run_search_audit`, `run_serp_teardown` | Brand or keywords |
| A competitor's TikTok ads | `tiktok_ads_research.run_tiktok_audit` | Brand + market (EU/UK/CH only) |
| What a page actually says | `web_scraping.firecrawl_scrape` | The URL |
| Instagram, TikTok, YouTube performance | `instagram_insights.business_discovery_get`, `tiktok_insights.video_insights`, `seo.upriver_get_trends` | @handle, #hashtag or a video link |

## What actually matters here

**Lead with a competitor, not with themselves.** "Want to see what your
competitor is running right now?" gets a yes far more often than "want to
analyse your SEO?" — and it's the same call.

**One finding beats a full audit.** Give the single most interesting thing you
found and offer to go deeper. A twelve-section report at this point doesn't get
read.

**Say where the limits are.** TikTok ad research covers EU, UK and Switzerland
only. Better to say so than to return an empty result that looks like a bug.

**Bridge back to their data.** After showing a competitor's ads, the natural
next line is "want to see how yours compare?" — which is
[Integrations](integrations.md), now with a reason attached.
