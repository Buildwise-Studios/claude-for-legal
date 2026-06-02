# Managed-agent templates for legal

Every agent in this repo ships **two ways**: as a Claude Code plugin (see the vertical directories at repo root), and as a **Claude Managed Agent** template your platform team deploys behind your own workflow engine. The same agent and skills run on both surfaces. Each directory below is a deploy manifest that references the canonical system prompt and skills from the matching plugin, so there is one source of truth.

These are **cookbooks, not products.** They are starting points. Adapt them to your document management system, your contract repository, your Slack workspace, your notification routing, your review cadence. They will not work out of the box without that adaptation.

Run `../scripts/deploy-managed-agent.sh <slug>` to upload skills, create leaf workers, and `POST /v1/agents` with the resolved config. Each template ships with [`steering-examples.json`](./reg-monitor/steering-examples.json) and a per-agent README covering its security tier and handoffs.

| Agent | Vertical plugin | What it watches | CMA steering event | Leaf workers |
|---|---|---|---|---|
| [`reg-monitor`](./reg-monitor/) | regulatory-legal | Regulatory feeds (Federal Register, agency RSS, TR) | `Check feeds as-of <date>, materiality: <threshold>` | feed-reader · materiality-filter · **digest-writer** |
| [`renewal-watcher`](./renewal-watcher/) | commercial-legal | Contract repository (Ironclad) for renewal and cancel-by deadlines | `Scan renewals <X>–<Y> days out, flag playbook deviations` | repo-reader · deadline-calculator · **alert-writer** |
| [`diligence-grid`](./diligence-grid/) | corporate-legal | Virtual data room (Box, Datasite, Intralinks, iManage) for new uploads + batch review | `Review folder <path> against schema <schema-id>` | doc-reader · extractor · normalizer · **grid-writer** |
| [`launch-radar`](./launch-radar/) | product-legal | Product roadmap / launch tracker (Jira, Linear, Asana) for launches needing legal review | `Scan tracker for launches in next <N> weeks` | tracker-reader · risk-classifier · **memo-writer** |
| [`docket-watcher`](./docket-watcher/) | litigation-legal | Court dockets (Trellis, CourtListener) for new filings, deadlines, and deliverables | `Watch docket <case-id> in <court>, matter <matter-id>` | docket-reader · deadline-mapper · **tracker-writer** |

**Bold** leaf = the only worker with `Write`.

## Manifest vs API

The `agent.yaml` files use the real `POST /v1/agents` field names with a few conveniences the deploy script resolves:

| Manifest convention | Resolves to |
|---|---|
| `system: {file: ../../<plugin>/agents/<agent>.md, append: "..."}` | `system: "<inlined contents + append>"` |
| `system: {text: "..."}` | `system: "<text>"` |
| `skills: [{from_plugin: ../../<plugin>}]` | uploads every `skills/*` under that dir → `[{type: custom, skill_id: ...}, ...]` |
| `skills: [{path: ../../...}]` | `skills: [{type: custom, skill_id: <uploaded-id>}]` |
| `callable_agents: [{manifest: ./subagents/x.yaml}]` | `callable_agents: [{type: agent, id: <created-id>, version: latest}]` |

> **Research preview:** `callable_agents` (multi-agent delegation) supports **one delegation level**. An orchestrator can call workers; workers cannot call further subagents.

## Cross-agent handoffs

Named agents never call each other directly. When one agent needs another (e.g., `launch-radar` surfaces a launch that needs a full review memo), it emits a `handoff_request` in its output; [`../scripts/orchestrate.py`](../scripts/orchestrate.py) (or your own event bus) routes it as a new steering event to the target session. The reference script hard-allowlists targets and schema-validates payloads.

## Audit log

The reference orchestrator writes a hash-chained audit log to `./out/handoff-audit.jsonl`: every entry carries a sequence number, the SHA-256 of the previous entry, and its own content hash, so edits, deletions, or reordering after the fact are detectable with `python3 ../scripts/orchestrate.py --verify-audit`. Each run opens with a `run_header` recording the agent slugs, truncated digests of the session and deployed-agent ids (raw identifiers never land in the log, so it can be exported safely), and the SHA-256 of the `agent.yaml` and practice profile in effect (set `AGENT_YAML_PATH` / `PRACTICE_PROFILE_PATH` / `COOKBOOK_SLUG` so this is captured); it closes with a `run_footer` that reports any failed audit writes. The log file is created owner-only (0600).

**What this log is, and is not.** It is the operator's own business record, produced by the same system it describes. The hash chain makes after-the-fact tampering *detectable*; it does not make the log independent evidence, and it does not record what a human reviewed, decided, or approved — those acts happen in your firm's systems and should be recorded there. Treat the log as one input to your records-retention and supervision process, not as a substitute for it.

## Security model

Legal documents and court filings are **untrusted input.** Every cookbook uses a three-tier worker split:

1. **Readers** touch untrusted documents and hold the connector(s) to their configured document source(s) — or, for `feed-reader`, an allowlisted `web_fetch` — plus `Read`/`Grep`, with no Write and no other egress. The manifests enable each connector's full toolset; the manifest does not enforce read-only, so point readers at a read-only deployment of the connector or restrict tools at deploy time. They return length-capped structured JSON. Any instruction embedded in a document is data, not a command.
2. **Analyzers** receive structured JSON from readers and apply rules from the user's configuration — no MCP, no web, no Write.
3. **Writers** produce the final output and are the only tier with `Write`. They never see raw documents.

The orchestrator holds no Write and reads no raw documents; it only routes.

## Work product and privilege

The headless append in every manifest instructs the agent to prepend the work-product/confidentiality header from the user's plugin configuration. A header is a label, not a control: whether work-product protection or privilege actually attaches depends on jurisdiction and context, and most monitoring outputs created in the ordinary course of business will not qualify. Confirm the header and the intended treatment with your legal team before deploying. If your deployment processes material that should not be retained, review Anthropic's data retention settings and your own storage retention before turning this on.

## What you get and don't get

- **You get:** a working manifest structure, a reference architecture with sensible security tiers, skills proven in the Claude Code plugins, and steering-event examples.
- **You don't get:** a production-ready agent. You need to wire the MCP connectors to *your* systems, set the cadence, configure the notification routing, tune the prompts for your practice, and run your own evaluation before trusting the output.
- **You especially don't get:** a replacement for a lawyer. These agents monitor, extract, and draft. A human configures the watchlist, thresholds, and calibration; a lawyer reviews each digest or memo and decides materiality and action; and only a human sends, files, or escalates anything externally.
