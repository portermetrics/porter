# porter-metrics

Connect Claude to **Porter Metrics** in one step. Installing this plugin bundles:

- **The Porter MCP server** (`.mcp.json`) — live marketing data from 25+ ad
  platforms, blends, hosted reports, 750+ actions and AI creative, at
  `https://mcp.portermetrics.com/mcp`. Sign-in is handled securely in your
  browser the first time you ask for data.
- **The `porter-metrics` skill** — teaches Claude to use Porter correctly:
  first run, connecting accounts, reading data, error recovery, reporting bugs /
  requesting features, and how to guide you if a network-domain step is needed.

## Install

```text
/plugin marketplace add portermetrics/porter
/plugin install porter-metrics@portermetrics
```

Full install channels (including claude.ai web & desktop):
<https://mcp.portermetrics.com/install>

## Reaching Porter's domain

The Porter tools run over the MCP transport and need no extra permission. The one
case that can prompt is when Claude reaches a Porter URL directly — uploading a
file to a signed `upload_url`, or opening a hosted report. If Claude's command
sandbox is on, that goes through a network allow-list Claude Code keeps under
**Settings → Capabilities → Domains**. A plugin can't populate that list, so the
skill instead tells the user, at the moment it's blocked, to add
`*.portermetrics.com` there (a one-time step). Admins can pre-allow it fleet-wide
via managed settings.

The skill is generated from the connector repo's canonical
`skill/porter-metrics/SKILL.md`.
