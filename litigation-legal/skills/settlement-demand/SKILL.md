---
name: settlement-demand
description: Build a plaintiff-side settlement demand package or a confidential mediation statement — candid liability summary covering strengths AND weaknesses, itemized damages presentation with documentation pointers, demand structure with anchor rationale and deadline, and FRE 408 / mediation-privilege framing. The demand number and authority to send always come from the client and attorney, never from the skill. Use when the user says "draft the settlement demand", "put together a demand package", "mediation statement", "what should our demand look like", or has a matter ready to push toward resolution.
argument-hint: "[slug] [--demand-package | --mediation-statement] [--version=N]"
---

# /settlement-demand

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, side, work-product header, settlement authority ladder, decision posture, house style. Also check `./claude-for-legal-config/litigation-legal/CLAUDE.md` in the working folder — in environments where the home path isn't writable, configuration lives there instead. If both exist, the home path wins; say so and offer to reconcile.
2. Conflicts gate: confirm the matter is in `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml`. If not, refuse and route to `/litigation-legal:matter-intake`.
3. Ask which deliverable: demand package (goes to opposing counsel) or mediation statement (goes to the mediator). They are different documents for different audiences — never mix them.
4. Follow the workflow and reference below.
5. Intake: liability theory, damages incurred and projected, insurance/collectability, prior negotiation history, deadline pressure points.
6. Build the liability summary — strengths AND weaknesses.
7. Build the damages presentation — specials itemized with documentation pointers, generals framed per jurisdiction practice, future damages flagged for expert support.
8. Build the demand structure — anchor rationale, deadline, what happens after. The NUMBER comes from the client/attorney, never from the skill.
9. Apply the confidentiality framing: FRE 408 / state equivalent for the demand letter; mediation privilege for the mediation statement.
10. Output: internal assessment (work-product header) + the external draft (no header, FRE 408 legend) + reviewer note + decision tree. Run the destination check before anything is positioned to leave the building.

---

# Settlement Demand

## Purpose

A settlement demand is advocacy aimed at a reader who is doing math. The package that works is the one that makes the other side's lawyer write a memo to their client saying "we should pay" — which means it must be credible: documented damages, a liability story that survives the other side's first round of scrutiny, and a demand number whose rationale can be defended out loud.

The failure modes this skill is built against: the demand that hides the case's weaknesses (the other side finds them anyway, and the credibility lost there prices every later number); the damages section that asserts totals without documentation pointers (unverifiable numbers get discounted to zero); and the mediation statement that gets sent to opposing counsel because someone grabbed the wrong file.

## Two deliverables — never mixed

Ask first, every time:

| | **Demand package** | **Mediation statement** |
|---|---|---|
| Audience | Opposing counsel (and through them, the opposing client and any insurer) | The mediator only |
| Posture | Advocacy. Strengths led, weaknesses acknowledged and framed. | Candor. The mediator needs the real risk assessment to move both sides. |
| Confidentiality frame | FRE 408 / state equivalent legend | Mediation privilege / confidentiality agreement / local ADR rules |
| Weakness handling | Acknowledged and framed (never hidden — see below) | Disclosed with the real assessment of how much they hurt |
| The number | The demand, with rationale | The real range and reservation point may appear — or not, per the attorney's mediation strategy `[review]` |

**Destination check — hard rule.** These two documents must never be confused. A mediation statement containing the candid risk assessment, sent to opposing counsel, is a case-altering error that cannot be recalled. Per the plugin CLAUDE.md `## Shared guardrails → Destination check`:

- Every output of this skill states its intended destination in its filename and its first line: `[FOR OPPOSING COUNSEL — FRE 408]` or `[FOR MEDIATOR ONLY — CONFIDENTIAL MEDIATION STATEMENT]`.
- Before producing a final version of either document, confirm the destination with the user out loud.
- If the user asks to send, attach, or copy a mediation statement (or the internal assessment) to anyone other than the mediator or the privilege circle, stop and flag: "That document contains your candid risk assessment. Sending it to [destination] discloses it to the other side. Confirm this is intentional, or I'll prepare the demand-package version instead."

