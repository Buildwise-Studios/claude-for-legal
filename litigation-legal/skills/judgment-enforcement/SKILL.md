---
name: judgment-enforcement
description: Plan post-judgment enforcement — judgment audit (finality, interest, renewal deadline), asset discovery via post-judgment devices and public records, enforcement device selection per asset type (garnishment, levy, lien, charging order, receivership, domestication), exemptions audit, and a fraudulent-transfer screen, ending in an enforcement plan ranked by likely recovery vs cost. Use when the user says "we won, now collect", "enforce the judgment", "the defendant won't pay", or needs a collection plan against a judgment debtor.
argument-hint: "[slug] [--judgment-date=YYYY-MM-DD] [--domesticate=<state>]"
---

# /judgment-enforcement

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, work-product header, risk calibration, landscape. Config lives at the home path or, in environments where that isn't writable (Claude Cowork), at `./claude-for-legal-config/litigation-legal/` in the working folder — check both; home wins if both exist.
2. If matter workspaces enabled, confirm or select the active matter; otherwise resolve the slug from the argument.
3. Follow the workflow and reference below.
4. Conflicts gate: confirm the matter is in `_log.yaml`; refuse and route to `/litigation-legal:matter-intake` if not.
5. FDCPA screen: determine whether the judgment arises from a consumer debt — if yes or unclear, the collection-law compliance flag attaches to every downstream step.
6. Run the judgment audit: final? appealed? amount, post-judgment interest, expiration/renewal deadline — every figure `[verify per jurisdiction]`.
7. Plan asset discovery: post-judgment discovery devices + public-records searches.
8. Select enforcement devices per asset type; run the exemptions audit and the fraudulent-transfer screen.
9. Write `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/enforcement-plan.md`; append to `history.md`.
10. Confirm with the user: "Here's the plan ranked by recovery vs cost — does the ranking match your read of the debtor?" Close with the decision tree.

---

# Judgment Enforcement

## Purpose

A judgment does not collect itself. Most defendants who litigated to judgment and lost do not mail a check; the second case — turning the judgment into money — starts the day the judgment enters, has its own deadlines, its own discovery, and its own ways to be lost. This skill plans that second case: what the debtor has, which device reaches each asset, what the law protects from collection, and whether assets walked out the door while the first case was pending.

The output is an enforcement plan ranked by likely recovery against cost, because enforcement is the part of litigation where spending $40,000 to collect $25,000 is a real and common failure.

## Jurisdiction assumption

This skill's frame is US practice: FRCP 69 (which borrows state enforcement procedure even in federal court `[model knowledge — verify]`), state enforcement-of-judgments law, the Uniform Enforcement of Foreign Judgments Act (UEFJA) for sister-state domestication, the Uniform Voidable Transactions Act (UVTA, formerly UFTA) for fraudulent transfers, and the FDCPA where the creditor is collecting a consumer debt. Every operative number in this domain — exemption amounts, interest rates, judgment lifespans, renewal windows, garnishment percentages — is set by state statute, changes, and is `[verify per jurisdiction]` without exception. **If the judgment or the debtor's assets are outside the US, say so before doing substantive work**, per the plugin CLAUDE.md `## Jurisdiction recognition`: cross-border enforcement runs through different instruments entirely (the 2019 Hague Judgments Convention, country-specific recognition statutes, or comity doctrine), and the US framework does not transfer. Tag every conclusion `[US framework — verify against [jurisdiction] law]` if the user asks you to proceed anyway, and offer to search for the applicable standard or route to a local practitioner.

## Hard rules — collection conduct

