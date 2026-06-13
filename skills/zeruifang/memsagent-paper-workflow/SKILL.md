---
name: memsagent-paper-workflow
description: Use when drafting, editing, or compiling the MEMSAgent IEEE Sensors Journal manuscript, bilingual article.md content, paper/main.tex, references.bib, Related Work structure, or Tectonic build workflow.
---

# MEMSAgent Paper Workflow

## Core Rule

Treat `article.md` as the bilingual drafting source and `~/Documents/MEMSAgent/paper/` as the writable TeX manuscript area. Do not edit the original Sensors template as the main source.

## Workflow

1. Confirm the current source files in `~/Documents/MEMSAgent`.
2. Preserve the bilingual drafting pattern in `article.md`: English paragraph followed by Chinese translation. Keep references managed separately.
3. Move requested paper content into `paper/main.tex`; use `paper/references.bib` for BibTeX and cite via `\\bibliography{references}`.
4. Keep the abstract citation-free and roughly 150-250 words unless the user asks otherwise.
5. Preserve the validated Related Work boundaries. If the user asks to replace subsection C and add D, do not merge the two sections.
6. Compile from the `paper/` directory after edits.

## Known Local Defaults

- Stable title: `MEMS Agent: Simulation-Aware Topology Exploration for MEMS Design`.
- Durable manuscript source: `paper/main.tex`.
- BibTeX file: `paper/references.bib`.
- Valid Related Work structure: A. MEMS topology optimization, B. data-driven MEMS design, C. LLM-based design agents and agentic AI, D. agentic reinforcement learning for structural and MEMS design.

## Build Command

```bash
mkdir -p build
~/.codex/plugins/cache/openai-bundled/latex-tectonic/0.1.0/bin/tectonic --outdir build main.tex
```

Run it from `~/Documents/MEMSAgent/paper/`.

## Common Failures

- If Tectonic fails before PDF output, confirm `build/` exists and the local `paper/ieeecolor.cls` is the patched class copy.
- If bulk citation renumbering touches the final References list incorrectly, rewrite the end-of-file references directly and verify citation distribution.
- If case details are not fixed, keep placeholders such as `[case A]` rather than freezing benchmarks prematurely.
