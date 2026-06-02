# Claude for Law School Clinics

*AI-assisted support for clinical legal education.*

A plugin for law school clinics — the institutions where law students, supervised by clinical professors, provide free legal services to people who can't afford representation. Immigration, housing, family law, consumer protection, criminal defense, civil rights.

**Every output is a draft for student analysis and attorney review — marked, gated, and logged. The plugin scaffolds the work; the acts that stay human: the professor configures the clinic and supervision model, the student does the analysis and verifies every citation, the supervising attorney reviews and approves, and only a human sends or files anything. Nothing leaves the clinic without going through the supervision model the professor set at setup.**

## The problem this solves

Clinics are structurally capacity-constrained. A supervising professor manages 5–10 students. Each student carries a handful of cases while juggling classes. Students turn over every semester. Administrative tasks — intake write-up, first drafts, research starting points, status updates — consume hours that could go to advising clients. The result: long waitlists, limited caseloads, people who give up waiting.

This plugin cuts the time cost of everything *around* the lawyering, so the same students and professor serve meaningfully more clients — and students spend more time on the analysis and strategy that make clinical education worthwhile.

The design principle: accelerate the non-educational parts, preserve the analytical work.

## Who uses it

| Role | Runs | Gets |
|---|---|---|
| **Supervising professor** | `/legal-clinic:cold-start-interview` (once), `/legal-clinic:supervisor-review-queue` (if formal review enabled) | Clinic context configured, student work reviewed |
| **Students** | `/legal-clinic:ramp` (start of semester), then `/legal-clinic:client-intake`, `/legal-clinic:draft`, `/legal-clinic:memo`, `/legal-clinic:research-start`, `/legal-clinic:status`, `/legal-clinic:client-letter` | Starting points — never final work product |

## Commands

| Command | What it does | What it doesn't do |
|---|---|---|
| `/legal-clinic:cold-start-interview` | **Professor.** One-time clinic config: practice areas, jurisdiction, supervision style, handbook/rules upload | — |
| `/legal-clinic:build-guide` | **Professor.** Author a per-practice-area guide: intake questions, pedagogy posture (assist / guide / teach), review gates, cross-plugin checks | Doesn't replace `/legal-clinic:cold-start-interview` — this tunes skills for one practice area |
| `/legal-clinic:ramp` | **Students.** Semester onboarding: clinic procedures, tool walkthrough, practice exercises | Doesn't replace the professor's orientation |
| `/legal-clinic:client-intake` | Structured intake: practice-area templates, cross-area issue spotting, conflict flags, triage | Doesn't decide whether to take the case |
| `/legal-clinic:draft [doc]` | First draft: asylum apps, eviction answers, protective orders, demand letters — jurisdiction-aware | Doesn't produce final work product |
| `/legal-clinic:memo` | IRAC-scaffolded case analysis with research gaps flagged | Doesn't write the analysis — scaffolds it |
| `/legal-clinic:research-start [issue]` | Research roadmap: statutes, case law areas, Westlaw search terms | **Leads, not authoritative citations** — students verify everything |
| `/legal-clinic:status [audience]` | Case status summary: client-facing, internal, or court-ready | Doesn't file anything |
| `/legal-clinic:client-letter [type]` | Routine correspondence: appointment confirms, doc requests, brief updates | Doesn't do substantive advice — that's `/legal-clinic:status client` or a conversation |
| `/legal-clinic:deadlines` | Track case deadlines — add, cross-case rollup with warnings at 14/7/3/1 days, overdue flags | Doesn't calculate deadlines from triggering events; student does the math per local rules |
| `/legal-clinic:client-comms-log [case]` | Append-only per-case communication log — calls, emails, letters, in-person | Doesn't store substantive legal analysis; comm record only |
| `/legal-clinic:semester-handoff` | End-of-semester offboarding — per-case handoff memos for the next cohort | Doesn't close cases; cases closing at semester end get a final `/legal-clinic:status internal` memo and are marked closed in the handoff document |
| `/legal-clinic:supervisor-review-queue` | **Professor, if formal review enabled.** What's waiting, approve/edit/return | Optional — one of three supervision models |
| `/legal-clinic:customize` | Change one part of the clinic profile (jurisdiction, supervision style, templates, semester) without re-running setup | Doesn't replace `/legal-clinic:cold-start-interview` for first-time setup |

## Ethical and confidentiality preconditions

Before using this plugin with real client matters, confirm with your clinic's supervising attorney and your school's IT / ethics office:

1. **Your Claude account tier and its data retention and training policies.** Team, Enterprise, Work, Education, and individual accounts have different guarantees about retention, training use, and subprocessor handling. Confirm what applies to the clinic's account.
2. **Your client consent and disclosure practices for AI-assisted work** per ABA Formal Opinion 512 (2024), your state bar's AI guidance (if any), and Model Rules 1.1, 1.4, 1.6, and 5.3. Decide whether and how the clinic discloses AI use to clients; document it.
3. **How privileged and confidential material will be handled** — what gets pasted into sessions, where outputs are stored, who has access, how long material is retained, how student turnover affects access.
4. **Whether any of your clinic's practice areas involve heightened confidentiality** (immigration, criminal defense, domestic violence, some family and civil rights matters) that require additional safeguards — and decide whether the plugin is appropriate for those case types at all.

