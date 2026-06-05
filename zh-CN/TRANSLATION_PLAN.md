# MIT 6.004 资料汉化计划

## 总目标

在仓库根目录新增 `zh-CN/` 目录，所有汉化内容都放在该目录中，原始英文文件保持不变。

## 最终目录规划

```text
zh-CN/
  README.md
  index.html
  glossary.md
  translation_manifest.json
  translation_notes.md
  TRANSLATION_PLAN.md

  lectures/
    *.html
    lecture_slides/
      *.pptx

  labs/
    lab1_cmos/
      lab.html
    lab2_adder/
      lab.html
    ...
    lab11_design_project/
      lab.html

  worksheets/
    *.docx
```

其中：

- `glossary.md` 用于统一专业术语。
- `translation_manifest.json` 用于记录每个文件的翻译状态。
- `translation_notes.md` 用于记录翻译原则、疑难术语、暂未处理项。
- `TRANSLATION_PLAN.md` 用于保存本计划。

## 阶段 0：准备与基线扫描

目标：搞清楚哪些文件要翻译，哪些文件只复制或忽略。

要做：

1. 扫描仓库文件类型。
2. 建立 `zh-CN/` 目录。
3. 建立翻译清单 `translation_manifest.json`。
4. 建立术语表 `glossary.md`。
5. 标记文件优先级。

初步分类：

```text
高优先级：
README.md
index.html
lectures/*.html
labs/lab*/lab.html

中优先级：
worksheets/*.docx
lectures/lecture_slides/*.pptx

低优先级：
PDF 文件
工具说明 HTML
少量 txt/md 文件

不翻译或仅复制：
图片
字体
MathJax
min.js
CSS
JSON 配置
UASM 代码
answers.zip
```

## 阶段 1：术语表建设

目标：先统一 MIT 6.004 课程里的核心术语，避免后面翻译混乱。

示例术语：

```text
digital abstraction -> 数字抽象
combinational logic -> 组合逻辑
sequential logic -> 时序逻辑
finite state machine -> 有限状态机
CMOS -> CMOS
MOSFET -> MOSFET
datapath -> 数据通路
control logic -> 控制逻辑
instruction set architecture -> 指令集架构
Beta processor -> Beta 处理器
pipeline -> 流水线
cache -> 缓存
cache coherence -> 缓存一致性
virtual memory -> 虚拟内存
interrupt -> 中断
synchronization -> 同步
```

翻译原则：

1. 专有名词首次出现可保留英文括注。
2. 代码、寄存器名、信号名、文件名、命令不翻译。
3. 数学公式不翻译结构，只翻译说明文字。
4. `Beta` 作为课程处理器名称保留英文。

## 阶段 2：课程入口汉化

目标：先让中文版有一个可浏览入口。

处理文件：

```text
README.md
index.html
```

产出：

```text
zh-CN/README.md
zh-CN/index.html
```

检查点：

1. 中文首页能打开。
2. 链接指向 `zh-CN/` 内的中文资料。
3. 没翻译完成的链接可以先保留英文源文件链接或标注“待翻译”。

## 阶段 3：讲义 HTML 汉化

目标：翻译课程主要阅读内容，并生成可浏览的中文讲义 HTML。

处理：

```text
lectures/*.html
```

产出：

```text
zh-CN/lectures/*.html
```

阶段 3 已通过 `L01_Basics_of_Information.html` 做试点。试点结论是：讲义体量差异较大，不能简单一次性全量翻译；应按具体讲义的文本量动态拆分，并使用缓存断点续翻，最后从原始 HTML 结构重新组装完整中文文件。

### 基本策略

1. 保留原 HTML 结构。
2. 只翻译可见正文、标题、列表项、图注和普通链接文本。
3. 保留公式、代码、路径、变量名、寄存器名、信号名、文件名和命令。
4. 保留原图资源引用，不复制大量图片。
5. 中文文件中的资源路径在构建阶段统一修正。
6. 每个文件只在完整构建并通过检查后，才在 manifest 中标记 `translated`。
7. 机器翻译产物统一标记 `review: pending`，不直接标记为 `reviewed`。