## Side context

This is a plaintiff-posture skill — the demand asserts a claim and a number. Read `## Side` in the practice profile:

- **Plaintiff / claimant:** aligned. Proceed.
- **Defense:** defense-side settlement papers are a different shape — a response to a demand, an offer, a mediation statement from the defense view (exposure framing, not damages framing). The mediation-statement variant of this skill works for defense with the framing flipped (confirm first); the demand-package variant does not. For triaging an inbound demand, route to `/litigation-legal:demand-received`.
- **Both / varies:** confirm the posture for this matter before starting.

## Jurisdiction note

This skill is US-frame: FRE 408, US damages categories (specials/generals), US insurance and policy-limits practice, court-annexed and private mediation conventions. Per the plugin CLAUDE.md `## Jurisdiction recognition` section: outside the US, settlement-communication protection works differently — England & Wales "without prejudice" (and "without prejudice save as to costs" / *Calderbank* offers, plus CPR Part 36 with its cost-shifting mechanics) is not FRE 408 and has its own traps; many civil-law jurisdictions have no equivalent doctrine at all. If the matter is non-US:

- Say so clearly, and do not apply FRE 408 labels to a non-US letter — a wrong label can create a false sense of protection.
- Offer the decision-tree options: search for the applicable settlement-privilege rule (tagged `[verify against primary source]`), route to a practitioner in the jurisdiction, or proceed with structure-only drafting where every protection-dependent element is flagged `[US framework — verify against [jurisdiction] law]`.
- The damages-presentation structure (itemized, documented) translates across jurisdictions; the protection framing does not.

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — theory, damages history, negotiation history, insurance. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<matter-slug>/settlement/`. Never read another matter's files unless `Cross-matter context` is `on`.

**Conflicts gate — unbypassable.** Before drafting, check `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't build settlement papers on a matter that hasn't been intaken — the conflicts check is the gate."

## Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, side, **settlement authority ladder** (who can authorize what amount), risk calibration, house style, insurance profile
- Active matter's `matter.md` and `history.md` — theory, claimed damages, prior offers and demands, insurance/tender status
- Any chronology (`/litigation-legal:chronology` output) — the liability narrative is built on it
- Any element chart (`/litigation-legal:claim-chart` output) — element strength ratings feed the liability summary directly
- Damages documentation: invoices, medical records/bills, payroll records, expert reports, repair estimates — whatever the matter file holds. The damages table points at these.
- Prior settlement correspondence — the negotiation history; a new demand that ignores the last exchange reads as amateur

If `CLAUDE.md` has `[PLACEHOLDER]` markers, surface the standard bounce (run `/litigation-legal:cold-start-interview`, or say "provisional" for generic defaults with every output tagged `[PROVISIONAL]`).

## Workflow

### Step 1: Intake

| Topic | What's needed | Why |
|---|---|---|
| **Liability theory** | The claims, the elements, how strong each is (pull from the element chart if one exists) | The liability summary |
| **Damages incurred** | Every category to date, with what documentation exists for each | The specials table |
| **Damages projected** | Future losses: ongoing treatment, future lost earnings, future contract losses | Flagged for expert support |
| **Insurance / collectability** | Does the defendant have coverage? Policy limits known? Is the defendant collectable beyond policy limits? | A demand above uncollectable limits is a different strategic document (policy-limits demand) `[review]` |
| **Prior negotiation history** | Every prior demand, offer, and counteroffer with dates | The new demand must advance the posture, not restate it |
| **Deadline pressure points** | Trial date, mediation date, statute of limitations, policy-limits time-demand windows, defendant's fiscal events | Drives the deadline and the "what happens after" |
| **Client objectives** | Speed vs. maximum recovery, appetite for trial, confidentiality needs, non-monetary terms (apology, reinstatement, reference, business terms) | The structure serves the objective, not the other way around |

### Step 2: Liability summary — strengths AND weaknesses

The liability section presents the claim the way a credible advocate does: confident about what's strong, honest about what isn't.

