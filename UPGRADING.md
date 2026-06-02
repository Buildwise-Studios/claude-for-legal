# Upgrading from 1.0.x

The v2.0 release ships plugins versioned 1.2.0 — the release tag and the
plugin versions are intentionally different; this is not a mismatch.

## Before updating

- **legal-clinic:** if you authored a plausibility-band file under the plugin's
  `references/plausibility-bands/`, copy it to
  `~/.claude/plugins/config/claude-for-legal/legal-clinic/plausibility-bands/`
  before updating — plugin updates replace the plugin directory and files
  stored inside it are lost. The config path is where the deadlines skill now
  looks first.

## After updating

- **commercial-legal:** NDA triage is capped at YELLOW until an attorney
  records `Reviewed by:` / `Reviewed on:` on your NDA positions. Have counsel
  confirm the positions once to re-enable GREEN.
- **legal-builder-hub:** the bundled Google Drive connector was removed. If
  your workflows used it, re-add Google Drive as a user-level connector
  (Settings → Connectors in Cowork, or `/mcp` in Claude Code).
- **Practice profiles:** skills now read a `## Jurisdiction` block and a
  configuration-attestation header. Run
  `/<plugin>:cold-start-interview --redo jurisdiction` (or `--full`) once to
  add them; until then, skills infer jurisdiction from matter facts and US
  defaults apply.
- **litigation-legal:** matters without a row in `matters/_log.yaml` are
  refused by the conflicts gate until you run
  `/litigation-legal:matter-intake` once per matter to backfill the record.
  `matter-workspace new` now routes through matter-intake as well.
- **Managed-agent cookbooks** (affects redeploys only; running deployments are
  unaffected): orchestrators no longer declare MCP servers (reader subagents
  do); the Definely and DocuSign connector entries were removed; diligence-grid
  grid mode requires the deploy pipeline to stage VDR folders locally; the
  deploy script no longer injects output-schema validation — run
  `scripts/validate.py` in your own harness; connectors with unset environment
  variables are skipped with a notice instead of failing the deploy. Archive
  `./out/handoff-audit.jsonl` before re-running `orchestrate.py` — the audit
  log is now hash-chained and `--verify-audit` flags pre-upgrade entries as a
  discontinuity.
