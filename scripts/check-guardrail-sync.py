#!/usr/bin/env python3
# Copyright 2026 Anthropic PBC
# SPDX-License-Identifier: Apache-2.0
"""Check the shared guardrail blocks in the 12 plugin CLAUDE.md templates for drift.

Every practice-profile template (`<plugin>/CLAUDE.md`) carries its own copy of
the shared guardrail blocks (reviewer note, source tags, destination check, ...).
Copies must be identical across plugins except for the plugin slug and the
documented per-plugin variants and absences. Mechanism — majority vote, no
canonical text embedded here:

  1. A block starts at the line beginning with its marker (a `## ` heading or a
     `**Bold lead.**`) and ends at the next known block start, `## ` heading,
     `---` rule, documented plugin-specific boundary, or end of file. Blocks in
     END_AFTER close on their known final line instead, because per-plugin
     content follows them with no structural separator.
  2. Copies are normalized: trailing whitespace stripped; the plugin's slug
     becomes `{PLUGIN}` in config paths and `/<plugin>:` commands only —
     sibling-plugin mentions in shared prose are intentionally literal.
  3. Every copy must byte-match the majority text across non-variant copies.
     ABSENT_OK pairs may be missing; VARIANT_OK pairs are checked for presence
     of the start marker only. (Requiring a verbatim canonical sentence inside
     variants was rejected: documented variants rewrite even the shared rule
     sentences — e.g. legal-builder-hub's reframed decision posture — so no
     canonical sentence survives in every legitimate variant.)

Exit 0 with a per-block summary when clean; exit 1 listing every drift or
undocumented absence, with a unified diff (first 10 changed lines) against the
majority text. `--list` prints the block inventory and exemption tables.
"""
from __future__ import annotations

import argparse
import difflib
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PLUGINS = [
    "ai-governance-legal", "commercial-legal", "corporate-legal",
    "employment-legal", "ip-legal", "law-student", "legal-builder-hub",
    "legal-clinic", "litigation-legal", "privacy-legal", "product-legal",
    "regulatory-legal",
]

# (name, start_marker) — start_marker is the exact text the block's first line
# starts with. Order follows the blocks' order in the templates.
BLOCKS = [
    ("header-jurisdiction-note", "**The header's protection is jurisdiction-specific.**"),
    ("reviewer-note", "**⚠️ Reviewer note — one block above the deliverable.**"),
    ("deliverable-clean", "**The deliverable below is clean.**"),
    ("quiet-mode", "**Quiet mode for client-facing and board-facing deliverables.**"),
    ("next-steps-decision-tree", "**Next steps decision tree.**"),
    ("additional-consideration", "**Additional consideration before the options.**"),
    ("decision-tree-followthrough", "Customize the options to the skill and the finding."),
    ("dashboard-offer", "**Dashboard offer for data-heavy outputs.**"),
    ("dashboard-input-escaping", "**Dashboard outputs escape untrusted input.**"),
    ("decision-posture", "## Decision posture on subjective legal calls"),
    ("shared-guardrails-intro", "## Shared guardrails"),
    ("no-silent-supplement", "**No silent supplement — three values, not two.**"),
    ("currency-trigger", "**Currency trigger.**"),
    ("verify-user-stated-facts", "**Verify user-stated legal facts before building on them.**"),
    ("disagree-with-cited-statute", "**When disagreeing with a cited statute, quote the text or decline to characterize it.**"),
    ("preflight-research-connector", "**Pre-flight check before any skill that cites authority.**"),
    ("source-tags", "**Source tags are derived from what you actually did, not what you'd like to claim.**"),
    ("tag-vocabulary", "**Tag vocabulary — at a glance.**"),
    ("destination-check", "**Destination check.**"),
    ("cross-skill-severity-floor", "**Cross-skill severity floor.**"),
    ("file-access-failures", "**File access failures.**"),
    ("verification-log", "**Verification log.**"),
    ("scaffolding-not-blinders", "## Scaffolding, not blinders"),
    ("wrong-skill-routing", "**Don't force a question through the wrong skill.**"),
    ("ad-hoc-questions", "## Ad-hoc questions in this domain"),
    ("proportionality", "## Proportionality"),
    ("jurisdiction-recognition", "## Jurisdiction recognition"),
    ("retrieved-content-trust", "## Retrieved-content trust"),
    ("handling-retrieved-results", "## Handling retrieved results"),
    ("large-input", "## Large input"),
    ("large-output", "## Large output"),
]

