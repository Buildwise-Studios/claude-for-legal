---
name: complaint-drafter
description: Draft a plaintiff-side complaint (federal or state) from the matter facts — element-mapped counts where every element has supporting facts pleaded, jurisdictional allegations, numbered paragraphs and prayer for relief, an Iqbal/Twombly plausibility check on every count, and a Rule 11 check. Use when the user says "draft the complaint", "we're filing suit", "turn these facts into a pleading", or has a matter ready to move from demand to filing.
argument-hint: "[slug] [--federal | --state=<state>] [--counts=<cause-of-action,...>]"
---

# /complaint-drafter

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, side, work-product header, decision posture, house style, frequent fora. Also check `./claude-for-legal-config/litigation-legal/CLAUDE.md` in the working folder — in environments where the home path isn't writable, configuration lives there instead. If both exist, the home path wins; say so and offer to reconcile.
2. Conflicts gate: confirm the matter is in `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml`. If not, refuse and route to `/litigation-legal:matter-intake`.
3. Follow the workflow and reference below.
4. Intake: parties, jurisdiction/venue basis, causes of action, facts, relief sought.
5. Element mapping per cause of action — every element needs supporting facts pleaded; flag elements with none as `[fact gap — cannot plead without]`.
6. Jurisdictional allegations: subject-matter jurisdiction, personal jurisdiction, venue.
7. Draft: caption, parties, jurisdiction and venue, factual allegations in numbered paragraphs, counts, prayer for relief, jury demand decision.
8. Run the Iqbal/Twombly plausibility check and the statute-of-limitations check on every count.
9. Run the Rule 11 check. Present the draft with the reviewer note and decision tree.
10. Write the draft to the matter folder. The skill never files anything.

---

# Complaint Drafter

## Purpose

Turns matter facts into a complaint that is structurally sound — every count element-mapped to pleaded facts, jurisdiction alleged, paragraphs numbered — and honest about its gaps. The failure mode this skill is built against is the complaint that reads well and pleads nothing: conclusory recitals of elements, facts that don't reach plausibility, a count the facts can't support included because it "might stick."

Filing a complaint triggers the signing attorney's Rule 11 certification. The skill's job is to make the gaps loud enough that no one signs without seeing them.

## A DRAFT, NOT A FILING

**Put this at the top of every output. Do not drop it. Do not soften it.**

> This is a draft complaint for attorney review, not a filing. Filing a complaint starts a lawsuit: it triggers Rule 11 certification by the signing attorney, starts response and removal clocks, fixes the claims and parties for the case, and creates a public record. A licensed attorney admitted in the forum reviews, edits, signs, and takes professional responsibility before anything is filed. The skill drafts; the lawyer files.

## Side context

This is a plaintiff-posture skill — the complaint asserts claims. Read `## Side` in the practice profile:

- **Plaintiff / claimant:** aligned. Proceed.
- **Defense:** a defense practitioner drafting a complaint is usually doing one of: a counterclaim, a third-party complaint, a declaratory-judgment action, or plaintiff-side work in a different matter. Confirm which — counterclaims and third-party complaints have additional procedural requirements (FRCP 13, FRCP 14) this skill flags but does not fully cover.
- **Both / varies:** confirm the posture for this matter before starting.

## Jurisdiction note

This skill is US-frame: FRCP pleading standards, Iqbal/Twombly plausibility, 28 U.S.C. jurisdiction statutes, US state-court equivalents. Per the plugin CLAUDE.md `## Jurisdiction recognition` section: if the matter belongs in a non-US forum (England & Wales claim form and particulars of claim, German Klageschrift, etc.), say so clearly — pleading conventions, fee consequences, and pre-action protocols differ materially, and a US-style complaint filed in the wrong form can carry cost sanctions. Offer the decision-tree options: search for the forum's pleading requirements (tagged `[verify against primary source]`), route to a practitioner in that jurisdiction, or proceed with the US structure as a content-organizing draft tagged `[US framework — verify against [jurisdiction] practice]` on every section. Never present a US-form complaint as filing-ready for a non-US forum.

