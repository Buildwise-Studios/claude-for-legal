# AI Governance Plugin

In-house AI governance counsel workflows: use case triage, AI impact assessments,
vendor AI review, and regulation-to-policy gap analysis. Built around a team practice profile
learned from your AI policy, a reference impact assessment, and your key vendor AI
agreements.

**Every output is a draft for attorney review — cited, flagged, and gated — not a legal conclusion.** The plugin does the work: reads the documents, applies your playbook, finds the issues, drafts the memo. The professional acts stay human: you configure the use-case registry and red lines, an attorney authorizes them, you verify the citations, and you decide risk tier, materiality, and whether a use case proceeds. Citations are tagged by source so you know which ones came from a research tool and which ones need checking. Privilege markers are applied conservatively so nothing waives by accident. Consequential actions — filing, sending, executing — are gated behind explicit confirmation.

## Who this is for

| Role | Primary workflows |
|---|---|
| **Privacy counsel / AI governance counsel** | Impact assessments, vendor AI review, reg gap analysis |
| **Product counsel** | Use case triage, launch review with AI component |
| **GC / Legal ops** | AI policy governance, escalation, board-level issues |
| **Procurement / legal** | Vendor AI contract review |

## First run: the cold-start interview

The plugin interviews you to learn: are you a builder, deployer, or both — which
regulations actually apply — what your use case red lines are — and what good impact
assessment looks like here. Then it reads your seed documents and learns your real
positions and house style.

```
/ai-governance-legal:cold-start-interview
```

## Commands

| Command | Does |
|---|---|
| `/ai-governance-legal:cold-start-interview` | Cold-start interview — writes your practice profile |
| `/ai-governance-legal:customize [section]` | Change one practice-profile setting (risk posture, escalation contacts, registry entries) without re-running the full interview; maintains attestation dates |
| `/ai-governance-legal:ai-inventory [list \| add \| edit \| classify \| show]` | Manage the EU AI Act per-system inventory — track each system's role and risk tier |
| `/ai-governance-legal:use-case-triage [use case]` | Classify a use case against your registry (approved / conditional / never) |
| `/ai-governance-legal:aia-generation [use case]` | Run an AI impact assessment (AIA) in your house style |
| `/ai-governance-legal:vendor-ai-review [vendor/file]` | Review a vendor AI agreement against your positions |
| `/ai-governance-legal:reg-gap-analysis [regulation]` | Diff a new regulation or guidance against current policy/practice |
| `/ai-governance-legal:policy-monitor` | Weekly sweep for AI policy drift, or direct query for a proposed new practice |
| `/ai-governance-legal:policy-starter` | Draft a firm AI usage policy from published model policies, adapted to your practice profile (draft for attorney review) |
| `/ai-governance-legal:matter-workspace` | Manage matter workspaces (multi-client private practice only) — new, list, switch, close, none |

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | Writes `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` from interview + seed docs |
| **customize** | Guided edit of one practice-profile section without re-running the cold-start interview; maintains attestation dates |
| **ai-inventory** | EU AI Act per-system inventory — role (provider, deployer, importer, distributor, authorized rep, product manufacturer) and risk tier per system |
| **use-case-triage** | Classifies use cases against the registry; flags missing assessments |
| **aia-generation** | AI impact assessment (AIA) in house format |
| **vendor-ai-review** | AI-specific vendor contract review against governance positions |
| **reg-gap-analysis** | New reg/guidance vs. current state, remediation plan |
| **policy-monitor** | Crawls outputs for practice drift; drafts AI policy language updates |
| **policy-starter** | Produces a first-draft AI usage policy sourced from published model policies (ABA, state bars, ILTA, CLOC, NIST, EU AI Act, peer policies), adapted to your practice profile — draft for attorney review, not a finished policy |
| **matter-workspace** | Create, list, switch, and close matter workspaces for multi-client practices; isolates each client/matter so context does not leak across them |

## Quick start

### 1. Setup

```
/ai-governance-legal:cold-start-interview
```

