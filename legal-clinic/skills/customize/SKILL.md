---
name: customize
description: >
  Guided customization of your legal clinic profile — change one thing without
  re-running the whole cold-start interview. Adjust clinic profile,
  jurisdiction, supervision style, practice-area templates, semester
  configuration, or output safeguards. Use when the user says "change my
  [thing]", "new semester", "add a practice area", "update my config", or
  "customize".
argument-hint: "[section name, or describe what you want to change]"
---

# /customize

## When this runs

The user typed `/legal-clinic:customize`. They (usually the professor, sometimes
a student) want to change something in the clinic profile — a jurisdiction, a
supervision style, a practice-area template, a semester rollover — without
re-running the whole cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md`.
   If the plugin config does not exist or still contains `[PLACEHOLDER]`
   values, say:

   > You haven't run setup yet. Run `/legal-clinic:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

   Config lives at the home path or, in environments where that isn't
   writable (Claude Cowork), at `./claude-for-legal-config/legal-clinic/` in
   the working folder — check both; home wins if both exist.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Clinic profile** — clinic name, host school, faculty lead, active
     practice areas, case type limits
   - **Jurisdiction** — primary state, courts, agencies, local rules path
   - **Supervision style** — informal vs. formal review queue; if formal,
     who reviews what before it goes out
   - **Practice-area templates** — which templates are active (immigration,
     housing, small business, family, expungement, etc.) and any local
     overrides
   - **Semester** — current semester, active students, rollover rules,
     handoff memo format
   - **Output safeguards** — plain-language standards for client-facing
     outputs, deadline warning rules, privilege labeling
   - **Seed documents** — clinic handbook, jurisdiction rules, template
     letters, sample memos, form libraries
   - **Outputs** — supervisor guide format, client letter templates, memo
     scaffolds
   - **Workflow** — case directories, deadline tracker location, review
     queue channel
   - **Integrations** — document storage / Slack / court e-filing status,
     fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new practice area:* "`/client-intake` will route matters of this
     type through the new template. `/draft`, `/memo`, and `/client-letter`
     will use the practice-area prompts. `/research-start` will add the
     corresponding Westlaw search terms."
   - *Supervision style informal → formal review queue:* "`/supervisor-review-queue` becomes
     active — student output will land there for supervisor sign-off before
     it goes to the client."
   - *New semester rollover:* "I'll archive the prior semester's active
     cases, carry forward matters you flag as continuing, and prompt the
     incoming students through `/ramp`."

5. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/legal-clinic:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "drop" a practice area,
  offer to mark it `[Archived]` and explain that archiving keeps case
  history accessible but hides the template from `/client-intake` routing.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., formal review queue on + informal supervision note;
  or practice area on + no jurisdiction rules configured), flag the
  tension.
- **Guardrail baselines are not removable.** These are load-bearing: the
  "NOT final work product" framing on `/draft`, plain-language standards on
  client-facing outputs, "does NOT decide case acceptance" on
  `/client-intake`, "NOT substantive advice" on `/client-letter`, and the
  scaffold-not-analysis framing on `/memo`. They exist because students
  ship work product — if the safeguards go, the risk of student work
  reaching a client without supervisor review goes up. Consistent with the
  profile's `## Output safeguards` ("built-in and not configurable"), do
  not remove or soften them through customize for any user; parameters
  within a safeguard (e.g., the plain-language reading-level target) remain
  adjustable by the supervising attorney. If a requested change touches one
  of these safeguards or the supervision style, check Role in `## Who's
  using this` first — if the user is not the supervising attorney, stop and
  redirect (mirror the cold-start role check): these gates are the
  supervising attorney's call under the student practice rule, so ask the
  supervising attorney to run `/legal-clinic:customize`.
- **One change at a time.** Don't re-ask the whole interview.
- **Re-attestation on material changes.** When a change touches playbook
  positions, severity thresholds, escalation chains, gates, or the allowlist:
  update `Last material change: [today's date]` in the profile header, and ask
  whether the authorizing attorney has reviewed this change. If yes, update
  `Authorized by:` with the new date; if no, append ` (pending attorney review
  since [date])` to the existing `Authorized by:` line.
