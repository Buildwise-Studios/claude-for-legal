# England & Wales — Claim Chart / Element Chart

*England & Wales reference for the claim-chart skill — **England and Wales only: Scotland and Northern Ireland are separate legal systems and this file does not cover them.** Reviewed by: [pending E&W practitioner review]; last confirmed against the CPR/PDs: [date pending]. **Treat the contents as unverified**: carry every `[verify — CPR/PD current text]` tag into downstream output, do not promote any statement here to a confirmed or `[settled]` citation, and tell the reviewing solicitor that the doctrine below has not yet had a practitioner pass.*

This file replaces the US pleading and dispositive-motion frame in the main SKILL.md when the procedural frame is England & Wales (CPR). The chart mechanics — element rows, pin cites, gap detection as the priority output — are unchanged. What changes is the vocabulary, the standards each phase of the chart is tested against, and where the elements come from.

---

## Vocabulary map

| US term in SKILL.md | England & Wales equivalent |
|---|---|
| Complaint | Claim form + particulars of claim (CPR Part 7 / Part 16) |
| Answer | Defence (CPR Part 15 / 16) |
| Motion to dismiss / Rule 12(b)(6) | Application to strike out — CPR 3.4(2)(a) |
| Motion for summary judgment (FRCP 56) | Summary judgment application — CPR Part 24 |
| Iqbal / Twombly plausibility | "No reasonable grounds" (strike-out) / "no real prospect" (summary judgment) |
| Affirmative defense | Matters pleaded in the defence (limitation, set-off, contributory negligence, etc.) |
| Pattern jury instructions (CACI / NYPJI) | None — civil jury trial is exceptional in E&W; elements come from case law and statute |
| Discovery | Disclosure (PD 57AD in the Business & Property Courts; CPR Part 31 elsewhere) |
| Rule 11 certification | Statement of truth (CPR Part 22) + contempt exposure (CPR 32.14) |
| Counsel of record signs | Statement of truth signed by the party or its legal representative |

Do not emit US terms in an E&W chart. A chart that talks about "the complaint" and "MSJ" to a solicitor reads as unreviewed AI output.

---

## 1. What must be pleaded — particulars of claim (CPR Part 16 / PD 16)

The particulars of claim must contain a **concise statement of the facts** on which the claimant relies (CPR 16.4(1)(a)). E&W pleading is fact pleading: the material facts that constitute each element of the cause of action, not evidence, not argument.

CPR 16.4 also requires, where applicable:

- details of any **interest** claimed — the basis (contract, statute — s.35A Senior Courts Act 1981 for High Court claims), the rate, the period, and the amount accrued at the date of calculation `[verify — CPR/PD current text]`
- a statement of any claim for **aggravated damages, exemplary damages, or provisional damages**, with grounds

**PD 16 requires certain matters to be specifically set out** in the particulars (or, for some, in the defence). The chart's `_elements` sheet should flag these because omitting them is a strike-out / amendment target. The recurring ones `[verify — CPR/PD current text for the paragraph numbers and the full list]`:

- claims based on a **written agreement**: attach or serve a copy of the contract / documents constituting the agreement
- claims based on an **oral agreement**: the contractual words used, who spoke them, to whom, when and where
- claims based on an **agreement by conduct**: the conduct relied on and when
- allegations of **fraud**, the details of any **misrepresentation**, **breaches of trust**, **wilful default**, **undue influence**, and **unsoundness of mind** — full particulars required
- **notice or knowledge** of a fact — particulars of how and when acquired
- facts relating to **mitigation** of loss

Fraud has a professional-conduct overlay: counsel and solicitors must not plead fraud without reasonably credible material establishing a prima facie case. A `gap` state on a fraud element is not just a discovery lead — it is a reason the allegation may not be pleadable at all. Flag `[review]`.

---

## 2. The standards the chart is tested against

### 2.1 Strike-out — CPR 3.4(2)(a)

The court may strike out a statement of case (or part of it) if it discloses **no reasonable grounds for bringing or defending the claim**. This is the nearest functional analogue to a Rule 12(b)(6) motion, but the test is not Iqbal/Twombly plausibility:

- The question is whether the statement of case, **taken at its highest**, discloses a legally recognisable claim or defence with the necessary elements pleaded.
- A claim that pleads every element with material facts will generally survive strike-out even if the evidence looks thin — evidential weakness is a summary-judgment question, not a strike-out question.
- CPR 3.4(2)(b) (abuse of process) and 3.4(2)(c) (failure to comply with a rule, PD, or order) are separate limbs — note them but they are not element-mapping questions.

**Chart use:** in pre-issue / pleadings phase, an element row with state `gap` or `not-found` against the *pleaded facts* is a strike-out vulnerability (own side) or a strike-out target (opponent's pleading under `--review`).

### 2.2 Summary judgment — CPR Part 24

The court may give summary judgment against a claimant or defendant on the whole claim or on an issue if:

1. the party has **no real prospect** of succeeding on the claim/issue (claimant) or of successfully defending it (defendant), **and**
2. there is **no other compelling reason** why the case or issue should be disposed of at a trial.

(CPR 24.3 in the current numbering; this rule was renumbered from CPR 24.2 in the 2023 amendments — `[verify — CPR/PD current text]`.)

"Real prospect" means realistic, not fanciful (*Swain v Hillman*). The court does not conduct a mini-trial, but it is not required to accept implausible assertions at face value; the often-cited synthesis of the principles is *Easyair Ltd v Opal Telecom Ltd* [2009] EWHC 339 (Ch) `[verify — characterization stable but confirm the principles list before citing in a filed document]`.

**Chart use:** in the summary-judgment phase, a `supported` row with no contradicting evidence is application material; a `disputed` row is what defeats the application (a triable issue). Either side can apply — including a claimant for summary judgment on the claim, which has no clean US-MSJ-practice analogue in many states.

### 2.3 Burden and standard of proof

Civil standard: **balance of probabilities** throughout. There is no E&W equivalent of the US "clear and convincing" intermediate standard; allegations of fraud are still decided on the balance of probabilities (though cogent evidence is in practice expected for serious allegations). If the chart is in patent/invalidity mode, do not import the US clear-and-convincing language.

---

## 3. Statement of truth (CPR Part 22) and contempt exposure

Every statement of case must be verified by a **statement of truth**: the party (or its legal representative) confirms that the facts stated are true — in the current prescribed wording, that the signatory believes the facts are true and acknowledges that proceedings for contempt of court may be brought against anyone who makes, or causes to be made, a false statement in a document verified by a statement of truth without an honest belief in its truth `[verify — CPR/PD current text for exact prescribed wording]`.

- A false statement in a verified document is punishable as **contempt of court** (CPR 32.14).
- This is the E&W functional counterpart of Rule 11, but it attaches to the *facts pleaded*, not to the legal contentions, and it binds the **client** (or the representative who signs on the client's behalf), not just the lawyer.

**Chart use:** every factual assertion that will be carried from the chart into a pleading must be verifiable by the client signing the statement of truth. A row whose evidence is `needs-evidence` cannot responsibly be pleaded as fact. Flag these rows: "cannot be verified by statement of truth on current evidence — `[review]`".

---

## 4. Element mapping for common E&W causes of action

There are no pattern jury instructions. Elements come from case law and statute. The lists below are baselines for the chart's `_elements` sheet — the controlling authority is the current case law, which the instructing solicitor or counsel confirms.

### 4.1 Breach of contract

1. **Existence of a binding contract** — offer, acceptance, consideration, intention to create legal relations, certainty of terms
2. **The term relied on** — express (pleaded verbatim per PD 16) or implied (state the basis: statute, e.g. terms implied by the Sale of Goods Act 1979 / Consumer Rights Act 2015, or implication in fact/law)
3. **Breach** — the conduct constituting breach, with particulars
4. **Causation and loss** — loss caused by the breach and not too remote (*Hadley v Baxendale* limbs: losses arising naturally, or within the parties' reasonable contemplation)

Note: E&W does not require the claimant to plead its own performance as a freestanding element the way the US baseline does, but non-performance may found a defence (e.g. conditions precedent, repudiation). `[verify — confirm against current authority before relying on this framing]`

### 4.2 Negligence

1. **Duty of care** — established category, or incrementally by analogy (*Caparo Industries plc v Dickman*; *Robinson v Chief Constable of West Yorkshire* for the established-category approach)
2. **Breach** — conduct falling below the standard of the reasonable person / reasonable professional (*Bolam* for professional negligence, qualified by *Bolitho*) `[verify — confirm characterization before citing]`
3. **Causation** — factual ("but for") and legal causation
4. **Remoteness** — reasonably foreseeable kind of damage (*The Wagon Mound* line) `[verify — confirm characterization before citing]`
5. **Loss** — actionable damage

### 4.3 Misrepresentation

Three routes; the chart must say which is pleaded because the elements and remedies differ:

| Route | Elements | Key points |
|---|---|---|
| **Fraudulent misrepresentation (deceit)** | False representation of fact; made knowingly, without belief in its truth, or recklessly (*Derry v Peek*); intention that claimant rely; reliance; loss | Full particulars required (PD 16); damages not limited by foreseeability |
| **Negligent misrepresentation under s.2(1) Misrepresentation Act 1967** | False representation of fact by a contracting party; claimant entered the contract in reliance; loss. Burden **reverses**: the representor must prove reasonable grounds to believe, and actual belief, that the statement was true | The "fiction of fraud" — damages assessed on the deceit measure `[verify — confirm characterization]` |
| **Negligent misstatement at common law** (*Hedley Byrne v Heller*) | Special relationship / assumption of responsibility; reasonable reliance; loss | Available where there is no contract between the parties |

Also flag: **rescission** as a remedy and its bars (affirmation, lapse of time, third-party rights, impossibility of restitution); **s.2(2)** damages in lieu of rescission.

### 4.4 Defences to map (defendant side)

- **Limitation** (Limitation Act 1980 — see the demand-received uk.md § Limitation for periods)
- **Contributory negligence** (Law Reform (Contributory Negligence) Act 1945) — apportionment, not a complete defence
- **Set-off** (legal and equitable)
- **Exclusion / limitation clauses** — incorporation, construction, and reasonableness under the Unfair Contract Terms Act 1977 (B2B) / fairness under the Consumer Rights Act 2015 (B2C)
- **Mitigation** — strictly a damages-reduction principle, not a defence, but it gets its own chart rows

---

## 5. Phase-aware framing — E&W version

Replaces SKILL.md Step 5 for E&W matters:

- **Pre-action.** The chart maps elements against the evidence available *before* the letter before claim goes out (see demand-draft uk.md). Gaps drive the pre-action disclosure / Norwich Pharmacal analysis (see subpoena-triage uk.md), not US-style discovery planning.
- **Pleadings.** Does the particulars of claim plead material facts for every element (CPR 16 / PD 16)? Any element resting on facts the client cannot verify by statement of truth is flagged. Strike-out exposure under CPR 3.4(2)(a) for missing elements.
- **Disclosure.** For each `gap` / `needs-discovery` element: which Extended Disclosure Model (PD 57AD Models A–E) and which Issues for Disclosure would close it? The gap list feeds the Disclosure Review Document, not a document-request set.
- **Summary judgment.** CPR Part 24 framing per § 2.2 above.
- **Trial.** Order of proof maps to witness statements (PD 57AC) and the trial bundle, not to live direct examination — evidence in chief is the witness statement; cross-examination is where the chart's `disputed` rows get tested.

---

## 6. Costs overlay — always on

Every E&W chart output should carry one line the US version does not need: **costs follow the event** (CPR 44.2 — the unsuccessful party will generally be ordered to pay the successful party's costs). A `gap` element that goes to trial and loses is not just a lost claim — it is the other side's costs. This changes the gap list's framing: gaps are not only proof problems, they are costs exposure. Tie into Part 36 / Calderbank analysis (demand-draft uk.md) where settlement is in play.