Within the US: federal and state pleading standards differ (some states are notice-pleading, some fact-pleading, California requires verification for some claims, New York has CPLR particularity rules for fraud). The skill asks which forum and flags forum-specific requirements as `[verify — local pleading rule]`.

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — the case theory, the demand history, the counterparty, the jurisdiction. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<matter-slug>/pleadings/`. Never read another matter's files unless `Cross-matter context` is `on`.

**Conflicts gate — unbypassable.** Before drafting, check `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't draft a complaint on a matter that hasn't been intaken — the conflicts check is the gate."

## Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, side, house style (citation format), risk calibration, frequent fora
- Active matter's `matter.md` and `history.md` — facts, theory, counterparty, demand correspondence
- Any prior demand letter (`demand-letters/[slug]/`) — the demand frames the claims; the complaint should be consistent with it
- Any existing element chart (`claim-charts/`) — a civil element chart from `/litigation-legal:claim-chart` is the ideal input to Step 2
- The baseline element library at `${CLAUDE_PLUGIN_ROOT}/skills/claim-chart/references/element-templates.md` — shared with `/litigation-legal:claim-chart`; the controlling pattern instruction or statute in the forum always controls

If `CLAUDE.md` has `[PLACEHOLDER]` markers, surface the standard bounce (run `/litigation-legal:cold-start-interview`, or say "provisional" for generic defaults with every output tagged `[PROVISIONAL]`).

## Workflow

### Step 1: Intake

Capture before drafting. Ask only for what the matter file doesn't already answer:

| Field | What's needed | Why |
|---|---|---|
| **Parties** | Full legal names, entity types, states of incorporation AND principal place of business (for diversity), capacity issues (minors, estates, d/b/a) | Caption, party allegations, diversity analysis |
| **Jurisdiction basis** | Diversity / federal question / state court | Drives the jurisdictional allegations entirely |
| **Venue basis** | Where defendant resides, where events occurred, any forum-selection clause | 28 U.S.C. § 1391 or state venue rules `[verify]` |
| **Causes of action** | Which counts; or "what happened" and the skill proposes counts for the attorney to choose from | The spine of the complaint |
| **Facts** | The chronology — dates, documents, actors, amounts | Every element's support comes from here |
| **Relief sought** | Damages (amount or category), injunction, declaratory relief, fees, interest | Prayer for relief; amount-in-controversy |

If the user asks the skill to propose causes of action: propose them as a list with a one-line element fit per count and `[review — count selection is a strategic and Rule 11 call]` on each. The attorney picks the counts; the skill does not decide what to sue on.

### Step 2: Element mapping — a claim chart in reverse

For each cause of action, before any prose is drafted, build the element map. This is `/litigation-legal:claim-chart` run in reverse: instead of mapping evidence to elements, map the facts you intend to PLEAD to the elements you must plead.

| Element (per controlling law) | Supporting facts to be pleaded | Pleading paragraph(s) | Status |
|---|---|---|---|
| 1. Existence of a contract | MSA executed 2024-03-01 between P and D | ¶¶ 12–14 | pleadable |
| 2. Plaintiff's performance | P delivered all milestones through Phase 2; D accepted | ¶¶ 15–18 | pleadable |
| 3. Defendant's breach | D failed to pay invoices 1041–1044, total $480K | ¶¶ 19–23 | pleadable |
| 4. Causation + damages | Unpaid invoices + downstream cancellation costs | ¶¶ 24–26 | `[fact gap — cannot plead without]` (downstream costs unquantified) |

