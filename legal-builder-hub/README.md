# Legal Builder Hub Plugin

Community legal skills discovery and installation. Browses GitHub registries (lpm-skills and the two Lawvable registries by default; add your own via /legal-builder-hub:registry-browser), installs and checks for updates (always proposed, never auto-applied), surfaces related community skills inside your other legal plugins. The cold-start interview doubles as the starter pack recommender — it asks your practice type and recommends what to install.

**Every community skill is surfaced raw before install, scanned for prompt-injection patterns, and evaluated against the Legal Skill Design Framework. The plugin helps you find and evaluate; reading the raw skill and deciding what to trust remain yours, and nothing installs or updates without your typed approval.**

## Who this is for

Everyone using the other legal plugins. This plugin is the discovery and installation surface for community skills.

## First run: cold-start

Asks your practice type, industry, team size, tooling comfort. Recommends a starter pack of community skills that match. Installs the ones you pick.

```
/legal-builder-hub:cold-start-interview
```

Your configuration is stored at `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md` and survives plugin updates. In Claude Cowork, where that path isn't writable, setup saves to `claude-for-legal-config/` in your working folder instead — keep using the same folder across sessions.

## Security posture

Installed community skills run with your access to client data, matter files, and your team's playbook. The hub treats every install and every update as a trust decision. Four layers of defense, none of which is sufficient on its own:

- **Allowlist (admin-controlled):** `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/allowlist.yaml` declares which registries, publishers, and MCP connectors community skills may use. `restrictive` mode (the shipped default — what governs if you never ran setup) refuses anything off-list; `permissive` mode (what the cold-start quick start writes, with your explicit consent) warns and asks instead. If the file is missing, the installer copies the shipped fail-closed default into place before reading anything else. The allowlist is checked before the installer reads any third-party content. See `skills/skill-installer/references/allowlist.md` for the schema.
- **Raw source, not summary:** the installer shows you the full raw `SKILL.md` — not an AI summary — before anything is written. A summary is a convenience; a skill that does something dodgy has to do it in text the raw display will show.
- **Heuristic scans:** both the installer and `skills-qa` scan the skill for prompt-injection patterns (override/authority claims, out-of-scope reads and writes, external URLs, hidden unicode, shell execution, credential asks). These are AI-heuristic scans, explicitly labeled as such — a clean scan is not a security audit, it is a prompt to read the text yourself.
- **Human approval, every time:** nothing is written to disk without a fresh typed `yes`. Approval is not inferred from earlier messages. For defense in depth, the installer runs the fetch / analysis in a read-only subagent by default — mandatory in restrictive mode, and in permissive mode skipped only if you type an explicit opt-out — so Write capabilities only become available after approval.

Updates use the same posture: the auto-updater pins to commit SHAs (not mutable tags), shows the full diff including hooks and MCP changes, and requires explicit approval per update. There is no auto-apply mode.

If a skill goes wrong after install: `/legal-builder-hub:disable [skill]` quiets it without removing files; `/legal-builder-hub:uninstall [skill]` removes it entirely. Both are restricted to community skills installed through this hub — they refuse to touch first-party plugin skills.

## Prerequisites

