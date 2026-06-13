# Tashan Skills

Shared Codex skills used by the TashanGKD workspace.

## Repository Layout

```text
skills/                  # Installable skill folders
catalog/skills.json      # Generated skill catalog
scripts/sync_local_skills.py
scripts/validate_skills.py
```

Each skill must contain a `SKILL.md` file with valid frontmatter:

```yaml
---
name: skill-name
description: What the skill does and when to use it.
---
```

## Install

Clone this repository with submodules, then copy the desired skill folders into your Codex skills directory:

```bash
git clone --recurse-submodules git@github.com:TashanGKD/tashan-skills.git
```

If you already cloned it:

```bash
git submodule update --init --recursive
```

```bash
mkdir -p ~/.codex/skills
cp -R skills/<skill-name> ~/.codex/skills/
```

To install all published skills:

```bash
cp -R skills/* ~/.codex/skills/
```

## Validate

```bash
python3 scripts/validate_skills.py
```

## Sync From A Local Codex Skills Directory

For maintainers:

```bash
python3 scripts/sync_local_skills.py --source ~/.codex/skills --target skills --catalog catalog/skills.json
python3 scripts/validate_skills.py
```

The sync script excludes local caches, nested git repos, `node_modules`, private config files, and known backup/system folders. It also redacts obvious hard-coded API keys and tokens.

`skills/pre-pp` is maintained as a git submodule because it is an independent, larger workflow project.

## Contribution Model

See [CONTRIBUTING.md](CONTRIBUTING.md).
