# Product Counsel Plugin

Product legal workflows: launch review, marketing claims review, feature risk assessment, and fast "is this a problem?" triage. Built around a risk calibration learned from your launch review history — what blocks at your company, not a generic standard.

**Every output is a draft for attorney review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. The professional acts stay human: you configure the risk calibration, you verify the cited rules, you decide what blocks and what ships, and the launch go/no-go is yours. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Primary workflows |
|---|---|
| **Product counsel** | Launch review, feature risk assessment, calibration maintenance |
| **Product managers** | "Is this a problem?" triage self-serve |
| **Marketing** | Claims review before ship |
| **GC / Legal leadership** | Feature risk assessments for escalated items |

## First run: the cold-start interview

Connects to your launch tracker (Jira/Linear), reads ten of your past launch reviews, and learns what you block vs. what you clear. Builds a risk calibration table that every other skill reads from.

Your configuration is stored at `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` and survives plugin updates. In Claude Cowork, where that path isn't writable, setup saves to `claude-for-legal-config/` in your working folder instead — keep using the same folder across sessions.

```
/product-legal:cold-start-interview
```

## Commands

| Command | Does |
|---|---|
| `/product-legal:cold-start-interview` | Cold-start interview |
| `/product-legal:customize [section]` | Change one profile setting (risk calibration, escalation contacts, review framework) without re-running the full interview; maintains attestation dates |
| `/product-legal:launch-review [PRD or ticket]` | Full launch review against your framework |
| `/product-legal:marketing-claims-review [copy]` | Marketing claims review |
| `/product-legal:feature-risk-assessment [feature or issue]` | Deep-dive risk assessment on one issue when launch review isn't enough |
| `/product-legal:is-this-a-problem [question]` | Fast "is this a problem?" answer |
| `/product-legal:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | Writes ~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md from interview + past launch reviews |
| **customize** | Guided edit of one practice-profile section without re-running the cold-start interview; maintains attestation dates |
| **launch-review** | Category-by-category review, calibrated to your company |
| **marketing-claims-review** | Claims taxonomy: puffery/factual/comparative/implied/absolute |
| **feature-risk-assessment** | Deep dive on one issue when launch review isn't enough |
| **is-this-a-problem** | Same-minute triage for the quick Slack question |
| **matter-workspace** | Create, list, switch, and close matter workspaces for multi-client practices; isolates each client/matter so context does not leak across them |

## Interactive commands vs. recurring agents

The commands above run when you invoke them — for when you're working a matter. The agents below are designed for a recurring cadence — they do not run on their own; trigger them with a recurring reminder or an external scheduler:

| Agent | What it watches | Suggested cadence |
|---|---|---|
| **launch-watcher** | Launch tracker (Jira/Linear) for upcoming launches that likely need legal review; filters tickets with launch dates in the next 30 days per the calibration table | Daily |

## Integrations

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. Skills work either way — but this plugin does not ship a case-law research connector; add CourtListener or your firm's research tool via `/mcp` to enable retrieval-backed citations.

Ships with connectors configured in `.mcp.json`:

- **Slack** — search messages, read channels, find discussions (general bucket)
- **Google Drive** — search, read, and fetch documents (general bucket)
- **Linear** — issue tracking and project management
- **Atlassian** — Jira issues and Confluence pages
- **Asana** — tasks and project tracking

With a tracker connected: cold-start pulls launch history, launch-review pulls ticket context, launch-watcher agent monitors the calendar.

## What this plugin does not do

- **No research connector ships with it.** The bundled connectors (Slack, Google Drive, Linear, Jira, Asana) are workflow tools; advertising, consumer-protection, and case-law cites come from model knowledge until you connect a research tool.
- **No citator.** Nothing here checks whether an authority is still good law — keep your citator subscription.
- **It does not approve launches.** Reviews and triage are calibrated drafts; the go/no-go is the counsel's call.
- **It does not write to your tracker.** Launch tickets are read for context; review outcomes are routed back through you.

## Quick start

```
/product-legal:cold-start-interview
```

Then:

```
/product-legal:is-this-a-problem "Can we A/B test the pricing page?"
```

→ Same-minute answer calibrated to your risk table.

```
/product-legal:launch-review PROJ-1234
```

→ Full review, category-by-category, with action items.

## How it learns

Your practice profile at `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, run `/product-legal:customize` to change one setting, edit the file directly, or tell a skill to record a new position.

## Notes

- Every review depends on the calibration table; if the table is wrong, every review is wrong. Re-run setup when your risk posture changes (new regulator, new consent decree, new GC).
- `is-this-a-problem` is designed for PMs to self-serve. It answers fast and routes to a real review when it should.
- Feature risk assessment is for the small minority of launches that need depth. Skip it for the rest rather than generating unnecessary paperwork.

## Prerequisites

Launch trackers (Linear, Jira, Asana) plus Slack and Google Drive are bundled in `.mcp.json`. Other integrations (document management, eDiscovery, case management, regulatory feeds) are not bundled — if you have an MCP server for one of these in your environment, the relevant features will use it. Without one, the plugin falls back to file upload and manual workflows. Run `/product-legal:cold-start-interview --check-integrations` to see what's available in your environment.

## Configuration

Your configuration is stored at `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` and survives plugin updates — you only run setup once.