**A demand that hides weaknesses sets the client up.** The other side knows the weaknesses — their lawyer's first memo listed them. A demand that pretends they don't exist tells the reader the demand number is inflated by exactly the amount of the pretense, and it burns credibility that the next round needs. The strongest demand concedes what's weak so the counterparty can't use it.

Structure:

- **The story** — 2–4 paragraphs of narrative, built from the chronology, every fact traceable to a document or witness `[VERIFY]` flags on anything unconfirmed.
- **Why we win** — element by element (from the chart): the evidence, named. Pin cites to documents the other side has seen or will see in discovery. Authority cited only with provenance tags (`[CourtListener]` / `[user provided]` / `[model knowledge — verify]`) per the plugin CLAUDE.md source-tag rules.
- **What you'll say and why it fails** — anticipate the 2–3 best defense arguments and answer them. This is where weaknesses get framed rather than hidden: "We anticipate you'll point to [weakness]. Here's why it doesn't change the outcome: [answer]." If a weakness genuinely doesn't have a good answer, the INTERNAL assessment says so plainly (`[review — this is the case's soft spot; the demand frames it as X but the client should understand the risk]`), and the external letter frames it as favorably as honesty allows — it never pretends the issue doesn't exist.

For the **mediation statement**, this section becomes candid: "Plaintiff's case is strong on liability (elements 1–3 are documented) and weaker on causation (the gap is [X]). We assess trial outcome risk as [range]." The mediator is not an adversary; lying to them wastes the mediation.

### Step 3: Damages presentation

**Specials (economic damages) — itemized, every line documented:**

| Category | Amount | Documentation | Status |
|---|---|---|---|
| Medical expenses to date | $84,212.40 | [Provider statements, Ex. 1–14] | documented |
| Lost wages (2026-01-15 to 2026-05-30) | $31,500.00 | [Employer letter + payroll records, Ex. 15] | documented |
| Property damage | $12,800.00 | [Repair invoice, Ex. 16] | documented |
| Future surgery (recommended) | $45,000 (est.) | [Dr. Chen treatment plan, Ex. 17] | `[expert support needed — treating physician declaration or life-care planner]` |
| Future lost earning capacity | TBD | — | `[expert support needed — vocational/economic expert; do not assert a number without one]` |

Rules:

- Every line has a documentation pointer — an exhibit, a record, an invoice. **A number without a pointer is flagged, not asserted.** The skill never totals undocumented amounts into the demand's damages figure; they appear (if at all) as "additional damages being quantified."
- **Future damages are flagged for expert support.** Asserting future medicals, future lost earnings, or business-valuation losses without expert grounding invites the response "prove it" and makes the whole table look soft.
- Math is shown. Subtotals, totals, and any multipliers are computed transparently and double-checked.

**Generals (non-economic damages) — framed per jurisdiction practice:**

Pain and suffering, emotional distress, loss of consortium, reputational harm. How these are presented varies by jurisdiction and practice culture (per-diem arguments allowed in some jurisdictions, prohibited in others; statutory caps in many `[verify — caps and presentation rules for [jurisdiction]]`). The skill structures the presentation (the human story, anchored to the specials, consistent with verdicts in the venue if the user provides comparables `[user provided]`) and flags the framing choice `[review — generals presentation is a strategic and jurisdiction-specific call]`.

**Punitive / statutory damages:** only if the liability theory supports them; flagged with the heightened standard (`[verify — [jurisdiction] punitive standard and any cap/ratio limits]`). A punitive demand without a supporting theory reads as bluster and discounts the rest of the package.

### Step 4: Demand structure

