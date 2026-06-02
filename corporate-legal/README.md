# Corporate Counsel Plugin

In-house corporate counsel workflows across four practice areas: M&A deals, board and corporate secretary, public company governance, and entity management. Activate only the modules that apply to your role. The cold-start interview is modular — it asks targeted questions per active area and writes only the relevant sections to your practice profile.

**Every output is a draft for attorney review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. The professional acts stay human: you configure the thresholds, you verify extracted terms against the underlying documents, and you decide what goes into a schedule, a consent, or a filing — and only you execute or file it. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Active modules |
|---|---|
| **In-house M&A counsel** | M&A |
| **Corporate / assistant secretary** | Board & Secretary |
| **GC at a public company** | M&A + Public Company + Board & Secretary |
| **GC at a private company** | M&A + Board & Secretary + Entity Management |
| **Legal ops / solo GC** | Whichever apply — mix and match |

## First run

```
/corporate-legal:cold-start-interview
```

Walks through module selection, then a short targeted interview for each active area. Writes a modular `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` with only the relevant sections. Your configuration is stored at that path and survives plugin updates. In Claude Cowork, where that path isn't writable, setup saves to `claude-for-legal-config/` in your working folder instead — keep using the same folder across sessions.

Per-deal setup (M&A module only):

```
/corporate-legal:cold-start-interview --new-deal
```

## Commands

| Command | Does |
|---|---|
| `/corporate-legal:cold-start-interview` | Modular cold-start, or `--new-deal` / `--module [m&a \| board \| public \| entities]` |
| `/corporate-legal:customize` | Change one profile setting — risk posture, modules, thresholds, formats — without re-running the interview |
| `/corporate-legal:diligence-issue-extraction [folder]` | Read VDR docs, extract issues in house format |
| `/corporate-legal:tabular-review` | Tabular review — one row per document, one column per data point, every cell cited to source, Excel output |
| `/corporate-legal:deal-team-summary` | Tiered briefs — exec / deal lead / working team |
| `/corporate-legal:material-contract-schedule` | Material contracts disclosure schedule from diligence findings |
| `/corporate-legal:closing-checklist` | Closing checklist — what's blocking, critical path |
| `/corporate-legal:ai-tool-handoff` | Luminance/Kira bulk-extraction handoff + QA layer |
| `/corporate-legal:board-minutes` | Draft board and committee minutes in house format |
| `/corporate-legal:written-consent` | Unanimous written consent — precedent-matched draft + signatory tracker |
| `/corporate-legal:entity-compliance` | Entity compliance tracker — init, report, update, audit, export |
| `/corporate-legal:integration-management` | Post-closing integration workplan, consents tracker, contract assignment, status reports |
| `/corporate-legal:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |

## Prerequisites

Slack, Google Drive, and Box are bundled in this plugin's `.mcp.json` (along with iManage, TopCounsel, Definely, and Solve Intelligence — see Integrations below). SharePoint, Intralinks, and Datasite are **not bundled** — they require MCP servers configured in your environment. Without a given connector, the plugin falls back to file output (drafts written locally rather than posted to a channel, tracker files written to disk rather than read from a connected repository).

Configure MCP servers in `.mcp.json` at the repo or user level. Skills and agents will detect what's available at runtime and adjust behavior.

## Skills

| Skill | Module | Purpose |
|---|---|---|
| **cold-start-interview** | All | Modular interview — activates only relevant sections |
| **diligence-issue-extraction** | M&A | VDR docs → issues in house format, by category |
| **tabular-review** | M&A | Review a document set against a typed column schema; cited cells; `.xlsx` / `.csv` / markdown output; feeds material-contract-schedule |
| **deal-team-summary** | M&A | Tiered briefs: exec / deal lead / working team |
| **material-contract-schedule** | M&A | Disclosure schedule per purchase agreement definition |
| **closing-checklist** | M&A | Self-updating: ingests from diligence and schedule builds |
| **ai-tool-handoff** | M&A | Luminance/Kira integration — bulk extraction + QA layer |
| **board-minutes** | Board & Secretary | Calendar-detected meetings → draft minutes in house format |
| **written-consent** | Board & Secretary | Unanimous written consents with precedent search from consents repository; scope warning for major one-off actions |
| **entity-compliance** | Entity Management | Compliance calendar tracker (YAML); filing deadlines by entity and state; health audit; CT Corp report ingestion; CSV export |
| **integration-management** | M&A | Post-closing integration tracker; phased workplan (Day 1/30/90/180); Required Consents tracker with PA deadlines; contract assignment at scale (repository or manual list); weekly status reports |
| **matter-workspace** | All | Create, list, switch, and close matter workspaces for multi-client practices; isolates each client/matter so context does not leak across them |

*The entity and transaction skills cover private companies. The Public Company module provides profile configuration only — §16, insider trading, and disclosure committee settings that inform ad-hoc questions; it ships no workflow skills.*

## Interactive commands vs. recurring agents

The commands above run when you invoke them — for when you're working a matter. The agents below are designed for a recurring cadence — they do not run on their own; trigger them with a recurring reminder or an external scheduler:

| Agent | Module | What it watches | Suggested cadence |
|---|---|---|---|
| **dataroom-watcher** | M&A | VDR for new document uploads; flags uploads that match high-priority categories; runs closing checklist status | Daily during active diligence |

## Integrations

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. Skills work either way — but this plugin does not ship a case-law research connector; add CourtListener or your firm's research tool via `/mcp` to enable retrieval-backed citations. (Solve Intelligence, below, covers patent and prior-art literature, not case law.)

Ships with:

- **Slack** — search messages, read channels, find discussions (general bucket)
- **Google Drive** — search, read, and fetch documents (general bucket)
- **Box** — data room and document management
- **iManage** — DMS access, permission-bound and auditable
- **TopCounsel** — outside counsel recommendations from The L Suite
- **Definely** — contract structure: definitions, cross-references, structural diffs
- **Solve Intelligence** — patent and non-patent literature search, prior art, claim analysis

Intralinks, Datasite, and other VDR connectors can be added to `.mcp.json` when partner URLs are available.

## What this plugin does not do

- **No case-law research connector ships with it.** Solve Intelligence covers patent literature; statutes and case law come from model knowledge (tagged `[verify]`) until you connect a research tool.
- **No citator.** Nothing here checks whether an authority is still good law — keep your citator subscription.
- **It does not run your data room.** Diligence skills read what you point them at; a 500-document first-pass review is a review-platform job, not a single-agent task.
- **It does not file or execute.** Consents, schedules, and checklists are drafts; filing and signing stay with the lawyer.

## How it learns

Your practice profile at `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## M&A notes

- Issue extraction applies materiality thresholds — does not read every document if threshold says top N by value.
- Buy-side and sell-side are both supported. Practice Profile captures which side applies to this deal; skills adjust posture accordingly.
- AI tool handoff (Luminance/Kira) is optional. If `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` says no tool, all extraction runs through the direct skill.
- Closing checklist initializes from the purchase agreement, then self-updates as diligence surfaces consents required.