Do not skip this step. The cold-start interview (`/legal-clinic:cold-start-interview`) captures these decisions as Part 0 before any other configuration.

## Confidence markers

Skills across this plugin flag confidence inline so students and supervising attorneys can see where the scaffold is uncertain vs. where it's asserting. Every marker is a prompt to verify — nothing marked is trusted.

- `[AI-ASSISTED DRAFT — requires student analysis and attorney review]` — baseline label applied to every output. Review label, not part of client-facing content; strip before anything goes out.
- `[UNCERTAIN: specific reason]` — the skill is genuinely unsure on this call (minority rule, debatable issue, jurisdiction the skill doesn't know well). Used in memo, intake, status, draft.
- `[VERIFY: claim — check source]` — a claim stated as likely but unverified. Student must confirm before relying — citations, local rule formats, rule statements. Used heavily in research-start, draft, status, memo.
- `[RESEARCH NEEDED: ...]` — memo scaffold marker where a rule statement is a research gap, not a conclusion. The student runs `/legal-clinic:research-start` and fills it in.
- `[STUDENT ANALYSIS: ...]` — memo scaffold marker where the application is blank by design. The student's reasoning fills it.
- `[STUDENT CONCLUSION: ...]` — memo scaffold marker where the conclusion is blank by design.
- `[FACT NEEDED: ...]` — draft scaffold marker where a required fact is missing from case notes. Student gets the fact; no guessing.
- `CHECK WITH [PROFESSOR] BEFORE SENDING` / `BEFORE FILING` — supervision-flag label applied in "configurable flags" supervision mode to outputs on flagged topics.

Trust the flags more than the absence of flags. An unflagged statement means the skill is confident — it does not mean the student or attorney skips verification. ABA Formal Opinion 512 requires verification regardless.

## Built-in safeguards

Every output from every skill includes:

- **AI-assisted label** — requires student analysis and attorney review
- **Confidence indicators** — `[UNCERTAIN: ...]` where genuinely unsure, rather than guessing
- **Verification prompts** — specific things to fact-check before relying on output
- **Ethical reminders** calibrated to the task

These are designed to reinforce the clinical education model: the student does the thinking, the plugin does the heavy lifting around it.

**Research outputs specifically:** `/legal-clinic:research-start` gives leads and frameworks for the student to verify and develop. It explicitly does **not** provide legal citations as authoritative. This is both an ethical safeguard and a pedagogical feature — students still learn to research and use judgment; they just start from a better place.

## Supervision workflow (configurable)

The plugin does not impose a single review workflow — student draft → professor review → approved. Some clinics want a hard gate; others find it overly prescriptive for their supervision structure.

The cold-start interview asks the professor to choose:

1. **Formal review queue** — client/court-bound output queues, professor approves, all logged
2. **Configurable flags, informal review** — certain triggers label output "CHECK WITH PROFESSOR," no queue mechanism
3. **Lighter-touch** — standard safeguard labels on everything, professor supervises through existing clinic structure (case rounds, one-on-ones)

Changeable later by editing `~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md`. Your configuration is stored at that version-independent path and survives plugin updates. In Claude Cowork, where that path isn't writable, setup saves to `claude-for-legal-config/` in your working folder instead — keep using the same folder across sessions.

## Semester turnover: the `/legal-clinic:ramp` solution

Every semester, clinics rebuild from scratch. New students need weeks to learn procedures, tools, practice-area basics. `/legal-clinic:ramp` is the interactive onboarding — it reads the clinic handbook the professor uploaded at setup and teaches it, with low-stakes practice exercises (fake intake, practice draft, research roadmap) before the student touches a real case.

`/legal-clinic:ramp --card` generates the one-page student reference card: commands, what Claude can and can't help with, verification habits. Hand it out on day one.

## Framework: ABA Formal Opinion 512 (2024)

The ethical framework this plugin operates within. Lawyers may use generative AI but must ensure competence in the technology, maintain confidentiality, supervise outputs, communicate with clients about AI use where appropriate, and verify before relying. The safeguards above — labels, confidence indicators, verification prompts, the explicit non-authority of research outputs — are built for this model.

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | Professor's one-time setup — practice areas, jurisdiction, supervision style, seed docs |
| **build-guide** | Professor's per-practice-area guide — intake, pedagogy posture (assist/guide/teach), review gates, cross-plugin checks |
| **ramp** | Student semester onboarding — procedures, tools, practice exercises |
| **client-intake** | Practice-area-specific intake with cross-area issue spotting, conflict flags, triage |
| **draft** | First-draft generation — practice-area templates, jurisdiction-aware, explicitly starting point |
| **memo** | IRAC scaffolding with research gaps flagged — the analysis is the student's |
| **research-start** | Research roadmap — leads not authorities, students verify and develop |
| **status** | Audience-aware case summaries — client / internal / court |
| **client-letter** | Routine correspondence from templates |
| **supervisor-review-queue** | Optional formal review workflow — only active if professor chose it |
| **customize** | Change one part of the clinic profile without re-running setup |
| **deadlines** | Per-case deadline tracking, cross-case rollup, warning cadence, overdue flags |
| **client-comms-log** | Append-only per-case communication record — calls, emails, letters, in-person |
| **semester-handoff** | End-of-semester offboarding memos; mirror of `/legal-clinic:ramp` |

*(Two deprecated skills — `form-generation`, `plain-language-letters` — redirect to `/legal-clinic:draft` and `/legal-clinic:client-letter` + `/legal-clinic:status client` respectively.)*

## Connectors and citation verification

**Connect a research tool first — the citation guardrails depend on it.** Without one, every cite is tagged `[verify]` and the reviewer note above each deliverable records that sources weren't verified. The plugin works either way; it just does more of the verification for you when a research tool is connected.

The legal research connectors in this plugin are the difference between a verified citation and a citation you have to check. A citation retrieved through **CourtListener** (Free Law Project's U.S. court opinions and PACER dockets) or **Descrybe** (primary-law search, citation lookup, quoted-language verification) is tagged with its source and can be traced back. A citation from the model's knowledge or from web search is tagged `[verify]` and should be checked before anyone relies on it. The plugin tiers its citations so your verification time goes where it matters.

## What this plugin does not do

- **No citator.** CourtListener and Descrybe retrieve opinions and check treatment, but neither replaces KeyCite/Shepard's — students verify every cite against a primary source before it goes into client work.
- **It does not do the lawyering.** Intake, drafts, memos, and research roadmaps are scaffolds; the student's analysis and the supervising attorney's review are the work product.
- **It does not file, send, or advise clients.** Everything client- or court-bound goes through the supervision model the professor configured.
- **It does not calculate deadlines from triggering events.** The student does that math against local rules; the tracker just tracks.

## Integrations

Ships with connectors configured in `.mcp.json`:

- **CourtListener** — Free Law Project's U.S. court opinions, PACER dockets, citation verification
- **Descrybe** — primary-law search, citation lookup, treatment check, quoted-language verification
- **Courtroom5** — jurisdiction-aware procedural guidance for self-represented litigants
- **Slack** — search messages, read channels, find discussions
- **Google Drive** — search, read, and fetch documents

No Clio connector ships with this plugin — case data comes in via file upload, and case metadata is captured in local intake and status files. If your environment provides a Clio MCP server, record it in the practice profile's integrations table and the relevant skills will use it.

Account tier and data handling are part of the IT and ethics review described under "Ethical and confidentiality preconditions" above. Confirm with that review where session data is processed and retained for the clinic's account tier — do not assume client data remains on the local machine.

## How it learns

Your practice profile at `~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md` isn't static — it improves as you use the plugin. Skills tell you when an output used a default you should tune. You can re-run setup, edit the file directly, or tell a skill to record a new position.

## File structure

```
legal-clinic/
├── .claude-plugin/plugin.json
├── .mcp.json
├── CLAUDE.md                          # Professor's clinic config — written by cold-start
├── README.md
├── deadlines.yaml                     # operational deadline ledger
├── skills/                            # each skill is also the slash command /legal-clinic:<skill>
│   ├── cold-start-interview/          # Professor — one-time setup
│   ├── customize/                     # Change one profile setting without re-running setup
│   ├── build-guide/                   # Professor — per-practice-area guide
│   ├── ramp/                          # Students — semester onboarding
│   ├── client-intake/
│   │   └── references/intake-templates/  # populated copies live in the config dir
│   ├── draft/
│   ├── memo/
│   ├── research-start/
│   ├── status/
│   ├── client-letter/
│   ├── supervisor-review-queue/       # Professor, if formal review enabled
│   │   └── references/review-queue.yaml  # empty template — live queue lives in the config dir
│   ├── deadlines/
│   ├── client-comms-log/
│   ├── semester-handoff/
│   ├── form-generation/               # deprecated → /draft (reference-only)
│   └── plain-language-letters/        # deprecated → /client-letter, /status client (reference-only)
├── handoffs/                          # per-semester handoff memos
│   └── [YYYY-term]/
│       ├── _summary.md
│       └── [case-id].md
├── client-comms/                      # per-case communication logs
│   └── [case-id]/
│       └── log.md
└── hooks/hooks.json
```

## Prerequisites

Some features reference external integrations (document management, launch trackers, eDiscovery, case management, regulatory feeds). These are not bundled — if you have an MCP server for one of these in your environment, the relevant features will use it. Without one, the plugin falls back to file upload and manual workflows. Run `/mcp` to see what's available in your environment.
