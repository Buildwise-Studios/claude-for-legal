---
name: cite-check
description: Standalone citation verification for any document — enumerate every citation into a numbered work plan, check each one in batches against the configured research connector, and return per-cite verdicts (confirmed / could-not-retrieve / miscited / misgrounded-partial / quote-mismatch / likely-fabricated) plus a fix list and a coverage line. Use when the user says "check the citations in this", "cite-check this brief / memo / letter", "are these cites real", "verify the authorities", or has any document whose citations need verification before it is filed, sent, or relied on.
argument-hint: "[path-to-document] [--batch-size=N] [--cases-only | --include-record-cites]"
---

# /cite-check

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, work-product header, citation style, decision posture, verification log. Also check `./claude-for-legal-config/litigation-legal/CLAUDE.md` in the working folder — in environments where the home path isn't writable, configuration lives there instead. If both exist, the home path wins; say so and offer to reconcile.
2. Pre-flight the research connector (CourtListener / Trellis per this plugin's `.mcp.json`; Westlaw / Descrybe if configured): run a test query and confirm it actually responds, not just that it's configured. Record the result for the reviewer note's **Sources:** line.
3. Read the input document end to end. **Enumerate** every citation into a numbered list with the proposition each is cited for. Report the count. The list is the work plan.
4. Follow the workflow and reference below.
5. **Batch:** work through the list in batches of ~10 (or `--batch-size=N`), never skipping, never sampling. Track progress explicitly ("checked 20 of 47").
6. **Verify each:** retrieve via the research connector, READ the relevant passage, confirm it supports the proposition AS STATED. No connector → every cite gets `[model knowledge — verify]` and the reviewer note says retrieval-backed checking wasn't possible.
7. **Verdict per cite** from the fixed vocabulary: `confirmed` / `could-not-retrieve` / `miscited` / `misgrounded-partial` / `quote-mismatch` / `likely-fabricated`.
8. Output: verdict table + fix list (everything not confirmed) + coverage line + reviewer note + decision tree.
9. Offer to record verified items in `~/.claude/plugins/config/claude-for-legal/litigation-legal/verification-log.md`.

---

# Cite Check

## Purpose

The deep cite-check protocol in `/litigation-legal:brief-section-drafter` only fires while a brief is being drafted. This skill is the standalone version: hand it any memo, brief, letter, or filing — yours or someone else's — and it verifies the citations in it. Same discipline, no drafting attached.

The point of the skill is coverage. A cite check that samples is not a cite check — a fabricated cite in the unchecked portion survives it. Enumerate first, then check everything on the list.

## Relationship to brief-section-drafter

`/litigation-legal:brief-section-drafter` runs this protocol inline on its own drafts (its "Citation extraction coverage" section). Use this skill when:

- The document was drafted by someone else (outside counsel, opposing counsel, a prior associate, an AI tool).
- The document was drafted earlier and is now headed for filing or sending.
- The user asks for a cite check and nothing else.

The verdicts and the coverage discipline are identical. If a brief-section draft is open in this conversation, either skill can check it — don't run both.

## Jurisdiction note

This skill's verification mechanics are US-frame: US citation formats (Bluebook / ALWD), US research connectors (CourtListener, Trellis), US good-law concepts (overruled, superseded, abrogated). Per the plugin CLAUDE.md `## Jurisdiction recognition` section: if the document cites non-US authority (UK, EU, Canadian, Australian, or other jurisdictions' cases and statutes), say so clearly — "I can't retrieval-verify [jurisdiction] authority with the configured connectors" — tag every such cite `[US-frame tooling — verify against [jurisdiction] source]`, and offer the decision-tree options (search for the applicable source, route to a practitioner in that jurisdiction, or proceed with every non-US cite flagged). Never report a non-US cite as `confirmed` on the strength of US tooling or model knowledge.

## Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, work-product header, citation style, verification log, decision posture
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/verification-log.md` → previously verified cites (skip re-verification inside the freshness window; note "previously verified by [name] on [date]")
- The input document — a path, a paste, or a draft produced earlier in this conversation
- If matter workspaces are enabled and a matter is active: the matter's record materials (for record cites — depositions, exhibits, declarations)

If `CLAUDE.md` has `[PLACEHOLDER]` markers, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor risk calibration, landscape, and house style to your practice.
>
> **Two choices:**
> - Run `/litigation-legal:cold-start-interview` (2 minutes) to configure your profile, then I'll run this tailored to your practice.
> - Say **"provisional"** and I'll run this against generic defaults — US jurisdiction, Bluebook, lawyer role — and tag every output `[PROVISIONAL — configure your profile for tailored output]`.

A cite check is less profile-dependent than most skills, so provisional mode is fine here — but the work-product header and the verification log still come from the profile, so say what's defaulted.

## Pre-flight: the research connector

Per the plugin CLAUDE.md `## Shared guardrails` pre-flight rule: test whether a research connector is actually responding before starting. The connectors this plugin ships in `.mcp.json` are **CourtListener** (federal and state case law, citation lookup) and **Trellis** (state trial court records). Westlaw or Descrybe count if the user has them connected.

- **Connector responding** → every verification below is retrieval-backed. Source tags are the connector's name.
- **No connector responding** → the skill still runs, but every cite's best possible verdict is capped: nothing can be `confirmed`. Cites the model recognizes get `could-not-retrieve` + `[model knowledge — verify]`; cites the model does not recognize at all get `likely-fabricated` with the caveat that this is a model-knowledge judgment, not a retrieval result. The reviewer note's **Sources:** line says: `not connected — retrieval-backed checking wasn't possible; verdicts are capped at could-not-retrieve and every cite needs manual verification`.

Do not let a missing connector silently degrade the output. The cap is the signal.

## Workflow

### Step 1: Enumerate — the list is the work plan

Read the entire document first. Extract EVERY citation into a numbered list. Never sample; never start checking before the enumeration is complete.

What counts as a citation (all of these go on the list):

| Type | Examples | Verifiable against |
|---|---|---|
| Cases | *Smith v. Jones*, 123 F.3d 456 (9th Cir. 1997) | Research connector |
| Statutes | 28 U.S.C. § 1332; Cal. Civ. Code § 1717 | Research connector / statute site |
| Regulations | 29 C.F.R. § 825.110 | Regulator site / connector |
| Court rules | FRCP 26(b)(1); Local Rule 7-3 | Court website / connector |
| Secondary sources | Restatement (Second) of Torts § 552; treatises; law review articles | Connector (limited) / manual |
| Record cites | Doe Dep. 42:15–43:7; Smith Decl. ¶ 12; Trial Ex. 14; DEF00012345 | The matter's record, if available |

