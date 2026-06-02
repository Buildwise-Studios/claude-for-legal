---
name: pre-suit-investigation
description: Structure the factual and legal investigation Rule 11 requires before filing — claim hypothesis, element-by-element evidence plan, witness interview outlines, defendant collectability screen, limitations audit, pre-suit notice check, and a ready-to-plead / not-ready assessment per element. Use when the user says "we're thinking about suing", "are we ready to file", "pre-suit investigation", or wants to plan the factual workup before drafting a complaint.
argument-hint: "[slug] [--claims=<comma-separated theories>] [--full]"
---

# /pre-suit-investigation

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, side, work-product header, risk calibration, landscape, conflicts clearance, document storage. Config lives at the home path or, in environments where that isn't writable (Claude Cowork), at `./claude-for-legal-config/litigation-legal/` in the working folder — check both; home wins if both exist.
2. If matter workspaces enabled, confirm or select the active matter; otherwise resolve the slug from the argument.
3. Follow the workflow and reference below.
4. Conflicts gate: confirm the matter is in `_log.yaml`; refuse and route to `/litigation-legal:matter-intake` if not.
5. Capture the claim hypothesis: what happened, who's liable, under what theory (or theories — `--claims` seeds the candidate list).
6. Build the investigation plan: for each element of each candidate claim, what evidence exists or could be obtained pre-suit.
7. Draft witness interview outlines for non-party witnesses; flag the no-contact rule for anyone represented.
8. Run the defendant collectability screen — public records only.
9. Run the limitations audit (every candidate claim gets a limitations date, all `[verify]`) and the pre-suit notice check.
10. Write `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/pre-suit-investigation.md` and the evidence-preservation checklist; append to `history.md`.
11. Confirm with the user: "Here's the ready-to-plead read per element — anything I miscalled?" Close with the decision tree.

---

# Pre-Suit Investigation

## Purpose

Rule 11(b) makes the signature on a complaint a certification: the factual contentions have evidentiary support (or will likely have it after discovery), and the legal contentions are warranted by existing law or a nonfrivolous argument to extend it. The investigation that earns that signature happens before filing, not after. This skill structures it — so the decision to file is made on an element-by-element evidence map instead of a hunch, and so the gaps are visible while there's still time to close them.

The output is an investigation memo, not a complaint. Drafting the pleading comes later; the memo is what establishes whether there is a supportable basis to draft it.

## Jurisdiction assumption

This skill's frame is US federal practice — Rule 11 (pre-filing inquiry), Rule 4.2 of the ABA Model Rules (the no-contact rule), state statutes of limitations, and US-style pre-suit notice statutes. State analogs to Rule 11 (e.g., California CCP § 128.7, Texas Rule 13) differ in safe-harbor mechanics and sanctions exposure `[model knowledge — verify]`. **If the matter, the parties, or the forum is non-US, say so before doing substantive work**, per the plugin CLAUDE.md `## Jurisdiction recognition`: the pre-action protocols of England & Wales, the demand-letter prerequisites of civil-law systems, and limitation regimes elsewhere are materially different, and applying the US frame produces an answer that looks right and isn't. Tag every conclusion `[US framework — verify against [jurisdiction] law]` if the user asks you to proceed anyway, and offer to search for the applicable standard or route to a local practitioner.

## Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → `## Side` (this is a plaintiff-posture skill — if the practice default is defense, confirm the user is acting as plaintiff for this matter), `## Outputs` (work-product header, reviewer note format), `## Decision posture`, risk calibration, landscape (frequent adversaries — a known adversary changes the collectability and retaliation read), conflicts clearance, document storage.
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/matter.md` — what intake captured: parties, theory, key dates, source.
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` — for the conflicts gate.
- Anything the user uploads or points at this session: client documents, contracts, correspondence, prior demand letters.

If the config CLAUDE.md has `[PLACEHOLDER]` markers, surface the bounce per plugin convention:

> I notice you haven't configured your practice profile yet — that's how I tailor risk calibration, landscape, and house style to your practice.
>
> **Two choices:**
> - Run `/litigation-legal:cold-start-interview` (2 minutes) to configure your profile, then I'll run this tailored to your practice.
> - Say **"provisional"** and I'll run this against generic defaults — US jurisdiction, middle risk appetite, lawyer role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