1. **FDCPA / state collection-law compliance flag.** If the judgment arises from a consumer debt — money owed by a natural person for personal, family, or household purposes — federal FDCPA (for those it covers) and state collection statutes (some of which, like California's Rosenthal Act, cover original creditors `[model knowledge — verify]`) regulate how collection happens: contact methods, timing, statements that can be made, and threats that cannot. The skill determines the consumer-vs-commercial character of the debt at Step 0 and, where consumer or unclear, attaches the compliance flag to every contact-the-debtor step in the plan: `[FDCPA / state collection law — review before any debtor contact]`. Violations carry statutory damages and fee-shifting against the creditor.
2. **Exemptions are debtor protections — present them accurately, never strategize around them.** Homestead exemptions, wage-garnishment limits, and retirement-account protections exist to keep judgment debtors housed, fed, and able to retire. The skill states what they protect, with accurate (verify-tagged) amounts, so counsel can calculate realistic recovery. It does not propose timing, structuring, or characterization tactics designed to defeat an exemption the debtor is entitled to claim. The line: identifying non-exempt assets is enforcement; engineering around exemptions is not something this skill helps with.
3. **Every jurisdiction-specific number is `[verify]`.** Exemption dollar amounts, post-judgment interest rates, judgment lifespans, renewal periods, garnishment percentages, and lien durations. No exceptions — these change by statute, by year, and sometimes by county. A stale exemption amount in an enforcement plan produces either an unlawful levy or money left on the table.
4. **No self-help, no harassment, no misrepresentation.** Enforcement runs through court process — writs, levies served by sheriffs or marshals, recorded liens. The skill never suggests repossession-style self-help, contact designed to embarrass the debtor, or communications that misstate what the creditor can legally do.

## Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → `## Outputs`, `## Decision posture`, risk calibration (enforcement spend vs. recovery is a risk-calibration call), landscape (the debtor may be a frequent adversary with known structure), house style.
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/matter.md` and `_log.yaml` row — the underlying matter, the judgment amount if recorded at close, the debtor's identity.
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/history.md` — whether `/litigation-legal:matter-close` already recorded a judgment outcome; this skill typically runs on a matter in `judgment` posture, before or instead of close.
- The judgment itself — the user uploads or points at it. The skill does not characterize a judgment it hasn't read; if unavailable, every judgment-audit field is `[user provided]` or `[PLACEHOLDER]`.
- Pre-suit collectability screen from `/litigation-legal:pre-suit-investigation`, if one was run — it's the starting asset map.

If the config CLAUDE.md has `[PLACEHOLDER]` markers, surface the bounce per plugin convention (run `/litigation-legal:cold-start-interview`, or say "provisional" for a generic-defaults run with every output tagged `[PROVISIONAL]`).

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Write outputs to the matter folder. Never read another matter's files unless `Cross-matter context` is `on`.

**Conflicts gate — unbypassable.** Before planning enforcement, check `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't plan enforcement on a matter that hasn't been intaken — the conflicts check is the gate."

A judgment obtained elsewhere (e.g., by predecessor counsel, or a domesticated foreign judgment) still gets intaken as a matter — `source: internal-report`, posture `judgment` — so the portfolio tracks the renewal deadline.

## Workflow

### Step 0: Consumer-debt screen (runs first, every time)

Before anything else: **what kind of debt underlies this judgment?**

- **Commercial** (business-to-business, or against a business entity) → FDCPA generally inapplicable; state commercial-collection norms still apply; proceed.
- **Consumer** (natural-person debtor; personal, family, or household purpose) → the FDCPA flag attaches (Hard rule 1). Note who the flag binds: the FDCPA covers "debt collectors" (third-party collectors, debt buyers, and attorneys who regularly collect `[model knowledge — verify]`); state statutes may cover the creditor directly. The plan marks every debtor-contact step.
- **Unclear** → treat as consumer until counsel determines otherwise. `[review]`

### Step 1: Judgment audit

Read the judgment (or take user-provided fields, tagged as such):

| Field | Value | Notes |
|---|---|---|
| Court + case number | | |
| Judgment date | | |
| Final? | yes / no | Post-trial motions resolved? Is it a final judgment or an interlocutory order? `[review]` |
| Appealed / appealable? | | Appeal deadline `[verify per jurisdiction]`; is enforcement stayed (supersedeas bond posted?) `[review]` |
| Principal amount | $ | From the judgment, not from memory |
| Costs / fees awarded | $ | Separate line; may require a post-judgment motion with its own deadline `[verify]` |
| Post-judgment interest rate | % `[verify per jurisdiction]` | Federal: 28 U.S.C. § 1961 (T-bill-pegged) `[model knowledge — verify]`; states: statutory, often much higher |
| Accrued interest to date | $ `[computed: principal × rate × days/365]` | Recompute at every action |
| Judgment lifespan | N years `[verify per jurisdiction]` | |
| **Renewal deadline** | **[date] `[verify per jurisdiction]`** | **The deadline that kills judgments. Calendar it now; missing it can extinguish the judgment entirely.** |

If the judgment is not final, is stayed, or has an unresolved appeal: **stop the planning at the audit**. Present the audit, flag the posture (`[review — enforcement may be premature or stayed]`), and let counsel decide whether limited steps (lien recording where permitted, asset surveillance via public records) are worth taking. Enforcement against a stayed judgment exposes the creditor to wrongful-levy liability.

### Step 2: Asset discovery

Two tracks, run in parallel:

**Track A — post-judgment discovery devices** (court process; available because the client holds a judgment):

- **Debtor examination** (judgment-debtor exam / supplementary proceedings) — the debtor answers asset questions under oath. The skill drafts the examination outline: bank accounts, employment, real property, vehicles, business interests, transfers in the lookback period (feeds Step 5), safe-deposit boxes, money owed to the debtor. Service and appearance requirements `[verify per jurisdiction]`.
- **Document subpoenas / post-judgment interrogatories and requests** — bank statements, tax returns (often requires heightened showing `[verify]`), accounts receivable, asset schedules.
- **Third-party discovery** — banks, employers, business partners, title companies. Third parties holding debtor assets can be examined too `[verify per jurisdiction]`.

**Track B — public records** (no court process needed; same sources as the pre-suit screen, now run in earnest):

- Real property (county recorder/assessor), UCC filings (competing secured creditors and what the debtor pledged), corporate registries (entities the debtor owns or officers), court dockets (other judgments — the debtor likely has other creditors; priority matters), DMV/vessel/aircraft registries where accessible, PACER (a bankruptcy filing changes everything — see the automatic-stay note in Step 3).

Output: an asset inventory table — asset, type, estimated value `[user provided / public record / PLACEHOLDER]`, senior encumbrances, and the device that reaches it (Step 3).

### Step 3: Enforcement device selection — per asset type

| Asset type | Device | Key mechanics | Watch for |
|---|---|---|---|
| Wages | **Wage garnishment** | Writ served on employer; employer withholds per pay period | Federal CCPA cap: generally the lesser of 25% of disposable earnings or the amount above 30× federal minimum wage `[model knowledge — verify]`; state limits are often lower `[verify per jurisdiction]`; some states bar wage garnishment almost entirely |
| Bank accounts | **Bank levy** | Writ of execution served on the bank; freezes then turns over | Exempt funds in the account (Social Security, disability — federally protected `[verify]`); joint accounts; the debtor learns and moves money — timing matters |
| Real property | **Judgment lien + foreclosure** | Record the abstract/judgment in each county where debtor owns property; lien attaches; foreclose or wait for sale/refinance | Homestead exemption (Step 4); senior liens; foreclosure on a homestead is often uneconomical — the lien-and-wait strategy usually wins |
| Business (operating) | **Till tap / keeper / receivership** | Sheriff collects cash on premises (till tap), or a keeper/receiver takes over receipts | Cost vs. yield; receivership is the expensive option for a business with real revenue `[verify per jurisdiction]` |
| LLC / partnership interests | **Charging order** | Court charges the debtor's distributional interest; creditor receives distributions | In many states the charging order is the **exclusive** remedy against LLC interests `[verify per jurisdiction]`; the debtor can often starve it by not distributing |
| Vehicles / personal property | **Writ of execution + sheriff's sale** | Levy and auction | Exemption amounts for vehicles/tools of trade `[verify]`; auction yields are poor — usually low priority |
| Receivables / debts owed to debtor | **Assignment order / garnishment of the account debtor** | Third parties who owe the debtor pay the creditor instead | Notice requirements; contesting third parties |
| Out-of-state assets | **Domestication under UEFJA** (or registration under 28 U.S.C. § 1963 for federal judgments `[model knowledge — verify]`) | File the foreign judgment in the asset's state; it becomes enforceable there | Each state's UEFJA filing mechanics and notice requirements `[verify]`; the receiving state's exemptions and procedures then govern; `--domesticate=<state>` focuses this row |

**Bankruptcy tripwire (applies to every device):** if the debtor files bankruptcy, the automatic stay halts all of this immediately — continuing to enforce after the stay violates federal law and creates liability `[model knowledge — verify]`. Liens perfected before filing generally survive; preferences (payments collected within 90 days of filing) can be clawed back by the trustee. The plan flags this on every device: enforcement is a race that bankruptcy ends.

### Step 4: Exemptions audit

For each asset in the inventory, what the debtor can protect — presented accurately per Hard rule 2:

| Exemption | What it protects | Amount / scope | Tag |
|---|---|---|---|
| Homestead | Equity in the primary residence | Varies enormously — from ~$25k to unlimited (TX, FL) | `[verify per jurisdiction]` |
| Wage exemption | Portion of earnings | Federal CCPA floor + state overlays, frequently more protective | `[verify per jurisdiction]` |
| Retirement accounts | ERISA-qualified plans (federal anti-alienation), IRAs | ERISA plans generally unreachable `[model knowledge — verify]`; IRA protection varies by state and amount `[verify]` |
| Public benefits | Social Security, disability, unemployment, veterans' benefits | Federally exempt from garnishment `[model knowledge — verify]` |
| Tools of trade / vehicle / personal effects | Statutory lists with dollar caps | `[verify per jurisdiction]` |
| Wildcard | Anything, up to a capped amount | `[verify per jurisdiction]` |

The audit's output is the **net-reachable column** of the asset inventory: asset value, minus senior encumbrances, minus applicable exemptions = what enforcement can actually reach. This column is what makes the Step 6 ranking honest.

### Step 5: Fraudulent-transfer screen (UVTA)

Did assets move while the case was pending — or after the judgment?

- **Badges of fraud** (UVTA § 4(b) `[model knowledge — verify]`): transfer to an insider; debtor retained possession or control after the transfer; transfer concealed; made after suit was filed or threatened; transfer of substantially all assets; debtor absconded; consideration not reasonably equivalent; debtor insolvent at or shortly after the transfer; transfer shortly before or after a substantial debt was incurred.
- **The screen:** compare the asset picture over time — pre-suit screen (if `/litigation-legal:pre-suit-investigation` ran), trial-period financial discovery, and the current Step 2 inventory. Property that appears in an earlier snapshot and not the current one, with a transfer to a spouse, family member, or affiliate entity in between, gets a row: transferee, date, consideration, badges present.
- **Clawback considerations:** UVTA actions have their own limitations period (commonly 4 years from transfer or 1 year from discovery `[verify per jurisdiction]`), are a separate lawsuit (or post-judgment motion in some states `[verify]`), and name the transferee as a defendant — which means a new conflicts check on the transferee before filing. Route back through `/litigation-legal:matter-intake` for any clawback action; it's a new matter.
- The screen identifies and documents; whether to bring the action is a counsel decision the Step 6 ranking informs (clawback litigation cost vs. asset value).

### Step 6: Output — the enforcement plan

Write to `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/enforcement-plan.md`:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> **⚠️ Reviewer note**
> - **Sources:** [research connector status per the pre-flight check — exemption amounts, interest rates, renewal periods, and device mechanics from training knowledge unless tagged otherwise; ALL require verification against current state statute before any writ issues]
> - **Read:** [judgment read? asset sources reviewed? | what was NOT read]
> - **Flagged for your judgment:** [N items marked `[review]` — finality/stay posture, consumer-debt character, exemption applications, clawback decision]
> - **Currency:** [exemption amounts and rates checked? | could not search — every figure is `[verify]`]
> - **Before relying:** verify the renewal deadline first (it is the only unrecoverable date in this plan); confirm the stay/appeal posture; nothing in this plan is served or filed without attorney sign-off.

# Enforcement Plan — [Matter Name]

**Matter:** [slug]
**Judgment:** $[principal] + $[accrued interest `[computed]`] entered [date], [court]
**Renewal deadline:** [date] `[verify per jurisdiction]` ← calendared
**Consumer-debt flag:** [yes — FDCPA/state compliance required | no — commercial | unclear, treated as consumer] `[review]`
**Built:** [YYYY-MM-DD]

---

## Judgment audit

[Step 1 table.]

## Asset inventory

[Step 2 inventory with the net-reachable column from Step 4.]

## Enforcement plan — ranked by likely recovery vs cost

| Rank | Device | Target asset | Net reachable | Est. cost | Time to money | Procedural steps + deadlines | Flags |
|---|---|---|---|---|---|---|---|
| 1 | [device] | [asset] | $[net of exemptions/encumbrances] | $[filing + service + counsel time] | [weeks/months] | [the specific writ/application sequence with each deadline `[verify]`] | [FDCPA / stay / bankruptcy-risk flags] |

*Ranking basis: net reachable value ÷ estimated cost, adjusted for time-to-money and execution risk. The ranking is a recommendation structure, not a decision — counsel reorders it.* `[review]`

## Exemptions audit

[Step 4 table — what the debtor is protected on, presented accurately.]

## Fraudulent-transfer screen

[Step 5 findings: transfers identified, badges present, clawback limitations dates `[verify]`, and the new-matter/conflicts note for any action against a transferee.]

## What we are NOT doing and why

[Devices considered and rejected — uneconomical, asset exempt, stay in place. Recorded so the next reviewer doesn't re-propose them.]
```

Append to `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[slug]/history.md`:

```
## [YYYY-MM-DD] — Enforcement plan built

Judgment $[amount]; renewal deadline [date]. Top-ranked device: [device] against [asset]. FDCPA flag: [yes/no]. Fraudulent-transfer findings: [N transfers flagged].
```

Update the `_log.yaml` row: `next_deadline:` becomes the earlier of the renewal deadline and the first procedural deadline in the plan; `stage: judgment-enforcement`. Show the diff before writing.

**Dashboard offer.** The plan is data-heavy (asset inventory + ranked device table). Offer the dashboard per plugin CLAUDE.md `## Outputs` — summary stats (judgment total with interest, net reachable total, top device), the ranked table, and a recovery-vs-cost chart. Escape all untrusted cell content per the dashboard rules.

## Consequential-action gates

Planning is analysis; **execution is consequential and irreversible in ways that create liability** (wrongful levy, FDCPA violations, stay violations). Before any of the following, read `## Who's using this` in the config CLAUDE.md; if the Role is Non-lawyer, require the attorney-review gate (1-page brief for their attorney; do not proceed on the user's say-so alone). For all roles, require an explicit go before:

- **Serving post-judgment discovery or noticing a debtor exam** — court process with sanctions exposure for misuse.
- **Applying for any writ, levy, or garnishment** — wrongful levy on exempt property or a stayed judgment creates creditor liability.
- **Recording a judgment lien** — generally lower-risk, but it's a public filing against title; slander-of-title exposure if the judgment is defective `[review]`.
- **Any direct contact with the debtor** — when the consumer flag is set, FDCPA/state-law compliance review happens first, every time.
- **Filing a domestication or a fraudulent-transfer action** — new proceedings; the transferee action also requires a fresh conflicts check via `/litigation-legal:matter-intake`.

> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent).

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — natural branches here:

1. **Draft the first device's papers** — I'll draft the [writ application / garnishment papers / debtor-exam notice] for the top-ranked device, for attorney review and filing.
2. **Run asset discovery first** — I'll draft the debtor-examination outline and document subpoenas; the plan gets re-ranked when the answers come back.
3. **Calendar and wait** — record the renewal deadline and lien positions, then watch for a sale or refinance event (often the cheapest path on real property). I'll draft the `/litigation-legal:matter-update` entry.
4. **Negotiate instead** — a payment plan or discounted lump sum may beat enforcement cost; I'll build the comparison off the ranked table.
5. **Close the matter** — if the plan shows enforcement is uneconomical, run `/litigation-legal:matter-close` with outcome "judgment — not economically collectible" so the record shows why.

The tree is the output; the lawyer picks.

## What this skill does not do

- **Execute anything.** No writ is applied for, no lien recorded, no garnishment served, no debtor contacted by this skill. It plans and drafts; counsel reviews, signs, files, and serves.
- **Help defeat exemptions.** Hard rule 2. The skill maps what's protected so the recovery math is honest — not so the protections can be engineered around.
- **Provide current exemption amounts, rates, or deadlines as fact.** Every such figure is `[verify per jurisdiction]`. The plan is a structure; the statutes supply the numbers.
- **Advise the debtor.** This is a creditor-side skill. If the user is the judgment debtor seeking protection advice, say so plainly and route to counsel — the same information has different duties attached.
- **Handle bankruptcy.** If the debtor files, the plan stops and bankruptcy counsel takes over — the automatic stay, claims process, and adversary proceedings are a different practice area.
