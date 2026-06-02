# England & Wales — Document Preservation

*England & Wales reference for the legal-hold skill — **England and Wales only: Scotland and Northern Ireland are separate legal systems and this file does not cover them.** Reviewed by: [pending E&W practitioner review]; last confirmed against the CPR/PDs: [date pending]. **Treat the contents as unverified**: carry every `[verify — CPR/PD current text]` tag into downstream output, do not promote any statement here to a confirmed or `[settled]` citation, and tell the reviewing solicitor that the doctrine below has not yet had a practitioner pass.*

This file replaces the US legal-hold frame (Zubulake / FRCP 37(e) / litigation-hold-letter practice) when the procedural frame is England & Wales (CPR). The headline: **E&W has no formalised "litigation hold letter" doctrine, but the substance of the duty is express in the rules** — PD 57AD imposes preservation duties, including written notification to employees, from the moment litigation is contemplated. The skill's issue → refresh → release → track workflow maps onto those duties almost unchanged; the vocabulary and the legal sources change.

---

## 1. The preservation duty — source and trigger

### 1.1 In the Business & Property Courts — PD 57AD

PD 57AD ¶3.1 places each party under disclosure duties that include the **duty to take reasonable steps to preserve documents** in its control that may be relevant to any issue in the proceedings `[verify — CPR/PD current text, ¶3.1(1)]`.

PD 57AD ¶4 sets out what preservation requires `[verify — CPR/PD current text for the precise sub-paragraph numbering]`:

- The duty applies to a person who **knows that it is or may become a party** to proceedings that **have commenced or may be commenced** — i.e. the duty arises when litigation is **contemplated**, not when proceedings are issued.
- Reasonable steps to preserve include:
  - **suspending** any relevant document-deletion or destruction processes (auto-delete, retention-policy purges) for the duration of the proceedings;
  - sending a **written notification** in any form to **relevant employees and former employees** identifying the documents (or classes of documents) to be preserved and notifying them not to delete or destroy them;
  - taking reasonable steps so that **agents or third parties** who may hold documents on the party's behalf do not delete or destroy them.
- Legal representatives have a parallel duty (PD 57AD ¶3.2) to take reasonable steps to ensure their client complies — and the Disclosure Certificate later requires the party to certify the preservation steps taken.

**This means the "hold notice" this skill drafts is not a US import — it is the written notification PD 57AD ¶4 expressly requires.** The artifact is the same; the legal basis is the rule itself.

### 1.2 Outside the B&PC

CPR Part 31 matters: the preservation duty arises from the prospective disclosure obligation and from the law of contempt / the court's case-management powers. The pre-action protocols also assume documents are preserved once a dispute is live `[verify — CPR/PD current text]`. The same hold workflow applies; the rule citation changes from PD 57AD to general disclosure duty.

### 1.3 Trigger language for the skill

US trigger: "litigation reasonably anticipated" (common law / Zubulake).
E&W trigger: a person "knows that it **is or may become** a party to proceedings that **have commenced or may be commenced**."

In practice these converge: receiving a letter before claim, sending one, a board decision to sue, a regulator's notice, or an incident that will obviously produce a claim all start the duty. When the trigger date is debatable, record the candidate dates and flag `[review]` — the trigger date is also the date litigation privilege analysis turns on (see privilege-log-review uk.md § 2), so getting it consistent across both matters.

---

## 2. The hold notice — E&W adaptations

The default template in the SKILL.md works with these changes:

- **Header/marking:** "Privileged & Confidential — Legal Advice" rather than the US attorney-client formulation. Note the marking is a label, not a guarantee — see the plugin CLAUDE.md on jurisdiction-specific header honesty.
- **Legal basis paragraph:** replace the US "the law requires preservation" sentence with: "Under the Civil Procedure Rules (Practice Direction 57AD), [company] is under a duty to preserve documents relevant to this matter, and to notify you in writing not to delete or destroy them. This notice is that notification."
- **Scope:** the duty covers documents in the party's **control** (CPR 31.8 concept: physical possession, right to possession, or right to inspect/copy) — this reaches documents held by agents, contractors, and some group companies. The custodian list should ask about third-party holders, not just employees.
- **Former employees:** PD 57AD ¶4 expressly extends the written notification to relevant **former** employees `[verify — CPR/PD current text]` — the US template's current-custodian focus under-scopes for E&W. Add a former-employee check to the issuance inputs.
- **Acknowledgment:** still best practice; also feeds the Disclosure Certificate's preservation-steps certification.

---

## 3. Consequences of failure

No US-style Rule 37(e) sanctions framework, but the consequences are at least as serious:

- **Adverse inferences.** The court may draw adverse inferences against a party that destroyed or failed to preserve documents.
- **Strike-out.** Destruction of evidence that makes a fair trial impossible can lead to strike-out of the claim or defence (CPR 3.4(2)(c) / inherent jurisdiction) `[verify — confirm framing against current authority]`.
- **Contempt of court.** Deliberate destruction of documents subject to a disclosure duty, or a false Disclosure Certificate (which is verified by a statement of truth), is punishable as contempt.
- **Costs sanctions** against the party, and potential **wasted costs / regulatory exposure** for legal representatives who failed in their PD 57AD ¶3.2 duties.
- **Relief from sanctions framing.** Where a preservation failure leads to a sanction, relief is analysed under CPR 3.9 and *Denton v TH White* [2014] EWCA Civ 906 (seriousness/significance of the breach → why it occurred → all the circumstances). A hold issued late but promptly remediated argues well under *Denton*; a hold never issued does not.

---

## 4. Workflow mapping

| SKILL.md phase | E&W operation |
|---|---|
| `--issue` | Draft and send the PD 57AD ¶4 written notification; suspend auto-deletion; record steps for the future Disclosure Certificate |
| `--refresh` | Reaffirm the notification; re-check custodians (joiners/leavers/role changes), new systems, scope drift from the Issues for Disclosure as they crystallise in the DRD |
| `--release` | Confirm proceedings concluded (including any appeal window), no related contemplated proceedings, and no regulatory/Limitation Act reason to continue preservation; then notify custodians that normal retention resumes |
| `--status` | Same portfolio report; add a column for whether the matter's Disclosure Certificate (if served) certified the preservation steps |

`--issue` extra inputs for E&W:
1. Is the matter in (or headed to) the **Business & Property Courts**? (Determines whether PD 57AD applies directly.)
2. **Former employees** holding relevant documents?
3. **Agents / third parties** (IT providers, accountants, agencies) holding documents within the party's control?
4. Trigger date — when did the party first know it may become a party to proceedings? (Record it; flag if contested.)

`--release` extra check for E&W: the Disclosure Certificate certified that preservation steps were taken — releasing the hold before final disposal (including appeals and any costs assessment that might require the documents) gets flagged `[review]`.

---

## 5. Cross-references

- Disclosure framework, Models A–E, adverse-documents duty: privilege-log-review uk.md § 4.
- Pre-action stage: the preservation duty typically arises at or before the letter before claim — see demand-draft uk.md (sending) and demand-received uk.md (receiving). Both of those skills hand off to `/legal-hold --issue`; for E&W matters that handoff should cite PD 57AD, not Zubulake.
- The duty to disclose **known adverse documents** (PD 57AD ¶3.1(2)) makes preservation failures more dangerous than in the US: a destroyed adverse document is a breach of two duties, not one.
