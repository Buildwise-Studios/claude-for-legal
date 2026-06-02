# England & Wales — Compulsory Process Against Non-Parties (No Subpoenas)

*England & Wales reference for the subpoena-triage skill — **England and Wales only: Scotland and Northern Ireland are separate legal systems and this file does not cover them.** Reviewed by: [pending E&W practitioner review]; last confirmed against the CPR/PDs: [date pending]. **Treat the contents as unverified**: carry every `[verify — CPR/PD current text]` tag into downstream output, do not promote any statement here to a confirmed or `[settled]` citation, and tell the reviewing solicitor that the doctrine below has not yet had a practitioner pass.*

This file replaces the US subpoena frame (FRCP 45, CIDs, grand-jury practice) when the procedural frame is England & Wales (CPR). The headline: **there is no subpoena in E&W civil procedure.** The word was abolished with the CPR; the instruments that exist instead have different names, different tests, different deadlines, and different cost rules. Triage starts by identifying which instrument actually landed.

---

## 1. Classify — what actually arrived?

| Instrument | What it compels | Rule | When it can be used |
|---|---|---|---|
| **Witness summons** | A person to attend court to give evidence and/or produce documents **at a trial or hearing** | CPR Part 34 (34.2–34.7) | Issued by a party; court permission needed in some cases (e.g. less than 7 days before trial) `[verify — CPR/PD current text]` |
| **Third-party (non-party) disclosure order** | A non-party to disclose **documents** before/during proceedings | CPR 31.17 (+ s.34 Senior Courts Act 1981 / s.53 County Courts Act 1984) | Only by court order, on application with evidence |
| **Norwich Pharmacal order** | A person mixed up in another's wrongdoing to provide **information** (typically: identify a wrongdoer) | Equitable jurisdiction (*Norwich Pharmacal Co v Customs and Excise Commissioners* [1974] AC 133) | Court order; respondent usually gets costs |
| **Pre-action disclosure order** | A **likely party** to disclose documents before proceedings start | CPR 31.16 | Court order, on application |
| **Bankers Trust order** | A bank/institution to disclose information to trace assets | Equitable jurisdiction | Court order; fraud/tracing contexts `[verify — confirm characterization]` |
| **Letter of request / Hague Evidence Convention request** | Evidence from an E&W resident for **foreign** proceedings | Evidence (Proceedings in Other Jurisdictions) Act 1975; CPR 34.16–34.21 `[verify — CPR/PD current text]` | Foreign court issues request; English court gives effect by order |
| **Regulatory information notice** | Documents/information for a regulator (FCA s.165 FSMA, CMA, ICO, SFO s.2 notice, HMRC) | The regulator's statute | Direct statutory compulsion — different regime entirely; route to regulatory counsel |

**Routing consequences:**

- A **witness summons** (CPR 34) is the closest analogue to a US trial subpoena — but it only operates for attendance/production *at a hearing*. There is no E&W equivalent of a US deposition subpoena or a documents-only subpoena returnable to a law office.
- US-style "we got a subpoena for our documents" in a civil case where the recipient is not a party will, in E&W, almost always be either (a) an **application** for a CPR 31.17 order (the recipient can oppose it before any duty arises), or (b) an order already made (comply or apply to set aside/vary).
- A **grand jury subpoena has no E&W equivalent**; the nearest analogues are SFO s.2 notices and other compelled regulatory production — escalate to specialist criminal/regulatory counsel exactly as the SKILL.md's grand-jury gate does.

---

## 2. Triage by instrument

### 2.1 Witness summons (CPR Part 34)

- **What it requires:** attendance at the stated hearing to give evidence and/or to produce the documents described. Documents are produced **to the court at the hearing** (or at a date the court fixes ahead of the hearing under CPR 34.2(4)(b)) `[verify — CPR/PD current text]`.
- **Conduct money:** the summons must be served with an offer of a sum to cover travel to and from court and compensation for loss of time `[verify — CPR/PD current text + current PD amounts]`. No conduct money is a service defect.
- **Challenges:** application to **set aside or vary** the summons (CPR 34.3(4)) — grounds include irrelevance, oppression, fishing, privilege, and that the documents sought are not sufficiently identified `[verify — confirm grounds against current authority]`.
- **Privilege:** the witness can claim privilege at the hearing; LPP (see privilege-log-review uk.md) and privilege against self-incrimination apply.
- **Non-compliance:** contempt of court; in the High Court, potential committal.

### 2.2 Third-party disclosure (CPR 31.17)

The applicant must show:

1. the documents sought are **likely to support the applicant's case or adversely affect the case of one of the other parties**, and
2. disclosure is **necessary to dispose fairly of the claim or to save costs**.

"Likely" means "may well" rather than "more probable than not" `[verify — confirm against current authority]`. The order must specify the documents or classes; fishing is not permitted.

