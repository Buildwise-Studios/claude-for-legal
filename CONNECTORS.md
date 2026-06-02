# Adding a Connector

The plugins work best when connected to authoritative sources. If you build or operate a legal data source, research tool, CLM, DMS, eDiscovery platform, or practice management system, this page describes how to submit your MCP connector for inclusion in the suite.

## What the suite does not include

Read this before assuming a research capability ships in the box:

- **No citator.** Nothing in the suite provides a KeyCite or Shepard's equivalent. Descrybe's treatment check is the closest available signal, and it ships in only three plugins (`legal-clinic`, `ip-legal`, `law-student`). Keep your citator subscription — several skills assume you will run cites through one before relying on them.
- **No Lexis content.** No connector reaches any LexisNexis database.
- **Thomson Reuters content only via CoCounsel Deep Research.** The vendor-maintained [`external_plugins/cocounsel-legal`](./external_plugins/cocounsel-legal) plugin runs Westlaw Deep Research and returns synthesized, cited reports. It is not direct Westlaw or Practical Law search, and it does not retrieve full document text.
- **Shipped research sources cover U.S. law only.** CourtListener, Descrybe, Trellis, Solve Intelligence, and CoCounsel Deep Research all cover U.S. law. Non-US sources (EUR-Lex, legislation.gov.uk, Australia, Singapore) are on the wanted list below.
- **Most connectors are workflow tools, not research sources.** Slack, Google Drive, Box, iManage, Ironclad, DocuSign, Definely, Everlaw, Aurora, TopCounsel, Lawve AI, Courtroom5, Linear, Jira, and Asana connect Claude to your own data and processes. Only CourtListener, Descrybe, Trellis, Solve Intelligence, and CoCounsel retrieve legal authority.

## What makes a good legal MCP connector

- **Remote MCP server over HTTPS** with OAuth or API-key auth (streamable HTTP or SSE transport)
- **Read-heavy tools** — search, fetch, list. Write tools (create, send, file) need an explicit confirmation prompt on the client side; say so in your tool descriptions.
- **Provenance in results** — return the source, date retrieved, and a citation-ready identifier. The plugins tag every cite by source; your connector should make that possible.
- **No instruction-like content in results** — the plugins treat retrieved content as data, not commands. If your tool results include metadata or system notes, mark them clearly so they don't look like embedded directives.
- **Rate limits and errors that degrade gracefully** — the plugins have a fallback for when a connector isn't responding; a clean error is better than a timeout.

## How to submit