# Plugin-specific blocks that sit directly after (or inside) a shared block's
# span. They end the preceding shared block but are not themselves checked —
# they are documented per-plugin content, not copies of a shared block.
EXTRA_BOUNDARIES = (
    "**Patent agent scope note.**",                       # ip-legal, after header-jurisdiction-note
    "**Dual severity.**",                                 # commercial-legal, after cross-skill-severity-floor
    "**Source hierarchy.**",                              # ai-governance/regulatory, inside Handling retrieved results
    "**When disagreeing with a user's cited statute,",    # corporate-legal's own deal-flavored rule
    "**Source tags describe what you actually did,",      # employment-legal's condensed source-tags
    "**Verbatim quotes from the record must be verbatim.**",   # litigation-legal, after verification-log
    "**Pinpoint cites must support the whole proposition.**",  # litigation-legal
    "**Before the options, one question.**",  # superseded lead of additional-consideration; bounds the
                                              # decision-tree block in templates not yet carrying the rename
)

# Blocks that close on a known final line instead of a following boundary:
# the per-plugin header-removal line (and, in some plugins, a Non-lawyer
# output mode block) follows with no structural separator and is documented
# per-plugin content, not part of the shared block.
END_AFTER = {
    "header-jurisdiction-note": "A false assurance of protection is worse than no marking.",
}

# (block, plugin) pairs where the block is intentionally absent.
ABSENT_OK = {
    ("header-jurisdiction-note", "law-student"),
    ("header-jurisdiction-note", "legal-builder-hub"),
    ("header-jurisdiction-note", "legal-clinic"),
    ("reviewer-note", "legal-builder-hub"),
    ("deliverable-clean", "legal-builder-hub"),
    ("disagree-with-cited-statute", "corporate-legal"),   # carries its own deal-flavored version instead
    ("preflight-research-connector", "law-student"),      # has a study-adapted version under "Citations unverified"
    ("preflight-research-connector", "legal-builder-hub"),
    ("source-tags", "employment-legal"),                  # condensed inline variant instead
    ("source-tags", "law-student"),                       # [settled] folded into its Tag vocabulary
    ("source-tags", "legal-builder-hub"),                 # [settled] folded into its Tag vocabulary
}

# (block, plugin) pairs whose copy legitimately differs from the majority.
VARIANT_OK = {
    ("deliverable-clean", "law-student"),             # appended casebook note (plugin's own adaptation)
    ("quiet-mode", "law-student"),                    # law-student: re-domained for academic context per attorney review (no work-product header to keep)
    ("next-steps-decision-tree", "law-student"),      # law-student: re-domained for academic context per attorney review (study artifacts, professor/TA escalation)
    ("decision-tree-followthrough", "law-student"),   # law-student: re-domained for academic context per attorney review (study-skill examples)
    ("dashboard-offer", "law-student"),               # law-student: re-domained for academic context per attorney review (study-data examples)
    ("destination-check", "law-student"),             # law-student: re-domained for academic context per attorney review (academic-integrity exposure, not privilege waiver)
    ("ad-hoc-questions", "law-student"),              # law-student: re-domained for academic context per attorney review (courses/exam calendar, study-partner framing)
    ("decision-posture", "ai-governance-legal"),      # domain-specific example list in the opening clause
    ("decision-posture", "law-student"),              # student-adapted example list and reviewer
    ("decision-posture", "legal-clinic"),             # clinic example list; supervising attorney narrows the list
    ("decision-posture", "legal-builder-hub"),        # reframed: hub QA-checks installed skills for this posture
    ("preflight-research-connector", "employment-legal"),  # narrower research-tool list (CourtListener, statute source)
    ("preflight-research-connector", "legal-clinic"),      # appends a sentence naming the clinic's own skills
    ("source-tags", "ip-legal"),                      # adds [USPTO] to the MCP-provenance bullet
    ("source-tags", "product-legal"),                 # adds a [platform policy] bullet + no-[settled] note
    ("source-tags", "legal-clinic"),                  # supervisor-upload parenthetical + trailing clinic sentence
    ("tag-vocabulary", "employment-legal"),           # CourtListener-only provenance tag list
    ("tag-vocabulary", "law-student"),                # student-adapted [review], reduced tags, [settled] folded in
    ("tag-vocabulary", "legal-builder-hub"),          # QA-criteria framing, [settled] folded in
    ("verification-log", "law-student"),              # shorter ending — no matter-workspace clause
    ("verification-log", "legal-clinic"),             # shorter ending — no matter-workspace clause
}

_MARKERS = tuple(m for _, m in BLOCKS)
_ALL_BOUNDARIES = _MARKERS + EXTRA_BOUNDARIES


def _is_boundary(line: str) -> bool:
    return line.startswith("## ") or line.strip() == "---" or line.startswith(_ALL_BOUNDARIES)


