# Writing And Structure For Chinese Opening Reports

Use this for drafting or restructuring opening reports, thesis proposals, and academic reports.

## Typical Section Logic

1. 选题背景及意义
   - Explain why the problem matters.
   - List challenges explicitly when needed.
   - Avoid vague motivation; identify bottlenecks.
2. 国内外研究现状与趋势
   - Organize by topic hierarchy, not by paper list.
   - Each subsection should end with a gap or implication.
3. 研究内容与预期目标
   - State the overall research object.
   - List 2-4 concrete research contents.
   - Each item should include problem, method, expected output.
4. 研究方法、技术路线、实验方案、可行性
   - Avoid repeating section 3.1.
   - Convert research contents into executable steps and validation plan.
   - Tie experiments to metrics and baselines.
5. 研究基础与条件
   - Do not write like a personal resume.
   - Describe research experience, prior outputs, platforms, and toolchain foundations as support for the proposed work.

## Challenge Lists

When the user asks for significance/challenges, use numbered items and make each item specific:

- system trend or application pressure;
- sensor/data movement bottleneck;
- MEMS geometry/simulation/manufacturing difficulty;
- data-driven method limitation;
- edge model resource bottleneck;
- lack of cross-layer validation.

## Chapter 3 To Chapter 4 Relationship

- Section 3.1 answers: what will be studied and what contributions are expected?
- Section 4.1 answers: how will the study be executed and verified?
- If 4.1 repeats 3.1, compress 4.1 and merge the experiment plan into the execution route.

## Technical Route Paragraph Pattern

```text
如图 N 所示，本课题的技术路线按照“研究目标-关键问题-方法基础-技术实现-实验验证”的层级展开，并围绕 A、B、C 三条主线组织。
```

Then write one paragraph per route:

- `对于 A，关键问题是... 方法基础包括... 技术实现上... 实验验证将...`
- `对于 B，关键问题是...`
- `对于 C，关键问题是...`

## Research Foundation

Write research foundation as capability evidence, not employment history:

- previous algorithm or paper result and why it supports this topic;
- agent/scientific workflow experience and why it supports tool-driven design;
- hardware/toolchain/GPU/FPGA/MLIR/codegen experience and why it supports verification.
