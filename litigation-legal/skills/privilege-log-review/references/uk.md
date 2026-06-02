# England & Wales — Privilege Review and Disclosure

*England & Wales reference for the privilege-log-review skill — **England and Wales only: Scotland and Northern Ireland are separate legal systems and this file does not cover them.** Reviewed by: [pending E&W practitioner review]; last confirmed against the CPR/PDs: [date pending]. **Treat the contents as unverified**: carry every `[verify — CPR/PD current text]` tag into downstream output, do not promote any statement here to a confirmed or `[settled]` citation, and tell the reviewing solicitor that the doctrine below has not yet had a practitioner pass.*

This file replaces the US privilege frame when the procedural frame is England & Wales (CPR). The two structural differences that change every call this skill makes:

1. E&W privilege is **legal professional privilege (LPP)** with two limbs — **legal advice privilege** and **litigation privilege**. There is **no US-style work-product doctrine.** Every "WP" classification in the US workflow must be re-analysed under one of the two limbs; "prepared in anticipation of litigation by or for counsel" is not the test.
2. E&W disclosure practice does not generally produce US-style document-by-document privilege logs. Privilege is asserted in the **disclosure process** (PD 57AD in the Business & Property Courts; CPR Part 31 elsewhere) — see § 4.

---

## 1. Legal advice privilege

Protects **confidential communications between a lawyer and their client** made for the **dominant purpose of giving or receiving legal advice**.