**Conflicts gate — unbypassable.** Before doing investigation work, check `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't plan an investigation against a prospective defendant who hasn't been conflicts-cleared — the conflicts check is the gate."

Pre-suit matters intake with `source: pre-suit-threat` and `role: plaintiff`. Do not proceed on an unintaken matter.

## Hard rules — investigation conduct

These are not style preferences. They are conduct rules whose violation has professional-responsibility consequences, and the skill enforces them rather than merely mentioning them.

1. **No contact with represented parties.** If the prospective defendant (or any witness) is known or reasonably believed to be represented by counsel in this matter, the no-contact rule (ABA Model Rule 4.2 and state analogs `[model knowledge — verify]`) bars communication about the subject of the representation without their counsel's consent. The skill never drafts outreach to a represented party, never suggests informal contact with one, and flags every witness whose representation status is unknown: `[review — confirm representation status before any contact]`. Constituents of a represented organization (officers, directors, managing agents, and employees whose acts bind the organization) are covered too — flag them.
2. **No pretexting, no misrepresentation.** Investigation methods that involve misrepresenting identity or purpose — pretext calls, fake personas, posing as a customer to extract admissions — implicate Model Rules 4.1 and 8.4(c) and, in some jurisdictions, criminal statutes. The skill does not plan, outline, or assist them. If the user proposes one, decline that step, say why, and offer the lawful alternative (formal discovery after filing, a public-records request, a preservation demand).
3. **Public records only for asset and collectability searches.** Pre-suit asset screening uses public sources: real-property records, UCC filings, corporate registries, court dockets, SEC filings, published news. No credit pulls (FCRA permissible-purpose limits apply pre-judgment `[model knowledge — verify]`), no bank-account discovery, no data brokers whose sourcing can't be verified as lawful.
4. **Preservation-friendly collection.** Evidence the client already holds is collected in a way that preserves metadata and chain of custody — copies, not originals moved; exports, not forwarded emails where avoidable. The client's own preservation duty has already attached (see Step 7).

## Workflow

### Step 1: Claim hypothesis

Capture the working theory in three sentences, not three pages:

- **What happened** — the core factual narrative, dated.
- **Who's liable** — each prospective defendant, and for entities, the specific entity (parent vs. subsidiary matters for both liability and collectability).
- **Under what theory** — the candidate causes of action. Seed from `--claims` if given; otherwise elicit. List every plausible theory now (breach of contract, fraud, breach of fiduciary duty, statutory claims, unjust enrichment as a fallback) — the limitations audit and notice check run per claim, and a theory dropped here is a theory whose deadline nobody is watching.

If a claim-element framework would help, offer `/litigation-legal:claim-chart --civil` — the element chart and this investigation plan are complements: the chart says what must be proved; this plan says how to get the proof.

### Step 2: Investigation plan — per element, per claim

For each candidate claim, list the elements (from the pattern instruction or statute, tagged per source-tag discipline — elements stated from training knowledge are `[model knowledge — verify]`). For each element, build the evidence inventory:

| Element | Evidence in hand | Evidence obtainable pre-suit | How to get it | Evidence only available in discovery |
|---|---|---|---|---|
| [element] | [client docs, with paths] | [what + source] | [method] | [what can't be obtained until after filing] |

Pre-suit evidence sources to work through systematically:

- **Client documents** — contracts, correspondence, internal records. Ask for paths; read what's pointed at; never characterize a document that wasn't read (`[not yet reviewed]` is the honest tag).
- **Public records** — court dockets (prior suits by or against the defendant), property records, corporate registry filings, professional-license records.
- **Witness interviews** — non-party witnesses (Step 3 builds the outlines).
- **FOIA / state public-records requests** — agency records, inspection reports, complaint histories. Note response-time reality: federal FOIA's statutory 20 working days is routinely exceeded `[model knowledge — verify]`; build the lag into the filing timeline.
- **Regulatory filings** — SEC filings (EDGAR), state insurance filings, environmental disclosures, recall notices.
- **Corporate registries** — Secretary of State records: entity status, registered agent (needed for service anyway), officers and directors, mergers and name changes.
- **Social media and public web** — public posts only, collected in a preservation-friendly way (capture with timestamps and URLs; no friending, following, or connection requests made to access non-public content — that's pretexting).

The Rule 11 question this table answers: **for each element, does evidentiary support exist now, or is it specifically identified as likely to exist after a reasonable opportunity for discovery?** Rule 11(b)(3) permits the latter — but only if the pleading says so, and only if the belief is reasonable. An element with nothing in either column is a `not ready` element.

### Step 3: Witness interview outlines

For each non-party witness:

- **Who they are and what they likely know** — tied to specific elements from Step 2.
- **Representation check first.** Before any outline is used: is this person represented in this matter? Are they a current employee, officer, or managing agent of a represented (or soon-to-be-represented) organization? If yes or unknown → `[review — no-contact rule; confirm status before contact]`. The outline gets drafted; the contact decision is the attorney's.
- **The outline** — open-ended questions first (what happened, in their words), documents to show them, specific factual gaps from Step 2 this witness could close, and the closing questions: who else knows, what documents exist, will they give a declaration.
- **Required disclosures** — the interviewer identifies themselves and who they represent, and tells an unrepresented witness they are not their lawyer (Model Rule 4.3 `[model knowledge — verify]`). Build this into the top of every outline.
- **Preservation ask** — every witness interview ends with a request to preserve their relevant documents and messages.

### Step 4: Defendant collectability screen

Is the defendant worth suing? Public records only (Hard rule 3):

| Check | Source | What it tells you |
|---|---|---|
| Real property | County recorder / assessor | Attachable assets, existing liens with priority |
| UCC filings | Secretary of State | Secured creditors with priority |
| Corporate status | Secretary of State registry | Active / dissolved / forfeited; shell risk |
| Prior judgments | Court dockets | Other creditors in line; pattern of non-payment |
| Bankruptcy history | PACER | Discharge risk; serial-filer pattern |
| Insurance likely? | Industry norms, contract insurance clauses | The realistic source of recovery in many cases |
| Parent / affiliate structure | Registry + SEC filings | Whether the entity to be sued is the entity with assets |

Output: a one-paragraph collectability read with a confidence level. A strong claim against an empty defendant is a business decision, not a legal one — say so plainly and put it in the memo. If the user wants the deep version after judgment is hypothetically entered, that workflow lives in `/litigation-legal:judgment-enforcement`; the pre-suit screen is the cheap preview.

### Step 5: Limitation-period audit

For **every** candidate claim from Step 1 — including the ones the user is lukewarm on:

| Claim | Accrual event | Limitations period | Date it runs | Tolling theories | Status |
|---|---|---|---|---|---|
| [claim] | [what starts the clock + when it happened] | [N years `[verify]`] | [YYYY-MM-DD `[verify]`] | [discovery rule / fraudulent concealment / equitable tolling / minority — flagged, not assumed] | 🟢 comfortable / 🟡 inside 6 months / 🔴 imminent or arguably passed |

Rules for this table:

- Every period and every computed run date is `[verify]` — limitations periods are jurisdiction-specific, claim-specific, and frequently amended. If a research connector is available, retrieve the statute and tag with the connector; otherwise `[model knowledge — verify]`.
- Tolling theories are **flagged, never assumed**. A memo that quietly relies on the discovery rule to make a stale claim look fresh is a memo that gets the client sanctioned. State the limitations date without tolling, then state the tolling theory separately with what it requires.
- The accrual event itself is often the contested issue (when did the claim accrue — injury, discovery, last act?). Where accrual is arguable, show both dates.
- A 🔴 row is an escalation trigger per the practice profile's risk calibration: surface it immediately, not at the end of the run.

### Step 6: Pre-suit notice requirements

Some claims cannot be filed without a notice step that has its own deadline — and missing it is often fatal regardless of the limitations period. Check each candidate claim and defendant type against, at minimum:

- **Government defendants** — federal (FTCA administrative claim, 2 years to present `[verify]`) and state/local government claims acts (some as short as 6 months `[verify]`, e.g., California Government Claims Act). The notice deadline is usually much shorter than the limitations period.
- **Medical malpractice** — many states require pre-suit notice, expert affidavits / certificates of merit, or screening panels `[verify per jurisdiction]`.
- **Shareholder derivative claims** — demand on the board, or pleading demand futility with particularity (Rule 23.1 / state analogs) `[verify]`.
- **Contractual notice-and-cure** — the contract itself may require notice and a cure period before suit; read the dispute-resolution clause. Mandatory mediation or arbitration clauses redirect the whole filing plan.
- **Consumer / statutory claims** — some statutes (e.g., California CLRA `[verify]`, many state consumer-protection acts) require pre-suit demand as a prerequisite to damages claims.
- **Condition-precedent doctrines** — administrative exhaustion (EEOC charge before Title VII suit `[verify]`), tax-refund claims, insurance proof-of-loss requirements.

Every entry: what's required, the deadline, whether it's been done, and `[verify per jurisdiction]` on every period. If a required notice hasn't been given, the investigation memo's ready-to-plead assessment for that claim is **not ready** regardless of the evidence.

### Step 7: Client preservation duty — starts now

The client's own duty to preserve attached when litigation became reasonably anticipated — which is, at the latest, now, because planning this investigation is the proof of anticipation. Two actions:

1. **Evidence-preservation checklist** (written as part of the output): the client documents, communications, devices, and systems that relate to the claim hypothesis, who holds them, and the instruction not to delete or modify.
2. **Point at the hold skill.** Offer to run `/litigation-legal:legal-hold [slug] --issue` immediately after this skill completes. A plaintiff who fails to preserve is handing the defense its best counterattack. The hold is not an optional follow-up; it is the other half of the Rule 11 posture.

### Step 8: Output — the investigation memo

Write to `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/pre-suit-investigation.md`:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> **⚠️ Reviewer note**
> - **Sources:** [research connector status per the pre-flight check — e.g., CourtListener ✓ verified | not connected — limitations periods and rule references are from training knowledge, verify before relying]
> - **Read:** [N client documents, N public-record sources | what was NOT read]
> - **Flagged for your judgment:** [N items marked `[review]` — representation-status calls, tolling theories, ready-to-plead calls on close elements]
> - **Currency:** [searched for limitations/notice-statute changes since [date] | could not search — verify [specific statutes]]
> - **Before relying:** verify every `[verify]` date against the current statute; confirm representation status of flagged witnesses; this memo is an investigation plan, not a filing authorization.

# Pre-Suit Investigation — [Matter Name]

**Matter:** [slug]
**Prospective defendant(s):** [list]
**Candidate claims:** [list]
**Built:** [YYYY-MM-DD]
**Earliest limitations / notice deadline:** [date `[verify]` — the single date that governs the timeline]

---

## Claim hypothesis

[What happened, who's liable, under what theory — three sentences.]

## Investigation plan

[Per-claim, per-element evidence tables from Step 2.]

## Witness interview outlines

[Per-witness outlines from Step 3, each with the representation-status flag.]

## Collectability screen

[Findings table + one-paragraph read from Step 4. Public records only; sources cited per row.]

## Limitations audit

[Table from Step 5. Every date `[verify]`.]

## Pre-suit notice requirements

[Findings from Step 6. Every period `[verify per jurisdiction]`.]

## Ready to plead?

| Claim | Element | Evidence status | Ready? |
|---|---|---|---|
| [claim] | [element] | [in hand / obtainable pre-suit / discovery-dependent (Rule 11(b)(3)) / nothing identified] | ✓ ready / 🟡 ready if obtained / ✗ not ready |

**Bottom line:** [Which claims are ready to plead, which need specified work first, which should be dropped. This is a draft assessment for attorney judgment — every ✗→✓ call is the attorney's, not the skill's.] `[review]`

## Evidence-preservation checklist (client-side)

[What to preserve, who holds it, the no-delete instruction. Offer /litigation-legal:legal-hold to formalize.]
```

