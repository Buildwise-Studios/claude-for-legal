---
name: customize
description: >
  Guided customization of your Legal Builder Hub profile — change one thing
  without re-running the whole cold-start interview. Adjust practice profile,
  installed starter pack, watched registries, update preferences, or the
  install allowlist. Use when the user says "change my [thing]", "add a
  registry", "update my profile", "edit my config", "edit my allowlist", or
  "customize".
argument-hint: "[section name, or describe what you want to change]"
---

# /customize

## When this runs

The user typed `/legal-builder-hub:customize`. They want to change something
in their Builder Hub profile — a watched registry, update notification
preferences, a practice area for recommendations — without re-running the
whole cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md`
   (and `~/.claude/plugins/config/claude-for-legal/company-profile.md` one
   level up, and `allowlist.yaml` next to the plugin config for allowlist
   changes). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/legal-builder-hub:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

   Config lives at the home path or, in environments where that isn't
   writable (Claude Cowork), at `./claude-for-legal-config/legal-builder-hub/` in
   the working folder — check both; home wins if both exist.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Your practice profile** — practice areas in scope, used to recommend
     community skills
   - **Installed starter pack** — which plugins and skills are installed via
     the hub, with install source
   - **Watched registries** — GitHub repositories / URLs the hub pulls
     community skills from
   - **Install allowlist** (`allowlist.yaml`) — mode (restrictive / permissive),
     trusted registries, trusted publishers, approved MCP connectors, accepted
     licenses. Editable here so changing an allowlist entry doesn't require a
     full `--redo` or hand-editing YAML.
   - **Update preferences** — check cadence (daily / weekly / on demand),
     notification channel (Slack / in-session). Updates are always proposed
     with a diff and applied only on explicit approval — there is no
     auto-apply setting to turn on.
   - **Skill install defaults** — install scope (user / project). The QA check
     (`/legal-builder-hub:skills-qa`) is not configurable: it always runs as
     part of `/legal-builder-hub:skill-installer`.
   - **Integrations** — Slack / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new watched registry:* "`/legal-builder-hub:registry-browser` will search this registry
     alongside the existing ones. `/legal-builder-hub:auto-updater` will check it on its next run."
   - *Adding a publisher to the allowlist:* "Skills from this publisher will pass
     the installer's allowlist gate. Everything else about the install — license
     gate, raw SKILL.md display, QA, typed approval — still applies."
   - *Allowlist mode restrictive → permissive:* "This widens what can be
     installed — unknown sources will be flagged and asked about instead of
     refused. Confirm before I write it."
   - *Update cadence weekly → daily:* "The registry-sync agent will check daily.
     Updates are still never applied without you reading the diff and approving."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/claude-for-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/legal-builder-hub:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a watched
  registry, offer to mark it `[Paused]` and explain that pausing keeps the
  install history but stops update checks.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., a watched registry that isn't on the allowlist in
  restrictive mode; or a practice profile that doesn't match any installed
  plugin), flag the tension.
- **The trust gates are not configurable.** Updates are always proposed and never
  auto-applied, and `/legal-builder-hub:skills-qa` always runs as part of
  `/legal-builder-hub:skill-installer`. If the user asks to turn either off,
  explain that these aren't settings — the configurable parts of the trust
  posture are the allowlist (mode and lists) and the update notification
  cadence.
- **Allowlist edits keep their warnings.** Switching mode to permissive gets a
  one-line "this widens what can be installed" warning and a confirmation
  before writing. Adding a registry, publisher, connector, or license names
  exactly what becomes installable as a result. Allowlist changes are written
  to `allowlist.yaml` AND mirrored in the profile's `## Sources I trust`
  section so the two stay in sync.
- **One change at a time.** Don't re-ask the whole interview.
- **Re-attestation on material changes.** When a change touches playbook
  positions, severity thresholds, escalation chains, gates, or the allowlist:
  update `Last material change: [today's date]` in the profile header, and ask
  whether the authorizing attorney has reviewed this change. If yes, update
  `Authorized by:` with the new date; if no, append ` (pending attorney review
  since [date])` to the existing `Authorized by:` line.
