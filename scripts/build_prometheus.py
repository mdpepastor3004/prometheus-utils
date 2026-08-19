#!/usr/bin/env python3
"""PROMETHEUS 템플릿 빌더"""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL_PATH = os.path.join(BASE, "templates", "p-template.html")
SPEC_PATH = os.path.join(BASE, "specs", "v2_utilities.json")


def load_specs():
    with open(SPEC_PATH, encoding="utf-8") as f:
        return json.load(f)


def substitute(template, mapping):
    out = template
    for key, val in mapping.items():
        out = out.replace("{{" + key + "}}", val)
    return out


def read_or_empty(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return f.read()
    return ""


def build_one(spec):
    slug = spec["slug"]
    out_dir = os.path.join(BASE, slug)
    os.makedirs(out_dir, exist_ok=True)

    with open(TPL_PATH, encoding="utf-8") as f:
        tpl = f.read()

    mapping = {
        "TITLE": spec.get("title", ""),
        "TITLE_SHORT": spec.get("title_short", ""),
        "EMOJI": spec.get("emoji", ""),
        "SUBTITLE": spec.get("subtitle", ""),
        "DESC": spec.get("desc", ""),
        "KEYWORDS": spec.get("keywords", ""),
        "LEAD_SOURCE": spec.get("lead_source", ""),
        "LEAD_BENEFITS": spec.get("lead_benefits", ""),
        "LEAD_PDF": spec.get("lead_pdf", "../ebook/report.pdf"),
        "FUNNEL_TAG": spec.get("funnel_tag", "프리미엄 리포트"),
        "FUNNEL_TEXT": spec.get("funnel_text", ""),
        "FUNNEL_BTN": spec.get("funnel_btn", "무료로 받기"),
        "FUNNEL_SUB": spec.get("funnel_sub", ""),
        "OG_URL": f"https://mdpepastor3004.github.io/prometheus-utils/{slug}/",
        "BODY": read_or_empty(os.path.join(BASE, "scripts", f"{slug}_body.html")),
        "SCRIPT": read_or_empty(os.path.join(BASE, "scripts", f"{slug}_script.js")),
        "STYLE_EXTRA": read_or_empty(os.path.join(BASE, "scripts", f"{slug}_style.html")),
    }

    html = substitute(tpl, mapping)
    target = os.path.join(out_dir, "index.html")
    with open(target, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK {slug} -> {target} ({os.path.getsize(target)} bytes)")


def main():
    specs = load_specs()
    if len(sys.argv) > 1 and sys.argv[1] != "all":
        targets = [s for s in specs if s["slug"] == sys.argv[1]]
        if not targets:
            print(f"NOT FOUND: {sys.argv[1]}")
            sys.exit(1)
        specs = targets
    for spec in specs:
        build_one(spec)


if __name__ == "__main__":
    main()