- **The anchor number — the skill structures the rationale; the client and attorney set the number.** This is a hard gate, not a style preference (see below). What the skill builds: the bridge from the damages table to a number — "documented specials of $X + generals framed at [multiplier/comparable basis] + [risk discount rationale]" — presented as a RANGE with the strategic considerations (anchoring high vs. credibility, policy limits, the defendant's likely authority structure) laid out for the attorney `[review]`. The attorney/client picks the number; the skill then writes the rationale for THAT number.
- **Deadline** — a date, not "promptly." Tied to a real consequence and a real pressure point from intake (trial calendar, mediation date, policy-limits time-demand rules `[verify — time-limited-demand statutes/case law in [jurisdiction], e.g., bad-faith setup doctrine]`).
- **What happens after** — what specifically follows if the deadline passes: filing suit (the complaint is drafted — reference it if `/litigation-legal:complaint-drafter` has run), arbitration demand, amended pleadings, the next motion. The consequence must be one the client is actually prepared to execute; an empty threat re-prices every future statement.
- **Non-monetary terms** — confidentiality, non-disparagement, reference letters, business terms, structured payments — listed if the client wants them, because terms left out of the demand are terms the client pays for later.
- **Payment logistics and release scope** — preview the release the client expects (claims released, parties covered, carve-outs). Release scope disputes kill more settlements-in-principle than money does.

### Step 5: Confidentiality framing

**Demand package (to opposing counsel):**

- Legend: "FOR SETTLEMENT PURPOSES ONLY — SUBJECT TO FRE 408 AND ALL APPLICABLE STATE EQUIVALENTS — INADMISSIBLE TO PROVE LIABILITY OR AMOUNT"
- Per the plugin's demand-draft guardrail: **protection attaches from conduct and context, not labels.** The letter is structured as a settlement communication (it offers compromise; it doesn't read as a press release). Facts the client needs admissible later are NOT exclusively located in the letter — FRE 408 does not protect evidence "otherwise discoverable" merely because it was presented in negotiations, and the letter shouldn't be the only place a key admission-adjacent statement lives `[review]`.
- The work-product header does NOT go on the outgoing letter (external deliverable, per plugin CLAUDE.md `## Outputs`).

**Mediation statement (to the mediator):**

- Legend per the governing frame: the mediation agreement's confidentiality clause, the court's ADR local rule, or the jurisdiction's mediation-privilege statute (Uniform Mediation Act jurisdictions vs. others `[verify — which applies]`). Cite the actual source if the user provides the mediation agreement `[user provided]`; otherwise flag.
- State whether the mediator may share contents with the other side. Many mediations run on "the mediator may share unless marked confidential" — mark the sections that are mediator-only explicitly.

## Hard gate — the number and the send

Two things this skill never does:

1. **It never sets the demand number.** The skill computes documented damages, builds ranges, structures rationales, and lays out the strategic considerations. The NUMBER — and any later acceptance, counteroffer, or authority to negotiate — comes from the client (who owns the claim) through the attorney (who advises on it). If the user says "just pick a number," the answer is: "I'll show you the bridge from the damages to a range and what each end of the range trades off — but the demand number is the client's call with your advice, not mine. Which number do you want the letter built around?" Check the practice profile's **settlement authority ladder** — if the contemplated demand or any anticipated settlement range crosses an authority threshold, flag who has to approve per the ladder.
2. **It never sends.** The demand package and mediation statement are drafts for attorney review. Sending a demand is a consequential act: it discloses theory, sets anchors, can trigger bad-faith/time-demand doctrines, and starts negotiation clocks. Per the plugin CLAUDE.md consequential-action gate: if the Role in `## Who's using this` is Non-lawyer, do not treat the draft as send-ready — generate the one-page attorney brief (the theory, the damages table with documentation status, the proposed number and its rationale, the open flags, what could go wrong) and route to attorney review. Sending requires an explicit human yes, from the person with authority to give it.

## Output

Write to the matter folder `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<slug>/settlement/`:

| File | Header | Destination line |
|---|---|---|
| `internal-assessment-v[N].md` | Work-product header (plugin CLAUDE.md `## Outputs`) | `[INTERNAL — PRIVILEGE CIRCLE ONLY]` |
| `demand-package-v[N].md` (and `.docx` via the docx skill on request) | NO work-product header; FRE 408 legend | `[FOR OPPOSING COUNSEL — FRE 408]` |
| `mediation-statement-v[N].md` (and `.docx` on request) | NO work-product header; mediation-confidentiality legend | `[FOR MEDIATOR ONLY — CONFIDENTIAL MEDIATION STATEMENT]` |

