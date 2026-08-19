import sys
fn = "signal_hunter.py"
with open(fn, encoding="utf-8") as f:\n    src = f.read()\n\n# 1) SEEDS 라인 위에 import 추가\nold = "SEEDS = {k: k for k in TITLES.keys()}"
new = "from _forms_block import render_micro_html\n\nSEEDS = {k: k for k in TITLES.keys()}"
if old in src:
    src = src.replace(old, new, 1)
    print("SEEDS import 삽입")
else:
    print("SEEDS 라인 없음, 이미 적용됨?")

# 2) forge_micro_service 함수 통째 교체
if "def forge_micro_service(signal):" in src:
    si = src.index("def forge_micro_service(signal):")
    ei = src.index("def build_dashboard")

    new_forge = '''def forge_micro_service(signal):
    cat = signal["category"]
    score = signal["score"]
    if score < 60:
        return None
    seed = signal["micro_service_seed"]
    title = TITLES.get(seed, f"\\U0001F52C {cat} 진단기")
    html = render_micro_html(cat, title)
    if not html:
        return None
    slug = f"micro_{cat}_{TIME_SLOT}"
    out = SRV_DIR / f"{slug}.html"
    out.write_text(html, encoding="utf-8")
    meta = {
        "slug": slug,
        "title": title,
        "category": cat,
        "score": score,
        "url": f"https://mdpepastor3004.github.io/prometheus-utils/micro_signals/services/{slug}.html",
        "created": NOW.isoformat(),
    }
    (SRV_DIR / f"{slug}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest_fp = SRV_DIR / "manifest.json"
    manifest = []
    if manifest_fp.exists():
        try:
            manifest = json.loads(manifest_fp.read_text(encoding="utf-8"))
        except Exception:
            manifest = []
    if not any(m.get("slug") == slug for m in manifest):
        manifest.append(meta)
        manifest_fp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return meta


'''
    src = src[:si] + new_forge + src[ei:]
    print("forge_micro_service 교체")
else:
    print("forge 함수 없음, 이미 적용됨?")

with open(fn, "w", encoding="utf-8") as f:\n    f.write(src)\nprint("done")
