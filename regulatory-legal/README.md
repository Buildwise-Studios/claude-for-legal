# Regulatory Counsel Plugin

Watches regulatory feeds, diffs new regulations against your policy library, surfaces gaps. Learns your materiality threshold so it doesn't alert on every commissioner's speech. Wired for the Federal Register API and direct regulator feeds; no research connector ships with it.

**Every output is a draft for attorney review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. The professional acts stay human: you configure the watchlist and materiality threshold, you verify cited regulations against the primary source, and you decide whether a flagged change requires action, disclosure, or policy work. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Primary workflows |
|---|---|
| **Compliance / regulatory counsel** | Watchlist maintenance, gap triage, policy update coordination |
| **Privacy / product counsel** | Receives filtered alerts relevant to their area |
| **GC** | Escalation recipient for material gaps with deadlines |

## First run: cold-start

Asks which regulators you watch, connects your policy document folder, learns what "material" means to you. Builds a watchlist and indexes your policy library.

```
/regulatory-legal:cold-start-interview
```

## Skills

| Skill | Does |
|---|---|
| `/regulatory-legal:cold-start-interview` | Cold-start: watchlist + policy index + materiality threshold |
| `/regulatory-legal:customize [section]` | Change one profile setting (watchlist, materiality threshold, feed configuration) without re-running the full interview; maintains attestation dates |
| `/regulatory-legal:reg-feed-watcher` | Check feeds now, report what's new |
| `/regulatory-legal:policy-diff [reg]` | Diff a specific reg change against policy library |
| `/regulatory-legal:gaps` | Open gaps tracker — what's been flagged and not yet closed |
| `/regulatory-legal:comments` | Review open NPRM comment periods, log decisions, track deadlines |
| `/regulatory-legal:policy-redraft` | Proposed marked-up policy redraft that closes a gap — a first draft for internal review, not a direct edit to source documents |
| `/regulatory-legal:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |
| **gap-surfacer** *(reference)* | Shared gap- and comment-tracker framework loaded by `/regulatory-legal:gaps` and `/regulatory-legal:comments` |

## Interactive skills vs. recurring agents

The skills above run when you invoke them — for when you're working a matter. The agents below are designed for a recurring cadence — they do not run on their own; trigger them with a recurring reminder or an external scheduler:

| Agent | What it watches | Suggested cadence |
|---|---|---|
| **reg-change-monitor** | Regulatory feeds — filters by the materiality threshold learned at cold-start and posts a digest of the items that meet it | Weekly (daily if the regulatory environment is active) |

## Connectors and citation verification

**Connect a research tool first — the citation guardrails depend on it.** This plugin does not ship one — add CourtListener or your firm's research tool via `/mcp` to enable retrieval-backed citations. Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. The plugin works either way; it just does more of the verification for you when a research tool is connected.

A research connector isn't just a data source — it's the difference between a verified citation and a citation you have to check. A citation retrieved through a connected research tool is tagged with its source and can be traced back. A citation from the model's knowledge or from web search is tagged `[verify]` and should be checked against a primary source before anyone relies on it. The plugin tiers its citations so your verification time goes where it matters.

## Integrations

Ships with the general bucket of connectors in `.mcp.json`:

- **Slack** — search messages, read channels, find discussions
- **Google Drive** — search, read, and fetch documents

Add regulatory feed connectors available in your environment via `/mcp`. Direct regulator RSS/email works as a fallback.

## What this plugin does not do

- **No research connector ships with it.** Feed checks use the Federal Register API and regulator sites; case-law and statute cites come from model knowledge until you connect a research tool.
- **No citator.** Nothing here checks whether an authority is still good law — keep your citator subscription.
- **It does not edit your policies.** Policy redrafts are marked-up proposals for the policy owner; source documents are never touched.
- **Coverage is what you watchlist.** It only watches the regulators and feeds configured at cold-start — it is not a comprehensive regulatory database.

## Prerequisites

Owner notifications (gap assignments, due-date reminders, NPRM alerts) require a Slack MCP server in your environment. Without one, the gap tracker and comment tracker still work — notifications just won't post, and the skills will flag ungated items in the status report instead.

## How it learns

Your practice profile at `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. The `reg-change-monitor` agent watches the regulatory feeds and flags changes against your policy library. You can re-run setup, run `/regulatory-legal:customize` to change one setting, edit the file directly, or tell a skill to record a new position.

## Notes

- Materiality filtering is the core function. Nearly everything qualifies as "technically a regulatory change" — the plugin learns which changes matter to this practice.
- Policy diff compares against indexed policies. If the policy library isn't connected, diffs run against what you paste.
- This is the automated version of privacy-legal's `reg-gap-analysis`. Pair them: this one watches, that one deep-dives.

## Configuration

Your configuration is stored at `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` and survives plugin updates — you only run setup once. In Claude Cowork, where that path isn't writable, setup saves to `claude-for-legal-config/` in your working folder instead — keep using the same folder across sessions.