The internal assessment holds: the candid liability assessment (including the soft spots and how the letter frames them), the full damages workup including undocumented items, the range analysis behind the number, and the negotiation strategy notes. It exists so the letter can stay clean while nothing is lost.

Versioning per the demand-draft convention: never overwrite a version that has been sent; revisions after send increment the version.

Append a one-line entry to the matter's `history.md`. If the matter's `_log.yaml` row has a `risk:` or materiality field that this settlement posture changes, flag the update — don't silently edit it (cross-skill severity rules apply).

Present in this order:

1. **⚠️ Reviewer note** (plugin CLAUDE.md format) — Sources (research connector status for any cited authority), Read (matter materials and damages documentation reviewed; what was NOT available), Flagged (counts of `[review]` / `[VERIFY]` / `[expert support needed]` items), Currency, Before-relying (typically: "the demand number needs your and the client's decision" + "future damages need expert support before this goes out").
2. **The internal assessment** (header applied).
3. **The external draft** (demand package or mediation statement — clean, with its legend and destination line).
4. **The decision tree.**

## What this skill does not do

- **It does not set the demand number, the bottom line, or the negotiation strategy.** It structures; the client and attorney decide.
- **It does not send anything, to anyone.** Drafts only, behind the destination check.
- **It does not assert undocumented damages.** Numbers without documentation pointers are flagged, never totaled into the demand.
- **It does not assert future damages without expert support.** Flagged, every time.
- **It does not hide weaknesses.** Not in the internal assessment (where they're stated plainly) and not in the letter (where they're framed, not omitted).
- **It does not provide a settlement-value opinion.** Ranges presented are arithmetic bridges from documented damages plus framing options — not a prediction of what a jury does or what the case "is worth."
- **It does not negotiate.** Responding to counteroffers is the attorney's work; the skill can draft the response when asked, through this same workflow.

## Relationship to other skills

- `/litigation-legal:matter-intake` — must run first (conflicts gate).
- `/litigation-legal:demand-draft` / `/litigation-legal:demand-intake` — the pre-litigation demand letter engine (payment demands, cure notices, C&Ds). Use those for asserting a claim before a matter is in active dispute resolution; use THIS skill for the settlement package once litigation or mediation is the frame. If the user wants a simple payment demand, route there.
- `/litigation-legal:demand-received` — the inbound mirror; a received demand gets triaged there, and this skill drafts the response posture if the response is itself an offer.
- `/litigation-legal:chronology` — the liability narrative is built from it.
- `/litigation-legal:claim-chart` — element strength ratings feed the liability summary; the chart's gap list is the honest input to the weaknesses section.
- `/litigation-legal:complaint-drafter` — "what happens after the deadline" is most credible when the complaint is already drafted; reference it.
- `/litigation-legal:cite-check` — any authority cited in the package gets checked before it goes out.
- `/litigation-legal:matter-update` — after a demand is sent or a mediation happens, the matter log gets updated there.

## Close with the next-steps decision tree

End with the next-steps decision tree per the plugin CLAUDE.md `## Outputs`, customized to what was built:

> **What next? Pick one and I'll help you build it out:**
> 1. **Set the number** — tell me the demand figure you and the client have decided on, and I'll finalize the rationale section and the letter around it.
> 2. **Close the documentation gaps** — I'll list every damages line missing a pointer or expert support, and draft the requests (to the client, the providers, or the expert) that would close them.
> 3. **Build the other deliverable** — [if demand package was built: "I'll build the mediation statement from the same workup — candid version, mediator audience."] [if mediation statement: vice versa.]
> 4. **Escalate** — I'll draft the authority memo to [the approver from your settlement authority ladder] with the range analysis, so the demand number can be authorized.
> 5. **Pressure-test it** — I'll play the opposing counsel's associate and write the response memo they'd write, so you see the holes before they do.
> 6. **Something else** — tell me what you'd do with this.