1. Publish your MCP server and document its tools, auth flow, and data coverage.
2. Open a PR adding your server to the relevant plugin's `.mcp.json` with the URL, auth method, and a one-line description of what it gives Claude.
3. Include a row for the table below: vendor, connector type (research / docket analytics / eDiscovery / CLM / DMS / e-signature / counsel network / skills registry / productivity), what the output is (direct source documents, a synthesized report, or the user's own data), what it requires (public / existing account / vendor subscription), read/write scope, and what it does **not** do — scope limits, jurisdictions not covered, content types not retrievable.
4. Include a note on which practice areas / plugins it's most useful for.
5. Submissions are tested against the plugin workflows before merge. Connectors that pass the retrieval-quality and injection-resistance checks go in the default `.mcp.json`; others get documented in the plugin README for users to add themselves.

## Current connectors

Connectors shipped in the default `.mcp.json` of each plugin, plus the vendor-maintained CoCounsel external plugin. Read/write scope reflects what the repo's `.mcp.json` and README state; `[vendor to confirm]` means the repo is silent.

### Research and court data

| Connector | Vendor | Type | Plugins | Output | Requires | Read/write | What it does NOT do |
|---|---|---|---|---|---|---|---|
| **CourtListener** | Free Law Project | research | legal-clinic, ip-legal, litigation-legal, law-student | direct source documents (U.S. opinions, PACER dockets) | none (public; optional API key) | Read | No citator signal; U.S. courts only |
| **Descrybe** | Descrybe | research | legal-clinic, ip-legal, law-student | direct source documents (primary law) | vendor subscription | Read | Treatment check is a signal, not a KeyCite/Shepard's replacement; U.S. law only |
| **Trellis** | Trellis | docket analytics | litigation-legal | direct source documents (state trial court dockets, rulings, verdicts) | vendor subscription | Read | U.S. state trial courts only — no federal coverage, no citator |
| **Solve Intelligence** | Solve Intelligence | research (patent) | corporate-legal, ip-legal | direct source documents (patent and non-patent literature, prior art) | vendor subscription | Read | Patent literature, not case law |
| **CoCounsel Legal** *(external plugin, vendor-maintained)* | Thomson Reuters | research | external_plugins/cocounsel-legal | synthesized report (cited, with Westlaw / Practical Law links) | vendor subscription (CoCounsel Legal with the MCP connector enabled) | Read | Not direct Westlaw / Practical Law search; no full-text document retrieval; U.S. law only; max three jurisdictions per run |

### Workflow, document, and practice systems

| Connector | Vendor | Type | Plugins | Output | Requires | Read/write | What it does NOT do |
|---|---|---|---|---|---|---|---|
| **Slack** | Slack | productivity | all 12 | your own data | your existing account | Read + write (send messages and canvases) | Not a legal research source |
| **Google Drive** | Google | productivity | all 12 | your own data | your existing account | Read + write (create and copy files) | Not a legal research source |
| **Ironclad** | Ironclad | CLM | commercial-legal | your own data | vendor subscription | Read (plain-language search, scoped to your permissions) | Does not create or modify contract records |
| **DocuSign** | DocuSign | e-signature | commercial-legal | your own data | vendor subscription | Read (agreement search, status tracking); signature-workflow write scope [vendor to confirm] | One connector — there is no separate DocuSign CLM connector |
| **iManage** | iManage | DMS | commercial-legal, corporate-legal | your own data | vendor subscription | Read (permission-bound, auditable) | Documents stay in iManage; not a research source |
| **Box** | Box | DMS | corporate-legal | your own data | your existing account | Read | Not a research source |
| **Definely** | Definely | productivity (contract drafting) | commercial-legal, corporate-legal | your own data | vendor subscription | Read (definitions, cross-references, structural diffs) | UK-hosted endpoint, but not a source of non-US law |
| **TopCounsel** | The L Suite (TechGC) | counsel network | commercial-legal, corporate-legal, litigation-legal | vendor dataset (counsel rankings and community sentiment) | vendor subscription | Read | Not a research source; recommendations, not engagements |
| **Everlaw** | Everlaw | eDiscovery | litigation-legal | your own data | vendor subscription | Read (search, retrieve); "organize" write scope [vendor to confirm] | Your productions, not case law |
| **Aurora** | Consilio | eDiscovery | litigation-legal | your own data | vendor subscription | Read-only (stated by vendor) | Not matter management or calendaring; not case-law research |
| **Courtroom5** | Courtroom5 | productivity (pro se procedural guidance) | legal-clinic | vendor dataset (procedural guidance, deadline calculations) | vendor subscription | [vendor to confirm] | Procedural guidance, not legal research or representation |
| **Lawve AI** | Lawve | skills registry | legal-builder-hub | vendor dataset (curated legal AI skills) | vendor subscription | Read | Not contract review or clause libraries; not a research source |
| **Linear** | Linear | productivity | product-legal | your own data | your existing account | [vendor to confirm] | Not a legal research source |
| **Atlassian (Jira / Confluence)** | Atlassian | productivity | product-legal | your own data | your existing account | [vendor to confirm] | Not a legal research source |
| **Asana** | Asana | productivity | product-legal | your own data | your existing account | [vendor to confirm] | Not a legal research source |

See the `.mcp.json` in each plugin directory for the authoritative list.

## Wanted connectors

These would make specific plugins significantly more useful. If you build or operate one, see "How to submit" above.

- **IP management systems** (Anaqua, Clarivate IPfolio, AppColl, Patrix, Alt Legal, FoundationIP) — full docket sync for `ip-legal` portfolio tracking
- **USPTO by customer number** — full portfolio status and deadlines, not just per-application lookup
- **USPTO TSDR / Trademark Status** — trademark status and deadlines for `ip-legal` brand management
- **Jira / Linear / Asana for OSS requests** — `ip-legal` OSS clearance can monitor and respond to incoming tickets
- **Direct Westlaw / Practical Law document retrieval; citator (KeyCite) signal** — CoCounsel Deep Research (synthesized cited reports) ships as the external `cocounsel-legal` plugin; direct document search/retrieval and a treatment signal do not
- **Citator** (KeyCite, Shepard's, or equivalent) — a treatment signal any plugin can call before a cite lands in work product
- **SS&C Intralinks / Datasite** — VDR access for `corporate-legal` diligence
- **Relativity / Everlaw beyond read** — eDiscovery workflow for `litigation-legal`
- **State bar CLE trackers** — `law-student` bar prep
- **Court e-filing systems** (PACER write, state e-filing) — with a hard irreversibility gate
- **Global AI Regulation Tracker** (techieray.com/GlobalAIRegulationTracker) — jurisdiction-tagged AI regulation tracking with structured API. Curated, verified, multi-jurisdiction. Would be a primary-source-adjacent feed for `ai-governance-legal` and `regulatory-legal`.
- **Regulatory primary sources** — a connector to official registers (eCFR, Federal Register, EUR-Lex, legislation.gov.uk, Federal Register of Legislation AU, Singapore Statutes Online) that bypasses the agent-blockers many legislative sites use. A curated regulatory knowledge base would be a high-value addition. These are also the path to non-US research coverage, which no shipped connector provides.

## Questions

Open an issue on this repo — partnership and integration questions go through issues as well.
