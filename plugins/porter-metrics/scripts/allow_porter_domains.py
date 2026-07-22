#!/usr/bin/env python3
"""PreToolUse gate that auto-approves network calls to Porter's own domains.

Why this exists
---------------
The Porter tools themselves run over the MCP transport and need no approval.
But two real flows have the *model* reach a Porter URL directly, and those would
otherwise interrupt the user with a permission prompt every time:

  * uploading a heavy asset — ``prepare_upload`` hands back a one-time signed URL
    on ``*.portermetrics.com`` that the model must ``PUT`` the bytes to;
  * fetching something Porter hosts — a report page, a signed download link.

A Claude Code plugin cannot ship an allow-list in ``settings.json`` (only the
``agent`` / ``subagentStatusLine`` keys are honoured there), so the supported way
to pre-approve a scoped set of calls is a ``PreToolUse`` hook that returns an
``allow`` decision. This is that hook.

Security model
--------------
It only ever *widens* to Porter's own domains, and only for calls it can prove
are scoped there. Anything it is not certain about is left to the normal
permission flow (it emits no decision — it never denies, so it can't break other
tools):

  * WebFetch — allow when the URL host is ``portermetrics.com`` or a subdomain,
    over https.
  * Bash — allow only a bare ``curl`` invocation with NO shell metacharacters
    (no ``; & | > < `` $()`` …) whose every URL is an https Porter host. A
    command that chains, pipes, or reaches any other host is deferred, so a
    prompt still guards it.

Everything else — other tools, other hosts, anything ambiguous — falls through
untouched.
"""
from __future__ import annotations

import json
import re
import sys
from urllib.parse import urlparse

_PORTER_HOST = re.compile(r"^(.+\.)?portermetrics\.com$", re.IGNORECASE)
# Shell control that could chain a second, unvetted command onto a curl we allow.
_SHELL_CONTROL = re.compile(r"[;&|<>`\n]|\$\(")
_URL = re.compile(r"https?://[^\s'\"]+", re.IGNORECASE)


def _is_porter_url(url: str) -> bool:
    try:
        p = urlparse(url)
    except ValueError:
        return False
    return p.scheme == "https" and bool(p.hostname) and bool(_PORTER_HOST.match(p.hostname))


def _webfetch_ok(tool_input: dict) -> bool:
    url = tool_input.get("url")
    return isinstance(url, str) and _is_porter_url(url)


def _bash_ok(tool_input: dict) -> bool:
    command = tool_input.get("command")
    if not isinstance(command, str) or not command.strip():
        return False
    if _SHELL_CONTROL.search(command):
        return False  # anything that could chain a second command → defer
    if command.split()[0] != "curl":
        return False  # only curl uploads/downloads, nothing else
    urls = _URL.findall(command)
    # Must target Porter, and ONLY Porter — one foreign URL and we defer.
    return bool(urls) and all(_is_porter_url(u) for u in urls)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return  # no decision → normal permission flow

    tool = payload.get("tool_name")
    tool_input = payload.get("tool_input") or {}

    allow = (tool == "WebFetch" and _webfetch_ok(tool_input)) or (tool == "Bash" and _bash_ok(tool_input))
    if not allow:
        return  # defer to the normal permission flow — never deny

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "permissionDecisionReason": "Porter Metrics — request scoped to *.portermetrics.com",
            }
        },
        sys.stdout,
    )


if __name__ == "__main__":
    main()
