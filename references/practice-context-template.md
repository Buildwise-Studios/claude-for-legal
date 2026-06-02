# Practice Context — cross-plugin work index

*Shared by all Claude for Legal plugins. Lives at `~/.claude/plugins/config/claude-for-legal/practice-context.md`, next to `company-profile.md` (or the working-folder fallback `./claude-for-legal-config/practice-context.md`). The skills that produce cross-relevant work products create it from this template on first write.*

*Append-only. One line per completed assessment/review that other practice areas may need to know about. Written by the skills that produce these artifacts; read by overlapping skills as a "check prior work" step. This is an INDEX (pointers), not a copy of the work product — the documents themselves stay where their plugin wrote them.*

*Matter-workspace rule: when matter workspaces are enabled, this index records only practice-level (non-matter) work. Matter-scoped work stays inside the matter folder and is never indexed here — cross-matter visibility would breach matter isolation.*

*Multi-client rule: If the practice profile is a multi-client practice (private practice — solo, small firm, or large firm) and matter workspaces are not enabled, skip the index entirely (reading and writing) — without workspace isolation, practice-level entries would let one client's assessments inform another client's work.*

*Confidentiality rules:*

- *The index is practice-level work-product — same confidentiality as the practice profiles. One line per artifact, status-only outcome, no substantive findings (the index travels in backups and syncs more readily than the documents it points to).*
- *The `Outcome` cell takes exactly one value from a closed set — `completed`, `draft`, `superseded`, or `withdrawn` — status only, never findings, conclusions, or risk ratings.*
- *Never index matter-scoped work (see the matter-workspace rule above).*
- *Never record client names in multi-client (firm) practices — use matter numbers or generic descriptors.*

| Date | Plugin | Skill | Subject | Outcome | Where the full document lives |
|---|---|---|---|---|---|
| [YYYY-MM-DD] | privacy-legal | pia-generation | [product/system name] | [completed / draft / superseded / withdrawn] | [path or DMS link] |
