<div align="center">

# Porter Metrics for Claude

**Bring your marketing data into Claude — and let it do the work.**

Ask Claude about your Facebook, Google, TikTok, LinkedIn or GA4 numbers in plain
language and get real answers from your own accounts. Build a shareable report,
schedule a weekly export, even generate ad creative — all inside the chat.

[Install](#install-in-two-minutes) · [What you can ask](#what-you-can-ask) · [Connecting your accounts](#connecting-your-accounts) · [Your data & privacy](#your-data--privacy) · [Help](#getting-help)

</div>

---

## What this is

This is the official Porter Metrics plugin for Claude. Installing it does three
things at once, so everything simply works from your first message:

- 🔌 **Connects Claude to Porter** — your live marketing data from **25+ platforms**
  (Meta/Facebook Ads, Google Ads, GA4, TikTok, LinkedIn, Shopify and more),
  plus reports, saved analyses and a catalog of **750+ actions**.
- 🧠 **Teaches Claude how to use Porter well** — so it asks for the right things,
  reads your data correctly, and recovers gracefully instead of guessing.
- ✅ **Skips the busywork** — routine Porter actions (uploading a file, opening a
  hosted report) are pre-approved for Porter's own website, so Claude isn't
  stopping to ask permission for every ordinary Porter task.

You don't need to be technical. If you can chat with Claude, you can use this.

---

## Install in two minutes

You'll need [Claude Code](https://www.claude.com/product/claude-code) (the Claude
app for your computer). In Claude, type these two commands:

```text
/plugin marketplace add portermetrics/porter
/plugin install porter-metrics@portermetrics
```

That's it. Claude will load the plugin and, the first time you ask for your
data, open a secure Porter sign-in page in your browser. Sign in once and you're
connected.

> **On claude.ai (web or desktop) instead of Claude Code?** You can add Porter
> there too — see **<https://mcp.portermetrics.com/install>** for every way to
> connect.

### If you run Claude's Bash sandbox

Most people can skip this. If you've turned on Claude Code's **sandbox** (the
setting that lets Claude run commands on its own), uploading files goes through a
network allow-list. The first time Claude uploads to Porter it will ask once to
allow **`portermetrics.com`** — click **Yes** and you're set for the session.

To never be asked, add Porter's domain to the allow-list once. Open your settings
(`~/.claude/settings.json`) and add:

```json
{
  "sandbox": { "network": { "allowedDomains": ["*.portermetrics.com"] } },
  "permissions": { "allow": ["WebFetch(domain:*.portermetrics.com)"] }
}
```

After that, `*.portermetrics.com` appears under **Settings → Capabilities →
Domains** and Porter uploads never prompt again. *(Rolling this out to a whole
team? Your admin can push the same allow-list to everyone via managed
settings — email [support@portermetrics.com](mailto:support@portermetrics.com).)*

---

## What you can ask

Once it's installed, just talk to Claude the way you'd brief a teammate:

| You say… | Claude does… |
| --- | --- |
| *"How much did we spend on Facebook Ads last week, by campaign?"* | Pulls the numbers live from your account and answers in the chat. |
| *"Which Google Ads campaigns have the worst cost per lead this month?"* | Reads your data, ranks it, and explains what stands out. |
| *"Blend my Facebook and Google spend into one daily view."* | Saves a reusable **blend** you can re-run any time. |
| *"Build me a shareable dashboard for this client."* | Creates a **hosted report** at a link you can send. |
| *"Email that report to the team every Monday at 9am."* | Sets up a recurring, automated send. |
| *"Pause the campaigns with a CPA over $40."* | Runs the action on the platform (after checking with you). |
| *"Generate a short product video with a voiceover for this ad."* | Creates the creative for you. |
| *"I don't see any of my accounts."* | Walks you through connecting your first one. |

If Porter can do it, you can ask for it in words — no menus, no exports, no
spreadsheets.

---

## Connecting your accounts

The first time you ask for data, Claude gives you a secure Porter link to open in
your browser. You sign in and pick the account (your Facebook page, Google Ads
account, and so on). After that, Claude can use it whenever you ask.

**Nothing connected yet is normal for a new setup** — it doesn't mean anything is
broken. Just say *"connect my Facebook Ads"* (or any platform) and Claude will
hand you the link to get started.

---

## Your data & privacy

- **You sign in yourself.** Claude connects to Porter through a secure sign-in in
  your browser. Your platform passwords are never shared with Claude.
- **Only your own accounts.** Claude sees the marketing accounts you connect —
  nothing else.
- **Scoped access.** The plugin pre-approves permission prompts **only** for
  Porter's own website (`*.portermetrics.com`) — for uploading files and opening
  your hosted reports. It never widens access anywhere else; anything outside
  Porter still asks for your OK the normal way. (If you use Claude's Bash
  sandbox, see the [one-time setup](#if-you-run-claudes-bash-sandbox) above.)
- Porter Metrics is **GDPR** compliant and **SOC 2 Type II** and **ISO 27001**
  certified. See <https://portermetrics.com> for details.

---

## Getting help

Porter is built right into Claude, so the fastest help is Claude itself:

- **Something looks wrong?** Just tell Claude — *"this looks like a Porter bug"* —
  and it can report it to our engineering team for you. Reported issues are
  normally fixed within **24 hours**.
- **Wish Porter did something it doesn't?** Say so, and Claude can pass a feature
  request to our product team (it'll show you the request and ask before sending).
- **Prefer a human?** Email **[support@portermetrics.com](mailto:support@portermetrics.com)**
  or visit **[portermetrics.com](https://portermetrics.com)**.

---

## What's inside this repo

<sub>For the curious — you don't need any of this to use the plugin.</sub>

This repository is a Claude plugin **marketplace** with one plugin,
`porter-metrics`, which bundles:

- **`.mcp.json`** — connects Claude to the Porter MCP server at
  `https://mcp.portermetrics.com/mcp` (secure sign-in handled automatically).
- **`skills/porter-metrics/`** — the instructions that teach Claude to use Porter
  correctly.
- **`hooks/`** — a small, tightly-scoped rule that auto-approves the *permission*
  prompt for calls to `*.portermetrics.com` (and nothing else). It never widens
  access elsewhere. Note: Claude's Bash sandbox has a separate network allow-list
  a plugin can't populate — see the [one-time setup](#if-you-run-claudes-bash-sandbox).

```text
porter/
├── .claude-plugin/marketplace.json     # the marketplace catalog
└── plugins/porter-metrics/
    ├── .claude-plugin/plugin.json      # the plugin manifest
    ├── .mcp.json                       # the Porter MCP connection
    ├── skills/porter-metrics/SKILL.md  # how Claude uses Porter
    ├── hooks/hooks.json                # pre-approve *.portermetrics.com
    └── scripts/allow_porter_domains.py # the scoped approval rule
```

---

<div align="center">
<sub>Made by <a href="https://portermetrics.com">Porter Metrics</a> · the marketing operating system.</sub>
</div>
