# Litigation Counsel Plugin

In-house litigation counsel support for managing a portfolio of matters. Cold-start captures your risk calibration, dispute landscape, and house style — the frame every matter is triaged against. Uniform intake turns new matters into structured log entries and per-matter history files. Status rollups and deep-dive briefings read from the log.

Built for counsel who own many matters at once, most of which are run by outside firms. This plugin is a structured reasoning layer, not a matter management system. If you have LawVu / SimpleLegal / Onit, it does not replace them — it sits alongside them.

**Every output is a draft for attorney review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. The professional acts stay human: you configure the risk calibration, you verify every cite and deadline against the record and the rules, you decide what gets filed, and you sign what goes out. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Prerequisites

Several features reference Gmail and scheduled-tasks integrations. These require MCP servers configured in your environment — they are not bundled. Without them, outputs are written to files for manual sending:

- **Gmail MCP** — `/litigation-legal:oc-status` creates Gmail drafts if authenticated; otherwise falls back to markdown drafts in `oc-status/[YYYY-MM-DD]/[slug].md`.
- **Scheduled-tasks MCP** — no automatic scheduling is shipped. Set a recurring calendar reminder to invoke weekly commands.

The plugin runs end-to-end without either; the integrations are additive.

## Who this is for

| Role | Primary use |
|---|---|
| **In-house litigation counsel** | All of it — intake, triage, status, history, briefings |
| **Associate GC / Deputy GC** | Portfolio oversight, board reporting rollups |
| **GC** | Quick status on the portfolio, deep dive on any one matter |

## First run: cold-start

The cold-start interview writes the *house* practice profile — persistent across every matter. Three pillars:

- **Risk calibration** — appetite, materiality thresholds, reserve/disclosure triggers, settlement authority, insurance profile, severity-likelihood matrix
- **Landscape** — company, geographies, regulated status, dispute patterns, frequent adversaries, outside counsel bench, internal stakeholders
- **House style** — board/audit committee memo format, reserve memo format, outside counsel directive style, privilege conventions, escalation norms

It offers sensible defaults at each step (e.g., a 3×3 severity-likelihood grid) and keeps everything freeform-editable. If no written framework exists yet, the interview prompts you to articulate one.

```
/litigation-legal:cold-start-interview
```

Your configuration is stored at `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` and survives plugin updates. In Claude Cowork, where that path isn't writable, setup saves to `claude-for-legal-config/` in your working folder instead — keep using the same folder across sessions.

## Commands

