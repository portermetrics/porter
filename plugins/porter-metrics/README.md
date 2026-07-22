# porter-metrics

Connect Claude to **Porter Metrics** in one step. Installing this plugin bundles:

- **The Porter MCP server** (`.mcp.json`) — live marketing data from 25+ ad
  platforms, blends, hosted reports, 750+ actions and AI creative, at
  `https://mcp.portermetrics.com/mcp`. Sign-in is handled securely in your
  browser the first time you ask for data.
- **The `porter-metrics` skill** — teaches Claude to use Porter correctly
  (first run, connecting accounts, reading data, error recovery, and reporting
  bugs / requesting features).
- **A scoped approval hook** — pre-approves network calls to `*.portermetrics.com`
  only (uploads via `prepare_upload`, hosted reports, signed links) so routine
  Porter tasks don't prompt. Everything else follows the normal permission flow.

## Install

```text
/plugin marketplace add portermetrics/porter
/plugin install porter-metrics@portermetrics
```

Full install channels (including claude.ai web & desktop):
<https://mcp.portermetrics.com/install>

## About the approval hook

`scripts/allow_porter_domains.py` runs on `PreToolUse` for `WebFetch` and `Bash`.
It returns an `allow` decision **only** when the call is provably scoped to a
`*.portermetrics.com` host over https (and, for Bash, a bare `curl` with no shell
chaining). In every other case it stays silent and the normal permission flow
applies — it never denies, and never widens access beyond Porter's own domain.

The skill is generated from the connector repo's canonical
`skill/porter-metrics/SKILL.md`.
