# Porter Metrics — Claude skills

Install the **porter-metrics** skill so Claude uses the Porter Metrics connector
correctly from the first message.

## Claude Code

```
/plugin marketplace add portermetrics/claude-skills
/plugin install porter-metrics@portermetrics
```

## npx (Claude Code and other agents)

```
npx skills add portermetrics/claude-skills
```

## claude.ai (web & desktop)

Download the ZIP from <https://mcp.portermetrics.com/skill.zip> and upload it in
**Settings → Capabilities → Skills**. See <https://mcp.portermetrics.com/install>
for every install channel.

---

The skill in `plugins/porter-metrics/skills/porter-metrics/` is generated from
the connector repo's canonical `skill/porter-metrics/SKILL.md` via
`scripts/build_skill_plugin.py` — edit it there, not here.
