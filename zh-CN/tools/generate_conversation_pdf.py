from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "zh-CN" / "conversation_showcase.pdf"
FONT = Path("C:/Windows/Fonts/NotoSansSC-VF.ttf")
if not FONT.exists():
    FONT = Path("C:/Windows/Fonts/simhei.ttf")


def register_fonts() -> str:
    font_name = "ConversationCN"
    pdfmetrics.registerFont(TTFont(font_name, str(FONT)))
    return font_name


def clean(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )


def bubble(role: str, text: str, styles, width):
    if role == "assistant":
        left = Paragraph(clean(text), styles["assistant"])
        right = ""
        data = [[left, right]]
        bg_col = 0
        bg = colors.HexColor("#F2F4F7")
    else:
        left = ""
        right = Paragraph(clean(text), styles["user"])
        data = [[left, right]]
        bg_col = 1
        bg = colors.HexColor("#DCFCE7")

    table = Table(data, colWidths=[width * 0.49, width * 0.49])
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (bg_col, 0), (bg_col, 0), bg),
                ("BOX", (bg_col, 0), (bg_col, 0), 0.6, colors.HexColor("#D0D5DD")),
                ("LEFTPADDING", (bg_col, 0), (bg_col, 0), 8),
                ("RIGHTPADDING", (bg_col, 0), (bg_col, 0), 8),
                ("TOPPADDING", (bg_col, 0), (bg_col, 0), 7),
                ("BOTTOMPADDING", (bg_col, 0), (bg_col, 0), 7),
            ]
        )
    )
    return table


