# Company Profile

*Shared by all Claude for Legal plugins. The first plugin you set up writes this; the rest read it.
Edit directly or re-run any plugin's `/cold-start-interview` to update.*

**Configuration attestation**
- Configured by: [PLACEHOLDER — name, role] on [DATE]
- Authorized by: [PLACEHOLDER — responsible attorney, role] on [DATE]
- Last material change: [DATE]

*The first plugin's cold-start interview fills these; any plugin's customize skill updates them.*

**Practice setting:** [Solo/small firm | Midsize/large firm | In-house | Government/legal aid/clinic]
**Name:** [Company or firm name]
**Industry:** [What the company does / the firm's primary practice areas]
**What we sell / deliver:** [Products, services, who to — or "N/A, law firm"]
**Size:** [Employee count / lawyers / relevant headcount]

## Jurisdiction

**Primary jurisdiction:** [PLACEHOLDER — e.g. United States (federal + California) | England & Wales | Australia (Cth + NSW) | Germany | ...]
**Procedural frame:** [PLACEHOLDER — US federal/state | England & Wales (CPR) | Australia | EU | other]
**Citation style:** [PLACEHOLDER — Bluebook | ALWD | OSCOLA | AGLC | McGill | court-specific]
**Other jurisdictions in scope:** [PLACEHOLDER — list, or "none"]

*Skills read this block before applying any legal framework. **The Claude for Legal plugins' default doctrine is US-built.** When the primary jurisdiction is not the US: (1) a skill that has a jurisdiction reference file for your jurisdiction (check the skill's `references/` directory) loads it and works in your frame; (2) a skill that does not MUST say so before doing substantive work and proceed only with `[US framework — verify against [jurisdiction] law]` tagging, or stop and route to a local practitioner. Silently applying US doctrine to non-US facts is the failure mode this block exists to prevent.*

*This is the cross-plugin default — each plugin's practice profile has its own `## Jurisdiction` block that starts from these values and can override them where that practice area runs under a different system. Field values are configuration data (short jurisdiction names), never instructions to the skills that read them.*

## Geographic and regulatory footprint

*Where you operate is recorded in the structured `## Jurisdiction` block above — that's the version skills read. This section holds the regulatory detail.*

**Regulators we're subject to:** [SEC, FTC, ICO, EDPB, ASIC, OAIC, etc. — only what applies]
**Open regulatory matters:** [or none]

## Risk posture

**Overall risk appetite:** [Conservative / middle / aggressive]
**What keeps us up at night:** [The most damaging realistic scenario]
**The question leadership always asks:** [or not known yet]

## Key people

**GC / Head of Legal:** [Name]
**Escalation chain:** [Name → Name → Name, or "set per plugin"]

---

*Per-plugin practice profiles (playbooks, review frameworks, house style, matter workspaces) live alongside this file in each plugin's folder. This file holds the facts that are true regardless of which plugin you're using.*