### 动态拆分规则

先分析每个讲义的可翻译文本块数量和字符量，再决定执行粒度：

```text
<= 20k 英文字符：一次翻译并构建
20k-40k 英文字符：拆成 2 个 chunk
40k-60k 英文字符：拆成 3 个 chunk
> 60k 英文字符：拆成 4 个或更多 chunk
```

拆分时不要按原始 HTML 字节硬切。应按解析后的文本节点或章节边界拆分，优先使用：

```text
h2 section -> paragraph/list item -> text node
```

这样可以避免切坏标签、公式和链接。

### 推荐执行流程

阶段 3 的单个讲义建议按下面流程处理：

```text
analyze   分析讲义文本量、文本块数量和建议 chunk 数
translate 翻译指定讲义的一个或多个 chunk，并立即写入缓存
build     使用原始 HTML 结构和翻译缓存组装完整中文 HTML
verify    检查 HTML 头部、资源路径、链接、公式和抽样中文内容
manifest  检查通过后更新 translation_manifest.json
```

核心原则是：拆分只影响翻译过程，不影响最终 HTML 结构。最终中文文件应始终由“原始 HTML 结构 + 翻译缓存”重新生成。

### 缓存与断点续翻

使用翻译缓存记录规范化后的英文文本和中文译文：

```text
zh-CN/translation_cache_v2.json
```

要求：

1. 每翻译成功一个文本块就立即保存缓存。
2. 中断后重跑时优先复用缓存，避免重复请求。
3. 如果某个文本块翻译失败，不应影响已完成缓存。
4. 只有完整 `build` 成功后才生成或覆盖最终 HTML 文件。

### 验收标准

每个讲义完成后必须检查：

1. `zh-CN/lectures/<file>.html` 存在。
2. 文件头部包含 `<!DOCTYPE html>` 和 `html lang="zh-CN"`。
3. MathJax、script、CSS 路径可用。
4. 所有本地 `href` / `src` 目标存在。
5. 公式块没有被翻译破坏。
6. 代码、变量、寄存器、路径没有被误翻译。
7. 抽查标题、开头段落和若干中间段落，确认中文可读。
8. manifest 中对应条目为 `status: translated`、`review: pending`。

### 讲义执行清单

阶段 3 按下面的小项推进。`文本块` 和 `英文字符` 是基于跳过 script/style/code/公式块后的可翻译文本统计；`chunk` 是建议拆分数。状态含义：

```text
completed-draft  已生成中文机器初稿，等待复查
pending          尚未生成中文讲义
```

