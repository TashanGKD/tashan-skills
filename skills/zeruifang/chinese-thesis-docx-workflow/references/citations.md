# Citation And Bibliography Rules

Use this when editing citations, references, figure source citations, or bibliography numbering.

## Literature Lookup With AMiner

Use AMiner when the task needs new references, citation matching, or claim-to-paper alignment:

- Use `aminer-deep-search` for multi-round collection around a research direction or survey section.
- Use `aminer-daily-paper` only for recommendation-style paper discovery.
- Use `aminer-pdf-citation-verifier` when a PDF/paper text is provided and the task is to verify whether references actually support claims.

AMiner should support the academic matching step, but do not let it replace document-level citation hygiene:

1. Match a paper to a concrete sentence or paragraph claim.
2. Insert the citation near the specific claim, not as a broad paragraph-end bundle.
3. Add the bibliography item in a consistent style.
4. Run whole-document citation renumbering by first appearance.
5. Verify no uncited or missing references remain.

## Body Citation Format

- Single citation: `[1]`
- Multiple noncontinuous citations: `[1,3,5]`
- Continuous runs of length 3 or more: `[1-5]`
- Keep pairs as `[1,2]` unless the local document already compresses pairs.

## Order Rule

References must be numbered by first citation appearance in the body, not by bibliography insertion order.

When moving a citation earlier, run a whole-document renumbering pass. A local edit such as adding `[71-74]` in chapter 1 will otherwise cause jumps.

## Bibliography Cleanup

- Only remove uncited references when requested.
- After removing or renumbering, verify:
  - every body citation resolves to a bibliography item;
  - every bibliography item is cited in the body;
  - body first-appearance order is `[1], [2], ...`;
  - the bibliography sequence is continuous.

## Figure Source Citations

If a caption cites a source, treat that caption as a citation context. If the figure moves earlier, that source may need an earlier reference number.

## Script

Use:

```bash
python3 ~/.codex/skills/chinese-thesis-docx-workflow/scripts/renumber_docx_citations.py input.docx --output output.docx
```

For validation only:

```bash
python3 ~/.codex/skills/chinese-thesis-docx-workflow/scripts/renumber_docx_citations.py input.docx --check-only
```
