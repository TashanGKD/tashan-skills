---
name: chinese-thesis-docx-workflow
description: Use when working on Chinese thesis, proposal, opening-report, dissertation, academic-review, or Word DOCX workflows that require structured academic writing, iterative versioned editing, citation renumbering, reference cleanup, figure/table captions, technical-route diagrams, defense-review records, supervisor/group comments, or formatting/logic cleanup. Especially use for `.docx` files, Chinese graduate reports, 开题报告, 学位论文, 考核记录, 导师意见, 小组意见, and bibliography/order normalization.
---

# Chinese Thesis DOCX Workflow

Use this skill to revise Chinese academic DOCX artifacts end to end while preserving version history, citation integrity, and formal report style.

## Quick Workflow

1. Identify the real latest DOCX.
   - Prefer `docx_versions/VERSION_INDEX.md` when present, but verify actual file hashes and modification times.
   - If the user manually edited a previous version, treat that actual file as the source of truth and update the index hash.
2. Create a new version before editing.
   - Use `vNNN_开题报告_<short-summary>.docx` or the existing local naming pattern.
   - Never overwrite the user's current version.
3. Inspect structure before changing text.
   - Use `scripts/extract_docx_text.py` to locate paragraphs, headings, drawings, captions, tables, and references.
4. Make scoped edits.
   - Match the user's latest request, local document structure, and prior style.
   - Keep changes close to the requested sections unless asked to globally normalize.
5. Validate.
   - DOCX zip integrity.
   - Paragraph placement around figures/headings.
   - Citation first-appearance order and bibliography continuity.
   - Version index hash match.
6. Report exact outputs.
   - Link the new DOCX and state what changed.
   - Mention any validation not possible, such as broken LibreOffice rendering.

## Scenario Router

- **Opening report or thesis writing**: Read `references/writing-and-structure.md`.
- **DOCX version management**: Read `references/versioning.md`.
- **Citation, bibliography cleanup, and literature lookup**: Use AMiner skills when collecting or matching papers, then run `scripts/renumber_docx_citations.py`; read `references/citations.md`.
- **Figures, captions, and technical-route diagrams**: Read `references/figures.md`.
- **Review questions, supervisor comments, group opinions, and summaries**: Read `references/review-records.md`.
- **Chinese academic style and expression cleanup**: Read `references/expression.md`.
- **Comparing versions or locating edits**: Use `scripts/compare_docx_text.py` and `scripts/extract_docx_text.py`.

## Hard Rules

- Preserve user edits. If a version's hash differs from the index, assume the user changed it and work from the actual file.
- Create a new DOCX version for each meaningful edit.
- Update `VERSION_INDEX.md` after creating a new DOCX version.
- Do not leave placeholder captions such as `图 2` without a descriptive title.
- Avoid duplicated figure/table numbers. If a figure is moved earlier, renumber later figure references and captions.
- Normalize citations by first appearance when citations move or new citation contexts are added.
- When adding new references, prefer AMiner-driven paper search/matching for academic sources before inserting citations.
- Compress continuous citation runs of length 3 or more with a hyphen, for example `[1-5]`; keep noncontinuous groups as `[1,3,5]`.
- Remove uncited references only when requested, and then verify every remaining bibliography item is cited.
- Prefer exact, scoped academic wording over broad promotional claims.
- Avoid the contrast pattern `不是……而是……` and variants such as `不只/不能只/不应只` when the user has requested this style constraint.
- For a first occurrence of a technical English term, use Chinese plus English/full abbreviation form when appropriate: `人工智能（artificial intelligence, AI）`.

## Useful Scripts

```bash
# Extract paragraphs, styles, drawings, captions, and references.
python3 ~/.codex/skills/chinese-thesis-docx-workflow/scripts/extract_docx_text.py path/to/file.docx --start 100 --end 130

# Compare body text between two versions.
python3 ~/.codex/skills/chinese-thesis-docx-workflow/scripts/compare_docx_text.py old.docx new.docx

# Renumber bracket citations and bibliography by first appearance.
python3 ~/.codex/skills/chinese-thesis-docx-workflow/scripts/renumber_docx_citations.py input.docx --output output.docx

# Check VERSION_INDEX.md hashes against actual DOCX files.
python3 ~/.codex/skills/chinese-thesis-docx-workflow/scripts/check_version_index.py docx_versions
```

## Validation Checklist

- `zipfile.ZipFile(docx).testzip()` returns `ok`.
- `extract_docx_text.py` confirms new text is in the intended section.
- Figures and captions are adjacent and numbered in reading order.
- `renumber_docx_citations.py --check-only` reports body first-order and reference sequence OK.
- `check_version_index.py` reports current latest and hashes match.
- If visual layout matters, render with LibreOffice/Poppler when available; otherwise state that visual rendering was unavailable.
