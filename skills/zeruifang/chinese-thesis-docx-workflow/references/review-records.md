# Review Records, Supervisor Comments, And Group Opinions

Use this for 开题考核记录, questions and answers, 导师意见, 小组意见, and 开题报告摘要.

## Question And Answer Records

Use three questions unless the user asks otherwise. Make each question concrete and likely from a review committee:

1. A domain-specific difficulty question.
2. A feasibility/overhead/generalization question.
3. A validation/evaluation/platform question.

For this MEMS/edge topic, good question categories are:

- MEMS 智能化设计的卡点:
  - geometry legality;
  - mesh/solver failure;
  - boundary condition completeness;
  - multi-objective performance;
  - manufacturability;
  - reward design.
- Dynamic inference and co-design overhead:
  - confidence/statistics overhead;
  - exit mechanism;
  - cache management;
  - compatibility with inference frameworks;
  - accelerator/software trigger design.
- Verification:
  - operator-level FLOPs/MACs;
  - model-level latency/accuracy;
  - embedded power;
  - FPGA/GPU/Vivado estimates;
  - baseline selection.

## Supervisor Opinion

Do not merely list the three research points. Include:

- why the topic is valuable;
- what the student has correctly recognized;
- where the real difficulties are;
- what should be narrowed;
- what minimal closed-loop system should be built first;
- final attitude, for example `同意开题`.

Tone: supportive, specific, academically formal.

## Group Opinion

Make it sound like a committee, not a project abstract:

- evaluate clarity and feasibility;
- identify concerns about breadth;
- request concrete baselines and metrics;
- emphasize representative tasks and validation platforms;
- end with recommendation.

## Avoid Generic Comments

Generic:

```text
该课题具有创新性，技术路线合理，建议通过。
```

Better:

```text
小组特别关注到，MEMS 智能化设计部分是本课题区别于一般端侧模型部署研究的重要内容。后续需要明确结构表示方式、合法性检查规则、有限元仿真接口、失败样本处理机制和奖励函数设计，避免停留在“用智能体做设计”的概念层面。
```
