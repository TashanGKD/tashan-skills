---
name: desktop-cache-cleanup
description: Use when cleaning macOS workspace disk caches, Docker build cache, package-manager caches, Feishu storage, or rerunning the user's weekly cache cleanup workflow on ~/Desktop/workspace.
---

# Desktop Cache Cleanup

## Core Rule

Always preview and measure before deleting. The user expects: pending cleanup items and risk notes first, execution second, before/after space accounting last.

## Workflow

1. Re-measure current state; do not rely on stale automation output.
2. Inspect dominant buckets first: Docker system/build cache, unused images, npm, pnpm, uv, pip, Homebrew, and Feishu storage.
3. Present the cleanup plan and risk notes before destructive deletion.
4. Run focused cleanup commands only for agreed safe buckets.
5. Re-measure and report reclaimed space by bucket plus `/System/Volumes/Data` free-space change.

## Useful Commands

```bash
docker system df -v
npm cache clean --force
pnpm store prune
uv cache prune
pip cache purge
brew cleanup -s
docker builder prune -af
docker image prune -af
```

Use `rm -rf` only for clearly identified cache directories such as `~/.npm`, `~/.cache/uv`, `~/Library/Caches/pnpm`, `~/Library/Caches/pip`, and `~/Library/Caches/Homebrew`.

## Feishu Rule

Scan and report Feishu app-support/container/crash paths, but do not blindly delete them. Prior runs found no large obviously safe Feishu cache tree.

## Common Failures

- If Docker access fails at the user socket, confirm Docker Desktop/API availability before claiming expected savings.
- If `rm -rf` returns `Operation not permitted`, report the blocked paths and continue with measurable safe buckets.
- If little space is reclaimed, check whether Docker build cache, not package caches, is still dominant.