def _normalize(lines: list[str], plugin: str) -> str:
    text = "\n".join(line.rstrip() for line in lines).strip("\n")
    # Slug -> {PLUGIN} only in config paths and slash commands; literal
    # sibling-plugin mentions in shared prose must survive as-is.
    text = text.replace(f"claude-for-legal/{plugin}/", "claude-for-legal/{PLUGIN}/")
    return text.replace(f"/{plugin}:", "/{PLUGIN}:")


def _extract(plugin: str) -> tuple[dict[str, str], list[str]]:
    """Return {block name: normalized text} plus a list of duplicated blocks."""
    lines = (ROOT / plugin / "CLAUDE.md").read_text(encoding="utf-8").splitlines()
    found: dict[str, int] = {}
    dupes: list[str] = []
    for i, line in enumerate(lines):
        for name, marker in BLOCKS:
            if line.startswith(marker):
                if name in found:
                    dupes.append(name)
                else:
                    found[name] = i
                break
    blocks: dict[str, str] = {}
    for name, start in found.items():
        last_line = END_AFTER.get(name)
        end = start + 1
        while end < len(lines) and not _is_boundary(lines[end]):
            end += 1
            if last_line and lines[end - 1].startswith(last_line):
                break
        blocks[name] = _normalize(lines[start:end], plugin)
    return blocks, dupes


def _print_diff(majority: str, actual: str, label: str) -> None:
    shown = 0
    for d in difflib.unified_diff(majority.splitlines(), actual.splitlines(),
                                  "majority", label, lineterm="", n=1):
        print(f"      {d}", file=sys.stderr)
        if d[:1] in "+-" and not d.startswith(("+++", "---")):
            shown += 1
            if shown >= 10:
                print("      … (diff truncated at 10 changed lines)", file=sys.stderr)
                return


def _list_inventory() -> None:
    print(f"Blocks ({len(BLOCKS)}):")
    for name, marker in BLOCKS:
        print(f"  {name:30s} {marker}")
    for title, table in (("Absence exemptions", ABSENT_OK), ("Variant exemptions", VARIANT_OK)):
        print(f"\n{title} ({len(table)} pairs):")
        for name, _ in BLOCKS:
            plugins = sorted(p for b, p in table if b == name)
            if plugins:
                print(f"  {name:30s} {', '.join(plugins)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check guardrail-block sync across plugin CLAUDE.md templates.")
    parser.add_argument("--list", action="store_true", help="print the block inventory and exemptions, then exit")
    args = parser.parse_args()
    if args.list:
        _list_inventory()
        return 0

    missing_templates = [p for p in PLUGINS if not (ROOT / p / "CLAUDE.md").is_file()]
    if missing_templates:
        print(f"missing templates: {', '.join(missing_templates)}", file=sys.stderr)
        return 2

    copies: dict[str, dict[str, str]] = {}
    problems: list[tuple[str, str, str | None]] = []  # (message, plugin, diff-vs-majority or None)
    for plugin in PLUGINS:
        copies[plugin], dupes = _extract(plugin)
        for name in dupes:
            problems.append((f"{name} [{plugin}]: block start marker appears more than once", plugin, None))

    summary: list[str] = []
    for name, _ in BLOCKS:
        majority_pool = [copies[p][name] for p in PLUGINS
                         if name in copies[p] and (name, p) not in VARIANT_OK]
        majority = Counter(majority_pool).most_common(1)[0][0] if majority_pool else None
        in_sync = variant_ok = absent_ok = 0
        for plugin in PLUGINS:
            text = copies[plugin].get(name)
            if text is None:
                if (name, plugin) in ABSENT_OK:
                    absent_ok += 1
                else:
                    problems.append((f"{name} [{plugin}]: block missing and absence not documented", plugin, None))
            elif (name, plugin) in VARIANT_OK:
                variant_ok += 1  # documented variant — presence of the start marker is the check
            elif majority is not None and text != majority:
                agree = majority_pool.count(majority)
                problems.append((
                    f"{name} [{plugin}]: drifts from majority text ({agree}/{len(majority_pool)} copies agree)",
                    plugin, f"{majority}\x00{text}"))
            else:
                in_sync += 1
        detail = f"{in_sync} in sync"
        if variant_ok:
            detail += f", {variant_ok} variant-ok"
        if absent_ok:
            detail += f", {absent_ok} absent-ok"
        summary.append(f"  ✓ {name:30s} {detail}")

    if problems:
        print("guardrail-sync check FAILED:", file=sys.stderr)
        for message, plugin, payload in problems:
            print(f"  {message}", file=sys.stderr)
            if payload:
                majority, actual = payload.split("\x00")
                _print_diff(majority, actual, f"{plugin}/CLAUDE.md")
        return 1
    print("\n".join(summary))
    print(f"guardrail sync clean: {len(BLOCKS)} blocks across {len(PLUGINS)} templates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