- **Lawyer** includes solicitors, barristers, and in-house lawyers acting in their legal (not executive/commercial) capacity. Foreign lawyers qualify. (Contrast EU competition proceedings, where in-house communications are not privileged — the SKILL.md's *Akzo Nobel* warning still applies to any EU competition overlay.)
- **The "client" problem — *Three Rivers (No 5)*.** Within a corporate client, the "client" for legal advice privilege purposes is narrowly confined to the individuals **authorised to seek and receive legal advice** on the company's behalf — not every employee. Communications between the lawyer and employees outside that group (e.g. fact-gathering interviews with staff) may **not** be covered by legal advice privilege. The Court of Appeal in *SFO v ENRC* [2018] EWCA Civ 2006 criticised this rule but held itself bound by it `[verify — confirm no subsequent Supreme Court decision has revisited Three Rivers (No 5)]`.
- **Dominant purpose.** Following *R (Jet2.com) v Civil Aviation Authority* [2020] EWCA Civ 35, the communication must have been made for the **dominant purpose** of obtaining or giving legal advice. Emails to mixed lawyer/non-lawyer recipient lists are analysed by dominant purpose.
- **Legal advice** is construed broadly — includes the "continuum of communications" and advice on what should prudently and sensibly be done in the relevant legal context (*Three Rivers (No 6)*) — but pure business/commercial advice from a lawyer is not privileged.

### Triage consequences for the three-state rule

- Lawyer ↔ authorised-client-group communication, dominant purpose legal advice → the confidently-privileged tier is available.
- Lawyer ↔ employee **outside** the authorised group (interview notes, fact-gathering) → never confidently privileged. This is the *Three Rivers (No 5)* trap; it is the single most common over-claim in E&W corporate privilege review. Route to the ⚠️ flag with the note "legal advice privilege may not cover employee communications outside the authorised client group; consider litigation privilege instead."
- Lawyer copied on business correspondence → same as US: copying legal does not create privilege.

---

## 2. Litigation privilege

Protects **confidential communications between a lawyer or client and a third party** (or documents created by/for them) made for the **dominant purpose of conducting litigation** that is **pending, reasonably contemplated, or existing**.

Three requirements (all must be met):

1. **Adversarial litigation** — actual, pending, or reasonably in contemplation. Investigations are not automatically adversarial litigation; reasonable contemplation of a criminal/regulatory prosecution can qualify (*SFO v ENRC* in the Court of Appeal) but the line is fact-specific.
2. **Dominant purpose** — the dominant purpose of the communication/document must be use in or advice on that litigation (*Waugh v British Railways Board* — a document prepared for two equal purposes fails).
3. **Confidentiality.**

This is the limb that covers what US practice calls work product (expert input, witness proofing, investigator reports) — but the test is materially narrower:

| US work product habit | E&W litigation privilege reality |
|---|---|
| "Prepared in anticipation of litigation" — broad, attaches early | Litigation must be **reasonably in contemplation** — a general apprehension or "litigation is always possible" is not enough |
| Opinion vs. fact work product tiers | No such tiering; the document is privileged or it is not |
| Protects materials prepared by or for the party's representative | Protects communications/documents whose **dominant purpose** is the litigation — mixed-purpose documents (e.g. an investigation report also serving compliance or PR purposes) are at risk |
| Survives in many forms even when underlying facts are discoverable | Same principle: facts are never privileged, only communications/documents |

**Triage consequence:** every entry the US workflow would mark "WP" is re-analysed: (a) was adversarial litigation pending or reasonably contemplated at the document's creation date, and (b) was the litigation its dominant purpose? Pre-litigation internal investigation material is the classic ⚠️ flag — never confidently privileged.

---

## 3. Adjacent doctrines that change calls

- **Without prejudice** — settlement communications are protected from disclosure to the court by the without-prejudice rule (see demand-draft uk.md § 3). A WP document in a disclosure set is a separate category from LPP; do not conflate.
- **Common interest privilege** — exists in E&W; sharing privileged material with a party having a common interest does not waive.
- **Joint privilege / joint retainer** — co-clients of the same lawyer.
- **Privilege against self-incrimination** — distinct, narrow, flagged for counsel.
- **Waiver** — privilege is the client's; it is waived by deployment (relying on the substance of the advice in proceedings — "cherry-picking" triggers collateral waiver of the whole topic) or by loss of confidentiality. There is no E&W equivalent of FRE 502 clawback orders, but inadvertent disclosure is governed by CPR 31.20: the receiving party may use an inadvertently disclosed privileged document only with the court's permission `[verify — CPR/PD current text]`.
- **No "subject-matter waiver" presumption as broad as the US one.** Collateral waiver exists but is tied to deployment and fairness. Flag waiver-scope questions for counsel — do not import US waiver breadth.

---

## 4. Where privilege is asserted — disclosure under PD 57AD, not a privilege log

In the Business & Property Courts, disclosure is governed by **PD 57AD** (which made the Disclosure Pilot, former PD 51U, permanent). Outside the B&PC, CPR Part 31 applies. The practical differences from US practice:

### 4.1 The PD 57AD framework

- **Initial Disclosure** — key documents served with the statements of case `[verify — CPR/PD current text, PD 57AD ¶5]`.
- **Extended Disclosure** — by reference to **Issues for Disclosure** agreed in the **Disclosure Review Document (DRD)**, under one of five models per issue:
  - **Model A** — disclosure confined to known adverse documents
  - **Model B** — limited disclosure (key documents)
  - **Model C** — disclosure of particular documents or narrow classes (request-led)
  - **Model D** — narrow search-based disclosure, with or without "narrative documents"
  - **Model E** — wide search-based disclosure (train-of-inquiry; exceptional)
- **Disclosure duties** (PD 57AD ¶3.1) include the duty to take reasonable steps to preserve documents, the duty to disclose **known adverse documents regardless of any order** `[verify — CPR/PD current text, ¶3.1(2)]`, the duty to comply with disclosure orders, the duty not to document-dump, and the duty to use reasonable efficiency. Legal representatives have their own duties (¶3.2), including taking reasonable steps to ensure the client complies.
- **The duty to disclose adverse documents is the headline difference from US practice.** A party must disclose documents it knows are adverse to its own case even under the narrowest model. There is no E&W concept of "responsive to a request" limiting this duty.

### 4.2 How privilege is claimed

- Privilege is claimed in the **Disclosure Certificate** / list of documents — typically by **category or class description**, not document-by-document logging (CPR 31.19 governs the procedure for claiming a right to withhold; PD 57AD ¶¶ on claims to privilege) `[verify — CPR/PD current text]`.
- The description must be sufficient for the other party and the court to understand the basis of the claim — but E&W practice tolerates generic class claims ("confidential correspondence between the defendant and its solicitors for the purpose of obtaining legal advice") far more than US privilege-log practice.
- A challenge to a privilege claim is made by application; the court can inspect the documents (CPR 31.19(6)) `[verify — CPR/PD current text]`.

**Triage consequence:** when the user hands this skill a US-style privilege log for an E&W matter, the format-check step should ask whether a document-level log is actually required (it may be, by order or agreement) or whether the deliverable is really the privilege sections of a Disclosure Certificate / list. Do not assume the US artifact.

### 4.3 Collateral use — CPR 31.22

Documents obtained through disclosure may be used **only for the purpose of the proceedings in which they were disclosed**, unless the court permits, the disclosing party consents, or the document has been read to or by the court at a public hearing. (PD 57AD ¶27 carries the equivalent restriction for B&PC disclosure `[verify — CPR/PD current text]`.) Breach is a contempt. The SKILL.md's "Disclosed-document use restrictions" gate already enforces this; this section is the doctrinal source.

---

## 5. Review workflow adjustments

The SKILL.md's three-state rule (confidently privileged / uncertain — keep designation and ⚠️ flag / confidently not privileged) and "never silently strip a designation" discipline are unchanged. The E&W-specific call table:

| Entry type | Default state | Why |
|---|---|---|
| Solicitor/barrister ↔ authorised client group, legal advice | Priv (legal advice privilege) | Core LPP |
| In-house lawyer ↔ authorised client group, legal advice | Priv with note | Privileged in E&W; flag if EU competition overlay |
| Lawyer interview notes of employees (no litigation contemplated) | ⚠️ | *Three Rivers (No 5)* — may fall outside legal advice privilege |
| Investigation reports, expert/consultant material, witness proofs — litigation reasonably contemplated | Priv + ⚠️ (litigation privilege, dominant purpose to confirm) | Dominant purpose is a judgment call |
| Same, but litigation only a general possibility at creation date | ⚠️ | Contemplation requirement likely fails |
| Documents marked "without prejudice" | ⚠️ — separate WP analysis | Different doctrine; label is not conclusive |
| Business documents with lawyer copied | Not priv (recommend) | Same as US |
| Underlying facts / pre-existing documents sent to lawyer | Not priv (recommend) | Sending a document to a lawyer does not privilege it |
| Known adverse documents claimed as privileged | ⚠️ escalate | The PD 57AD adverse-documents duty makes wrongly-claimed privilege here a serious compliance failure |

Every date matters more than in US review: litigation privilege turns on **when** litigation became reasonably contemplated. The review should establish that date (or flag it as undetermined) before classifying any pre-action documents.
