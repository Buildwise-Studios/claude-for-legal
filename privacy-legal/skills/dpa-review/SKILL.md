---
name: dpa-review
description: >
  Review a Data Processing Agreement against your DPA playbook — auto-detects
  whether you're processor or controller and applies the right half of the playbook.
  Use when the user says "review this DPA", "check this data processing addendum",
  "customer sent their DPA", "is this DPA okay", or attaches a DPA.
argument-hint: "[file | Drive link | paste text]"
---

# /dpa-review

1. Load `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → DPA playbook. If placeholders, stop and prompt setup.
2. Check the practice context index for prior cross-plugin work on this counterparty (vendor AI reviews, PIAs) — see `## Check prior cross-plugin work`.
3. Get the DPA. Determine direction: are we processor (customer's DPA) or controller (vendor's)? Ask if ambiguous.
4. Run the workflow below — term-by-term against the appropriate playbook row.
5. Run privacy policy consistency check.
6. Output: review memo with redlines. Save per house style.
7. Record the completed review in the practice context index — see `## Record in the practice context index`.

```
/privacy-legal:dpa-review customer-dpa.pdf
```

---

# DPA Review

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

DPAs come in two flavors and the review is nearly opposite for each. When a customer sends their DPA, we're defending our operational flexibility. When we send one to a vendor, we're protecting our (and our customers') data. Both reviews read from the same `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` playbook but from opposite rows.

## First: which direction?

Before anything else, establish:

- **We are the processor** → customer is sending us their DPA → read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → "When we are the processor" table
- **We are the controller** → we're sending a DPA to a vendor (or reviewing theirs) → read "When we are the controller" table

If unclear, ask. Getting this wrong inverts every recommendation.

## Jurisdiction assumption

This review assumes the jurisdictional scope specified in your configuration. Privacy rules, response deadlines, and lawful bases vary materially by jurisdiction (GDPR vs. state consumer privacy laws vs. sectoral). If the controller, processor, or data subjects are in a different jurisdiction than configured, this review may not apply as written.

## Load prior context on this counterparty / activity

Before reviewing, check the outputs folder for prior work on this counterparty or processing activity. Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## Outputs` for the outputs folder path. Scan for:

- **Prior `use-case-triage` results** for the same counterparty / processing activity — the triage produces a risk rating and conditions that this DPA review should honor or explicitly depart from.
- **Prior `pia-generation` outputs** covering this counterparty / processing activity — the PIA may have flagged risk mitigations the DPA needs to implement.
- **Prior `dpa-review` outputs** for the same counterparty — earlier DPA reviews set expectations about what was acceptable, what was flagged, and what was settled. A fresh review that silently contradicts the earlier one erodes trust in the work product.

If a prior output is found, cite it in the review:

> "Prior triage ([date]) rated this [risk level] and conditioned approval on [X]. This DPA review is consistent with that finding." — or —
> "Prior triage ([date]) rated this [risk level]. This DPA review departs from that finding because [reason — new facts, different scope, contract term that changed the picture]."

**Carry severity from the upstream output as a floor** per the cross-skill severity floor rule in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## Shared guardrails`. A processing activity the triage rated 🔴 cannot be quietly downgraded to 🟢 in the DPA review; any demotion is stated and explained.

If no prior output is found (new counterparty / new activity), say so explicitly in the review — "No prior triage or PIA on this counterparty in outputs folder" — so the reviewing attorney knows the check ran.

## Check prior cross-plugin work

The section above covers this plugin's own outputs. Other practice areas' work lives elsewhere — read the shared practice context index at `~/.claude/plugins/config/claude-for-legal/practice-context.md` (or the working-folder fallback `./claude-for-legal-config/practice-context.md`) — an append-only, cross-plugin index of completed assessments and reviews, one pointer line per work product:

| Date | Plugin | Skill | Subject | Outcome | Where the full document lives |
|---|---|---|---|---|---|

Look for entries whose Subject matches this counterparty or the processing activity:

- **Prior vendor AI reviews of the same vendor** (ai-governance-legal, `vendor-ai-review` entries) — the AI review covers training-on-data, model changes, and AI liability terms that sit alongside the DPA terms; the two reviews should not contradict each other.
- **Prior PIAs naming this vendor as processor** (`pia-generation` entries) — the PIA may have flagged risk mitigations the DPA needs to implement.

If a relevant entry exists, surface it before starting:

> "A vendor AI review for [vendor] was completed on [date] (ai-governance-legal) — its findings on training-on-data, model changes, and AI liability complement this DPA review. Want me to incorporate it? (You'll need to point me at the document; the index has its location.)"

The index records pointers, not findings — to incorporate prior work, the user points you at the document (the index has its location).

If the index doesn't exist or has no relevant entries, say nothing and proceed — no noise. If matter workspaces are enabled and a matter is active, skip the check entirely — matter-scoped work is never indexed at practice level, and cross-matter visibility would breach matter isolation.

If the practice profile sets `**Cross-plugin practice index:** off`, skip this section entirely — do not read or write the index. If the practice profile is a multi-client practice (private practice — solo, small firm, or large firm) and matter workspaces are not enabled, skip the index entirely (reading and writing) — without workspace isolation, practice-level entries would let one client's assessments inform another client's work.

## Load the playbook

Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DPA playbook`. Also read `## Privacy policy commitments` — the DPA can't contradict what the privacy policy promises.

## Federal sectoral overlay (ask first, before the term-by-term walk)

Before walking the term-by-term review, answer: **does the data flowing through this DPA include any federally-regulated category?** GDPR and state consumer-privacy law supply one floor; federal sectoral law often supplies another that does not appear in the generic DPA playbook. A DPA that satisfies GDPR can still miss GLBA, HIPAA, or COPPA obligations — a gap that matters for fintech, healthtech, edtech, and children's-service counterparties.

> **Activity-based federal overlays — ask first:**
>
> Does this processing touch:
> - **Financial account data or "nonpublic personal information" about consumers** (GLBA / Reg P)? If yes, the DPA needs: (a) an NPI-sharing restriction consistent with 15 U.S.C. § 6802(a)-(c) and Reg P (no sharing for marketing to non-affiliated third parties without opt-out / opt-in), (b) safeguards language aligned with the Safeguards Rule (16 C.F.R. Part 314), (c) incident notification that reaches FTC/OCC timing where applicable, (d) a clean carve-out so a CCPA § 1798.145(e) exemption doesn't accidentally waive GLBA-level obligations.
> - **Protected health information held by a covered entity or business associate** (HIPAA Privacy / Security Rules)? If yes, the DPA needs: a Business Associate Agreement (BAA) layered with or integrated into the DPA per 45 C.F.R. § 164.504(e), breach notification timing aligned with HITECH (BA to CE within 60 days of discovery; CE to individuals within 60 days; CE to HHS contemporaneously for breaches of 500+ individuals, annual log for smaller breaches; media notice for breaches affecting more than 500 residents of a state or jurisdiction), permitted-uses clause, subcontractor BAA flow-down. A commercial DPA without BAA flow-down for PHI is a defect.
> - **Education records held by a school or a service provider acting for a school** (FERPA)? If yes, the DPA needs: a "school official" / directory-information framing consistent with 34 C.F.R. § 99.31, parental-consent flow-through, state student-privacy analog handling (NY Ed Law 2-d, CA SOPIPA, IL SOPPA).
> - **Data from children under 13 collected by an operator of an online service directed to children or with actual knowledge** (COPPA)? If yes, the DPA needs: verifiable-parental-consent flow-through, retention limits, deletion-on-request machinery, prohibition on behavioral advertising absent VPC.
> - **Another sectoral federal regime** (VPPA for video-viewing records, CPNI for carrier data, DPPA for DMV records, TCPA for call/SMS consent, GLBA Reg S-P for broker-dealers, §5 FTC Act for unfair/deceptive practices around sensitive data)?
>
> If yes to any: the federal overlay usually supplies the controlling substantive restriction, not just an exemption from a state consumer privacy law. Research the currently-operative provision and cite it. A DPA that is "exempt" from CCPA under § 1798.145(e) because it is GLBA-covered is still subject to the GLBA restrictions — the CCPA exemption moves the governing framework, it doesn't eliminate it. Flag sectoral gaps in the deal-breakers list alongside GDPR / state-privacy gaps.

If no sectoral overlay applies, note that explicitly — "no federally-regulated data categories identified; sectoral overlay n/a" — so the reviewing attorney sees that the check happened, rather than wondering whether it was skipped.

## The term-by-term review

### Core terms (check every DPA)

Walk every DPA through these terms, clause by clause. The *specific* numeric and substantive positions (notice periods, breach timelines, acceptable/unacceptable floors) come from `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DPA playbook`. The regulatory floors that any DPA has to clear come from primary law — **research the currently operative rule** for each applicable regime and cite primary sources before stating a floor.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a regime's breach window, transfer-mechanism requirement, subprocessor-change rule, or any other floor, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [regime / topic]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution tiering.** Tag every citation in the review — regulatory floors, SCC versions, adequacy decisions, regulator guidance, case law — with its source. For model-knowledge citations, use one of three tiers rather than a single blanket "verify" tag:
>
> - `[settled — last confirmed YYYY-MM-DD]` — stable, well-known statutory and regulatory references that have been checked against a primary source on the stated date (e.g., GDPR Art. 28, Art. 33 72-hour breach notice, SCC Decision 2021/914 by number). The date matters — even "stable" references change. When you can't confirm the date of the last check, use `[model knowledge — verify]` instead; an unconfirmed "settled" is a confident overclaim. Still verify before filing, but lower priority.
> - `[verify]` — model-knowledge citations that are real but should be verified: specific implementing regulations, regulator guidance, case holdings, adequacy decisions, SCC modules and versions, UK Addendum / IDTA status, thresholds, effective dates.
> - `[verify-pinpoint]` — pinpoint citations (specific subsection letters, clause numbers within SCCs, paragraph numbers, volume/page references) carry the highest fabrication risk and should ALWAYS be verified against a primary source.
>
> Tool-retrieved citations keep their source tag (`[Westlaw]`, `[Commission / regulator site]`, or the MCP tool name); web-search citations remain `[web search — verify]`; user-supplied citations remain `[user provided]`. The tiering directs verification effort to the citations most likely to need it. Never strip or collapse the tags.

| Term | Looking for | Playbook field | Common fights |
|---|---|---|---|
| **Roles** | Clear controller/processor designation; matches reality | — | Counterparty labels the relationship (e.g., "joint controller") in a way that doesn't match reality |
| **Processing scope** | Limited to documented instructions; defined purposes | — | Open-ended scope expanders ("and related purposes") |
| **Subprocessors** | Current list disclosed, change mechanism defined | Subprocessor changes | Blanket approval vs. veto vs. notice-only |
| **Security measures** | Annex references specific controls or standards | Security standards | "appropriate technical and organizational measures" with no annex commits to nothing specific |
| **Breach notification** | Defined trigger ("discovery" vs "confirmation"), defined timeline | Breach notification | Timeline tightness; clock trigger; "without undue delay" is vague |
| **Audit rights** | Method (report vs. on-site), frequency, notice, cost allocation | Audit rights | On-site audits on tight notice |
| **International transfers** | Transfer mechanism identified, supplementary measures, transfer impact assessment reference | Transfers | Outdated or missing transfer mechanisms |
| **Deletion/return** | Timeline post-termination, certification, backup carveout | Deletion on termination | "Commercially reasonable" deletion is undefined |
| **Liability** | Within MSA cap or separate; carveouts | Liability for data | Uncapped data breach liability is an existential exposure |

### When we're the processor: defensive review

Customer DPAs push operational burden onto the processor. For each clause below, compare the customer's ask to the playbook. Where the customer's ask is outside the playbook, push back to the team's standard position (from the config CLAUDE.md) and be ready to fall back to the acceptable position.

| Clause | Risk | Research / playbook lookup |
|---|---|---|
| Subprocessor approval right (veto) | Can't add infrastructure without customer-by-customer approval | Apply playbook position on subprocessor changes |
| On-site audit on short notice | Unworkable at scale | Apply playbook position on audit rights |
| Aggressive breach notification window | Often demands notice before we know what happened | Research the regulatory floor for each applicable regime (cite primary sources); compare to playbook position |
| Hard data residency (single country/DC) | May not match architecture | Apply playbook position on data location; confirm what we can actually commit to |
| Processor liability uncapped | Existential exposure | Apply playbook position on liability for data |
| Customer may issue binding "instructions" | Open-ended operational control | Define instructions as "documented in the Agreement or agreed in writing" |
| Deletion on very short timeline | Backup and log retention makes this impossible | Apply playbook position on deletion on termination; document backup rotation carveout |

### When we're the controller: protective review

Vendor DPAs typically offer the controller minimal protections. For each clause below, compare to the controller-side playbook.

| Clause | Gap | Research / playbook lookup |
|---|---|---|
| No subprocessor list | No visibility into who processes the data | Require published current list + advance notice per playbook |
| "Industry standard security" | No defined standard | Require annex with specific controls, or reference to a named standard (e.g., SOC 2, ISO 27001) |
| No breach notification timeline | Notification timing left to the vendor | Research applicable regulatory floor; require playbook position |
| No audit rights at all | Can't verify anything | Require at minimum an independent audit report per playbook |
| Vendor can use data for "service improvement" | Potential training on our data | Strike; processing limited to providing the service to us |
| No international transfer mechanism | No lawful transfer mechanism | **Research the currently operative transfer mechanism** for the corridor in question (origin/destination jurisdictions, applicable regime, any adequacy decision, any supplementary measures). Cite primary sources and verify currency. |
| No deletion commitment | No retention limit after termination | Require playbook position on deletion + certification on request |

## Consistency check: privacy policy

The DPA you sign can't promise something the privacy policy doesn't cover, and vice versa.

- If the DPA commits to processing only for purposes X, Y, Z — does the privacy policy list those purposes?
- If the privacy policy says "we never sell data" — does any DPA clause look like a sale under CCPA?
- If the privacy policy names specific subprocessor categories — does the DPA subprocessor list match?

Flag mismatches. They're usually the privacy policy being stale, not the DPA being wrong, but someone needs to fix one of them.

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artifact, not a rewrite. Wholesale clause replacement signals "we threw out your drafting" — it's aggressive, it forces the counterparty to re-read the whole clause, and it discards the parts of their drafting that were fine. Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks" and are faster to read, understand, and accept.

Default to the smallest edit that achieves the playbook position:
- Replace a **word** before a phrase. ("twelve (12)" → "twenty-four (24)")
- Replace a **phrase** before a sentence. ("paid by the Buyer" → "paid and payable by the Buyer")
- Restructure a **subclause** before replacing the sentence. (Add "(a)" and "(b)" to split a compound condition.)
- Replace a **sentence** before replacing the clause.
- Only replace a **whole clause** when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft — and when you do, say so in the transmittal: "We've replaced §8.2 rather than marking it up because the changes were extensive. Happy to walk you through the delta."

When in doubt, choose the smaller edit. A surgical redline shows the client the document was read carefully; a wholesale replacement puts that in doubt.

## Output

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# DPA Review: [Counterparty]

**Direction:** [We are processor / We are controller]
**Reviewed:** [date]
**Attached to:** [MSA / standalone]

---

## Bottom line

[Two sentences. Can we sign? What has to change?]

**Issues:** [N]🟢 [N]🟡 [N]🟠 [N]🔴

---

## Term-by-term

[For each core term, use a standard deviation-memo format: what the
counterparty's DPA says, what our playbook says, the gap, the risk, and the
proposed redline language. Keep each term to a short self-contained block so a
reviewer can skim.]

---

## Privacy policy consistency

[🟢 Consistent | 🟡 Flags: list]

---

## Recommended redlines

[Consolidated — ready to send back]

---

## If they won't move

[For each issue: the fallback from the config CLAUDE.md, or escalation routing if no
fallback exists]
```

## International transfers note

If the DPA contemplates cross-border data transfers, **research the currently operative transfer mechanism requirements** for the applicable corridor(s). For each origin/destination pair, identify: the applicable regime, whether any adequacy decision is in force, which transfer mechanism is required or available (e.g., Standard Contractual Clauses and their applicable version/module, UK Addendum or IDTA, BCRs, derogations), whether a transfer impact assessment or equivalent is required, and what supplementary measures may be needed. Cite primary sources (regulation, Commission decision, regulator guidance, controlling case law) with pinpoint cites and verify currency — adequacy decisions, SCC versions, and required supplementary measures change through new Commission decisions, court rulings, and regulator guidance. Flag uncertainty for attorney verification.

If a transfer mechanism is missing and there is an international transfer, that is a 🔴 — there is no lawful transfer mechanism.

## Gate: signing a DPA

Reviewing a DPA is research. *Signing* it — or instructing someone to countersign on our behalf — is the consequential act.

**Before proceeding to sign or countersign a DPA (including returning an executed version, consenting to automatic execution on a counterparty platform, or instructing a signatory to execute):** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. If the Role is Non-lawyer:

> Signing a DPA is a legal act — it binds the company to specific data-protection obligations that flow to regulators and data subjects. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty, direction (we are processor / controller), the terms that deviate from the playbook and how they were resolved, any open fallback decisions, and the three things to ask the attorney before executing.]
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent).

Do not proceed past this gate without an explicit yes.

## Record in the practice context index

**Record in the practice context index.** After the review is complete, append a one-line entry to `~/.claude/plugins/config/claude-for-legal/practice-context.md` (or the working-folder fallback `./claude-for-legal-config/practice-context.md`): date, this plugin, this skill, the subject (product/system/vendor name), the outcome status, and where the full document lives. If the index doesn't exist, create it from the template at `references/practice-context-template.md` in the plugin root (or, if the template isn't available, with the column schema shown below). The `Outcome` cell takes exactly one value from a closed set — `completed`, `draft`, `superseded`, or `withdrawn` — status only, never findings, conclusions, or risk ratings. Skip this step when working inside a matter workspace — matter-scoped work is never indexed at practice level.

If the practice profile sets `**Cross-plugin practice index:** off`, skip this section entirely — do not read or write the index. If the practice profile is a multi-client practice (private practice — solo, small firm, or large firm) and matter workspaces are not enabled, skip the index entirely (reading and writing) — without workspace isolation, practice-level entries would let one client's assessments inform another client's work.

| Date | Plugin | Skill | Subject | Outcome | Where the full document lives |
|---|---|---|---|---|---|
| [YYYY-MM-DD] | privacy-legal | dpa-review | [counterparty name] | [completed / draft / superseded / withdrawn] | [path or DMS link] |

The index is practice-level work-product — same confidentiality as the practice profiles. Record pointers, not findings: one line per artifact, status-only outcome, no substantive findings (the index travels in backups and syncs more readily than the documents it points to). Never record client names in multi-client (firm) practices — use matter numbers or generic descriptors.

**Sibling-plugin handoff.** If the counterparty provides AI features or services and the ai-governance-legal plugin is installed, suggest as a next step: run `/ai-governance-legal:vendor-ai-review [vendor]` — it will pick up this work from the practice context index.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't draft a DPA from scratch. If the answer is "use our template," pull the template from the seed docs path in the config CLAUDE.md.
- It doesn't do the Transfer Impact Assessment itself — it flags when one is needed.
- It doesn't decide whether to accept terms outside the fallbacks. It routes those per the escalation table.