| Command | Does |
|---|---|
| `/litigation-legal:cold-start-interview` | Cold-start → writes house `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` |
| `/litigation-legal:matter-intake` | Uniform intake → writes `matters/[slug]/` + appends to `_log.yaml` |
| `/litigation-legal:portfolio-status` | Portfolio rollup — risk distribution, upcoming deadlines, stale matters |
| `/litigation-legal:matter-briefing [slug]` | Deep briefing on one matter — read-ready before a GC or outside counsel call |
| `/litigation-legal:matter-update [slug]` | Append a dated event to a matter's history; refresh the log's `last_updated` |
| `/litigation-legal:matter-close [slug]` | Archive a matter out of the active portfolio (retained, not deleted) |
| `/litigation-legal:demand-intake [title]` | Pre-drafting context gathering for a demand letter (payment / breach / C&D / employment separation / preservation) |
| `/litigation-legal:demand-draft [slug]` | Draft the letter from intake — runs FRE 408 / privilege gate, outputs `.docx`, writes post-send checklist |
| `/litigation-legal:demand-received [path]` | Triage an inbound demand letter — options analysis, portfolio cross-check, hand off to matter/demand-intake |
| `/litigation-legal:subpoena-triage [path]` | Triage a subpoena — classify, scope/burden/privilege, objections framework, compliance plan |
| `/litigation-legal:legal-hold [slug] [--issue/--refresh/--release/--status]` | Issue, refresh, release, or report holds — writes `.docx` + updates log |
| `/litigation-legal:chronology [slug]` | Build or update a chronology from declared doc sources + uploads — tagged by significance per matter theory |
| `/litigation-legal:oc-status` | Draft weekly OC status-request emails across the portfolio; Gmail drafts if MCP available |
| `/litigation-legal:claim-chart` | Build or review an element chart — patent claim chart (infringement / invalidity / review) or civil element chart (any cause of action or defense) with gap detection |
| `/litigation-legal:brief-section-drafter [section]` | Draft a brief section in house style, consistent with the case theory — every fact cited, every case checked |
| `/litigation-legal:deposition-prep [witness]` | Build a deposition outline for a witness — documents, topics organized around case theory, impeachment material |
| `/litigation-legal:privilege-log-review [log or document set]` | First-pass privilege log review — obvious calls made, hard calls flagged for attorney review |
| `/litigation-legal:cite-check [path]` | Standalone citation verification — enumerate every cite, retrieve and read each via the configured research connector, per-cite verdicts (confirmed / miscited / misgrounded-partial / quote-mismatch / likely-fabricated) |
| `/litigation-legal:pre-suit-investigation [slug]` | Rule-11-oriented investigation plan — element-by-element evidence map, limitation audit, notice-requirement check |
| `/litigation-legal:complaint-drafter [slug]` | Plaintiff-side pleading draft — element-mapped counts, jurisdictional allegations, plausibility check, Rule 11 check |
| `/litigation-legal:discovery-requests [slug]` | Propound written discovery — interrogatories, RFPs, RFAs built from an element-to-evidence plan with proportionality framing |
| `/litigation-legal:damages-model [slug]` | Structured damages model — documented specials, expert-flagged projections, mitigation audit, low/mid/high scenarios |
| `/litigation-legal:settlement-demand [slug]` | Demand packages and mediation statements — candid liability assessment, documented damages, FRE 408 framing |
| `/litigation-legal:judgment-enforcement [slug]` | Post-judgment collection plan — asset discovery, enforcement device selection, exemptions audit, fraudulent-transfer screen |
| `/litigation-legal:matter-workspace <new / list / switch / close / none> [slug]` | Manage matter workspaces for multi-client practices — create, list, switch, close, or detach the active matter |
| `/litigation-legal:customize` | Change one practice-profile setting without re-running cold-start; maintains the attestation dates |

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | House practice profile — risk calibration, landscape, style |
| **matter-intake** | Uniform intake questions; writes matter file + log row |
| **portfolio-status** | Rollup across the log — risk, deadlines, staleness |
| **matter-briefing** | Deep read of one matter from its file + history |
| **matter-update** | Structured event append; updates `last_updated` in log |
| **matter-close** | Archive semantics; captures outcome |
| **demand-intake** | Adaptive context gathering for a demand letter — parties, facts, leverage, privilege filters |
| **demand-draft** | FRE 408 / privilege gate, then drafts `.docx` with `[CITE:___]` placeholders; writes post-send checklist; offers matter creation |
| **demand-received** | Triage an inbound demand — merit, options, portfolio cross-check |
| **subpoena-triage** | Classify subpoena, analyze scope/burden/privilege, produce objections framework + compliance plan |
| **legal-hold** | Issue / refresh / release / status-report on holds; writes `.docx` notice; updates log's `legal_hold` fields |
| **chronology** | Extract dated events from declared doc sources + uploads; de-dupe; tag significance per matter theory |
| **oc-status** | Weekly portfolio-wide OC status-request email drafter; markdown + Gmail drafts |
| **claim-chart** | Patent claim chart (infringement / invalidity / review) or civil element chart (any cause of action or defense). Element-by-element mapping, every cell pin-cited, gap detection. Ships with a cause-of-action template library. |
| **brief-section-drafter** | Draft a brief section in house style, tied to the case theory — every fact cited, every case checked |
| **deposition-prep** | Deposition outline for a witness — documents pulled, topics organized around case theory, impeachment material surfaced |
| **privilege-log-review** | First-pass privilege log review — obvious privilege calls made, close calls flagged for attorney review |
| **cite-check** | Standalone citation verification — exhaustive enumerate-then-batch coverage with per-cite verdicts and mandatory retrieval-and-read when a research connector is configured |
| **pre-suit-investigation** | Pre-filing factual and legal investigation — evidence mapping, limitations audit, pre-suit notice requirements |
| **complaint-drafter** | Plaintiff-side pleading drafts — element mapping, jurisdictional allegations, Iqbal/Twombly plausibility check, Rule 11 check |
| **discovery-requests** | Interrogatories, requests for production, and requests for admission from an element-to-evidence discovery plan |
| **damages-model** | Damages quantification — itemized specials, expert-flagged future damages, mitigation audit, scenario ranges |
| **settlement-demand** | Demand letters and confidential mediation statements with documented damages and candid risk assessment |
| **judgment-enforcement** | Post-judgment collection — asset discovery, garnishment/levy/lien selection, exemptions, fraudulent-transfer screening |
| **matter-workspace** | Create / list / switch / close / detach matter workspaces for multi-client practices |
| **customize** | Guided practice-profile changes without re-running the interview; maintains attestation dates |

Eight litigation skills also ship an England & Wales reference (`references/uk.md`) — when the practice profile's procedural frame is England & Wales (CPR), the skill loads it and works in that frame (CPR pleading standards, PD 57AC witness statements, PD 57AD disclosure, Part 36, witness summonses) instead of silently applying US doctrine. The E&W content is staged for practitioner review.

## Interactive commands vs. recurring agents

The commands above run when you invoke them — for when you're working a matter. The agents below are designed for a recurring cadence — they do not run on their own; trigger them with a recurring reminder or an external scheduler:

| Agent | What it watches | Suggested cadence |
|---|---|---|
| **docket-watcher** | Court dockets for matters in the active portfolio — pulls new filings, computes candidate deadlines, cross-references each matter's history and deliverables | Weekly |

## How the data is organized

