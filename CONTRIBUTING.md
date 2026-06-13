# Contributing Skills

## Add Or Update A Skill

1. Put one skill under `skills/<skill-name>/`.
2. Ensure `skills/<skill-name>/SKILL.md` exists.
3. Keep the skill self-contained:
   - `SKILL.md` for core routing and workflow.
   - `references/` for longer guidance.
   - `scripts/` for reusable automation.
   - `assets/` only for small reusable assets.
4. Run:

```bash
python3 scripts/validate_skills.py
```

## Submodule Skills

Use a submodule for a skill that is already maintained as an independent repository or has its own release cycle/toolchain. Current example:

```text
skills/pre-pp -> https://github.com/MiraclePlus/pre-pp.git
```

When changing a submodule skill, contribute to the upstream repository first, then update the submodule pointer here.

## Naming Rules

- Use lowercase letters, digits, and hyphens only.
- The folder name must match `name:` in `SKILL.md`.
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