Have ready (if they exist): your AI or acceptable use policy, one prior impact assessment,
key vendor AI agreements, model inventory or approved tool list.

Your configuration is stored at `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` and survives plugin updates. In Claude Cowork, where that path isn't writable, setup saves to `claude-for-legal-config/` in your working folder instead — keep using the same folder across sessions.

### 2. Triage a new use case

```
/ai-governance-legal:use-case-triage "Sales team wants to use AI to score leads automatically"
```

Output: risk tier, registry match or gap, required conditions, impact assessment needed
or not.

### 3. Run an impact assessment

```
/ai-governance-legal:aia-generation "AI-powered resume screening for HR"
```

Intake questions → impact assessment in your house format → policy consistency check →
mitigation conditions.

### 4. Review a vendor AI agreement

```
/ai-governance-legal:vendor-ai-review openai-terms.pdf
```

Output: term-by-term vs. your positions, proposed redlines, gaps to escalate.

## Plugin triangle: AI governance ↔ product counsel ↔ privacy

These three plugins are designed to work together. AI governance is the third leg.

- **Product counsel** detects when a launch has an AI component → hands off to
  `/ai-governance-legal:use-case-triage` and `/ai-governance-legal:aia-generation`
- **Privacy** detects when an AI use case involves personal data → hands off to
  `/privacy-legal:pia-generation`, if the plugin is installed
- **AI governance** detects when an impact assessment raises data protection issues →
  hands off to `/privacy-legal:pia-generation`, if the plugin is installed

The handoff is explicit: each plugin flags when the other is needed and states what
question to answer there.

## File structure

```
ai-governance-legal/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md
├── README.md
├── references/
│   └── currency-watch.md
└── skills/
    ├── cold-start-interview/
    ├── customize/
    ├── ai-inventory/
    ├── use-case-triage/
    ├── aia-generation/
    ├── vendor-ai-review/
    ├── reg-gap-analysis/
    ├── policy-monitor/
    ├── policy-starter/
    └── matter-workspace/
```

## How it learns

Your practice profile at `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. The `policy-monitor` skill sweeps for drift between your AI governance policy and your practice when you run it (weekly, via your own scheduler) and proposes updates. You can re-run setup, run `/ai-governance-legal:customize` to change one setting, edit the file directly, or tell a skill to record a new position.

## Connectors

Ships with Slack and Google Drive in `.mcp.json` — productivity connectors, not research sources. This plugin does not ship a case-law or regulatory research connector; add CourtListener or your firm's research tool via `/mcp` to enable retrieval-backed citations. Without one, cites to the EU AI Act, state AI statutes, and regulatory guidance come from model knowledge and are tagged `[verify]`.

## What this plugin does not do

- **No research connector ships with it.** AI-regulation and case-law cites come from model knowledge or web search until you connect a research tool.
- **No citator.** Nothing here checks whether an authority is still good law — keep your citator subscription.
- **It does not derive your obligations.** The AI inventory registers systems, roles, and risk tiers; the obligation analysis stays with the lawyer.
- **Consequential actions are gated.** Nothing is filed, sent, or published without explicit confirmation.

## Notes

- Gap check (`reg-gap-analysis`) handles incoming regulations. Policy monitor handles internal practice drift. Different tools for different directions of change.
- Policy monitor requires an outputs folder to be configured (set during setup) for the sweep to work. Direct-query mode works without it.
- Use case triage is only as good as the registry. Spend the setup interview getting
  the red lines right — they drive everything.
- Impact assessment format comes from your seed assessment. If you didn't provide one
  during setup, it uses a baseline structure — re-run setup with a reference to improve it.
- Builder and deployer obligations are treated separately. If you're both, the skills
  ask which hat you're wearing for each task.
- Gap analysis is manual (you point it at a regulation or guidance doc). For automated
  monitoring, pair with the `regulatory-legal` plugin, if the plugin is installed.
- The `## Company profile` section is the first block of `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` by convention. Company-level
  facts come from the shared `~/.claude/plugins/config/claude-for-legal/company-profile.md`,
  used by all plugins in this suite — edit that file to change the context everywhere.
