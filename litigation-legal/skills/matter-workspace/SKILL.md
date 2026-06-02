---
name: matter-workspace
description: Manage matter workspaces for multi-client practices — create, list, switch, close, or detach the active matter. Use when the user wants to create a new matter workspace, switch the active matter, list matters, archive a matter, or work at practice-level only without an active matter.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Practitioners work across multiple clients and matters. A matter workspace keeps one client or engagement's context separate from every other. This command manages those workspaces.

## Subcommands

- `/litigation-legal:matter-workspace new <slug>` — create a new matter workspace by handing off to `/litigation-legal:matter-intake`, which runs the conflicts gate and writes `matter.md`, `history.md`, and the `_log.yaml` row
- `/litigation-legal:matter-workspace list` — list matters with status and active flag
- `/litigation-legal:matter-workspace switch <slug>` — set the active matter
- `/litigation-legal:matter-workspace close <slug>` — archive a matter (move to `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_archived/`, never delete)
- `/litigation-legal:matter-workspace none` — detach from any active matter, work at practice-level only

Note: `/litigation-legal:matter-briefing [slug]` (no subcommand) is a separate command that produces a briefing on a specific matter — useful for in-house portfolio review. Matter workspace management lives here.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` — confirm the `## Matter workspaces` section is populated. If `Enabled` is `✗`, tell the user: "Matter workspaces are off — you're configured as an in-house practice with one client, so the plugin works from practice-level context automatically. If you actually work across multiple clients, re-run `/litigation-legal:cold-start-interview --redo` and select a private-practice setting. Otherwise, you don't need `/matter-workspace` at all." Don't error — the disabled state is the expected one for in-house users.
2. Follow the workflow and reference below.
3. Dispatch on the first token of `$ARGUMENTS`:
   - `new` → hand off to `/litigation-legal:matter-intake` (passing the slug if given). Matter creation has exactly one path — the intake's conflicts gate and `_log.yaml` row are what every downstream skill checks; this skill does not write matter files itself.
   - `list` → enumerate `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/*/matter.md`, print a table, mark the active matter.
   - `switch` → update the `Active matter:` line in the practice-level CLAUDE.md.
   - `close` → move `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/<slug>/` to `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_archived/<slug>/`, log the close date in `history.md`.
   - `none` → set `Active matter:` to `none — practice-level context only`.
4. Show the user what changed and confirm before writing.

## Notes

- The skill never reads across matters unless `Cross-matter context` is `on` in the practice-level CLAUDE.md.
- Archiving is not deletion — closed matters remain readable for retention/conflicts purposes.
- Slugs are lowercase with hyphens. If a slug is reused across archived and active, the archived one is preserved under `_archived/<slug>/`.

---

# Matter Workspace

Multi-client practitioners (private practice — solo, small firm, large firm) work across many matters. Context from one must not leak into another. This skill is the thin file-management layer that enforces that separation.

**Default state is off.** In-house users never see this — they run at practice-level only. Matter workspaces turn on at cold-start for private-practice users, or by editing `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗`, this skill does not run; the `/matter-workspace` skill explains the disabled state and suggests `/cold-start-interview --redo` for users who actually need matter isolation.

## Storage layout

All matter data lives under:

```
~/.claude/plugins/config/claude-for-legal/litigation-legal/
├── CLAUDE.md                       # practice-level practice profile
└── matters/
    ├── <slug>/
    │   ├── matter.md               # client, counterparty, matter type, key facts, overrides
    │   ├── history.md              # dated log of events, decisions, drafts, reviews
    │   ├── notes.md                # free-form working notes
    │   └── outputs/                # skill outputs for this matter (optional subfolder)
    └── _archived/
        └── <slug>/                 # closed matters — readable but not active
```

Slugs are lowercase with hyphens. Examples: `acme-v-zenith-2026`, `smith-employment-2026`, `ftc-inquiry-2026`.

## Active matter is in the practice CLAUDE.md

The `Active matter:` line under `## Matter workspaces` in the practice-level CLAUDE.md is the single source of truth. Switching a matter edits that line. No separate state file.

## Subcommand logic

### `new <slug>`

1. Confirm slug is not already present in `matters/<slug>/`, `matters/_archived/<slug>/`, or `matters/_log.yaml`. If reused, ask the user to pick a different slug.
2. Hand off to `/litigation-legal:matter-intake`, passing the slug. The intake owns matter creation: it runs the conflicts gate, interviews for the matter facts, writes `matters/<slug>/matter.md` and `history.md`, and appends the structured row to `matters/_log.yaml` that every substantive skill's conflicts gate checks. Do not create matter files here — a matter created without the `_log.yaml` row is refused by the downstream skills.
3. After the intake completes, create an empty `matters/<slug>/notes.md` if the intake didn't.
4. Do **not** auto-switch to the new matter. Ask: "Want to switch to `<slug>` now? (`/litigation-legal:matter-workspace switch <slug>`)"

### `list`

Enumerate `matters/*/matter.md`. Read each file's front-matter or first few lines to extract status. Print a table:

| Slug | Client | Matter type | Status | Opened | Active |
|---|---|---|---|---|---|

Mark the currently-active matter with `*`. Include `_archived/*` under a separate "Archived" heading if any exist.

### `switch <slug>`

1. Confirm `matters/<slug>/matter.md` exists. If not, offer `/litigation-legal:matter-workspace new <slug>`.
2. Edit the `Active matter:` line in the practice-level CLAUDE.md to `Active matter: <slug>`.
3. Show the user the matter.md summary so they can confirm they're on the right matter.

### `close <slug>`

1. Confirm `matters/<slug>/` exists.
2. Append a "Closed" entry to `matters/<slug>/history.md` with today's date.
3. Move `matters/<slug>/` → `matters/_archived/<slug>/`.
4. If the closed matter was the active matter, set `Active matter:` to `none — practice-level context only`.

### `none`

Set `Active matter:` in the practice-level CLAUDE.md to `none — practice-level context only`. Confirm with the user.

## `matter.md` and `history.md` templates

The canonical `matter.md` and `history.md` templates live in `/litigation-legal:matter-intake`, which writes them at creation. This skill reads those files; it does not define a competing shape.

## Cross-matter context

The practice-level CLAUDE.md has a `Cross-matter context:` flag. When it's `off` (the default), a skill working in matter A **never reads** files in `matters/B/` for any other `B`. This is the confidentiality guarantee the setting exists to provide.

When it's `on`, a skill may read files across matter folders only when the user explicitly asks it to (e.g., "compare our position on liability caps across the last five vendor matters"). Even when `on`, the default is to load only the active matter unless the user asks for a cross-matter view.

## What this skill does not do

- **Run a conflicts check.** Conflicts are the practitioner's/firm's job. Matter creation routes through `/litigation-legal:matter-intake`, whose conflicts gate captures what the user declares; this skill itself never records a conflicts posture.
- **Enforce retention.** Closing archives a matter; it does not delete. Retention policy is out of scope.
- **Auto-route outputs.** The substantive skill decides where to write; this skill tells it *which folder* is active, not what to put in it.
- **Decide whether cross-matter is appropriate.** It reads the flag and obeys.
