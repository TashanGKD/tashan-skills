---
name: bp-deck-visual-workflow
description: Use when creating or refining BP/PPT/WPS visual assets, slide backgrounds, Chinese concept graphics, slide-master assets, or layout-flexible presentation imagery in ~/Documents/bp.
---

# BP Deck Visual Workflow

## Core Rule

Derive visuals from the BP story and the actual deck layout. Do not blindly reuse logos, mountains, business flywheels, or generic AI imagery.

## Workflow

1. Reopen the narrative source before generating: usually `科研科创AI项目陪跑_BP草案.md` and nearby `支撑材料/叙事说明/*`.
2. Restate the visual role: background support art, concept strip, standalone infographic, or slide-master asset.
3. For backgrounds, default to high whitespace, white or pale base, no logo, no mountain motif, minimal elements, and layout tolerance for multiple slide types.
4. For Chinese concept graphics, prefer local script-driven generation when typography and layout control matter. Reuse or inspect existing scripts and outputs before one-shot image generation.
5. Apply assets to the real WPS/PPT surface when the task is a deck task. Check `幻灯片母版`, slide thumbnails, and the local media folder before calling the asset done.
6. Iterate from visual critique: hierarchy, canvas balance, left/right weight, text density, and whether it looks too obviously AI-generated.

## Known Local Cues

- Core story: turn fragmented, vague, hard-to-land AI needs in universities/research groups into verifiable, deliverable, reusable project assets.
- Existing deck/assets have appeared around `灵感共创Xdatawhale.pptx`, `灵感共创Datavhale.pptx`, `bg_horizontal.png`, `bg_vertical_simple.png`, `three-ones-strip.svg`, and `workspace/tashanhomepage/material/media`.
- Accepted direction: organized project materials, paper/card texture, user-side workbench feel, strong whitespace.

## Validation

For generated assets, verify dimensions and preview the image. For deck work, inspect the actual slide/master result, not only the exported asset. Report where the output file lives and what visual constraints were checked.

## Common Failures

- If the user says the result is `太商务` or `太像 AI 生成的`, lower abstraction and remove glow, translucent tech layers, and flywheel metaphors.
- If the user says `山还是有点多`, treat it as aggressive removal, not mild reduction.
- If Chinese text quality is poor, move to local layout generation or editable SVG rather than repeating image prompts.