| 序号 | 讲义 | 文本块 | 英文字符 | 建议 chunk | 状态 | 目标文件 |
| ---: | --- | ---: | ---: | ---: | --- | --- |
| 1 | L01 Basics of Information | 193 | 32976 | 2 | completed-draft | `zh-CN/lectures/L01_Basics_of_Information.html` |
| 2 | L02 The Digital Abstraction | 132 | 31311 | 2 | completed-draft | `zh-CN/lectures/L02_The_Digital_Abstraction.html` |
| 3 | L03 CMOS Technology | 148 | 41829 | 3 | pending | `zh-CN/lectures/L03_CMOS_Technology.html` |
| 4 | L04 Combinational Logic | 160 | 43407 | 3 | pending | `zh-CN/lectures/L04_Combinational_Logic.html` |
| 5 | L05 Sequential Logic | 135 | 34908 | 2 | pending | `zh-CN/lectures/L05_Sequential_Logic.html` |
| 6 | L06 Finite State Machines | 140 | 36582 | 2 | pending | `zh-CN/lectures/L06_Finite_State_Machines.html` |
| 7 | L07 Pipelined Circuits | 124 | 31432 | 2 | pending | `zh-CN/lectures/L07_Pipelined_Circuits.html` |
| 8 | L08 Design Tradeoffs | 117 | 33903 | 2 | pending | `zh-CN/lectures/L08_Design_Tradeoffs.html` |
| 9 | L09 Designing an Instruction Set | 183 | 48322 | 3 | pending | `zh-CN/lectures/L09_Designing_an_Instruction_Set.html` |
| 10 | L10a Assembly Language | 98 | 22432 | 2 | pending | `zh-CN/lectures/L10a_Assembly_Language.html` |
| 11 | L10b Models of Computation | 59 | 11924 | 1 | pending | `zh-CN/lectures/L10b_Models_of_Computation.html` |
| 12 | L11 Compilers | 185 | 31485 | 2 | pending | `zh-CN/lectures/L11_Compilers.html` |
| 13 | L12 Procedures and Stacks | 203 | 31572 | 2 | pending | `zh-CN/lectures/L12_Procedures_and_Stacks.html` |
| 14 | L13 Building the Beta | 154 | 34619 | 2 | pending | `zh-CN/lectures/L13_Building_the_Beta.html` |
| 15 | L14 Caches and the Memory Hierarchy | 244 | 58633 | 3 | pending | `zh-CN/lectures/L14_Caches_and_the_Memory_Hierarchy.html` |
| 16 | L15 Pipelining the Beta | 216 | 45409 | 3 | pending | `zh-CN/lectures/L15_Pipelining_the_Beta.html` |
| 17 | L16 Virtual Memory | 195 | 41874 | 3 | pending | `zh-CN/lectures/L16_Virtual_Memory.html` |
| 18 | L17 Virtualizing the Processor | 159 | 33851 | 2 | pending | `zh-CN/lectures/L17_Virtualizing_the_Processor.html` |
| 19 | L18 Devices and Interrupts | 179 | 40592 | 3 | pending | `zh-CN/lectures/L18_Devices_and_Interrupts.html` |
| 20 | L19 Concurrency and Synchronization | 202 | 34070 | 2 | pending | `zh-CN/lectures/L19_Concurrency_and_Synchronization.html` |
| 21 | L20 System-level Communication | 137 | 36379 | 2 | pending | `zh-CN/lectures/L20_System_level_Communication.html` |
| 22 | L21 Parallel Processing | 179 | 38405 | 2 | pending | `zh-CN/lectures/L21_Parallel_Processing.html` |
| 23 | Wrap-up | 22 | 5697 | 1 | pending | `zh-CN/lectures/Wrap_up.html` |

### 小项执行方式

每个讲义按以下小项执行：

1. `analyze`：确认文本块、英文字符和建议 chunk 数。
2. `translate chunk`：按 chunk 翻译并写入 `translation_cache_v2.json`。
3. `build`：从原始 HTML 和缓存组装 `zh-CN/lectures/<file>.html`。
4. `verify links`：检查所有本地 `href` / `src` 是否存在。
5. `verify structure`：检查 `<!DOCTYPE html>`、`html lang="zh-CN"`、MathJax/script/CSS 路径。
6. `sample review`：抽查标题、首段、中段、尾段和公式附近说明。
7. `manifest`：检查通过后将对应条目标为 `status: translated`、`review: pending`。

### 推荐批次

优先继续课程顺序，但按 chunk 总量控制每批规模：

```text
批次 3A：L02
批次 3B：L03
批次 3C：L04
批次 3D：L05 + L06
批次 3E：L07 + L08
批次 3F：L09
批次 3G：L10a + L10b
批次 3H：L11 + L12
批次 3I：L13
批次 3J：L14
批次 3K：L15
批次 3L：L16
批次 3M：L17 + L18
批次 3N：L19 + L20
批次 3O：L21 + Wrap-up
```

大讲义单独成批，避免长时间运行中断后难以验收。小讲义可以两篇合并一批。
### 后续复查

阶段 3 的第一轮目标是生成完整中文机器初稿。完成全部讲义后，应增加一次复查 pass，重点处理：

