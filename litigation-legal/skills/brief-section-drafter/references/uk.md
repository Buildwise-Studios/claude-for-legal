# England & Wales — Brief Section Drafter

*England & Wales reference for the brief-section-drafter skill — **England and Wales only: Scotland and Northern Ireland are separate legal systems and this file does not cover them.** Reviewed by: [pending E&W practitioner review]; last confirmed against the CPR/PDs: [date pending]. **Treat the contents as unverified**: carry every `[verify — CPR/PD current text]` tag into downstream output, do not promote any statement here to a confirmed or `[settled]` citation, and tell the reviewing solicitor that the doctrine below has not yet had a practitioner pass.*

This file replaces the US brief-drafting frame when the procedural frame is England & Wales (CPR). The single most important correction: **"a brief" is not one kind of document in E&W.** Before drafting anything, identify which of three different documents the user actually needs — they have different rules, different authors, and different sanctions for getting them wrong.

---

## 1. Three documents, three rule sets — sort first

| Document | What it is | Who writes it | Governing rules | Statement of truth? |
|---|---|---|---|---|
| **Statement of case** (particulars of claim, defence, reply) | The formal pleading — material facts only, no evidence, no argument | Solicitor / counsel, verified by client | CPR Part 16, PD 16, CPR Part 22 | **Yes** — contempt exposure for false statements (CPR 32.14) |
| **Skeleton argument** | The written advocacy document for a hearing — submissions, authorities, bundle references | Counsel (or solicitor-advocate) | Court guides + PDs (PD 52A for appeals; Commercial Court Guide / King's Bench Guide / Chancery Guide for first instance) | No — it is submission, not evidence |
| **Witness statement** | The witness's evidence in chief, in their own words | **The witness** — not the lawyer, and not this skill | CPR Part 32; **PD 57AC** for trial witness statements in the Business & Property Courts | **Yes** — plus PD 57AC confirmation of compliance and legal representative's certificate |

If the user says "draft the brief," ask which of these they mean. Drafting argument into a witness statement, or evidence into a skeleton, is not a style problem — it is non-compliance with sanctions attached.

The US sections in the SKILL.md map as follows:
- "Statement of facts" → in E&W this content lives in the **chronology / factual background section of a skeleton argument** (cross-referenced to the bundle) or in **witness statements** (the evidence itself). There is no separately-filed "statement of facts."
- "Argument section" → skeleton argument submissions.
- "Standard of review" → relevant for appeals (permission / review standards under CPR Part 52); state the test from the rule, not from US doctrine.

---

## 2. Skeleton arguments — conventions

A skeleton argument is a concise summary of submissions, not a US-style brief. Conventions that recur across the court guides `[verify — CPR/PD current text and the specific court guide for the forum]`:

- **Concise.** The Court of Appeal caps skeletons at 25 pages (PD 52A) `[verify — CPR/PD current text]`; first-instance guides impose their own limits. Going over requires permission, and overlong skeletons attract costs sanctions.
- **Structure.** Issues, then submissions on each issue, in the order the court will decide them. Numbered paragraphs. No rhetorical build-up — the judge reads it before the hearing.
- **Cross-referenced to the bundle.** Every factual assertion cites the hearing bundle page ([Bundle/Tab/Page]). A skeleton that cites documents not in the bundle is non-compliant.
- **Authorities.** Cite per the Practice Direction (Citation of Authorities) [2012] 1 WLR 780 `[verify — CPR/PD current text]`: neutral citations; the official Law Reports (AC, QB/KB, Ch, Fam) where a case is reported there; one authority per proposition unless more is genuinely necessary; state the proposition each authority is cited for. Authorities bundles are separate and have their own rules.
- **Reading list and time estimate** — appellate and Business & Property Courts skeletons typically must include a reading list for the judge and an estimate of reading time `[verify — court guide for the forum]`.
- **No evidence.** A skeleton cannot introduce facts not in the evidence. If the fact is not in a witness statement or document in the bundle, it cannot appear in the skeleton as fact.

### Costs consequences of non-compliance

Courts disallow the costs of preparing non-compliant skeletons (overlong, late, argumentative beyond the rules) and have done so expressly in reported decisions. When this skill drafts a skeleton, it must check the page limit and filing deadline for the specific court and flag both in the drafting notes. `[verify — the forum's current guide]`

---

## 3. Witness statements — PD 57AC (integrate with the existing gate)

The SKILL.md already carries a PD 57AC gate ("Witness statements for England & Wales — PD 57AC") that refuses to draft a narrative as the witness. **That gate controls.** This section adds the compliance details for the work the gate permits:

- **Own words.** The statement must be in the witness's own words and, so far as practicable, prepared from the witness's own recollection — not constructed from documents and then put to the witness.
- **No argument, no commentary on other evidence.** A trial witness statement sets out only matters of fact of which the witness has personal knowledge; it must not argue the case, narrate the documents, or comment on other witnesses' evidence.
- **List of documents.** The statement must identify by list the documents the witness has referred to or been referred to for the purpose of providing the evidence `[verify — CPR/PD current text for exact requirement wording]`.
- **Confirmation of compliance.** The witness signs a confirmation of compliance with PD 57AC; the relevant legal representative signs a **certificate of compliance**.
- **Statement of truth** (CPR Part 22) — contempt exposure for false statements.
- **Sanctions** for non-compliance: the court may strike out all or part of the statement, order it to be re-drafted, make adverse costs orders, or order the witness to give evidence in chief orally `[verify — CPR/PD current text, PD 57AC ¶5]`.

What this skill may do for witness statements (mirrors the gate): question prompts to elicit recollection; capture and organise the witness's words; generate the list of documents shown; run a compliance checklist against a witness-drafted statement; draft the certificate of compliance for the legal representative's review. Nothing else.

---

## 4. Statements of case — drafting rules

When the section being drafted is a pleading (not a skeleton):

- Material facts only. No evidence ("the email of 3 March shows..."), no law (save where required, e.g. statutory basis of claim), no argument.
- Specific matters per PD 16 (fraud, misrepresentation, knowledge, mitigation — see claim-chart uk.md § 1).
- Verified by statement of truth — every pleaded fact must be one the client can honestly verify. Facts the client cannot verify on current evidence are flagged `[review — cannot be verified by statement of truth on current evidence]`.
- Amendments after service need consent or permission (CPR Part 17), and late amendments attract costs.

---

## 5. Citation style — OSCOLA and court requirements

- House citation style for E&W work is **OSCOLA** (already in the practice profile's options) — but court documents follow the **court's** citation requirements (neutral citations, Law Reports hierarchy) over academic OSCOLA conventions where they differ.
- Every authority cited carries the source-attribution tag system from the plugin CLAUDE.md unchanged (`[model knowledge — verify]`, `[user provided]`, research-tool tags). E&W citations recalled from training data are exactly as fabrication-prone as US ones.
- Good-law checking: the US instruction "Shepardize" maps to checking the authority's status on Westlaw UK / LexisNexis / ICLR / BAILII and confirming it has not been overruled, doubted, or superseded by later authority or statute.

---

## 6. The filing gate — E&W version

The SKILL.md's filing gate cites Rule 11 / Rule 3.3. For E&W, the consequences that attach to filing/serving are:

- **Statement of truth / contempt** (CPR 22 / 32.14) for false factual statements in pleadings and witness statements.
- **Professional duties to the court** — solicitors (SRA Principles and Code of Conduct: duty not to mislead the court) and barristers (BSB Handbook: duty to the court overrides the client's interest) `[verify — current code provisions]`.
- **Costs sanctions** — wasted costs orders against legal representatives (s.51(6) Senior Courts Act 1981) for improper, unreasonable, or negligent conduct `[verify — confirm provision]`.
- **AI-specific:** E&W courts have issued guidance on AI use in litigation and have referred lawyers to regulators for filing AI-fabricated citations. Every citation in a draft must be verified against a primary source before filing — this is not a US-only risk.

The non-lawyer routing in the gate (SRA / Bar Standards Board referral) is already E&W-aware; keep it.
