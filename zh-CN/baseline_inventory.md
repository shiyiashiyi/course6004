# 阶段 0 基线盘点

生成日期：2026-06-05

## 文件类型统计

| 类型 | 数量 | 处理策略 |
| --- | ---: | --- |
| `.png` | 681 | 跳过，中文资料继续引用原图 |
| `.js` | 82 | 跳过，属于代码或工具库 |
| `.html` | 46 | 按类型分为高优先级讲义/实验和低优先级工具说明 |
| `.woff` | 44 | 跳过，字体资源 |
| `.json` | 28 | 跳过，配置或工具数据 |
| `.pptx` | 26 | 中优先级，后续生成中文课件 |
| `.docx` | 23 | 中优先级，后续生成中文练习文档 |
| `.pdf` | 21 | 低优先级，优先作为参考 |
| `.gif` | 10 | 跳过，中文资料继续引用原图 |
| `.uasm` | 10 | 跳过，代码不翻译 |
| `.css` | 6 | 跳过，样式资源 |
| `.md` | 3 | 低优先级或项目说明 |
| `.txt` | 2 | 低优先级或辅助文本 |
| 其他二进制/字体/压缩文件 | 8 | 跳过 |

## 翻译优先级统计

| 优先级 | 数量 | 说明 |
| --- | ---: | --- |
| high | 36 | `README.md`、`index.html`、讲义 HTML、实验 `lab.html` |
| medium | 49 | Worksheet DOCX 和课件 PPTX |
| low | 35 | PDF、工具说明 HTML、少量辅助文本 |
| skip | 870 | 图片、字体、代码、配置、第三方工具库、压缩包 |

## 高优先级范围

- `README.md`
- `index.html`
- `lectures/*.html`
- `labs/lab*/lab.html`

## 中优先级范围

- `worksheets/*.docx`
- `lectures/lecture_slides/*.pptx`

## 低优先级范围

- `worksheets/pdfs/*.pdf`
- `labs/*.pdf`
- `labs/tool_docs/*.html`
- `labs/tools/*.html`
- `labs/sandboxes/*.html`
- 少量 `.txt` / `.md`

## 跳过范围

- 图片、GIF、图标。
- 字体文件。
- JS/CSS/JSON 工具或配置。
- UASM 代码和测试数据。
- `answers.zip`。

## 阶段 0 产物

- `zh-CN/TRANSLATION_PLAN.md`
- `zh-CN/glossary.md`
- `zh-CN/translation_notes.md`
- `zh-CN/translation_manifest.json`
- `zh-CN/baseline_inventory.md`
- `zh-CN/lectures/`
- `zh-CN/lectures/lecture_slides/`
- `zh-CN/labs/`
- `zh-CN/worksheets/`
