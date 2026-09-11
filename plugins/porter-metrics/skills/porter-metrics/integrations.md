[← Milestones](milestones.md)

## 1 · Integrations — get their data in

Nothing else works until something is connected. But connecting is also the
step with the highest drop-off: it leaves the chat, goes through an OAuth
screen, and comes back. Ask for one, not a list.

| Step | How | What to ask |
|---|---|---|
| First source | `connect_account(connector=…)` returns an `authorization_url` — give it to them and **wait**. Then `list_accounts` to confirm. | "Where does most of your marketing budget go?" — Meta / Google Ads / TikTok / LinkedIn / my website (GA4) / my store (Shopify) |
| More accounts on it | `connect_account` again on the same connector | Only if `list_accounts` shows one and they mentioned managing several brands or clients. |
| A second source | `connect_account` on a different connector | "What would you want to see next to it?" — my site traffic / another ad platform / my store's sales / my email or CRM |

## What actually matters here

**One is enough to move on.** The second source is worth far more *after* they
have seen a report built from the first — then it's "add GA4 and you'll see
which of those clicks actually converted", which is a reason, not a chore.

**Wait for them.** The OAuth happens in their browser and you cannot finish it.
If `list_accounts` is still empty right after, wait a moment and retry once
before concluding anything.

**`connection_status` is not an error.** `available` means the platform reports
the account but Porter hasn't queried it yet; it becomes `connected` on first
use. Never present `available` to the user as a problem — it isn't one.

Pass the `account_id` through exactly as it came back. Never rebuild or shorten
it.

→ Next: [Reporting](reporting.md)
