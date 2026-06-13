# Figures, Captions, And Technical Route Diagrams

Use this for inserting, moving, captioning, or describing figures in Chinese academic DOCX files.

## Captions

- Captions should be descriptive, not placeholders.
- Use `图 N <title>` and keep the caption immediately below the image.
- If a figure is a cited external/source figure, include the citation in the caption or nearby text.
- If a figure is self-drawn, do not invent a citation.
- When moving a figure earlier or later, renumber all later figure references and captions.

## Nearby Description

Do not leave figures floating without explanation. Add 1-3 sentences near the figure:

- What the figure shows.
- How it connects to the local section.
- Which research logic or evidence it supports.

Prefer integrating the figure reference into an existing paragraph:

```text
本课题的技术路线按照“研究目标-关键问题-方法基础-技术实现-实验验证”的层级展开，如图 4 所示，围绕...
```

## Technical Route Diagram Pattern

A clear route figure can use five horizontal layers:

1. 研究目标
2. 关键问题
3. 理论与方法基础
4. 研究方法与技术实现
5. 实验验证

For three-column research routes, align text exactly between figure and body:

- MEMS 智能化设计
- 端侧动态推理与软硬件协同优化
- 跨层协同验证框架

Each column should have:

- key bottleneck;
- method basis;
- implementation loop;
- validation task;
- bottom result chain.

## Visual Style

- Avoid excessive decoration.
- Avoid top/bottom horizontal lines unless they are part of the source style and requested.
- Keep text short enough that it does not touch borders.
- Prefer simple blue/gray/green fills, restrained borders, and arrows.
- If using draw.io, keep a `.drawio` source next to the exported PNG.

## Common Caption Examples

```text
图 2 端侧感算融合芯片智能化设计方法总体框架
图 3 深度学习辅助的非参数化 MEMS 设计系统组成 [55]
图 4 研究方法与技术路线框图
```
