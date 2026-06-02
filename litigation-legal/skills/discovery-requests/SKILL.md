---
name: discovery-requests
description: Draft propounding written discovery — interrogatories, requests for production, and requests for admission — built from an element-to-evidence discovery plan, with a definitions-and-instructions section, FRCP numerical limits flagged, an objection-proofing pass, and FRCP 26(b)(1) proportionality framing throughout. Works from either side of the v. Use when the user says "draft interrogatories", "draft RFPs", "draft requests for admission", "we need written discovery", or "what discovery should we serve".
argument-hint: "[slug] [--rogs | --rfps | --rfas | --all] [--set=N]"
---

# /discovery-requests

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, side, work-product header, decision posture, document storage. Also check `./claude-for-legal-config/litigation-legal/CLAUDE.md` in the working folder — in environments where the home path isn't writable, configuration lives there instead. If both exist, the home path wins; say so and offer to reconcile.
2. Conflicts gate: confirm the matter is in `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml`. If not, refuse and route to `/litigation-legal:matter-intake`.
3. Follow the workflow and reference below.
4. Intake: claims and defenses in play, what you must prove, what you suspect the responding party has, case schedule and any discovery-order limits.
5. Build the discovery plan: each element you must prove → the evidence that would prove it → the discovery device that gets that evidence.
6. Draft the requests — numbered, with the definitions-and-instructions section, FRCP 33/34/36 disciplines applied, numerical limits counted and flagged.
7. Run the objection-proofing pass: overbreadth, proportionality, privilege carve-outs, ESI specifications.
8. Output: the discovery plan + the request sets + reviewer note + decision tree. Write to the matter folder. Nothing is served by the skill.

---

# Discovery Requests

## Purpose

Written discovery drafted backwards from what must be proved. The failure mode this skill is built against is the kitchen-sink request set — 75 boilerplate RFPs that draw 75 boilerplate objections, a meet-and-confer, and a motion-to-compel cycle, while the three documents that actually prove the case were never specifically asked for. Every request in this skill's output traces to an element of a claim or defense. If a request can't say which element it serves, it doesn't go in the set.

Works from either side: a plaintiff propounds to prove the prima facie case and quantify damages; a defendant propounds to break the plaintiff's elements, build affirmative defenses, and pin the plaintiff's contentions down.

## A DRAFT, NOT SERVED DISCOVERY

**Put this at the top of every output. Do not drop it. Do not soften it.**

> These are draft discovery requests for attorney review, not served discovery. Serving discovery starts the responding party's clock, counts against numerical limits, exposes your case theory to the other side, and creates obligations (FRCP 26(g) certification — every request is signed as warranted, non-harassing, and proportional). A licensed attorney reviews, edits, signs, and serves. The skill drafts; the lawyer serves.

## Side context

Read `## Side` in the practice profile, then confirm for this matter:

- **Plaintiff:** the plan maps the prima facie elements you must prove plus damages. RFAs target authentication and the defendant's denials.
- **Defense:** the plan maps the plaintiff's elements (which one can be broken?), the affirmative defenses (the defense carries the burden on those), and contribution/indemnity targets. Contention interrogatories aimed at the plaintiff's theory carry more weight here.
- **Both / varies:** ask which side this matter is, then proceed accordingly. Never mix frames in one set.

## Jurisdiction note

This skill is US-frame and defaults to the Federal Rules of Civil Procedure: FRCP 26 (scope and proportionality), 33 (interrogatories), 34 (production), 36 (admissions). Per the plugin CLAUDE.md `## Jurisdiction recognition` section:

- **State court:** limits and devices differ materially — California's CCP separates form and special interrogatories (35-limit on specials, Code Civ. Proc. § 2030.030), Texas has discovery-control plans, New York's CPLR practice differs on interrogatories vs. depositions priority. The skill flags every rule-dependent number `[verify — [state] limit]` and asks for the forum before counting against limits.
- **Non-US:** "discovery" as practiced in the US largely does not exist elsewhere. England & Wales disclosure (CPR 31 / PD 57AD), German civil procedure's lack of party-driven discovery, and EU data-protection constraints on document collection are different regimes — applying FRCP framing there produces nonsense. Say so, warn, and route per the CLAUDE.md decision-tree options. Tag anything produced for a non-US matter `[US framework — verify against [jurisdiction] procedure]`.
- **Arbitration:** discovery is what the arbitration agreement and the institution's rules (AAA, JAMS, ICC) say it is — usually far narrower. Flag and ask before drafting court-style discovery for an arbitration.

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — claims, defenses, side, case schedule, any discovery order or ESI protocol. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<matter-slug>/discovery/`. Never read another matter's files unless `Cross-matter context` is `on`.

**Conflicts gate — unbypassable.** Before drafting, check `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't draft discovery on a matter that hasn't been intaken — the conflicts check is the gate."

## Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, side, house style, document storage
- Active matter's `matter.md` and `history.md` — claims, defenses, theory, schedule
- The pleadings — the complaint and answer define what's "relevant to any party's claim or defense" under FRCP 26(b)(1); discovery into unpleaded theories is an objection magnet
- Any element chart from `/litigation-legal:claim-chart` — the gap list IS the discovery plan's input; rows marked `gap` or `needs-discovery` are exactly what these requests exist to close
- Any scheduling order, discovery order, ESI protocol, or protective order — these override the FRCP defaults and the skill's templates
- Prior discovery in the matter — to avoid duplication and to count sets/limits correctly (`--set=N` numbers this set)

If `CLAUDE.md` has `[PLACEHOLDER]` markers, surface the standard bounce (run `/litigation-legal:cold-start-interview`, or say "provisional" for generic defaults with every output tagged `[PROVISIONAL]`).

## Workflow

### Step 1: Intake

- **Claims and defenses in play.** From the pleadings. Discovery scope under FRCP 26(b)(1) is bounded by them.
- **What must you prove?** The elements you carry the burden on (your claims if plaintiff, your affirmative defenses if defendant) and the opposing elements you want to break.
- **What do you suspect they have?** Specific documents, systems, custodians, communications you believe exist. "I think their VP of Sales emailed about this in March" turns into a precise RFP; a hunch with no anchor turns into an overbreadth objection.
- **What do you already have?** Don't ask for what's already produced or publicly available — proportionality counts "the parties' relative access to relevant information."
- **Schedule and limits.** Discovery cutoff, any court-ordered limits beyond the FRCP defaults, how many interrogatories/RFAs already used in prior sets.

### Step 2: The discovery plan — element to evidence to device

The plan is the deliverable that makes the requests defensible. Build it before drafting a single request:

