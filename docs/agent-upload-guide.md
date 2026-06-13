# Agent Upload Guide

This guide is for agents that upload Codex skills into this shared repository.

## Goal

Publish each contributor's skills under a personal owner directory:

```text
skills/<owner>/<skill-name>/
```

Use the contributor's stable GitHub handle or name pinyin as `<owner>`. Examples:

```text
skills/zeruifang/chinese-thesis-docx-workflow/
skills/alice/paper-review/
skills/bob/frontend-workflow/
```

Do not place skills directly under `skills/`.

## Standard Upload Flow

1. Clone with submodules.

```bash
git clone --recurse-submodules git@github.com:TashanGKD/tashan-skills.git
cd tashan-skills
```

2. Sync local skills into the contributor's owner directory.

```bash
python3 scripts/sync_local_skills.py --owner <owner> --source ~/.codex/skills
```

3. Validate the repository.

```bash
python3 scripts/validate_skills.py
```

Validation also checks that `catalog/skills.json` matches the current skill files. If validation says the catalog is out of date, rerun the sync command or `scripts/organize_skills.py`.

4. Review the diff.

```bash
git status --short
git diff --stat
```

5. Commit and push.

```bash
git add .
git commit -m "fix(skills): publish <owner> skills"
git push
```

## Manual Skill Additions

If a skill is not in `~/.codex/skills`, copy it manually into:

```text
skills/<owner>/<skill-name>/
```

Then run:

```bash
python3 scripts/organize_skills.py --owner <owner>
python3 scripts/validate_skills.py
```

The skill directory must contain `SKILL.md`. Its frontmatter must include:

```yaml
---
name: skill-name
description: Clear trigger and usage description with enough detail.
---
```

The folder name must match `name:`.

## Submodules

Use a git submodule when a skill is maintained as an independent repository, has a large toolchain, or should keep its own release history.

```bash
git submodule add <repo-url> skills/<owner>/<skill-name>
git submodule update --init --recursive
python3 scripts/validate_skills.py
```

When updating a submodule skill, update the upstream repository first, then commit only the pointer change in this repository.

## Security Rules

Before committing, make sure the diff does not contain:

- API keys, JWTs, OAuth tokens, private keys, cookies, passwords.
- `.env`, `config.json`, `.pem`, `.key`, `.p12`, browser state, meeting/email caches.
- `node_modules`, `.git`, `__pycache__`, `.DS_Store`, temporary files, backup folders.
- Absolute private paths that are not needed by the skill.

Use environment variables in scripts:

```python
api_key = os.environ.get("OPENAI_API_KEY")
```

## Quality Rules

- Keep `SKILL.md` concise and action-oriented.
- Put long explanations in `references/`.
- Put reusable commands in `scripts/`.
- Keep examples free of private user data.
- Document any external dependency or token requirement.
- Prefer portable paths and environment variables over machine-specific paths.

## Validation Expectations

`scripts/validate_skills.py` enforces:

- `skills/<owner>/<skill-name>/SKILL.md` structure.
- lowercase owner and skill folder names.
- `name:` matching the skill folder name.
- non-trivial descriptions.
- no duplicate skill names inside the same owner directory.
- basic sensitive-token scanning.
- generated catalog consistency.

Different owners may publish skills with the same `name:`, but agents should avoid needless duplication when a shared skill can be improved instead.

## Failure Recovery

If CI fails with a missing `SKILL.md` under a submodule path, ensure the workflow checkout uses:

```yaml
- uses: actions/checkout@v4
  with:
    submodules: recursive
```

If CI fails because a skill is directly under `skills/`, run:

```bash
python3 scripts/organize_skills.py --owner <owner>
python3 scripts/validate_skills.py
```