Append to `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/history.md`:

```
## [YYYY-MM-DD] — Pre-suit investigation plan built

Candidate claims: [list]. Earliest deadline: [date]. Ready-to-plead: [summary]. Preservation checklist issued: [yes/no].
```

## Consequential-action gates

Drafting the plan is analysis; **acting on it is consequential**. Before any of the following, read `## Who's using this` in the config CLAUDE.md. If the Role is Non-lawyer, require the attorney-review gate (generate the 1-page brief for their attorney per the plugin pattern; do not proceed on the user's say-so alone). For all roles, require an explicit go before:

- **Contacting any witness** — and never if the representation-status flag is unresolved.
- **Sending a FOIA / public-records request** — it's an external act that names the client's interest and starts agency clocks.
- **Sending a preservation demand to the prospective defendant** — it shows the client's hand and may trigger their own filing (a declaratory-judgment race). That trade-off is an attorney's call. Route drafting to `/litigation-legal:demand-intake` (type: preservation).
- **Filing anything.** This skill never drafts the complaint. The ready-to-plead assessment feeds the decision; the pleading is downstream work the attorney directs.

> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent).

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — natural branches here:

1. **Issue the legal hold** — run `/litigation-legal:legal-hold [slug] --issue` (the client's preservation duty has already attached).
2. **Build the element chart** — run `/litigation-legal:claim-chart --civil` for the lead claim, fed by this investigation plan.
3. **Close the gaps** — work the "obtainable pre-suit" column: I'll draft the public-records requests and witness outlines for attorney sign-off.
4. **Send a demand first** — run `/litigation-legal:demand-intake` if a pre-suit demand (or required statutory notice) should precede filing.
5. **Get more facts / something else** — tell me what you'd do with this.

The tree is the output; the lawyer picks.

## What this skill does not do

- **Draft the complaint.** The investigation memo informs the filing decision; pleading drafting is separate downstream work under attorney direction.
- **Contact anyone.** It drafts outlines and request letters for review; a human sends them, after the representation-status and gate checks.
- **Decide that a claim is timely.** It computes candidate dates, all `[verify]`; the limitations call — especially anything resting on tolling — is the attorney's.
- **Run asset searches beyond public records.** Credit reports, bank-account discovery, and pretext-derived information are off-limits pre-suit (Hard rules 2–3). The post-judgment toolkit is `/litigation-legal:judgment-enforcement`.
- **Substitute for the conflicts check.** The gate verifies intake happened; clearance itself lives in `/litigation-legal:matter-intake` and the practice's declared conflicts method.
