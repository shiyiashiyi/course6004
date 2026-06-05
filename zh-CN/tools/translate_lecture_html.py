from __future__ import annotations

import argparse
import json
import math
import re
import sys
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Doctype, NavigableString
from deep_translator import GoogleTranslator


ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "lectures"
TARGET_DIR = ROOT / "zh-CN" / "lectures"
MANIFEST = ROOT / "zh-CN" / "translation_manifest.json"
CACHE_PATH = ROOT / "zh-CN" / "translation_cache_v2.json"

SKIP_PARENTS = {"script", "style", "pre", "code", "textarea"}
MANUAL = {
    "Lecture": "讲义",
    "Worksheet": "练习题",
    "Summary": "总结",
    "Encodings": "编码",
    "Encoding Numbers": "数字编码",
    "Error Detection": "错误检测",
    "Error Correction": "错误校正",
    "Quantifying Information": "信息的量化",
    "Variable-length Encodings": "变长编码",
}

_request = requests.sessions.Session.request


def request_with_timeout(self, method, url, **kwargs):
    kwargs.setdefault("timeout", 20)
    return _request(self, method, url, **kwargs)


requests.sessions.Session.request = request_with_timeout


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def should_translate(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if not re.search(r"[A-Za-z]", stripped):
        return False
    if stripped.startswith("$$") or stripped.endswith("$$"):
        return False
    if "\\begin{" in stripped or "\\end{" in stripped:
        return False
    if stripped.startswith("$") and stripped.endswith("$") and len(stripped) < 120:
        return False
    return True


def split_ws(text: str) -> tuple[str, str, str]:
    prefix_len = len(text) - len(text.lstrip())
    suffix_len = len(text) - len(text.rstrip())
    prefix = text[:prefix_len]
    suffix = text[len(text) - suffix_len :] if suffix_len else ""
    core = text[prefix_len : len(text) - suffix_len if suffix_len else len(text)]
    return prefix, core, suffix


def load_cache() -> dict[str, str]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8-sig"))
    return {}


def save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def source_path(filename: str) -> Path:
    path = SOURCE_DIR / filename
    if not path.exists():
        raise FileNotFoundError(path)
    return path


def soup_for(path: Path) -> BeautifulSoup:
    return BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")


def text_items(path: Path) -> list[str]:
    soup = soup_for(path)
    items: list[str] = []
    title = soup.find("title")
    if title and title.string and should_translate(title.string):
        items.append(normalize(title.string))

    for node in soup.find_all(string=True):
        if not isinstance(node, NavigableString):
            continue
        parent = node.parent
        if parent and parent.name in SKIP_PARENTS:
            continue
        text = str(node)
        if should_translate(text):
            items.append(normalize(text))
    return items


def suggested_chunks(chars: int) -> int:
    if chars <= 20000:
        return 1
    if chars <= 40000:
        return 2
    if chars <= 60000:
        return 3
    return max(4, math.ceil(chars / 20000))


def chunk_bounds(items: list[str], chunks: int) -> list[tuple[int, int]]:
    chunks = max(1, chunks)
    total = sum(len(item) for item in items)
    target = max(1, math.ceil(total / chunks))
    bounds: list[tuple[int, int]] = []
    start = 0
    acc = 0
    for i, item in enumerate(items):
        acc += len(item)
        remaining_items = len(items) - (i + 1)
        remaining_chunks = chunks - len(bounds) - 1
        if acc >= target and remaining_chunks > 0 and remaining_items > 0:
            bounds.append((start, i + 1))
            start = i + 1
            acc = 0
    bounds.append((start, len(items)))
    return bounds


def analyze(filename: str) -> dict[str, int | str]:
    path = source_path(filename)
    items = text_items(path)
    chars = sum(len(item) for item in items)
    chunks = suggested_chunks(chars)
    return {
        "file": filename,
        "text_blocks": len(items),
        "english_chars": chars,
        "suggested_chunks": chunks,
    }


def translate_core(translator: GoogleTranslator, core: str, cache: dict[str, str]) -> None:
    if not core:
        return
    if core in cache:
        return
    if core in MANUAL:
        cache[core] = MANUAL[core]
        save_cache(cache)
        return
    for attempt in range(4):
        try:
            cache[core] = translator.translate(core)
            save_cache(cache)
            return
        except Exception as exc:
            if attempt == 3:
                print(f"WARN: translation failed, keeping source: {core[:80]!r}: {exc}", file=sys.stderr)
                cache[core] = core
                save_cache(cache)
                return
            time.sleep(1.5 * (attempt + 1))


def translate_chunk(filename: str, chunk: int, chunks: int | None) -> dict[str, int | str]:
    path = source_path(filename)
    items = text_items(path)
    if chunks is None:
        chunks = suggested_chunks(sum(len(item) for item in items))
    bounds = chunk_bounds(items, chunks)
    if chunk < 1 or chunk > len(bounds):
        raise ValueError(f"chunk must be between 1 and {len(bounds)}")
    start, end = bounds[chunk - 1]
    cache = load_cache()
    translator = GoogleTranslator(source="en", target="zh-CN")
    for idx, core in enumerate(items[start:end], start + 1):
        print(f"{filename} chunk {chunk}/{len(bounds)} item {idx}/{len(items)}", flush=True)
        translate_core(translator, core, cache)
    return {
        "file": filename,
        "chunk": chunk,
        "chunks": len(bounds),
        "start": start + 1,
        "end": end,
    }


def fix_paths(soup: BeautifulSoup) -> None:
    html = soup.find("html")
    if html is not None:
        html["lang"] = "zh-CN"
    head = soup.find("head")
    if head is not None:
        head["lang"] = "zh-CN"

    for tag in soup.find_all(True):
        for attr in ("src", "href"):
            value = tag.get(attr)
            if not isinstance(value, str):
                continue
            if value.startswith("../labs/"):
                tag[attr] = "../" + value
            elif value.startswith("lecture_slides/"):
                tag[attr] = "../../lectures/" + value


def apply_cached_translation(text: str, cache: dict[str, str]) -> tuple[str, bool]:
    prefix, core, suffix = split_ws(text)
    normalized = normalize(core)
    if normalized in MANUAL:
        return prefix + MANUAL[normalized] + suffix, True
    if normalized in cache:
        return prefix + cache[normalized] + suffix, True
    return text, False


def build_file(filename: str, update: bool = True) -> dict[str, int | str]:
    path = source_path(filename)
    cache = load_cache()
    soup = soup_for(path)
    fix_paths(soup)
    missing = 0

    title = soup.find("title")
    if title and title.string and should_translate(title.string):
        translated, ok = apply_cached_translation(title.string, cache)
        missing += 0 if ok else 1
        title.string.replace_with(translated)

    for node in list(soup.find_all(string=True)):
        if not isinstance(node, NavigableString):
            continue
        parent = node.parent
        if parent and parent.name in SKIP_PARENTS:
            continue
        text = str(node)
        if should_translate(text):
            translated, ok = apply_cached_translation(text, cache)
            missing += 0 if ok else 1
            node.replace_with(translated)

    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    target = TARGET_DIR / filename
    body = "".join(str(item) for item in soup.contents if not isinstance(item, Doctype))
    body = re.sub(r"^html\s*(?=<html)", "", body, count=1)
    target.write_text("<!DOCTYPE html>\n" + body, encoding="utf-8", newline="\n")

    if missing == 0 and update:
        update_manifest({f"lectures/{filename}"})
    return {"file": filename, "target": str(target.relative_to(ROOT)), "missing": missing}


def update_manifest(translated_sources: set[str]) -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8-sig"))
    for entry in manifest["entries"]:
        if entry.get("source") in translated_sources:
            entry["status"] = "translated"
            entry["review"] = "pending"
            entry["notes"] = "Chinese lecture HTML generated in stage 3; requires human review for terminology and machine-translation phrasing."
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["analyze", "translate-chunk", "build", "translate-file"])
    parser.add_argument("filename")
    parser.add_argument("--chunk", type=int)
    parser.add_argument("--chunks", type=int)
    args = parser.parse_args()

    if args.command == "analyze":
        print(json.dumps(analyze(args.filename), ensure_ascii=False, indent=2))
    elif args.command == "translate-chunk":
        if args.chunk is None:
            raise SystemExit("--chunk is required")
        print(json.dumps(translate_chunk(args.filename, args.chunk, args.chunks), ensure_ascii=False, indent=2))
    elif args.command == "build":
        print(json.dumps(build_file(args.filename), ensure_ascii=False, indent=2))
    elif args.command == "translate-file":
        info = analyze(args.filename)
        chunks = int(info["suggested_chunks"])
        for chunk in range(1, chunks + 1):
            translate_chunk(args.filename, chunk, chunks)
        print(json.dumps(build_file(args.filename), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
