# England & Wales — Witness Evidence Without Depositions

*England & Wales reference for the deposition-prep skill — **England and Wales only: Scotland and Northern Ireland are separate legal systems and this file does not cover them.** Reviewed by: [pending E&W practitioner review]; last confirmed against the CPR/PDs: [date pending]. **Treat the contents as unverified**: carry every `[verify — CPR/PD current text]` tag into downstream output, do not promote any statement here to a confirmed or `[settled]` citation, and tell the reviewing solicitor that the doctrine below has not yet had a practitioner pass.*

This file does not adapt the deposition workflow to England & Wales — it **reframes it**, because **depositions are not part of standard E&W civil procedure.** There is no pre-trial oral examination of the other side's witnesses as of right. If the practice profile's frame is England & Wales and the user asks for "depo prep," the first job is to find out what they actually need, because it is one of four different things.

---

## 1. Routing — what does the user actually need?

Ask, then route:

| What the user is actually doing | Route to |
|---|---|
| **Preparing their own witness's evidence for trial** | Witness statement preparation under PD 57AC — route to `brief-section-drafter` (its PD 57AC gate and witness-statement mode), § 2 below |
| **Preparing to challenge the other side's witnesses at trial** | Cross-examination preparation, § 3 below — this skill's outline mechanics apply, repointed at trial |
| **A court-ordered deposition before an examiner (rare)** | CPR 34.8 deposition, § 4 below |
| **A US deposition of a witness located in England & Wales** | Cross-border deposition, § 5 below — US rules apply to the deposition itself, E&W and Hague rules govern whether/how it can happen here |

Never silently run the US deposition workflow for an E&W matter. An "outline for the deposition of the defendant's CFO" in a Commercial Court case is a document for a procedure that does not exist — producing it marks the work as unreviewed AI output.

---

## 2. What replaces depositions: witness statements (PD 57AC)

In E&W civil litigation, a witness's evidence in chief is given by **witness statement**, exchanged before trial (CPR 32.4–32.5). The other side's first opportunity to question the witness orally is **cross-examination at trial**. There is no intermediate oral discovery of witnesses.

