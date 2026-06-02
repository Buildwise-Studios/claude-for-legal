---
name: registry-browser
description: >
  Search watched registries for community legal skills, showing matches with
  descriptions and offering to show the full SKILL.md before install. Use when
  the user says "browse", "search skills", "find a skill for", "what's out
  there for", or wants to add a new registry to the watchlist.
argument-hint: "[search query]"
---

# /registry-browser

1. Load `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md` → watched registries.
2. Use the workflow below.
3. Search each registry. Show matches with descriptions.
4. Offer to show full SKILL.md for any match.

---

## Purpose

Find skills across the watched registries: search, preview, and decide before handing off to the installer.

## Load context

`~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md` → watched registries list.

## Workflow

### Step 1: Fetch registry indexes

For each watched registry:

- GitHub repos: fetch `skills/` directory listing and each `SKILL.md` frontmatter (name + description).
- Marketplace-style registries: fetch the index.

Cache the index locally at `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/registry-cache.json` (in Claude Cowork, where that path isn't writable, use `claude-for-legal-config/registry-cache.json` in the working folder — the plugin directory is replaced on update and is not for user data) so browsing is fast. Refresh cache if >7 days old or on request.

### Step 2: Search

Match query against skill names and descriptions. Simple keyword match is fine — these are small enough that fuzzy search is overkill.

Also: browse by category if the registry organizes skills that way.

### Step 3: Present matches

```markdown
## Search: "[query]"

**Found [N] skills across [M] registries:**

### [skill-name]
**From:** [registry name]
**Description:** [from frontmatter]
[View full SKILL.md] [Install]

### [skill-name]
[...]
```

### Step 4: Preview

On "view full SKILL.md": fetch and show the whole file. The user reads it before deciding to install.

### Step 5: Add a registry

If the user has a URL to a registry not in the watchlist:

1. Fetch it, validate it's a skills repo (has `skills/` or `.claude-plugin/`)
2. Show what's in it
3. Add to `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md` → watched registries on confirmation

Watching is discovery, not trust — in restrictive mode, installs from this registry stay blocked until it is added to `allowlist.yaml` (offer `/legal-builder-hub:customize`).

## Default registries

The default set (mirrored in `references/registries.yaml` and listed in the shipped default allowlist — known, not pre-trusted: each install asks a confirmation until you set your own policy):

- **lpm-skills** — 14 legal project management skills. Practice-agnostic. — `github.com/legalopsconsulting/lpm-skills`
- **Lawvable / awesome-legal-skills** — curated list of AI agent skills for legal work — `github.com/lawvable/awesome-legal-skills`
- **Lawvable / agent-skills** — curated collection of agent skills for legal work — `github.com/lawvable/agent-skills`

The plugin's `.mcp.json` also configures a **Lawve AI** MCP registry server (`mcp.lawve.ai`). It is a configured connector, not a pre-trusted source — its listings can be browsed here, but anything installed from it goes through the same allowlist and `/legal-builder-hub:skill-installer` gates as a skill from any GitHub registry.

## What this skill does not do

- Install anything. It browses. skill-installer installs.
- Rate or review skills. It shows you the SKILL.md; you judge.
- Search the whole internet. Only watched registries.