**The hard rule:** every element either has supporting facts or carries `[fact gap — cannot plead without]`. A count with any unfilled fact gap is presented to the attorney as **not currently pleadable** — with the options: (a) gather the missing facts (the skill lists exactly what's needed), (b) drop the count, or (c) the attorney determines the gap can be pleaded on information and belief consistent with Rule 11(b)(3) `[review — attorney call]`.

**The skill never softens a fact gap to make a claim pleadable.** It does not write "upon information and belief" to paper over a gap, does not generalize a date it doesn't have, and does not assert an amount that hasn't been given. That softening is exactly how a Rule 11 problem gets drafted into a complaint.

Element sources: the baseline library at `${CLAUDE_PLUGIN_ROOT}/skills/claim-chart/references/element-templates.md`, the forum's pattern jury instructions, or the governing statute. The controlling formulation in the forum controls — flag jurisdiction-specific divergences (Delaware's 3-element breach of contract, New York's CPLR 3016(b) fraud particularity, California's verification requirements) the same way `/litigation-legal:claim-chart` does.

### Step 3: Jurisdictional allegations

Draft these as their own section, before the facts. Wrong or missing jurisdictional allegations get complaints dismissed without anyone reaching the merits.

**Subject-matter jurisdiction (federal):**

- **Diversity (28 U.S.C. § 1332):** complete diversity — every plaintiff diverse from every defendant. Allege each party's citizenship correctly: individuals by domicile; corporations by BOTH state of incorporation and principal place of business; LLCs and partnerships by the citizenship of every member `[verify — member citizenship is the most common diversity pleading error]`. Amount in controversy exceeds $75,000 exclusive of interest and costs — the facts pleaded must plausibly support the amount.
- **Federal question (28 U.S.C. § 1331):** the claim arises under federal law — name the statute. Well-pleaded complaint rule: the federal question must appear in the complaint itself, not an anticipated defense.
- **Supplemental jurisdiction (28 U.S.C. § 1367):** for state-law counts riding with federal ones — same case or controversy.

**Personal jurisdiction:** allege the basis — defendant's residence/incorporation in the forum (general), or suit-related contacts with the forum (specific). Flag if personal jurisdiction looks contestable: `[review — PJ over [defendant] may be challenged; consider whether the contacts pleaded survive a 12(b)(2) motion]`.

**Venue (28 U.S.C. § 1391):** judicial district where any defendant resides (if all reside in the state), or where a substantial part of the events occurred, or the fallback. If a contract has a forum-selection clause, flag it — it may mandate or forbid this forum `[review]`.

**State court:** the state's jurisdictional and venue statutes instead `[verify — cite the state provisions for [state]]`.

### Step 4: Draft

Structure (adapt to forum and house style):

1. **Caption** — court, parties, case number placeholder, document title
2. **Preliminary statement** — optional; 2–4 paragraphs framing the case. House-style call.
3. **Parties** — one numbered paragraph per party with citizenship/entity allegations
4. **Jurisdiction and venue** — from Step 3
5. **Factual allegations** — numbered paragraphs, chronological, one fact per paragraph where practical. Every paragraph the element map relies on exists here. Specificity over adjectives: "On March 14, 2026, Defendant sent X" beats "Defendant repeatedly and wrongfully sent X."
6. **Counts** — one per cause of action: "COUNT I — [CAUSE OF ACTION] (against [defendant(s)])"; incorporation by reference of prior paragraphs; the elements alleged with the supporting facts; what relief flows from this count.
7. **Prayer for relief** — itemized: compensatory damages, statutory damages where authorized `[verify statutory basis]`, injunctive relief described with specificity, pre- and post-judgment interest, fees `[verify — fee-shifting basis: contract / statute / none]`, costs, other relief.
8. **Jury demand** — a decision, not a default. FRCP 38(b): the right is waived if not timely demanded. Flag: `[review — jury demand is a strategic call; the right is waived if not demanded within 14 days after the last pleading]`.
9. **Signature block** — the signing attorney's name, bar number, firm, contact. The signature line is presented EMPTY with the Rule 11 note attached.

Drafting rules carried from the plugin's shared guardrails: facts traceable to sources (every factual allegation maps to a document, date, or witness the client can produce — if not, `[VERIFY: ___]` inline); no invented quotes; citations as `[CITE: ___]` placeholders or tagged with provenance (`[user provided]`, `[CourtListener]`, `[model knowledge — verify]`); verbatim contract language quoted only with the contract in front of you.