- Slack notifications from the registry-sync agent require a Slack MCP server configured in your environment. Without one, the agent writes its digest to a file.
- The default registry list ships with `lpm-skills` and the two Lawvable registries (see "Watched registries" below). These are known sources, not pre-trusted ones: until you set your own policy in setup, every install from them asks a confirmation per install naming the registry and publisher. Add registries you trust via `/legal-builder-hub:customize` or by editing `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/allowlist.yaml` (the file the installer's gate reads); `/legal-builder-hub:registry-browser` adds registries to the discovery watchlist only.

## Commands

| Command | Does |
|---|---|
| `/legal-builder-hub:cold-start-interview` | Practice profile + starter pack recommendation |
| `/legal-builder-hub:registry-browser [query]` | Search watched registries for skills |
| `/legal-builder-hub:skill-installer [skill]` | Install a community skill |
| `/legal-builder-hub:auto-updater` | Check for updates to installed skills |
| `/legal-builder-hub:related-skills-surfacer` | Suggest skills based on what you've been doing |
| `/legal-builder-hub:skills-qa [skill]` | Evaluate a skill against the Legal Skill Design Framework before installing |
| `/legal-builder-hub:disable [skill]` | Disable an installed community skill without removing files |
| `/legal-builder-hub:uninstall [skill]` | Uninstall a community skill installed through the hub |
| `/legal-builder-hub:customize` | Change one profile, registry, or allowlist setting without re-running the interview |

## Skills

| Skill | Purpose |
|---|---|
| **cold-start-interview** | Practice profile → starter pack |
| **registry-browser** | Search across watched registries |
| **skill-installer** | Allowlist-gate, fetch, show raw SKILL.md, trust-check, QA, install community skills |
| **uninstall** | Uninstall a community skill installed through the hub (first-party plugin skills are off-limits) |
| **disable** | Disable a community skill without removing its files; re-enable later |
| **skill-manager** | Reference: detailed uninstall/disable/re-enable workflows used by the `uninstall` and `disable` skills |
| **skills-qa** | Evaluate a skill against the Legal Skill Design Framework — design, failure modes, trust surface, and a prompt-injection heuristic scan |
| **auto-updater** | Check for updates; show diff and trust review; apply only on explicit approval |
| **related-skills-surfacer** | Surface related community skills after a task (direct or via hook) |
| **customize** | Change one profile, registry, or allowlist setting without re-running the interview |

## Interactive commands vs. scheduled agents

The commands above run when you invoke them — for when you're working a matter. The agents below run on a schedule — for what moves while you're not looking:

| Agent | What it watches | Default cadence |
|---|---|---|
| **registry-sync** | Watched registries for new and updated skills; posts notifications per update preferences | Weekly |

## Watched registries (default)

The default allowlist ships with known community registries pre-configured (the list below — known sources, not pre-trusted ones). Edit your per-install allowlist at `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/allowlist.yaml` to add, remove, or switch between restrictive and permissive modes.

- **lpm-skills** — Legal project management (Scott Margetts / LegalOps Consulting) — `github.com/legalopsconsulting/lpm-skills`
- **Lawvable / awesome-legal-skills** — Curated list of AI agent skills for legal work — `github.com/lawvable/awesome-legal-skills`
- **Lawvable / agent-skills** — Curated collection of agent skills for legal work — `github.com/lawvable/agent-skills`
- Add your own via `/legal-builder-hub:registry-browser` or by editing the allowlist

The plugin's `.mcp.json` also configures a **Lawve AI** MCP registry server (`mcp.lawve.ai`) that lists community legal skills. It is a configured connector, not a pre-trusted source — skills discovered through it go through the same allowlist and installer gates as skills from any GitHub registry.

## How it learns

Your practice profile at `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md` isn't static — it improves as you use the plugin. The hub re-reads it on every `/legal-builder-hub:registry-browser` and `/legal-builder-hub:related-skills-surfacer`, so adjusting your practice type, industry, or watched registries sharpens future recommendations. Edit the file directly or re-run `/legal-builder-hub:cold-start-interview --redo` when your work shifts.

## What this plugin does not do

- **No legal research connector.** Lawve AI is a registry of community-written legal AI skills, not a research source; the hub ships no case-law connector and no citator.
- **It does not certify community skills.** Scans and QA are heuristic prompts to read the skill yourself — a clean scan is not a security audit.
- **It never installs without you.** Nothing is written to disk without a fresh typed approval, and updates are never auto-applied.

## Notes

- Community skills are read before install. You see the **raw** SKILL.md — not a summary — before you accept.
- Updates are never auto-applied. The auto-updater shows the full diff and requires explicit approval, per update, every time.
- The related-skills-surfacer can run inside other plugins via a Stop hook each plugin must declare (not wired by default); otherwise invoke `/legal-builder-hub:related-skills-surfacer` directly to check if the community has something relevant to what you've been doing.
- Enterprise / firm deployments: keep `mode: restrictive` (the shipped default) in `allowlist.yaml` and populate the `registries`, `publishers`, and `connectors` lists. In restrictive mode the installer refuses to fetch, analyze, or install anything from an unlisted source.