Each entry on the list records: **(#) the citation as written · the proposition it's cited for · any quoted language attributed to it.** The proposition matters as much as the cite — a cite check that only asks "does this case exist" misses the misgrounded-citation failure mode entirely.

`--cases-only` limits the list to cases, statutes, regulations, and rules. `--include-record-cites` (the default when a matter workspace is active and the record is reachable) adds record cites. If record materials aren't available, record cites are enumerated but reported as `could-not-retrieve — record not available to this session`.

After enumeration, report: "Found **N** citations: [breakdown by type]. That's [N/batch-size] batches."

### Step 2: Batch — never skip, never sample

Work through the list in batches of ~10. For a large document, say up front how many batches there will be and track progress explicitly after each one: "checked 20 of 47."

- Do not stop early. Do not summarize the remaining cites as "the rest appear fine." If the run is interrupted (context, time, user redirect), report exactly where it stopped: "checked 30 of 47 — cites 31–47 are UNCHECKED" — and put that in the reviewer note.
- Per the plugin CLAUDE.md `## Large output` rule: if the document is enormous (hundreds of cites), scope first — tell the user the batch count and offer to run it across multiple turns. A silent truncation is the failure mode this rule exists to prevent.

### Step 3: Verify each cite

For each cite in the batch, when a research connector is available:

1. **Retrieve.** Query the connector for the citation. If it returns nothing, try reasonable variants (party name + year, docket number, parallel cite) before concluding it can't be retrieved.
2. **Read.** Open the retrieved text and read the passage relevant to the proposition — not just the case caption, not just the syllabus or headnotes. A cite is never confirmed by existence alone.
3. **Compare.** Does the passage support the proposition AS STATED in the document? Element by element if the proposition has multiple parts. Holding vs. dicta vs. dissent matters — a proposition cited as a holding that appears only in a dissent is `miscited`.
4. **Check quotes.** If the document puts quotation marks on language attributed to this source, compare character-for-character. See the quote-attribution rule below.
5. **Check good-law signals if the connector exposes them.** Subsequent history, overruling, abrogation. If the connector doesn't expose this, note it: good-law status was not checked, only existence and support.

When no connector is available: steps 1–2 are impossible. Tag the cite `[model knowledge — verify]`, give the model-knowledge assessment of whether the cite looks real and on-point, and cap the verdict per the pre-flight rule.

### Step 4: Verdict — fixed vocabulary

Every cite gets exactly one verdict. Do not invent intermediate labels; the fixed vocabulary is what makes the output scannable and the fix list actionable.

| Verdict | Meaning | Goes on the fix list? |
|---|---|---|
| **confirmed** | Retrieved, the relevant passage was read, and it supports the proposition as stated (every part of it). | No |
| **could-not-retrieve** | The connector did not return the source, or no connector is available, or the source type isn't retrievable (record cite without the record). Says nothing about whether the cite is good — it says the check couldn't be completed. | Yes — manual verification |
| **miscited** | The source exists but says something else. The proposition is not supported by what the source actually holds. State what the source actually says. | Yes — replace or re-frame |
| **misgrounded-partial** | The source supports part of a multi-part proposition. State exactly which part fails. | Yes — split the cite or narrow the proposition |
| **quote-mismatch** | The quoted text differs from the source. Show both versions side by side. | Yes — conform the quote or remove the quotation marks |
| **likely-fabricated** | No trace of the cited authority found — wrong reporter, no case by that name, no such section. Flag hard. | Yes — remove; check sibling cites from the same origin |

**`could-not-retrieve` is never reported as `confirmed`.** A false "this cite is fine" when the source couldn't be read is worse than "couldn't check this one" — it's the exact overclaim this skill exists to prevent.

**`likely-fabricated` is a hard flag, not a soft one.** When a cite has no trace, say so in those words, put it at the top of the fix list, and recommend checking every other cite that came from the same origin (same draft section, same prior memo, same AI tool) — fabrications cluster.

## Quote-attribution rule

Any quoted language attributed to a person, a court, or a document gets verified verbatim or flagged. Quotes are never "close enough."

- A quote that paraphrases accurately but isn't verbatim is still `quote-mismatch`. Show both versions; the fix is either conforming the quote character-for-character (with ellipses and brackets marking every alteration) or removing the quotation marks and paraphrasing with attribution.
- This applies to record quotes (witness testimony, opposing counsel's statements, contract language) the same as to case quotes. Per the plugin CLAUDE.md shared guardrail: a quote that's almost right misrepresents the record and is sanctionable if filed.
- If the source couldn't be retrieved, quoted language attributed to it is flagged `[verify exact quote — source not retrieved]` and the cite's verdict is `could-not-retrieve`, never `confirmed`.

## Partial-support rule

Multi-part propositions get element-by-element comparison. If the document says "X requires A, B, and C, see *Case*," the cited case must support A AND B AND C. If it supports A and B but is silent on C, the verdict is `misgrounded-partial` and the output states: "supports A and B; does not address C."

This is the hardest error to catch and the most common way a court catches a lawyer stretching — the cite exists, the passage exists, but the passage doesn't support the proposition as stated. It passes a "does the case exist" check and fails a "does the case say that" check. It's why Step 1 records the proposition, not just the cite.

## Output

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` `## Outputs` (role-dependent — lawyer vs. non-lawyer). The cite-check report is internal work product even when the document being checked is external-facing.

Open with the **⚠️ Reviewer note** per the plugin CLAUDE.md format — one block, everything the reviewer needs:

> **⚠️ Reviewer note**
> - **Sources:** [CourtListener ✓ verified / Trellis ✓ / not connected — retrieval-backed checking wasn't possible, verdicts capped at could-not-retrieve]
> - **Read:** [whole document, N pages; all N citations enumerated]
> - **Flagged for your judgment:** [N cites on the fix list]
> - **Currency:** [good-law signals checked via connector / not checked — existence and support only]
> - **Before relying:** [resolve the fix list; manually verify the could-not-retrieve items; do not file with any likely-fabricated cite present]

Then three sections:

### 1. Verdict table

| # | Citation | Cited for | Verdict | Source tag | Notes |
|---|---|---|---|---|---|
| 1 | *Smith v. Jones*, 123 F.3d 456 (9th Cir. 1997) | Elements of fraud under CA law | confirmed | [CourtListener] | Pin cite at 460 supports all five elements |
| 2 | Cal. Civ. Code § 1717 | Fee-shifting is mutual | confirmed | [CourtListener] | |
| 3 | *Doe v. Roe*, 99 F.4th 1 (2d Cir. 2024) | Three-part test, parts A, B, C | misgrounded-partial | [CourtListener] | Supports A and B; does not address C |
| 4 | *Acme v. Zenith*, 456 U.S. 789 (1982) | "Quoted language here" | likely-fabricated | — | No case at this cite; no party-name match in any reporter |

### 2. Fix list

Everything not `confirmed`, ordered: `likely-fabricated` first, then `miscited`, `quote-mismatch`, `misgrounded-partial`, `could-not-retrieve`. For each: the cite, what's wrong, and the concrete fix (replace with X / narrow the proposition to Y / conform the quote / verify manually against Z). The fix list is what the attorney works through — make every entry actionable.

### 3. Coverage line

The last line of the report, always, in this exact shape:

> **Coverage: checked N of N citations — M confirmed, K could-not-retrieve, J miscited, I misgrounded-partial, H quote-mismatch, G likely-fabricated.**

If the run was interrupted, the coverage line says so: "checked 30 of 47 — 17 UNCHECKED (cites 31–47)." Coverage honesty outranks a clean-looking report.

## Verification log

For every cite that ends up `confirmed` (or corrected and then confirmed), offer to append a line to `~/.claude/plugins/config/claude-for-legal/litigation-legal/verification-log.md` per the plugin CLAUDE.md format:

`[YYYY-MM-DD] [cite] verified by [user name] against [connector] — confirmed / corrected to [X]`

And on the way in: any cite already in the log within the freshness window gets noted in the verdict table ("previously verified by [name] on [date] against [source]") — still re-checked if a connector is available (re-checking is cheap), but the prior verification is part of the record.

## Hard gate — filing and sending

This skill verifies; it does not bless. Before the checked document is **filed or sent**:

- A licensed attorney resolves every item on the fix list and takes professional responsibility for the filing. Filing a document containing a fabricated or miscited authority carries Rule 11 and Rule 3.3 (candor toward the tribunal) exposure — sanctions for AI-fabricated citations in filed briefs are no longer hypothetical; they are routine.
- If the Role in `## Who's using this` is Non-lawyer: do not treat a clean cite-check as filing clearance. Generate the one-page attorney brief (what was checked, what was found, what's unresolved) and route to attorney review per the plugin CLAUDE.md consequential-action gate.
- The skill never files, sends, or marks a document as filing-ready. Its output is a report.

## What this skill does not do

- **It does not certify.** "Confirmed" means retrieved-read-and-supports in this session. The attorney's signature is the certification; this report is an input to it.
- **It does not check good-law status unless the connector exposes it.** Existence and support are not the same as "still good law." When subsequent-history data wasn't available, the report says so.
- **It does not fix the document.** It produces the fix list. Applying fixes is a separate step the user directs (and the decision tree offers).
- **It does not sample.** If the user asks for a "quick check of the main cites," explain that a partial check gives false comfort, then do what they ask with the coverage line stating exactly what was and wasn't checked.
- **It does not verify non-US authority with US tooling.** Flagged, not faked.

## Relationship to other skills

- `/litigation-legal:brief-section-drafter` — drafts carry `[CITE NEEDED]` / `[VERIFY]` markers; this skill is how those markers get resolved before filing.
- `/litigation-legal:demand-draft` — the citation-verification pass its post-send checklist requires can be run with this skill.
- `/litigation-legal:claim-chart` — pin cites in a chart's evidence cells are record cites this skill can verify when the record is reachable.
- `/litigation-legal:complaint-drafter` — complaint drafts route here before filing.
- `/litigation-legal:settlement-demand` — demand packages cite cases and records; check them before the package goes out.

## Close with the next-steps decision tree

End with the next-steps decision tree per the plugin CLAUDE.md `## Outputs`. Customize to what the check found:

> **What next? Pick one and I'll help you build it out:**
> 1. **Apply the fix list** — I'll produce a corrected version of the document with every fixable item resolved and the unresolvable ones left flagged for you.
> 2. **Research the gaps** — for each `could-not-retrieve` and `miscited` item, I'll draft the research queries (or run them, if the connector is up) to find the right authority.
> 3. **Escalate** — [if any `likely-fabricated`] I'll draft a short note to [the partner / the drafting attorney] flagging the fabricated cites and where they came from.
> 4. **Record the verifications** — I'll write the confirmed items to the verification log so the next reviewer doesn't re-check them.
> 5. **Something else** — tell me what you'd do with this.