1. 小节标题和课程术语是否统一。
2. 明显机器翻译腔。
3. 公式、代码、寄存器、文件名附近的说明是否准确。
4. 链接文字和页面导航是否自然。
5. 大讲义中的术语是否与 `glossary.md` 一致。
## 阶段 4：实验说明汉化

目标：让学生能用中文读懂实验要求。

处理：

```text
labs/lab*/lab.html
```

产出：

```text
zh-CN/labs/lab*/lab.html
```

注意：

1. 实验步骤翻译成自然中文。
2. 命令、代码、模块名、测试文件名不翻译。
3. Checkoff、template、uasm、json 等开发文件保持英文原样。
4. 图片继续引用原目录资源，减少重复文件。

建议顺序：

```text
lab1_cmos
lab2_adder
lab3_fsm
lab4_alu
lab5_assembly
lab6_procedures
lab7_beta
lab8_caches
lab9_virtual_memory
lab10_tinyos
lab11_design_project
```

## 阶段 5：Worksheet 文档汉化

目标：生成中文练习文档。

处理：

```text
worksheets/*.docx
```

产出：

```text
zh-CN/worksheets/*_zh-CN.docx
```

策略：

1. 保留 Word 样式、表格、编号。
2. 翻译题目和说明。
3. 代码、公式、信号名不翻译。
4. `answers` 类文件可以单独标注，避免和普通题目混在一起。

建议优先级：

```text
先翻译 worksheet
再翻译 answers
```

## 阶段 6：PPTX 课件汉化

目标：生成中文版课件。

处理：

```text
lectures/lecture_slides/*.pptx
```

产出：

```text
zh-CN/lectures/lecture_slides/*_zh-CN.pptx
```

策略：

1. 保留原页面布局、图片、图形。
2. 翻译文本框。
3. 公式、代码、信号名保留。
4. 每个 PPTX 生成后抽检页面，防止中文溢出文本框。
5. 中文太长时优先简化表达，而不是破坏版式。

这是工作量最大的一部分，建议最后做。

## 阶段 7：PDF 处理

PDF 不作为第一翻译源。

处理原则：

1. 如果 PDF 有对应 DOCX/PPTX，翻译源文件即可。
2. 如果只有 PDF，没有源文件，再考虑提取文本生成 Markdown 或 DOCX。
3. 不建议直接修改 PDF，容易破坏排版。

## 阶段 8：质量检查

每批完成后检查：

```text
git status
```

确保只有 `zh-CN/` 新增或修改，原目录没有变化。

检查内容：

1. 原始英文文件未改动。
2. 中文 HTML 可以打开。
3. 链接没有明显断裂。
4. DOCX/PPTX 能正常打开。
5. 术语一致。
6. 代码、命令、寄存器、文件名没有被误翻。
7. 中文没有明显机器翻译腔。
8. 重要概念没有误译。

## 阶段 9：最终交付清单

完成后应有：

```text
zh-CN/README.md
zh-CN/index.html
zh-CN/glossary.md
zh-CN/translation_manifest.json
zh-CN/translation_notes.md
zh-CN/TRANSLATION_PLAN.md
zh-CN/lectures/
zh-CN/labs/
zh-CN/worksheets/
zh-CN/lectures/lecture_slides/
```

`translation_manifest.json` 中应记录类似状态：

```json
{
  "source": "lectures/L01_Basics_of_Information.html",
  "target": "zh-CN/lectures/L01_Basics_of_Information.html",
  "type": "html",
  "status": "translated",
  "review": "pending"
}
```

## 推荐执行顺序

1. 建立 `zh-CN/`、术语表、翻译清单。
2. 翻译 `README.md` 和 `index.html`。
3. 翻译 `lectures/*.html`。
4. 翻译 `labs/lab*/lab.html`。
5. 翻译 `worksheets/*.docx`。
6. 翻译 `lectures/lecture_slides/*.pptx`。
7. 处理必要 PDF。
8. 全量质量检查。

这个顺序最稳：先做网页和入口，马上能用；再做实验和练习；最后处理最重的 PPTX。