### Step 5: Iqbal/Twombly plausibility check — every count

After drafting, audit every count against *Ashcroft v. Iqbal*, 556 U.S. 662 (2009) and *Bell Atlantic Corp. v. Twombly*, 550 U.S. 544 (2007) `[model knowledge — verify]`:

- **Conclusory recitals flagged.** Any paragraph that restates an element in legal language without facts ("Defendant breached its duty of care") is flagged: `[Iqbal/Twombly — conclusory; a court disregards this paragraph; the facts that make it plausible are ¶¶ __ / are missing]`.
- **Plausible, not just possible.** For each count: do the facts pleaded, taken as true, make the claim plausible — not merely conceivable? Where the answer depends on an inference, state the inference and whether an "obvious alternative explanation" (Iqbal's phrase) undercuts it.
- **Fraud counts:** FRCP 9(b) particularity — the who, what, when, where, and how of the misrepresentation. A fraud count that can't answer all five is flagged as a 9(b) dismissal target.
- The check's output is a per-count verdict: **plausible as drafted / plausible if ¶¶ __ are strengthened / not plausible on the facts provided** — with the conclusory paragraphs listed.

State-court note: some states apply different (often lower notice-pleading or higher fact-pleading) standards — the check still runs, because a complaint that survives Iqbal/Twombly survives notice pleading, but flag `[verify — [state]'s pleading standard]`.

### Step 6: Statute of limitations check — every count

For each count: `[verify — limitation period for [claim] in [jurisdiction]; accrual date appears to be [date from facts]; filing deadline approximately [date]]`.

The skill does not assert limitation periods as fact — they are jurisdiction-specific, claim-specific, and subject to tolling, discovery rules, and borrowing statutes. The flag forces the attorney to run the real check. If the facts suggest a count may already be time-barred, say so prominently: `[review — POSSIBLE LIMITATIONS PROBLEM: the facts show accrual on [date], which is more than [the typical period] before today. Verify before filing — filing a time-barred claim has Rule 11 implications.]`

## The Rule 11 check

**This runs after drafting and before the draft is delivered. It is loud by design. Do not compress it to a footnote.**

> ## ⚠️ RULE 11 CERTIFICATION — READ BEFORE THIS COMPLAINT GOES ANYWHERE
>
> By presenting this complaint to the court, the signing attorney certifies under FRCP 11(b) that:
>
> 1. It is not presented for any improper purpose (harassment, delay, needless cost);
> 2. The claims are warranted by existing law or a nonfrivolous argument for extending, modifying, or reversing existing law;
> 3. **The factual contentions have evidentiary support or, if specifically so identified, will likely have evidentiary support after a reasonable opportunity for investigation or discovery;**
> 4. Denials of factual contentions are warranted (not applicable to a complaint, but part of the certification).
>
> This draft contains:
> - **[N] factual allegations flagged `[VERIFY]`** — these do not currently have identified evidentiary support. They must be verified or removed before signature.
> - **[N] elements flagged `[fact gap — cannot plead without]`** — the counts containing them are not pleadable as drafted.
> - **[N] allegations pleaded on information and belief** — each must individually satisfy Rule 11(b)(3)'s "likely to have evidentiary support after discovery" standard. `[review]`
>
> The skill did not soften any fact gap to make a claim pleadable. If a count reads thin, it is because the facts provided are thin. Sanctions under Rule 11(c) run against the signing attorney and the firm — not the drafting tool.
>
> State-court equivalents (e.g., Cal. CCP § 128.7, N.Y. 22 NYCRR 130-1.1) impose comparable certifications. `[verify — the forum's rule]`

## Hard gate — filing

The skill never files. Before anyone files:

- A licensed attorney admitted in the forum reviews every paragraph, resolves every `[VERIFY]`, `[fact gap]`, and `[review]` flag, runs the citations through `/litigation-legal:cite-check`, and signs.
- **Non-lawyer users (per `## Who's using this`):** this draft is a structure for a lawyer to work from, not a document to file pro se as-is. Filing a complaint pro se is legally permitted for individuals (not for corporations, which must appear through counsel in federal court) but carries every Rule 11 obligation with none of the training. If the user is proceeding without a lawyer:
  - Recommend a licensed attorney review the draft before filing — many offer limited-scope review at fixed cost.
  - Point at the court's self-help resources: federal district courts' pro se offices, state court self-help centers, and legal aid organizations in the user's jurisdiction.
  - Generate a one-page brief for that review: parties, counts, the element map, every open flag, and the questions to ask the attorney.
- Filing also has a cost the gate names: filing fees, service obligations (FRCP 4 — deadlines and methods), and the fact that the complaint locks the case theory the rest of the litigation has to live with.

## Output

Write to the matter folder: `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<slug>/pleadings/complaint-draft-v[N].md` (and `.docx` via the docx skill if requested). Append a one-line entry to the matter's `history.md`.

The complaint itself is a court filing — it does NOT carry the work-product header (a filed complaint is public). The element map, the Rule 11 check output, and the drafting notes ARE internal work product and carry the header from the plugin CLAUDE.md `## Outputs`.

Present in this order:

1. **⚠️ Reviewer note** (plugin CLAUDE.md format): Sources line (research connector status for any cited authority), Read line (what matter materials were read), Flagged line (counts of `[VERIFY]` / `[fact gap]` / `[review]` flags), Currency line, Before-relying line (the 1–2 things to do first — typically "resolve the fact gaps in Count [N]" and "run /litigation-legal:cite-check").
2. **Element maps** (one per count) — internal work product, header applied.
3. **The draft complaint** — clean, numbered, no inline meta-commentary other than the flag tags.
4. **The Rule 11 check block.**
5. **The decision tree.**

## What this skill does not do

- **It does not file, serve, or sign.** Ever. It drafts.
- **It does not decide which counts to bring.** It maps which counts the facts can support and flags the rest. Count selection is the attorney's strategic and Rule 11 call.
- **It does not soften fact gaps.** A gap stays loud until a human fills it or cuts the count.
- **It does not assert limitation periods, local pleading rules, or fee-shifting bases as fact.** Those are `[verify]` flags pointing at jurisdiction-specific law.
- **It does not draft an answer, a counterclaim's procedural wrapper, or a motion.** Those are different documents with different rules; flag and route.

## Relationship to other skills

- `/litigation-legal:matter-intake` — must run first (conflicts gate). The matter file is this skill's primary input.
- `/litigation-legal:claim-chart` — the civil element chart and this skill's element map are the same artifact pointed in opposite directions. A pre-filing claim chart (`--civil`, phase: pre-filing) IS Step 2; reuse it.
- `/litigation-legal:demand-draft` / `/litigation-legal:demand-intake` — the demand usually precedes the complaint. The complaint's facts must be consistent with what the demand asserted; flag contradictions.
- `/litigation-legal:cite-check` — run on the draft before filing.
- `/litigation-legal:chronology` — the factual-allegations section is a chronology in numbered-paragraph form; an existing chronology is the best input to Step 4.
- `/litigation-legal:discovery-requests` — after the pleadings close, the element map's `[fact gap]` rows become the discovery plan.

## Close with the next-steps decision tree

End with the next-steps decision tree per the plugin CLAUDE.md `## Outputs`, customized to the draft:

> **What next? Pick one and I'll help you build it out:**
> 1. **Close the fact gaps** — I'll list exactly what facts/documents are needed for each `[fact gap]` and draft the questions to the client (or the witnesses) that would get them.
> 2. **Run the cite check** — I'll run `/litigation-legal:cite-check` on the draft so the authorities are verified before review.
> 3. **Tighten a count** — pick the count and I'll strengthen its factual allegations against the Iqbal/Twombly flags.
> 4. **Escalate** — I'll draft the short memo to [the GC / the partner / the client] presenting the draft, the open flags, and the filing decision that needs to be made.
> 5. **Hold** — I'll note in the matter history that a complaint draft exists and what it's waiting on.
> 6. **Something else** — tell me what you'd do with this.
