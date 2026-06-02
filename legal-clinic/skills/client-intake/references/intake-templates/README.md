# Practice-Area Intake Templates

Cold-start populates these from the professor's intake form(s), writing them to
`~/.claude/plugins/config/claude-for-legal/legal-clinic/intake-templates/` — the
version-independent config path, so they survive plugin updates. If none provided,
`/client-intake` uses the default question sets in `client-intake/SKILL.md` Step 2.

One file per practice area the clinic handles:

- `immigration.md` — status, entry, prior applications, country conditions, family, criminal history, timeline
- `housing.md` — housing type, what happened, lease/payment, habitability, timeline
- `family.md` — relationship, children, safety, existing orders, timeline
- `consumer.md` — debt type, who's contacting, documentation, filed against, timeline

Each template: the questions to ask, in the order to ask them, with notes on
sensitive handling (e.g., criminal history in immigration — explain why asking).