For trial witness statements in the Business & Property Courts, **PD 57AC** governs. The SKILL.md already carries the PD 57AC gate (own words, no argument, list of documents, confirmation of compliance, legal representative's certificate) — that gate and the brief-section-drafter uk.md § 3 are the canonical references. Do not duplicate the rules here; route.

What this skill CAN do in the witness-statement world (mirroring the gate):

- Prepare **question prompts** for the solicitor's interview of the witness (open, non-leading — PD 57AC and the Statement of Best Practice appended to it constrain how interviews are conducted `[verify — PD 57AC Appendix, Statement of Best Practice]`)
- Organise the witness's own account once captured
- Build the **list of documents** the witness was referred to
- Run a **compliance checklist** against a drafted statement

---

## 3. Cross-examination preparation — where this skill's mechanics survive

The deposition outline's structure (background → lock in good facts → confront with documents → box in on the pivot fact) is, with adjustments, the structure of a **cross-examination plan** for trial. Differences that change the plan:

- **You have the witness's evidence in advance.** The witness statement IS their evidence in chief. The cross-examination plan is built against the statement's specific paragraphs, not against guesses about what they'll say. Every challenge point cites the statement paragraph and the contradicting document (bundle reference).
- **You must put your case.** The rule in *Browne v Dunn* (the "puttage" rule): a party must put to the witness in cross-examination the parts of its own case that contradict the witness's evidence, or risk being barred from inviting the court to disbelieve the witness on that point in closing `[verify — confirm current application]`. The plan therefore has a **mandatory coverage list** — every contradiction between the client's case and this witness's statement — which has no US-deposition counterpart: completeness is required, not optional.
- **No "discovery" questions.** Cross-examination at trial is not for finding out what the witness knows — it is for challenging their account and putting your case. Exploratory lines that make sense in a US deposition (where you want the witness talking) are usually wrong at trial (where every open question is a risk).
- **The judge is the audience.** No jury in most civil trials. Theatrical impeachment sequences calibrated for a US jury read poorly; the effective E&W cross is precise, document-anchored, and brief.
- **Hostile/friendly framing changes:** you generally cannot cross-examine your own witness (unless declared hostile); your own witnesses are prepared via § 2, not via this skill's confrontation mechanics. Witness coaching/rehearsal of evidence is **prohibited** — witness familiarisation (process, not content) is permitted; practising answers to expected cross-examination is not `[verify — Bar Council / *R v Momodou* guidance as applied in civil practice]`.

Output artifact: a **cross-examination plan** keyed to [witness statement ¶] and [bundle page], with the *Browne v Dunn* coverage list as a completeness check, plus the impeachment material (prior inconsistent statements, contemporaneous documents) the SKILL.md already collects.

---

## 4. Actual depositions in E&W — CPR 34.8 (exceptional)

A deposition does exist in E&W procedure, but only **by court order**, and it is for **preserving evidence that cannot be given at trial**, not for discovery:

- The court may order a person to be examined **before the hearing** takes place, before a judge, an examiner of the court, or another nominated person (CPR 34.8) `[verify — CPR/PD current text]`.
- Typical use: a witness who is seriously ill, very elderly, or will be abroad and unavailable at trial.
- The deposition transcript may be put in evidence at trial (CPR 34.9–34.11 govern conduct and use) `[verify — CPR/PD current text]`.
- The examination broadly follows trial rules (examination in chief / cross-examination), and the witness can be required to produce documents.

If this is genuinely what is happening, the US outline mechanics partially apply (it is an oral examination), but the purpose is evidence preservation — both sides examine as they would at trial.

---

## 5. US deposition of an E&W-located witness

When the matter is US litigation but the witness is in England & Wales, the deposition itself is a US-procedure event; what E&W law governs is **whether and how it can take place here**:

- **Willing witness, voluntary deposition:** depositions of willing witnesses for use in foreign proceedings can generally be conducted in England by agreement (in person or by video) — England does not prohibit voluntary depositions on its soil the way some civil-law jurisdictions do `[verify — confirm no current restriction; check any notification requirements]`. Practicalities: a court reporter, the oath (administered under the foreign court's rules), and a venue.
- **Unwilling witness:** a US subpoena has no force in E&W. The route is a **letter of request** from the US court under the **Hague Evidence Convention**, given effect by the English court under the Evidence (Proceedings in Other Jurisdictions) Act 1975 — the English court orders the examination, which is then conducted under English-court supervision (see subpoena-triage uk.md § 3). The English court will narrow or refuse requests that amount to fishing/discovery rather than evidence for trial `[verify — confirm against current authority]`.
- **The witness's own exposure:** an E&W-resident employee being deposed in US litigation should have the company's (and possibly their own) counsel address: privilege differences (E&W LPP vs. US privilege — see privilege-log-review uk.md), data protection (UK GDPR — testimony about personal data is processing/transfer), and any confidentiality obligations to third parties.
- **Prep for the witness:** US deposition-prep conventions (the witness preparation session, practice questions) are normal and permissible **for the US proceeding** — but if the witness will also be a witness in related E&W proceedings, coaching that would be prohibited in E&W (§ 3 above) creates a real problem for their E&W evidence. Flag `[review]` whenever the same witness appears in both a US and an E&W proceeding arising from the same facts.

For this scenario, the SKILL.md's US workflow applies to the deposition content (it IS a US deposition), with the cross-border overlay above added to the outline's "Notes for the attorney" section.

---

## 6. Vocabulary guard

Terms to never emit in E&W-frame outputs (except in the cross-border § 5 context): "deposition" (as a standard discovery step), "deponent," "30(b)(6) witness," "errata sheet," "objections for the record." Their nearest E&W counterparts:

| US | E&W |
|---|---|
| Deposition (discovery) | — (does not exist; witness statements + trial cross-examination) |
| 30(b)(6) corporate representative deposition | — (no direct equivalent; corporate knowledge comes via disclosed documents, witness statements of relevant individuals, and CPR Part 18 requests for further information) |
| Errata sheet | — (witness statements are corrected by a further statement before trial; trial evidence is corrected in re-examination) |
| Deposition transcript designations | Trial transcript references |
| Interrogatories | CPR Part 18 request for further information (narrower than US interrogatories) |