def transcript() -> list[tuple[str, str]]:
    return [
        (
            "user",
            "拉取仓库代码，如果有权限问题及时跟我说。\n仓库：https://github.com/shiyiashiyi/course6.004.git",
        ),
        (
            "assistant",
            "我先检查当前目录和 git 状态。发现 Git 报 dubious ownership：仓库目录属于你的 Windows 用户，但命令运行在 Codex 沙盒用户下。随后我把当前目录加入 Git safe.directory。",
        ),
        (
            "assistant",
            "继续检查后发现本地仓库没有远端，分支是 master，工作区干净。我尝试访问 GitHub，但最初遇到 connection aborted / timeout，判断是网络连接问题，不是 GitHub 权限或邮箱账号问题。",
        ),
        (
            "user",
            "检查现在 git 拉取等操作用的是啥电子邮箱账号。",
        ),
        (
            "assistant",
            "查到 Git 提交身份：user.name = Yebby，user.email = yebbyhuang@rektec.com.cn。拉取/推送认证使用 Git Credential Manager，但当时没有看到已保存的 GitHub 账号。",
        ),
        (
            "user",
            "再拉取试试。",
        ),
        (
            "assistant",
            "我多次重试 fetch/ls-remote。错误从连接中断到 github.com:443 连接失败不等，判断仍是网络/VPN/代理层面的问题，不是仓库权限问题。",
        ),
        (
            "user",
            "我执行 clone 时提示：destination path 已存在且不是空目录。判断报错原因。",
        ),
        (
            "assistant",
            "原因是 C:\\Users\\77374\\Documents\\MIT6.004 已经存在且不是空目录，不能直接 clone 覆盖。还注意到你这次仓库名是 course6004.git，和之前 course6.004.git 不同。",
        ),
        (
            "user",
            "MIT6.004 本来就是要用这个远端仓库，在现有目录里改远端再拉取。",
        ),
        (
            "assistant",
            "我把 origin 改为 https://github.com/shiyiashiyi/course6004.git，确认远端 main 存在，执行 fetch，并把本地切到跟踪 origin/main。最终最新提交为 5bec56c add encrypted zip file with solutions。",
        ),
        (
            "user",
            "仓库里都是英文资料。我希望你搞一个新的文件夹，把资料汉化之后放到新文件夹里，不要改变原有文件。先规划。",
        ),
        (
            "assistant",
            "我扫描仓库结构，确认有 lectures、labs、worksheets，包含 HTML、PPTX、DOCX、PDF、大量图片和工具库文件。随后提出 zh-CN/ 中文镜像目录方案，不改原文件。",
        ),
        (
            "assistant",
            "完整计划分为：阶段 0 准备与基线扫描；阶段 1 术语表；阶段 2 课程入口；阶段 3 讲义 HTML；阶段 4 实验说明；阶段 5 worksheets；阶段 6 PPTX；阶段 7 PDF；阶段 8 质量检查；阶段 9 交付清单。",
        ),
        (
            "user",
            "把计划生成 md 文件备份。",
        ),
        (
            "assistant",
            "我创建 zh-CN/TRANSLATION_PLAN.md，保存完整汉化计划。此时只新增 zh-CN/，原始英文资料未改动。",
        ),
        (
            "user",
            "完成计划 0。",
        ),
        (
            "assistant",
            "执行阶段 0：建立 zh-CN/ 基础目录、glossary.md、translation_notes.md、translation_manifest.json、baseline_inventory.md，并按 high/medium/low/skip 标记文件优先级。统计为 total 990，high 36，medium 49，low 35，skip 870。",
        ),
        (
            "user",
            "按计划进入阶段 1。",
        ),
        (
            "assistant",
            "执行阶段 1：扩展 glossary.md，建立按主题分组的术语表，覆盖数字抽象、组合逻辑、CMOS、时序逻辑、ISA/Beta、流水线、缓存、虚拟内存、中断、并发同步和实验工具。",
        ),
        (
            "user",
            "进入阶段 2。",
        ),
        (
            "assistant",
            "执行阶段 2：生成 zh-CN/README.md 和 zh-CN/index.html。中文首页链接暂时指向英文原文并标注“中文待翻译”，避免断链。manifest 中 README.md 和 index.html 标为 translated。",
        ),
        (
            "user",
            "检查项目是否准确完成了阶段 0、1、2。",
        ),
        (
            "assistant",
            "核对结果：阶段 0、1、2 已准确完成。manifest 可解析，入口文件已 translated，zh-CN/index.html 本地 href/src 路径检查通过，原始英文资料未被修改。",
        ),
        (
            "user",
            "浏览器实际打开验证我已经手动实现，判断是否可以进行阶段 3。",
        ),
        (
            "assistant",
            "可以进入阶段 3。阶段 3 的目标是翻译 lectures/*.html 到 zh-CN/lectures/*.html，建议从 L01 开始，保留 HTML 结构、公式、代码、链接和图片引用。",
        ),
        (
            "user",
            "进行阶段 3 的工作。",
        ),
        (
            "assistant",
            "我先尝试本地翻译能力，发现没有离线翻译引擎。随后安装 deep-translator，并获准使用 Google Translate 翻译公开课程讲义。L01 初次整篇翻译暴露出请求超时、缓存、DOCTYPE、换行导致中文生硬等问题。",
        ),
        (
            "assistant",
            "优化后加入 translation_cache_v2.json、请求超时、空白规范化、资源路径修正。最终生成 zh-CN/lectures/L01_Basics_of_Information.html，manifest 标为 translated / pending。",
        ),
        (
            "user",
            "先查看目前进度，回顾 L01 翻译过程，思考总结优化，然后对阶段 3 重新规划。",
        ),
        (
            "assistant",
            "我确认只完成 L01，停止残留 Python 进程，总结出新策略：按讲义体量动态拆分 chunk，使用缓存断点续翻，最后由原 HTML + 缓存 build 完整中文 HTML。",
        ),
        (
            "user",
            "是否可以根据具体讲义的翻译量动态调节？大讲义再拆分，最后组装？判断可行性。",
        ),
        (
            "assistant",
            "判断可行，而且更合理。推荐 analyze / translate chunk / build / verify / manifest 流程。拆分只影响翻译过程，不影响最终 HTML 结构。",
        ),
        (
            "user",
            "优化计划文件。",
        ),
        (
            "assistant",
            "我更新 TRANSLATION_PLAN.md 的阶段 3：加入 L01 试点结论、动态拆分规则、缓存机制、验收标准、review: pending 规则。",
        ),
        (
            "user",
            "对阶段三的讲义内容，拆分出完整计划小项，更新计划文件。对 L01 做好标注。",
        ),
        (
            "assistant",
            "我统计 23 个讲义的文本块、英文字符和建议 chunk 数，写入“讲义执行清单”。L01 标为 completed-draft，L02-L21 和 Wrap-up 标为 pending，并加入批次 3A 到 3O。",
        ),
        (
            "user",
            "我们上一次做到哪里啦？下一步要做什么？",
        ),
        (
            "assistant",
            "当时进度：阶段 3 进行中，L01 completed-draft。下一步是批次 3A：L02 The Digital Abstraction，建议 2 个 chunk。",
        ),
        (
            "user",
            "执行 3A 的计划。",
        ),
        (
            "assistant",
            "我升级 translate_lecture_html.py 为 analyze / translate-chunk / build 模式。完成 L02 两个 chunk，处理一次失败缓存项并重试，build missing 0，链接检查通过，manifest 和计划均更新为 completed-draft。",
        ),
        (
            "user",
            "批次 3B。",
        ),
        (
            "assistant",
            "执行 L03 CMOS Technology：分析为 147 文本块、41825 英文字符、3 chunks。三个 chunk 完成，build missing 0，链接检查通过。发现机器翻译中 drain/source 等术语待复查，标为 completed-draft / review pending。",
        ),
        (
            "user",
            "执行批次 3C。",
        ),
        (
            "assistant",
            "执行 L04 Combinational Logic：分析为 159 文本块、43403 英文字符、3 chunks。三个 chunk 完成，build missing 0，链接检查通过。我额外修掉两处明显英文残留长句。最终 L04 标为 completed-draft。",
        ),
        (
            "assistant",
            "当前阶段 3 进度：L01、L02、L03、L04 已生成中文机器初稿；L05-L21 与 Wrap-up 仍 pending。下一步按计划是批次 3D：L05 Sequential Logic + L06 Finite State Machines。",
        ),
    ]