| Element / target | What evidence would prove it | Who has it | Device | Request # |
|---|---|---|---|---|
| Breach (D failed to pay invoices) | Invoice records, payment ledgers, internal AP communications | Defendant's finance dept | RFP | RFP 4–7 |
| D's knowledge of the defect | Internal emails, QA reports, complaint logs | Defendant | RFP + ROG (identify custodians) | RFP 12–14, ROG 6 |
| Damages — lost profits | P's own records (already have) + D's sales data for cover calculation | Both | RFP (D's sales data) | RFP 18 |
| Authentication of the MSA | Admission | Defendant | RFA | RFA 1–2 |
| D's affirmative defense: waiver | What facts D contends support it | Defendant | Contention ROG | ROG 11 |

Rules for the plan:

- **Every element with the burden on you appears.** If an element has no row, the case has a proof hole no discovery is aimed at — flag it: `[review — no discovery is targeted at element [N]; is it already proven, or is this a gap?]`
- **Every request traces back to a row.** Requests that serve no element get cut in the objection-proofing pass.
- **Device selection is deliberate:** documents and ESI → RFP; identification of people, systems, facts, and contentions → interrogatory; pinning down authenticity and discrete facts → RFA; testimony and follow-up → flag for deposition (route to `/litigation-legal:deposition-prep`, not this skill).

### Step 3: Draft the requests

#### Definitions and instructions (one section, shared by all sets)

Standard defined terms — include, and tailor to the matter:

- **"You" / "Your"** — the responding party, its officers, directors, employees, agents, attorneys, and all persons acting on its behalf
- **"Document"** — coextensive with FRCP 34(a); includes ESI, drafts, and non-identical copies
- **"Communication"** — any transmission of information, in any form
- **"Identify"** (person) — name, last known address, telephone, employer, title; (document) — date, author, recipients, type, subject, custodian
- **"Relating to" / "Concerning"** — referring to, describing, evidencing, or constituting
- **The Agreement / the Product / the Incident** — matter-specific defined terms; define once, use consistently
- **Relevant time period** — bounded dates; an unbounded period is an instant overbreadth objection

Instructions: continuing duty to supplement (FRCP 26(e)), privilege-log requirement for withheld documents (FRCP 26(b)(5)), ESI form of production (specify: native with metadata, or as the ESI protocol requires).

#### Interrogatories (FRCP 33)

- **The 25 limit, including discrete subparts, is counted and displayed.** The skill numbers each interrogatory, counts subparts that are likely to be deemed "discrete" under the case law (related subparts about a common theme usually count as one; unrelated questions joined by "and" count separately `[review — subpart counting is judgment]`), and shows the running total: "This set uses approximately 14 of 25." Exceeding the limit without leave of court means the responding party answers the first 25 and ignores the rest — the skill warns LOUDLY if the draft exceeds it.
- Identification interrogatories early (custodians, systems, people with knowledge); contention interrogatories flagged with a timing note (courts often defer them until later in discovery — FRCP 33(a)(2) `[verify — forum practice]`).
- Each interrogatory is a single, answerable question. Compound sprawl draws objections and produces useless answers.

#### Requests for production (FRCP 34)

- **Reasonable particularity** — FRCP 34(b)(1)(A). "All documents relating to the Agreement" fails; "Documents sufficient to show monthly payment amounts under the Agreement from January 2024 to present" works. Two patterns, used deliberately:
  - **"All documents [narrow category]"** — when you need everything in a genuinely narrow category (e.g., the contract drafts exchanged between the parties).
  - **"Documents sufficient to show [fact]"** — when you need the fact, not the haystack. This pattern defeats both overbreadth and burden objections.
- ESI: specify form of production per the ESI protocol if one exists; if none exists, flag that the form-of-production negotiation should happen at the FRCP 26(f) conference `[review]`.
- Each RFP names its time period (or incorporates the defined relevant period).

#### Requests for admission (FRCP 36)

Two strategic uses, both in the set:

- **Authentication admissions** — "Admit that the document attached as Exhibit A is a true and correct copy of [the Agreement]." Cheap to draft, expensive for the other side to deny (FRCP 37(c)(2) cost-shifting for unreasonable denials), and they remove authentication from trial.
- **Element admissions** — "Admit that You did not make any payment under the Agreement after March 1, 2026." Aim these at facts the responding party cannot plausibly deny; an RFA the other side can comfortably deny teaches them your theory for free. `[review — each element admission is a strategic disclosure call]`
- Note the mechanics in the set's instructions: matters admitted are conclusively established (FRCP 36(b)); failure to timely respond is admission; denials must fairly respond to the substance.

### Step 4: Objection-proofing pass

Re-read every request as if you were the responding party's associate paid to object. For each request, check:

| Objection | The check | The fix |
|---|---|---|
| Overbreadth | Unbounded time period? "All documents relating to" a broad topic? | Bound the period; narrow to "sufficient to show" or a named category |
| Proportionality (FRCP 26(b)(1)) | Is the burden of this request proportional to its value? Would you defend this request at a meet-and-confer in one sentence? | Each request's plan row IS the one-sentence defense; if you can't write it, cut or narrow the request |
| Privilege | Does the request sweep in attorney-client communications or work product on its face? | Add the carve-out: "excluding documents protected by the attorney-client privilege or work-product doctrine; provide a privilege log for any document withheld" |
| Vagueness | Undefined terms? "Relevant," "appropriate," "improper"? | Use defined terms; replace adjectives with facts |
| Equally available | Public records, your own client's documents? | Cut — proportionality factor weighs relative access |
| Premature contention | Contention ROGs served before discovery has developed? | Flag the timing; consider deferring `[review]` |

The pass output: requests revised in place, plus a short log of what was tightened and why (the attorney sees what the pass changed).

**Proportionality framing throughout.** FRCP 26(b)(1) factors — the importance of the issues, the amount in controversy, the parties' relative access to information, the parties' resources, the importance of the discovery in resolving the issues, and whether the burden or expense outweighs the likely benefit. The discovery plan is the proportionality record: if a motion to compel ever happens, the plan is what gets attached to show each request was aimed at something.

## Hard gate — service

The skill never serves discovery. Before anyone serves:

- A licensed attorney reviews every request, confirms the limits math against what's already been used in the matter, signs under FRCP 26(g) — which is a certification, with sanctions attached (FRCP 26(g)(3)), that every request is consistent with the rules, not for harassment, and not unreasonable or unduly burdensome.
- **Non-lawyer users (per `## Who's using this`):** serving discovery is a litigation act with procedural consequences (it can trigger the other side's right to serve discovery on you, and defective service wastes a set against your limits). Have an attorney review before service; the skill generates the one-page attorney brief (the plan, the sets, the limits math, the open flags) for that review.
- Service mechanics, response-deadline calendaring (30 days for each device under FRCP 33(b)(2), 34(b)(2)(A), 36(a)(3) `[verify — order or stipulation may modify]`), and meet-and-confer follow-up are post-service tasks the decision tree offers to set up.

## Output

Write to the matter folder: `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<slug>/discovery/`:

- `discovery-plan-[set-N]-YYYY-MM-DD.md` — the element-to-evidence plan. **Internal work product — carries the work-product header.** This is the document that must never be produced or served; it is the case theory in table form. Destination check applies hard here.
- `interrogatories-set-[N]-draft.md` / `rfps-set-[N]-draft.md` / `rfas-set-[N]-draft.md` — the request sets. These are drafts of documents that will be SERVED on the opposing party — they do NOT carry the work-product header (per the plugin CLAUDE.md `## Outputs`: external-facing deliverables don't get the internal header). Caption block, definitions and instructions, numbered requests, signature block (empty, with the FRCP 26(g) note).

Append a one-line entry to the matter's `history.md`.

Present in this order:

1. **⚠️ Reviewer note** (plugin CLAUDE.md format) — Sources, Read (which pleadings/charts/orders were read), Flagged (count of `[review]` / `[verify]` items), Currency (rule numbers cited are `[model knowledge — verify]` unless retrieved this session), Before-relying (typically: "confirm the limits math against prior sets" and "confirm the forum's local rules / discovery order override nothing here").
2. **The discovery plan** (header applied).
3. **The request sets** (clean, numbered).
4. **The objection-proofing log.**
5. **The decision tree.**

## What this skill does not do

- **It does not serve anything.** Drafts only.
- **It does not respond to discovery.** Responding to the other side's requests (objections, responses, productions, privilege logs) is different work — `/litigation-legal:privilege-log-review` covers the privilege-log piece; the rest is a future skill. Don't force it through this one.
- **It does not draft deposition notices or subpoenas.** Depositions route to `/litigation-legal:deposition-prep`; third-party subpoenas (FRCP 45) have their own service and objection rules — flag and route to `/litigation-legal:subpoena-triage` for inbound, or note the gap for outbound.
- **It does not assert numerical limits, response deadlines, or local-rule requirements as fact.** Every rule-dependent number carries `[verify]` — discovery orders and local rules override the FRCP defaults constantly.
- **It does not decide what to reveal.** Every request discloses theory. The strategic calls (especially RFAs and contention ROGs) carry `[review]` and the attorney makes them.

## Relationship to other skills

- `/litigation-legal:matter-intake` — must run first (conflicts gate).
- `/litigation-legal:claim-chart` — the chart's `gap` / `needs-discovery` rows are this skill's input; this skill's requests are how those rows get closed. After responses come in, update the chart.
- `/litigation-legal:complaint-drafter` — the pleadings define discovery scope; the complaint's element maps carry forward into the discovery plan.
- `/litigation-legal:deposition-prep` — the discovery plan rows marked "testimony" route there; document discovery from this skill feeds the depo outline's exhibits.
- `/litigation-legal:legal-hold` — if the client's own preservation isn't locked before serving discovery, fix that first; serving discovery while the client's own documents are being auto-deleted is how sanctions happen.
- `/litigation-legal:cite-check` — if the requests cite case law in instructions or definitions (rare but it happens), check them.

## Close with the next-steps decision tree

End with the next-steps decision tree per the plugin CLAUDE.md `## Outputs`, customized to what was drafted:

> **What next? Pick one and I'll help you build it out:**
> 1. **Tighten the sets** — pick any request and I'll narrow it, or tell me what the responding party is likely to object to and I'll pre-empt it.
> 2. **Build the response calendar** — I'll lay out the service date → response deadline → meet-and-confer window → motion-to-compel deadline chain for your calendar, flagged `[verify against the scheduling order]`.
> 3. **Map to depositions** — I'll take the plan rows that need testimony and start `/litigation-legal:deposition-prep` outlines for each witness.
> 4. **Escalate** — I'll draft the short note to [the partner / GC] presenting the discovery plan and what it will cost to pursue.
> 5. **Hold** — I'll note in the matter history that draft discovery exists and what it's waiting on (e.g., the FRCP 26(f) conference).
> 6. **Something else** — tell me what you'd do with this.
