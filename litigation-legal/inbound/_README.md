# inbound/ — incoming legal correspondence

> **Location.** This layout lives at `~/.claude/plugins/config/claude-for-legal/litigation-legal/inbound/` (or `./claude-for-legal-config/litigation-legal/inbound/` where the home path isn't writable, e.g. Claude Cowork). The copy inside the installed plugin is documentation only — never store live files there; the install directory is replaced on plugin update.

This folder layout holds triage and response work for anything arriving from the outside world: demand letters received, subpoenas served on the company, regulator inquiries, preservation demands, cease-and-desist letters aimed at the company.

Separate from `demand-letters/` (outbound) and `matters/` (tracked portfolio) because inbound items have their own workflow: read → triage → decide → respond (or escalate to matter). Not everything that comes in becomes a tracked matter.

## Layout

```
inbound/
├── _README.md
└── [slug]/
    ├── incoming.pdf              # or .eml / .docx — the original (or link/pointer)
    ├── triage.md                 # analysis: scope, merit, options, recommendation
    └── response-v1.docx          # drafted response, if one is sent (v2, v3 as iterated)
```

## Slug conventions

`[type]-[sender-short]-[yyyy-mm]`. Examples:

- `demand-rec-acme-2026-04` (demand letter received)
- `subpoena-smith-v-us-2026-04` (third-party subpoena)
- `regulator-ftc-inquiry-2026-04`
- `preservation-vendor-2026-04` (preservation letter received)

## Workflow

| Type | Command | Outputs |
|---|---|---|
| Demand letter received | `/litigation-legal:demand-received [path]` | triage.md + optional response draft |
| Subpoena served | `/litigation-legal:subpoena-triage [path]` | triage.md + objections memo |
| Regulator inquiry | — (no dedicated skill; file here and triage manually) | triage.md |

Each triage cross-checks `matters/_log.yaml` for related matters (same counterparty, overlapping subject). If a related matter exists, the triage flags it and offers to add this as a related_matter entry. If this inbound item should itself become a tracked matter, the triage hands off to `/matter-intake` with fields pre-populated.

## Relationship to matters

- Inbound + related to existing matter → link via `related_matters` field in `_log.yaml`; file stays in `inbound/`.
- Inbound + should become a matter → create matter; matter.md cross-links back to `inbound/[slug]/`.
- Inbound + handled and closed (no matter needed) → stays in `inbound/` as a record.

## Relationship to outbound

If the response to an inbound demand is itself an outbound demand (a counter-demand), the triage hands off to `/demand-intake` pre-populated. The outbound demand lives in `demand-letters/`, with a cross-link back to this inbound folder.