def build_pdf() -> None:
    font = register_fonts()
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleCN",
            fontName=font,
            fontSize=20,
            leading=28,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#111827"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubTitleCN",
            fontName=font,
            fontSize=10.5,
            leading=16,
            textColor=colors.HexColor("#475467"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="assistant",
            fontName=font,
            fontSize=9.2,
            leading=14,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#101828"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="user",
            fontName=font,
            fontSize=9.2,
            leading=14,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#052E16"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="section",
            fontName=font,
            fontSize=13,
            leading=18,
            spaceBefore=8,
            spaceAfter=8,
            textColor=colors.HexColor("#1D2939"),
        )
    )

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
        title="MIT 6.004 汉化项目对话过程",
    )
    width = A4[0] - doc.leftMargin - doc.rightMargin
    story = []
    story.append(Paragraph("MIT 6.004 汉化项目对话过程", styles["TitleCN"]))
    story.append(
        Paragraph(
            "整理版记录：右侧为用户发言，左侧为 Codex 回应。内容覆盖从拉取仓库代码、处理 Git 权限与网络问题，到规划并推进中文资料翻译的主要过程。",
            styles["SubTitleCN"],
        )
    )
    story.append(Spacer(1, 8))
    summary = (
        "当前项目进度：已完成阶段 0、1、2；阶段 3 已完成 L01-L04 的中文机器初稿。"
        " 下一步计划是批次 3D：L05 Sequential Logic + L06 Finite State Machines。"
    )
    story.append(bubble("assistant", summary, styles, width))
    story.append(PageBreak())
    story.append(Paragraph("对话记录", styles["section"]))

    for role, text in transcript():
        story.append(bubble(role, text, styles, width))
        story.append(Spacer(1, 5))

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
    print(OUT)
