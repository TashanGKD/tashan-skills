# Contributing Skills

## Add Or Update A Skill

1. Put your skills under `skills/<owner>/<skill-name>/`.
2. Use a stable owner directory such as your GitHub handle or real-name pinyin, for example `skills/zeruifang/`.
3. Ensure `skills/<owner>/<skill-name>/SKILL.md` exists.
3. Keep the skill self-contained:
   - `SKILL.md` for core routing and workflow.
   - `references/` for longer guidance.
   - `scripts/` for reusable automation.
   - `assets/` only for small reusable assets.
4. Rebuild the catalog and validate:

```bash
python3 scripts/sync_local_skills.py --owner <owner> --source ~/.codex/skills
python3 scripts/validate_skills.py
```

## Submodule Skills

Use a submodule for a skill that is already maintained as an independent repository or has its own release cycle/toolchain. Current example:

```text
skills/zeruifang/pre-pp -> https://github.com/MiraclePlus/pre-pp.git
```

When changing a submodule skill, contribute to the upstream repository first, then update the submodule pointer here.

## Naming Rules

- Owner and skill directory names must use lowercase letters, digits, and hyphens only.
- Each skill folder name must match `name:` in `SKILL.md`.
- Skill names may repeat across different owner directories, but avoid unnecessary duplication.
- Do not include backup folders such as `*.backup.*`.

## Security Rules

Never commit:

- API keys, JWTs, OAuth tokens, private keys, cookies, or passwords.
- Local `config.json`, `.env`, `.pem`, `.key`, `.p12`, or credential files.
- Personal meeting/email cache, browser state, or private workspace dumps.
- `node_modules`, `.git`, `__pycache__`, `.DS_Store`, or generated caches.

Use environment variables in scripts and docs, for example:

```python
api_key = os.environ.get("OPENAI_API_KEY")
```

## Review Checklist

- Is the skill useful outside the original author's machine?
- Does the description clearly say when the skill should trigger?
- Are detailed examples moved to `references/` instead of bloating `SKILL.md`?
- Are scripts executable and documented in `SKILL.md`?
- Are all references to private local paths removed or generalized?
- Is the skill placed under the contributor's own `skills/<owner>/` directory?
