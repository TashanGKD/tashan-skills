---
name: xhs-tech-publishing
description: Use when preparing Chinese technical Xiaohongshu posts, image-text notes, 3:4 infographics, topic subdirectories, Creator-platform drafts, or AI hardware explainer content under ~/Documents/xhs.
---

# XHS Tech Publishing

## Core Rule

Treat every topic as a publishable package, not a loose chat summary. The local artifact should help produce both post copy and images.

## Workflow

1. Confirm the topic directory under `~/Documents/xhs`. If the topic is new, create a focused subdirectory rather than mixing it into a broad folder.
2. Build or update the package files: `README.md`, `research-summary.md`, `post-draft.md`, `image-prompt.md`, and `source-index.md`.
3. Narrow the post to one mechanism chain before polishing. For Cerebras/WSE topics, prefer a concrete line such as defect map -> spare PE -> Fabric bypass -> compile-time placement/routing -> simulation metrics.
4. Fact-check technical claims before platform upload. Use primary sources when available; otherwise mark claims as uncertain or soften them.
5. Design the visual for the platform canvas early. If the Creator preview shows density or aspect-ratio problems, regenerate as `3:4` instead of trying to rescue a landscape asset.
6. Reframe sensitive or company-heavy copy toward methods, constraints, workload mapping, and tradeoffs before publishing.

## Visual Defaults

- Increase mechanism density when the user says `信息量不足`; add concrete parts, counts, paths, and measurements rather than more abstract labels.
- Keep English technical abbreviations clear when they are the real terms: WSE, NoC, MIMD, CSL, PE, GPU, TPU.
- For Cerebras programming-model visuals, use the stable scaffold: `MIMD vs SIMD/SIMT/GPU`, `CSL/Color`, then `compiler -> runtime -> hardware/PE fabric`.
- Use Creator preview as a validation surface, not just as an upload form.

## Validation

Before reporting ready, show evidence for:

- the topic directory and changed files;
- source or fact-check coverage for risky claims;
- visual dimensions or platform preview fit;
- final title/body/hashtags if a Creator draft was edited.

## Common Failures

- If the topic sprawls across GPU/TPU/Cerebras comparisons, narrow to one chip family and one mechanism.
- If the post is too dense or sensitive, generalize toward engineering constraints and effective-compute tradeoffs.
- If `~/Documents/xhs` is not a git repo, use direct file inspection and do not promise commit-based proof.
