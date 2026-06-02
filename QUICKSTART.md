# Quick Start

Installation takes about a minute. This page covers install and first-run setup; [README.md](README.md) is the full reference.

## Install in Claude Cowork
1. [Install Claude Desktop](https://claude.com/download)
2. Get access to Claude Cowork — see the [Claude Cowork page](https://claude.com/product/cowork) for plan availability, or ask your workspace admin to enable it
3. Follow the instructions in the video below:

https://github.com/user-attachments/assets/51394f0a-5277-4fe2-b81c-5c5e9ac876b5

The same steps, written out, are in the [README's Claude Cowork section](README.md#claude-cowork).

## Install in Claude Code

1. **Open Claude Code** in your terminal. (Using the **Claude Cowork** desktop app? Use the [Install in Claude Cowork](#install-in-claude-cowork) section above instead — these steps are terminal-only.) Not sure which you have? If you have a terminal window open with Claude in it, that's Claude Code.

2. **Download this repository.** On the repo's GitHub page, click the green **Code** button → **Download ZIP**, then unzip it. (If you use git, `git clone` works too — or skip the download: `/plugin marketplace add` also accepts the repo's GitHub URL.)

3. **Add the marketplace.** In Claude Code, type `/plugin marketplace add ` (with a space at the end), then **drag the unzipped `claude-for-legal` folder onto the terminal window** — it'll fill in the path. Then press Enter.

   (Or type the full path: `/plugin marketplace add /Users/you/Desktop/claude-for-legal`)

4. **Install your plugin.** Pick the one that matches your work from the table below, then:
   ```
   /plugin install privacy-legal@claude-for-legal
   ```

5. **⚠️ Restart Claude Code.** Close and reopen. This step is not optional — the plugin isn't live until you restart.

6. **Run setup.** Takes 2 minutes (quick start) or 10-15 minutes (full).
   ```
   /privacy-legal:cold-start-interview
   ```

7. **Connect a research tool.** Citations are flagged unverified without one. Four plugins ship a case-law research connector pre-configured — `legal-clinic`, `ip-legal`, `litigation-legal`, and `law-student` — and you'll be prompted to authorize it the first time a skill needs it. The other plugins ship productivity/workflow connectors only: add CourtListener or your firm's research tool yourself (in Cowork: Settings → Connectors; in Claude Code: `/mcp`).

## Install user-scoped, not project-scoped

When you run `/plugin install`, you may be asked whether to install for this project only or for all projects (user scope). **Pick user scope.**

Project scope means the plugin only loads when Claude Code runs inside that one project folder — to use it on your outlines in Downloads, your contract in Documents, or your client file in Dropbox, you would have to work from that folder every time. User scope makes the plugin available from any folder you work in. Neither scope changes what the plugin can access: Claude only reads files you explicitly point it at or that are in the current directory.

If you already installed project-scoped and want to switch: `/plugin uninstall <plugin>`, then `/plugin install <plugin>@claude-for-legal` from your home directory.

## Which plugin is for me?

(This table also lives in the [README](README.md#which-plugin-do-i-need).)

| You are a… | Install… | First command after setup |
|---|---|---|
| Privacy lawyer / DPO | `privacy-legal` | `/privacy-legal:use-case-triage` |
| Commercial / contracts lawyer | `commercial-legal` | `/commercial-legal:review` |
| Corporate / M&A lawyer | `corporate-legal` | `/corporate-legal:diligence-issue-extraction` |
| Employment lawyer / HR counsel | `employment-legal` | `/employment-legal:wage-hour-qa` |
| Product counsel | `product-legal` | `/product-legal:is-this-a-problem` |
| IP lawyer / patent agent | `ip-legal` | `/ip-legal:clearance` |
| Litigator (in-house or firm) | `litigation-legal` | `/litigation-legal:matter-intake` |
| Regulatory / compliance counsel | `regulatory-legal` | `/regulatory-legal:reg-feed-watcher` |
| AI governance lead | `ai-governance-legal` | `/ai-governance-legal:use-case-triage` |
| Clinic supervisor (law school) | `legal-clinic` | `/legal-clinic:client-intake` |
| Law student | `law-student` | `/law-student:socratic-drill` |
| Legal ops / looking for skills | `legal-builder-hub` | `/legal-builder-hub:registry-browser` |

## What you're installing

Each plugin learns your playbook through a setup interview, writes it to a practice profile file (`~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md`), and every skill reads from it. The profile is yours — edit it, re-run setup, or tell a skill to update it.

> **Known issue (Claude Cowork):** in Cowork that home path isn't writable, so setup saves your configuration to `claude-for-legal-config/` inside your working folder instead and notes the location in the folder's CLAUDE.md. Keep using the same working folder across sessions — your profile lives where the folder lives.

**Every output is a draft for attorney review.** The plugins flag what they're unsure about, mark citations by source, and gate anything irreversible. Claude drafts and flags; the professional acts stay yours — you configure, an attorney authorizes the positions, you verify the cites, you decide what matters, and only you sign, send, or file. They make that review faster; they don't replace it.

## What's in the box

12 practice-area plugins, 5 managed-agent cookbooks, 16+ connectors. The full reference is in [README.md](README.md).

## Stuck?

- **"Command not found"** after install → you forgot step 5. Restart Claude Code.
- **"Run setup first"** → run `/<plugin>:cold-start-interview` before any other command.
- **Citations flagged `[verify]`** → connect a research tool (step 7). Without one, every cite is from training data, not a current database. If your plugin doesn't ship a research connector (most don't — see step 7), you have to add one yourself.
- **"I can't read [file]"** → point the skill at the file's full path, or start Claude Code from the folder that contains the file. If the plugin's commands are missing entirely when you work from other folders, it's installed project-scoped — see "Install user-scoped, not project-scoped" above and reinstall user-scoped.
- **Setup ran but the configuration didn't save** (or skills keep saying "run setup first") → in Claude Cowork, setup saves to `claude-for-legal-config/` in your working folder, not your home directory. Open the same working folder you ran setup in and the profile will be found.
- **The plugin doesn't do X** → run `/legal-builder-hub:related-skills-surfacer` to find a better match, or check the plugin's README for "What this plugin does not do."
