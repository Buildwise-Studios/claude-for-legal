# matters/ — portfolio data

> **Location.** This layout lives at `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/` (or `./claude-for-legal-config/litigation-legal/matters/` where the home path isn't writable, e.g. Claude Cowork). The copy inside the installed plugin is documentation only — never store live matter files there; the install directory is replaced on plugin update.

This folder layout holds the portfolio. Two layers:

- **`_log.yaml`** — the ledger. One row per matter. Parseable by skills. Source of truth for rollups.
- **`[slug]/`** — per-matter detail. Narrative and history. Where humans read and edit.

## Layout

```
matters/
├── _log.yaml                  # ledger (all matters, including closed)
├── _README.md                 # this file
└── [matter-slug]/
    ├── matter.md              # narrative intake + theory + posture
    └── history.md             # append-only event log
```

## Slug conventions

Lowercase, hyphens, year at the end. Examples:
- `acme-v-us-2026`
- `ftc-inquiry-2026`
- `employment-smith-2026`

Year makes the slug stable even if a similar matter arises later. The folder name matches the slug exactly.

## Who writes what

| File | Written by | Edit directly? |
|---|---|---|
| `_log.yaml` | `/matter-intake`, `/matter-update`, `/matter-close` | Yes, but reflect the change in the matter's `history.md` |
| `matter.md` | `/matter-intake` at intake; appended by `/matter-close` | Yes, for evolving theory / posture notes |
| `history.md` | `/matter-intake` seeds; `/matter-update` and `/matter-close` append | Append-only in practice — treat past entries as record |

## Closed matters

Stay here. Don't delete. `/portfolio-status` filters them from active rollups by default; `/portfolio-status --all` includes them. Closed matters remain a reference point when assessing new matters.

## Corrections

If a past history entry was wrong, don't edit it. Append a new entry that references and corrects it, so the correction itself is part of the record.