```
~/.claude/plugins/config/claude-for-legal/litigation-legal/
├── CLAUDE.md                          # HOUSE practice profile — risk, landscape, style
├── matters/
│   ├── _log.yaml                      # the portfolio ledger (one entry per matter)
│   └── [matter-slug]/
│       ├── matter.md                  # matter-specific intake + theory + posture
│       ├── history.md                 # append-only event log
│       ├── chronology.md              # advocacy-facing timeline (on demand)
│       └── legal-hold-v[N].docx       # hold notices (issue, refresh, release)
├── demand-letters/                    # outbound demands
│   └── [slug]/
│       ├── intake.md
│       ├── draft-v1.docx
│       └── checklist.md
├── inbound/                           # incoming demands, subpoenas, regulator letters
│   └── [slug]/
│       ├── incoming.[ext]
│       ├── triage.md
│       └── response-v1.docx           # if a response is sent
└── oc-status/                         # weekly OC status-request drafts
    └── [YYYY-MM-DD]/
        ├── _summary.md
        └── [slug].md                  # one email per matter
```

All matter data lives in this config directory, which survives plugin updates — not inside the installed plugin folder. The same-named directories shipped with the plugin are schema documentation and templates. Where the home path is not writable (e.g., Claude Cowork), the same tree is rooted at `claude-for-legal-config/litigation-legal/` in your working folder.

Separate folders because each has a distinct workflow. Matters get tracked in the portfolio; demand letters and inbound items may or may not rise to a matter; OC status drafts are periodic artifacts. When things relate, the `related_matters` field and cross-links in `matter.md` tie them together.

The log is YAML because it's parseable by rollup skills. Per-matter files are markdown because that's where you read and edit. Both are stored in the folder as plain text — no proprietary file formats.

## Connectors and citation verification

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. The plugin works either way; it just does more of the verification for you when a research tool is connected.

The legal research connectors determine which citations arrive verified and which need checking. A citation retrieved through **CourtListener** (U.S. court opinions, PACER dockets, citation verification), **Trellis** (state trial court dataset — dockets, rulings, verdicts, judge and opposing counsel analytics), **Everlaw** (your eDiscovery projects), or **Aurora** (read-only Consilio ediscovery — every record cited to source) is tagged with its source and can be traced back. A citation from the model's knowledge or from web search is tagged `[verify]` and should be checked against a primary source before anyone relies on it. The tiering directs verification time to the citations that need it.

## Integrations

Ships with connectors configured in `.mcp.json`:

- **CourtListener** — U.S. court opinions, PACER dockets, citation verification
- **Trellis** — state trial court dockets, rulings, verdicts, judge and opposing counsel analytics
- **Everlaw** — search and retrieve documents from your Everlaw projects
- **Aurora** — read-only Consilio eDiscovery, every record cited to source
- **TopCounsel** — outside counsel recommendations from The L Suite
- **Slack** — search messages, read channels, find discussions
- **Google Drive** — search, read, and fetch documents

Designed to be useful with nothing connected. Relativity, DISCO, CLM, and email connectors are not included.

## What this plugin does not do

- **No citator.** CourtListener retrieves opinions and Trellis covers state trial courts, but nothing here is a KeyCite/Shepard's replacement — run cites through your citator before filing.
- **It is not a matter management system.** It sits alongside LawVu / SimpleLegal / Onit as a reasoning layer, not a replacement.
- **It does not file or serve anything.** Demands, holds, and brief sections are drafts behind explicit gates; unresolved `[CITE]` / `[VERIFY]` markers mean not final.
- **U.S. coverage only.** CourtListener/PACER for federal, Trellis for state trial courts; no non-US court data ships with it.

## How it learns

Your practice profile at `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## Notes

- Every skill reads from `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` first. If your risk appetite changes or you bring on new outside counsel, update it — don't paper over it in individual matters.
- `## Company profile` is the first section of `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` by convention. Its company-level fields are sourced from the shared `company-profile.md` in the same config folder — edit there once and every `-legal` plugin picks up the change.
- `_log.yaml` is the source of truth for portfolio state. Keep it clean.
- Matter history is append-only. If something was wrong, note the correction as a new entry — don't edit the past.
- Closed matters stay in `_log.yaml` (searchable history). `/litigation-legal:portfolio-status` filters them out of active rollups by default.

## Inline marker conventions

Three markers appear in skill outputs and drafts. They are not disclaimers — they are action items:

- `[CITE: specific cite needed]` — a legal authority placeholder. Counsel fills or confirms before sending.
- `[VERIFY: specific fact]` — a factual assertion not yet confirmed to source. Counsel verifies before relying.
- `[SME VERIFY: specific judgment call]` — a judgment (merit read, significance tag, objection strength, privilege status) that requires subject-matter expert review. SME = licensed attorney qualified in the relevant jurisdiction / area. Used liberally — anything judgment-heavy should carry this.

A draft or triage with unresolved markers is not final, regardless of how polished it reads.
