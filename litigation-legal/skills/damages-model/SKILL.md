---
name: damages-model
description: Build a structured damages model for a civil claim — damages theory per claim, a categories table where every number is documented or marked as a gap, specials build-up, future damages flagged for experts, mitigation audit, prejudgment interest, and comparative-fault scenarios, ending in a low/mid/high range with stated assumptions. Use when the user says "what are our damages", "build the damages model", "quantify the claim", or needs a damages number for a demand, mediation statement, or disclosure.
argument-hint: "[slug] [--claim=<count name>] [--update]"
---

# /damages-model

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, side, work-product header, risk calibration, house style. Config lives at the home path or, in environments where that isn't writable (Claude Cowork), at `./claude-for-legal-config/litigation-legal/` in the working folder — check both; home wins if both exist.
2. If matter workspaces enabled, confirm or select the active matter; otherwise resolve the slug from the argument.
3. Follow the workflow and reference below.
4. Conflicts gate: confirm the matter is in `_log.yaml`; refuse and route to `/litigation-legal:matter-intake` if not.
5. Establish the damages theory per claim (expectation / reliance / restitution; economic + non-economic; statutory).
6. Build the categories table — every item is documented, needs-documentation, or needs-expert. Never invent an amount.
7. Build the specials, the future-damages list (`[needs expert]`), the mitigation audit, prejudgment interest, and the fault-haircut scenarios.
8. Compute the low/mid/high range as scenario math on stated assumptions.
9. Write `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/damages-model.md`; append to `history.md`. If `--update`, read the prior model, diff, and version it.
10. Confirm with the user: "Here's the model. Every `[PLACEHOLDER — needs documentation]` is a number I don't have — anything you can fill now?" Close with the decision tree.

---

# Damages Model

## Purpose

Damages are the element most often asserted and least often built. A claim with strong liability and an unsupported number settles badly, survives summary judgment only to die at trial, and makes the demand letter that opens the negotiation an invitation to call the bluff. This skill builds the damages case the way it will eventually be proved: item by item, each with a calculation basis and a document behind it — or an honest flag that the document doesn't exist yet.

The model is a working document. It starts full of gaps; the gaps are the work plan.

## Jurisdiction assumption

This skill's frame is US law: contract damages (expectation / reliance / restitution), tort damages (economic and non-economic), statutory damages regimes, prejudgment interest statutes, and comparative/contributory fault rules. All of these vary by state — non-economic damages caps, the new-business rule's strictness, prejudgment interest rates and accrual triggers, and whether the jurisdiction is pure comparative, modified comparative (50% or 51% bar), or contributory `[model knowledge — verify]`. **If the matter or governing law is non-US, say so before doing substantive work**, per the plugin CLAUDE.md `## Jurisdiction recognition` — civil-law damages concepts (e.g., no punitive damages in most of Europe, different interest regimes, loss-of-chance doctrines) do not map onto this structure. Tag every conclusion `[US framework — verify against [jurisdiction] law]` if the user asks you to proceed anyway, and offer to search for the applicable standard or route to a local practitioner.

## Hard rules — numbers

1. **The skill never invents an amount.** Every number in the model comes from one of: a document the skill read this session (cited by path or Bates), a figure the user stated (`[user provided]`), or arithmetic on those two (`[computed: <formula>]`). Anything else is `[PLACEHOLDER — needs documentation]`. A model with twenty placeholders is useful; a model with twenty plausible-sounding invented numbers is a malpractice exposure.
2. **Ranges are scenario math, not predictions.** The low/mid/high range is computed from stated assumptions ("low assumes the court excludes lost profits entirely; high assumes full recovery plus prejudgment interest from breach date"). The skill never says "this case is worth about $X" — that's a settlement-judgment call reserved to counsel, and it depends on liability odds this model deliberately does not estimate.
3. **Punitive damages get the constitutional caveat, every time.** If punitives are in the model: they are rarely awarded, require conduct findings (malice, oppression, fraud, recklessness — standard varies by state `[verify]`), and are constitutionally constrained — single-digit ratios to compensatory damages are the guidepost from *State Farm v. Campbell* `[model knowledge — verify]`, with anything above that presumptively suspect. Punitives go in their own row, excluded from the low and mid scenarios by default, never summed silently into a headline number.
4. **Source-tag discipline applies to law, not just numbers.** Damages-availability rules (is emotional distress recoverable on this claim? does the economic-loss rule bar this tort claim?), interest rates, and caps carry the same provenance tags as everything else: `[verify]`, `[model knowledge — verify]`, or a research-connector tag if retrieved this session.

## Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → `## Side` (plaintiff posture: the model supports the demand and the proof; defense posture: the same structure works as an exposure model — say which frame is active), `## Outputs`, `## Decision posture`, risk calibration (the model's mid scenario feeds the severity bands), house style.
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/matter.md` — claims pleaded or contemplated, key dates (breach/injury date drives interest accrual), exposure range from intake (this model replaces that gut number).
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/chronology.md` if it exists — dated events anchor accrual and mitigation timelines.
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/claim-charts/` if any exist — the damages element of each chart is what this model substantiates.
- Documents the user uploads or points at: invoices, contracts, medical bills, payroll records, repair estimates, financial statements, expert reports.

If the config CLAUDE.md has `[PLACEHOLDER]` markers, surface the bounce per plugin convention (run `/litigation-legal:cold-start-interview`, or say "provisional" for a generic-defaults run with every output tagged `[PROVISIONAL]`).

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Write outputs to the matter folder. Never read another matter's files unless `Cross-matter context` is `on`.

**Conflicts gate — unbypassable.** Before building the model, check `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't build a damages model on a matter that hasn't been intaken — the conflicts check is the gate."

## Workflow

### Step 1: Damages theory per claim

For each claim in the matter (from `matter.md`, the claim charts, or `--claim`):

- **Contract claims** — pick the measure and say why: **expectation** (benefit of the bargain — the default), **reliance** (out-of-pocket, when expectation is too speculative), or **restitution** (defendant's gain, when that exceeds the loss or the contract is unenforceable). The measures are alternatives, not additives — flag any double-count risk between them. Check the contract itself for limitation-of-liability clauses, consequential-damages waivers, and liquidated-damages provisions; a clause read this session is a cite, an unread contract is `[contract not reviewed — limitation clauses unknown]`.
- **Tort claims** — **economic** (medical specials, lost earnings, property damage) and **non-economic** (pain and suffering, emotional distress, loss of consortium). Note any statutory caps on non-economic damages `[verify per jurisdiction]` and whether the economic-loss rule limits tort recovery for what is really a contract loss `[model knowledge — verify]`.
- **Statutory claims** — statutory damages where the statute provides them (per-violation amounts, ranges, multipliers), fee-shifting, and treble-damages provisions. Statutory amounts are quoted from the statute (retrieved and tagged), or `[model knowledge — verify]`.
- **Every claim** — what the claim CANNOT recover, stated explicitly. The fastest way to lose credibility in a mediation is a model that includes a category the cause of action doesn't support. Flag overlaps between claims (the same lost dollar pleaded under contract and tort is recovered once).

### Step 2: Categories table — the spine of the model

Every damages item gets a row:

| # | Category | Claim(s) | Amount / range | Calculation basis | Supporting documentation | Status |
|---|---|---|---|---|---|---|
| 1 | [e.g., unpaid invoices] | [breach of K] | [$X `[user provided]` / `[PLACEHOLDER — needs documentation]`] | [e.g., sum of invoices 1042–1057] | [path / Bates / "none yet"] | documented / needs-documentation / needs-expert |

Status definitions — these drive the work plan:

- **documented** — the amount is supported by a document read this session, cited in the row.
- **needs-documentation** — the amount is asserted (by the user or inferred from the narrative) but the supporting document hasn't been provided. The amount stays in the table tagged `[user provided]` or stays as `[PLACEHOLDER — needs documentation]` if no figure was given.
- **needs-expert** — the amount cannot be established by fact documents alone (lost profits, earning capacity, future medicals, diminution in value, reasonable royalty). The row gets `[needs expert]` and names the expert discipline (forensic accountant, vocational economist, life-care planner, appraiser).

### Step 3: Specials build-up

The hard, document-backed losses — itemized, not lumped:

- **Medical** (tort) — each provider, each bill, billed vs. paid amounts noted (the collateral-source and "billed vs. paid" rules vary by state `[verify per jurisdiction]`), liens flagged (health insurer, Medicare/Medicaid — these reduce the net recovery and are someone's repayment obligation).
- **Lost wages** (to date) — pay records, the off-work period, the rate. Document-pointed: payroll records or W-2s, not memory.
- **Repair / replacement costs** — estimates vs. invoices distinguished (an estimate is a projection; an invoice is a special).
- **Out-of-pockets** — every receipt-backed item: travel to treatment, mitigation expenses (these double-count with the mitigation audit — reconcile), cover purchases (UCC § 2-712 cover for goods cases `[model knowledge — verify]`).

Each item lands as a row in the Step 2 table. The build-up section is the itemization behind the rows.

### Step 4: Future / projected damages — `[needs expert]`

Everything that requires projection gets flagged, not computed:

- **Lost earning capacity** — vocational and economic expert territory. The skill can list the inputs an expert will need (age, occupation, earnings history, work-life expectancy) but does not compute present value itself.
- **Future medical** — life-care planner territory.
- **Lost profits** — forensic accountant territory, with the **new-business rule caveat** stated wherever the claimant is a new or unestablished business: many jurisdictions bar or sharply limit lost-profits recovery for businesses without an earnings track record, though the modern trend is toward treating it as an evidentiary (reasonable-certainty) hurdle rather than a per-se bar `[model knowledge — verify]`. A lost-profits number for a two-year-old startup carries this caveat in bold.
- **Future non-economics** — jury territory; the model carries it as a stated-assumption range in the scenarios, never as a computed figure.

The skill may do **arithmetic** the user explicitly requests on stated assumptions (e.g., "project $X/month for 24 months = $Y `[computed: X × 24, assumption: 24-month period — needs expert validation]`"), but the row's status stays **needs-expert**. Arithmetic is not an expert opinion.

### Step 5: Mitigation audit

The duty to mitigate is the defense's first cross-examination of the damages case. Audit it now:

- **What mitigation the law expected** — cover (contract/goods), seeking comparable employment (employment), following medical advice (injury), re-letting (lease) `[model knowledge — verify]` per claim type.
- **What was actually done** — dated, documented. This feeds the chronology; offer to sync with `/litigation-legal:chronology`.
- **Exposure if mitigation is found inadequate** — which categories shrink and by roughly how much (scenario math, stated assumptions).
- **Mitigation expenses** — recoverable as damages themselves; make sure they're in the Step 2 table once and only once.

### Step 6: Prejudgment interest

- **Statutory basis** — the statute or rule that provides prejudgment interest for each claim `[verify per jurisdiction]`, whether it's discretionary or of right, and whether the claim must be "liquidated" or "certain" to qualify `[model knowledge — verify]`.
- **Rate and accrual date** — `[verify per jurisdiction]` — statutory rates change and several states peg them to a floating index. The accrual trigger (breach date, demand date, filing date) is claim- and state-specific.
- **The computation** — shown as a formula on the documented principal, by scenario, clearly labeled: `[computed: principal × rate × years — rate and accrual date require verification]`. Interest computed on a placeholder principal is itself a placeholder.

### Step 7: Comparative / contributory fault haircut scenarios

For tort claims (and contract claims where causation-apportionment or failure-to-mitigate operates similarly):

- State the jurisdiction's regime: pure comparative / modified comparative (50% bar or 51% bar) / contributory negligence `[verify per jurisdiction]` — in a contributory jurisdiction, any plaintiff fault can bar recovery entirely, which changes the whole scenario table.
- Build the haircut table: recovery at 0% / 25% / 50% plaintiff fault (and the bar threshold if modified). These are scenario math, not predictions of what a jury will assign.

### Step 8: Output — the model

Write to `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/damages-model.md`:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> **⚠️ Reviewer note**
> - **Sources:** [research connector status per the pre-flight check — interest rates, caps, and damages-availability rules from training knowledge unless tagged otherwise]
> - **Read:** [N supporting documents read | N items have no documentation yet]
> - **Flagged for your judgment:** [N items marked `[review]`; N rows `[needs expert]`; N rows `[PLACEHOLDER — needs documentation]`]
> - **Currency:** [interest rates / caps checked against current statute? | could not search — verify before using]
> - **Before relying:** this model contains no invented numbers — every figure is documented, user-provided, or a placeholder. The range is scenario math on stated assumptions, not a case valuation. Do not put any number from this model into a demand, disclosure, or mediation statement until its row reads "documented."

# Damages Model — [Matter Name]

**Matter:** [slug]
**Claims modeled:** [list]
**Built:** [YYYY-MM-DD]   **Version:** [N]
**Documented total:** $[sum of documented rows only]
**Gap count:** [N needs-documentation / N needs-expert]

---

## Damages theory

[Per-claim measure selection and exclusions from Step 1.]

## Categories table

[The Step 2 table — the spine.]

## Specials build-up

[Step 3 itemization.]

## Future / projected damages

[Step 4 — every row `[needs expert]`, with the expert discipline named. New-business rule caveat where applicable.]

## Mitigation audit

[Step 5.]

## Prejudgment interest

[Step 6 — basis, rate `[verify per jurisdiction]`, computation by scenario.]

## Fault scenarios

[Step 7 haircut table.]

## The range

| Scenario | Assumptions | Amount |
|---|---|---|
| **Low** | [e.g., documented specials only; no lost profits; no interest; 25% fault haircut] | $[computed] |
| **Mid** | [stated] | $[computed] |
| **High** | [e.g., all categories including expert-dependent items at claimed values; full interest; no haircut] | $[computed] |

*Punitive damages: [excluded from all scenarios / shown separately] — rarely awarded, conduct-dependent, constitutionally constrained to single-digit ratios as a guidepost `[model knowledge — verify]`.*

**Assumption register:** [every assumption behind the scenarios, numbered, so a reviewer can reject one and see what moves]

## Work plan (the gaps)

| Row | What's missing | Who gets it | By when |
|---|---|---|---|
| [#] | [the document or the expert] | [client / counsel / expert] | [date] |
```

Append to `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/history.md`:

```
## [YYYY-MM-DD] — Damages model v[N] built

Documented total: $[X]. Gaps: [N needs-documentation, N needs-expert]. Range: $[low]–$[high] on stated assumptions.
```

**`--update` runs:** read the prior model, carry forward documented rows, re-ask about gap rows, and present a diff (what got documented, what changed, what's still open). Version increments. The exposure/value figure in `_log.yaml` may warrant updating — propose the change, show the diff, and let the user confirm before writing (cross-skill severity floor: if the new mid scenario crosses a severity band in the practice profile's risk calibration, flag the band change rather than silently re-rating).

**Dashboard offer.** This output is data-heavy (categories table + scenarios). Offer the dashboard per plugin CLAUDE.md `## Outputs` — summary stats (documented total, gap count, range), the categories table sortable by status, and a chart of documented vs. gap amounts by category. Escape all untrusted cell content per the dashboard rules.

## Consequential-action gates

The model is internal work product. **Numbers leave the building only through a gate.** Before any of the following, read `## Who's using this` in the config CLAUDE.md; if the Role is Non-lawyer, require the attorney-review gate (1-page brief for their attorney; do not proceed on the user's say-so alone). For all roles, require an explicit go before:

- **Putting a number in a demand letter** — route to `/litigation-legal:demand-intake` / `/litigation-legal:demand-draft`; the demand amount is a strategy call (anchor high vs. credible-first-offer) the model informs but does not make.
- **Serving the computation in initial disclosures** (FRCP 26(a)(1)(A)(iii)) or discovery responses — these are court-facing representations with supplementation duties; placeholder rows cannot be served.
- **Sharing the model with a mediator, opposing counsel, or an insurer** — that's a privilege/work-product destination decision per the plugin CLAUDE.md `## Shared guardrails` destination check.
- **Engaging an expert** — the engagement defines discoverability (consulting vs. testifying expert); counsel structures it.

> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent).

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — natural branches here:

1. **Work the gaps** — I'll turn the work plan into specific document requests to the client and a list of expert disciplines to engage.
2. **Feed the demand** — run `/litigation-legal:demand-intake` with this model as the damages basis (documented rows only, unless you decide otherwise).
3. **Update the claim chart** — push the documented rows into the damages element of `/litigation-legal:claim-chart`.
4. **Re-rate the matter** — the mid scenario [does / does not] cross your severity bands; I'll draft the `/litigation-legal:matter-update` entry.
5. **Something else** — tell me what you'd do with this.

The tree is the output; the lawyer picks.

## What this skill does not do

- **Invent, estimate, or "ballpark" any amount.** Hard rule 1. The placeholders are the honest answer.
- **Value the case.** The range is scenario math on damages; case value requires liability odds, collectability, and cost-of-litigation judgments this skill does not make. Collectability lives in `/litigation-legal:pre-suit-investigation` (pre-suit screen) and `/litigation-legal:judgment-enforcement` (post-judgment).
- **Replace the damages expert.** Rows marked `[needs expert]` stay that way until a retained expert's figures replace them — at which point the row cites the expert report.
- **Decide what number goes in the demand.** The model informs; counsel anchors.
- **Compute taxes, liens, or net-to-client.** Fee arrangements, costs, lien resolution, and tax treatment of recoveries are real and out of scope — flag them in the reviewer note so nobody mistakes the gross range for a net one.
