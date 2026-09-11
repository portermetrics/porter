# Contributing

**This repository is generated. Do not edit it here.**

Every file you see comes from `skill/plugin/` in the private `porter-mcp-server`
repo, published by `scripts/publish_plugin.py` on each merge to `master`. A
commit made directly in this repo is not merged with the source — it is
**overwritten by the next publish**, without warning and without a conflict.

## Where to make a change

| You want to change… | Edit this, in `porter-mcp-server` |
|---|---|
| What the skill teaches Claude | `skill/porter-metrics/SKILL.md` — the canonical source |
| The plugin manifests, README or MCP config | `skill/plugin/…` |

Then run `python scripts/build_skill_plugin.py`, bump the `version` in **both**
`plugin.json` and `marketplace.json`, and open a PR to `dev`. The publish to this
repo happens on its own once that reaches `master`.

`python scripts/publish_plugin.py` (no flags) shows you what a merge would
publish here, without publishing it.

## Why this file exists

It is not a hypothetical rule. On 2026-07-22 the publish step — manual back then
— stopped being run, and work continued on both sides. This repo gained a whole
`SKILL.md` section the source never had, while the source gained the Stripe
connector and the media-generation markers this repo never got. For seven weeks
this repo served a July skill under version **2.0.0** while the source carried
newer content under **1.1.0**, so every user installing through the plugin
marketplace or `npx` received the stale one.

Reconciling that took a manual, file-by-file merge. The publish is automated now
so it cannot drift again — but only as long as this repo stays a destination and
not a place where work happens.

## The version matters

The marketplace pins the plugin version: users only receive an update when the
number changes. `publish_plugin.py` refuses to publish changed content under a
version that is already published, rather than let a change go nowhere.
