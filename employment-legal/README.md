# Employment Counsel Plugin

In-house employment law workflows: hiring review, termination review, policy drafting, handbook updates, jurisdiction-aware wage & hour Q&A. Built around a jurisdictional footprint learned at cold-start — the plugin knows which states you're in and what's different about each.

**Every output is a draft for attorney review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. The professional acts stay human: you configure the jurisdictions and escalation rules, you verify the cited rules against current law, and you make the employment decision — the termination call, the classification, the conversation. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Primary workflows |
|---|---|
| **Employment counsel** | Termination review, policy drafting, wage/hour analysis |
| **HR business partners** | Hiring review, handbook questions, first-line wage/hour Q&A |
| **GC** | Escalation recipient for high-risk terms and RIFs |

## First run: cold-start

Asks which states and countries you have employees in, reads your handbook and three recent termination memos, builds a jurisdiction-aware escalation table.

```
/employment-legal:cold-start-interview
```

Your configuration is stored at `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` and survives plugin updates. In Claude Cowork, where that path isn't writable, setup saves to `claude-for-legal-config/` in your working folder instead — keep using the same folder across sessions.

## Prerequisites

- **Persistent data path.** The leave register, investigation logs, and expansion trackers are written to `~/.claude/plugins/config/claude-for-legal/employment-legal/`, a version-independent path that survives plugin updates. These files contain privileged and sensitive personnel information — make sure that directory is backed up and access-controlled.
- **Legal research access.** Skills in this plugin intentionally do not store substantive legal rules (salary thresholds, restrictive-covenant enforceability, final-pay timing, release consideration periods, country-specific employment frameworks, etc.). Every jurisdiction-specific rule is researched and cited at the time of review. This plugin ships only Slack and Google Drive connectors — no legal research connector — so make sure the session has access to the research tools you rely on (web search, a research connector you add via `/mcp`, team reference materials).
- **Outside counsel.** No country-specific or jurisdiction-specific legal advice is produced without outside counsel engagement on any close call or new jurisdiction.

## Skills

| Skill | Does |
|---|---|
| `/employment-legal:cold-start-interview` | Cold-start interview — learns jurisdictional footprint + escalation rules from handbook + term memos |
| `/employment-legal:customize` | Change one part of the practice profile (jurisdictions, risk posture, escalation, review rules) without re-running setup |
| `/employment-legal:hiring-review` | Offer letter + restrictive covenant review, jurisdiction check |
| `/employment-legal:termination-review` | Termination review with high-risk flag detection |
| `/employment-legal:policy-drafting [topic]` | Draft a policy with state supplements where needed |
| `/employment-legal:wage-hour-qa [question]` | Wage/hour or general employment Q&A, jurisdiction-aware |
| `/employment-legal:worker-classification` | Classify a proposed worker engagement and flag misclassification gaps |
| `/employment-legal:expansion-kickoff [country]` | Kick off international expansion planning for a new country |
| `/employment-legal:expansion-update [country]` | Update an in-progress expansion tracker |
| `/employment-legal:investigation-open` | Open a new internal investigation matter |
| `/employment-legal:investigation-add` | Add documents, interview notes, or observations to an open investigation |
| `/employment-legal:investigation-query` | Ask questions against an open investigation log |
| `/employment-legal:investigation-memo` | Draft or update the privileged investigation memo |
| `/employment-legal:investigation-summary` | Draft an audience-specific summary from the investigation memo |
| `/employment-legal:leave-tracker` | Check open leaves for deadline alerts and required decisions |
| `/employment-legal:log-leave` | Add a new leave to the leave register |
| `/employment-legal:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |
| `/employment-legal:handbook-updates` | Diff proposed changes against current handbook, flag state supplement impact |

Reference skills `internal-investigation` and `international-expansion` carry the detailed frameworks and templates — the per-mode skills above load them as needed.

## Interactive skills vs. recurring agents

The skills above run when you invoke them — for when you're working a matter. The agents below are designed for a recurring cadence — they do not run on their own; trigger them with a recurring reminder or an external scheduler:

| Agent | What it watches | Suggested cadence |
|---|---|---|
| **leave-tracker** | Open leaves with hard legal deadlines — FMLA, state equivalents (CA CFRA, NY PFL), USERRA, ADA leave as accommodation; fires decision-point alerts before deadlines are missed | Weekly (Monday) |

## How it learns

Your practice profile at `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## What this plugin does not do

- **No research connector ships with it.** Wage/hour thresholds, covenant enforceability, and final-pay rules are researched at review time from web search or a research tool you connect — not from a bundled connector.
- **No citator.** Nothing here checks whether an authority is still good law — keep your citator subscription.
- **It does not make employment decisions.** Termination and classification reviews are checklists and risk flags for counsel and HR; the decision and the conversation stay human.
- **It does not touch your HRIS.** Leave data is tracked in a local register unless you connect your own HRIS integration.

## Notes

- Jurisdiction awareness is central to this plugin. It knows which of your states differ on final-pay timing, covenants, and breaks — and researches the current rule at review time rather than reciting one.
- Termination review is NOT a replacement for the conversation with HR and the manager. It is a checklist that catches commonly missed items.
- Wage/hour Q&A cites the rule but flags close calls for human review.
