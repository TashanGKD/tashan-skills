# DOCX Versioning

Use this when a workspace contains `docx_versions/` or the user asks for version management.

## Directory Pattern

- Store every edited DOCX under `docx_versions/`.
- Keep lock files such as `.~*.docx` out of version history.
- Name files as `vNNN_开题报告_<change-summary>.docx` unless the project already uses another naming pattern.
- Update `VERSION_INDEX.md` after each new version.

## Source Of Truth

1. Read `VERSION_INDEX.md`.
2. Compare the indexed hash with the actual file hash.
3. If the hash differs, assume the user manually edited/saved that version.
4. Copy the actual file into the next version.
5. Update the old version's hash in the index before or alongside the new entry.

## Version Index Entry

Use one concise English description row:

```markdown
| v028 | `v028_开题报告_同步技术路线图表述.docx` | Synchronized section 4.1 wording with the revised technical route figure descriptions while preserving the user-added figure. | `<sha256>` |
```

Also update:

```markdown
## Current Latest

- `v028_...docx`
```

## Common Pitfalls

- Do not use the index hash blindly after the user edits a DOCX in WPS/Word.
- Do not create `v026` after a user already created or modified `v026`; find the next unused version.
- Do not overwrite root working files unless explicitly requested.