- **Triage posture when this lands as an application:** the recipient non-party can consent, stay neutral, or oppose. Opposition grounds: the two-limb test isn't met, the classes are too wide, burden/proportionality, confidentiality, privilege.
- **Costs:** the general rule is that the **applicant pays the non-party's costs** of the application and of compliance (CPR 46.1) `[verify — CPR/PD current text]` — the opposite default from US third-party subpoena practice. Build the costs estimate into the response; this is recoverable money, not just burden.

### 2.3 Norwich Pharmacal

Available against a person who is **mixed up in (facilitated) the wrongdoing of another**, even innocently, and is able to provide information necessary to identify the wrongdoer or enable a claim. Requirements (as commonly framed) `[verify — confirm current formulation]`:

1. a good arguable case of wrongdoing by someone;
2. the respondent is mixed up in / facilitated it;
3. the respondent is able to provide the information necessary to enable the wrongdoer to be sued or the wrong redressed;
4. disclosure is necessary and proportionate (no alternative means).

Costs: the applicant ordinarily pays the respondent's reasonable costs of compliance. A Norwich Pharmacal respondent who resists unreasonably can lose that protection.

### 2.4 Pre-action disclosure (CPR 31.16)

Against a **likely party** to anticipated proceedings (not a true non-party tool). Test: both applicant and respondent are likely to be parties; the documents would fall within standard disclosure if proceedings had started; pre-action disclosure is desirable to dispose fairly of the anticipated proceedings, assist resolution without proceedings, or save costs.

If the company receives one of these, it is not a bystander — it is the prospective defendant. Cross-check `_log.yaml` and the inbound demand-letter pipeline (demand-received uk.md): a CPR 31.16 application usually follows a letter before claim.

---

## 3. Cross-border: US process meeting E&W documents/witnesses

### 3.1 Responding to a US subpoena seeking documents or testimony located in E&W

A US subpoena has **no direct legal force in England & Wales**. The triage:

1. **Jurisdictional hook.** Does the US court have personal jurisdiction over the E&W entity (e.g. it is a party to the US litigation, or a US affiliate is the subpoena target and "controls" the E&W documents)? If yes, the practical compulsion runs through the US case even though the subpoena doesn't run here. If no, the proper route for the requesting party is a **letter of request** under the **Hague Evidence Convention**, given effect by the English court under the Evidence (Proceedings in Other Jurisdictions) Act 1975.
2. **English court limits on letters of request:** no general "discovery" — document requests must identify specific or compendiously-described documents; fishing requests are refused or blue-pencilled `[verify — confirm against current authority]`.
3. **Data protection.** Producing personal data directly to a US litigant/court is a transfer and processing question under **UK GDPR / Data Protection Act 2018**. Article 48-equivalent considerations: a foreign court order is not by itself a lawful basis for transfer; the Hague route, or a recognised transfer mechanism plus a lawful basis, is needed `[verify — UK GDPR current text and ICO guidance]`. Flag for data-protection counsel; this is a real exposure, not a formality.
4. **Blocking / trading-interests considerations.** The UK has the **Protection of Trading Interests Act 1980**, which can prohibit compliance with certain extraterritorial foreign orders (historically aimed at US antitrust discovery) `[verify — confirm scope and current relevance]`. Rarely invoked, but check before producing.
5. **Privilege.** E&W LPP and US privilege do not have identical scope. Producing material in the US that is privileged in E&W (or vice versa) creates waiver risk in both places. Flag for counsel in both jurisdictions.

### 3.2 E&W proceedings needing evidence from abroad

Outbound letters of request (CPR 34.13) for examination of witnesses out of the jurisdiction; Hague Convention or bilateral arrangements depending on the destination state. Note for the deadline calendar: this takes months, not weeks.

---

## 4. Deadlines and workflow adjustments

The SKILL.md's deadline-driven triage (Step 7) maps as follows:

- **Witness summons:** the operative dates are the hearing date and any document-production date fixed by the court; an application to set aside should be made promptly and before the compliance date.
- **CPR 31.17 / 31.16 / Norwich Pharmacal applications:** the operative deadline is the **hearing date of the application** and the date for serving evidence in response (per the application notice / court directions). The response is witness evidence opposing or limiting the order, not "objections" served on counsel.
- **Orders already made:** comply by the date in the order, or apply promptly to vary/set aside. Non-compliance with an order is contempt — there is no E&W analogue of serving objections to suspend compliance the way FRCP 45(d)(2)(B) works.
- **Regulatory notices:** statutory deadlines from the notice itself; some (e.g. SFO s.2) have criminal sanctions for non-compliance.

The SKILL.md's "objection deadlines often run from the EARLIER of compliance date or fixed days after service" heuristic is **US-specific — do not apply it.** In E&W the question is "is this an application I respond to, or an order I comply with / apply to set aside?"

---

## 5. Costs framing

Run every triage with the E&W costs lens:

- Non-parties responding to CPR 31.17 / Norwich Pharmacal generally recover their reasonable compliance costs from the applicant.
- A non-party who unreasonably resists can be ordered to pay the applicant's costs.
- Witness summons recipients get conduct money but not full compliance costs.

This changes the recommendation section: in the US, burden is a ground to object; in E&W, burden is partly a ground to oppose and partly an invoice to the applicant.
