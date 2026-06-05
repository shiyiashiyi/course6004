# 汉化说明

## 阶段 0 完成内容

- 建立 `zh-CN/` 中文资料目录。
- 建立中文资料的基础子目录：`lectures/`、`lectures/lecture_slides/`、`labs/`、`worksheets/`。
- 建立术语表 `glossary.md`。
- 建立翻译追踪清单 `translation_manifest.json`。
- 对仓库资料做文件类型扫描，并按优先级标记翻译对象。

## 阶段 1 完成内容

- 扩展 `glossary.md`，建立按主题分组的课程术语表。
- 覆盖信息与数字抽象、组合逻辑、CMOS、时序逻辑、ISA、Beta、编译器、流水线、缓存、虚拟内存、中断、并发、实验工具等主题。
- 明确不翻译清单：代码、命令、路径、文件名、寄存器名、信号名、模块名、测试名和常用英文缩写。
- 明确后续翻译风格：讲义重准确，实验重可执行，worksheet 保留题目结构，PPTX 控制中文长度。

## 阶段 2 完成内容

- 生成 `zh-CN/README.md`，提供中文资料说明和本地浏览方式。
- 生成 `zh-CN/index.html`，提供中文课程简介和中文课程大纲。
- `zh-CN/index.html` 中尚未翻译的讲义和实验链接暂时指向英文原文，并标注“中文待翻译”，避免阶段 2 出现断链。
- 在 `translation_manifest.json` 中将 `README.md` 和 `index.html` 标记为 `translated`。

## 翻译范围

优先翻译：

- `README.md`
- `index.html`
- `lectures/*.html`
- `labs/lab*/lab.html`
- `worksheets/*.docx`
- `lectures/lecture_slides/*.pptx`

暂缓或仅作为参考：

- PDF 文件。如果有对应 DOCX/PPTX/HTML 源文件，优先翻译源文件。
- `labs/tool_docs/*.html` 和 `labs/tools/*.html`，这些属于工具说明或运行环境，优先级低于课程主体资料。

不翻译：

- 图片、字体、压缩包。
- `MathJax`、压缩 JS/CSS、第三方工具库。
- 代码、配置、测试输入、汇编文件。

## 文件处理原则

- 不修改原始英文资料。
- 中文资料统一写入 `zh-CN/`。
- HTML 翻译保留标签结构，只翻译可见文本。
- DOCX/PPTX 翻译尽量保留原样式和布局。
- 代码块、公式、寄存器、信号名、文件名、命令保持英文原样。
- 每完成一个文件，在 `translation_manifest.json` 中更新 `status` 和 `review`。

## 状态字段

- `pending`：尚未开始。
- `translated`：已生成中文版本。
- `reviewed`：已人工或二次检查。
- `reference_only`：作为参考，不计划直接翻译。
- `skip`：不翻译。

## 优先级字段

- `high`：课程入口、讲义和实验说明。
- `medium`：worksheet 和 PPTX 课件。
- `low`：PDF、工具说明、少量辅助文本。
- `skip`：资源、代码、第三方库或压缩包。
