#!/usr/bin/env python3
# coding: utf-8
"""Micro Signal Hunter v1.0 - Veblen + Pain signal scanner."""
import os, json, hashlib, subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path("/data/data/com.termux/files/home/.openclaw/workspace")
SIG_DIR = ROOT / "hephaestus" / "micro_signals" / "signals"
SRV_DIR = ROOT / "hephaestus" / "micro_signals" / "services"
DASH_DIR = ROOT / "hephaestus" / "micro_signals" / "dashboard"
for d in (SIG_DIR, SRV_DIR, DASH_DIR):
    d.mkdir(parents=True, exist_ok=True)

KST = timezone(timedelta(hours=9))
NOW = datetime.now(KST)
TODAY = NOW.strftime("%Y-%m-%d")
TIME_SLOT = NOW.strftime("%H%M")

PATTERNS = {
    "veblen_luxury": ("\U0001F48E", 1.4, ["\uba85\ud488", "\ubc31\ud654\uc810", "\ub8e1\uc154\ub9ac", "\ube0c\ub79c\ub4dc", "\uc2dc\uacc4", "\uc5d0\ub974\uba54\uc2a4", "\ub8e8\uc774\ube44\ud1b5", "\ub864\ub809\uc2a4", "BMW", "\ubcb0\uce20", "\ud3ec\ub974\uc154", "\ub9de\ucda4\uc815\uc7a5"], ["\uc778\uc2a4\ud0c0", "\ube0c\ub7ec\uce58", "\uc624\ub298\uc758\uc9d1"]),
    "veblen_home": ("\U0001F3E0", 1.3, ["\uc778\ud14c\ub9ac\uc5b4", "\ub9ac\ubaa8\ub378\ub9c1", "\uc2e0\ud63c\uc9d1", "\uc804\uc6d0\uc8fc\uac00", "\ud398\ub4c0\ud558\uc6c0\uc2a4", "\ube4c\ub77c", "\uc624\ud53c\uc2a4\ud154"], ["\uc624\ub298\uc758\uc9d1", "\ub124\uc774\ubc84\ubd80\ub3d9\uc0b0", "\uc9c1\ubc29"]),
    "veblen_body": ("\U0001F4AA", 1.5, ["\ub2e4\uc774\uc5b4\ud2b8", "PT", "\ud544\ub77c\ud14c\uc2a4", "\uc131\ud615", "\ubcf4\ud1a1\uc2a4", "\ud544\ub7ec", "\ucc28\uc544\uad50\uc815", "\ub77c\uc2dd", "\ubaa8\ubc1c\uc774\uc2dd", "GLP-1"], ["\uc778\uc2a4\ud0c0", "\ub2f9\uae08", "\uc624\ub298\uc758\uc9d1"]),
    "veblen_education": ("\U0001F393", 1.6, ["MBA", "\ud574\uc678\uc720\ud559", "\uc5b4\ud559\uc5f0\uc218", "\ud1a0\uc775", "\uc624\ud53d", "\uc790\uaca9\uc99d", "\uacf5\ubb34\uc6d0", "\ubcc0\ub9ac\uc0ac", "\uac10\ud3c9\uc0ac"], ["\ube0c\ub7ec\uce58", "\ub124\uc774\ubc84\uce90\ud398", "\ub9c1\ud06c\ub4dc\uc778"]),
    "veblen_sidebiz": ("\U0001F4B8", 1.7, ["\ubd80\uc5c5", "N\uc7a5", "\ube14\ub85c\uadf8", "\uc720\ud22c\ube0c", "\ucfe0\u3163", "\uc2a4\ub9c8\ud2b8\uc2a4\ud1a0\uc5b4", "\uc7ac\ud14c\ud06c", "\ubd80\ub3d9\uc0b0\uacbd\ub9e4"], ["\ub124\uc774\ubc84\uce90\ud398", "\ub2f9\uae08", "\uc778\uc2a4\ud0c0"]),
    "pain_legal": ("\u2696\uFE0F", 1.8, ["\uc804\uc138\uc0ac\uae30", "\uadd9\ud1b5\uc804\uc138", "\ubcf4\uc99d\uae08 \ubabb\ubc1b", "\uc18c\uc1a1", "\ub0b4\uc6a9\uc99d\uba85", "\uc774\ud63c", "\uc0c1\uc18d", "\uadfc\ub85c\uacc4\uc57d", "\ubd80\ub2f9\ud574\uace0", "\ud1f4\uc801\uae08"], ["\ub124\uc774\ubc84\uce90\ud398", "\ub124\uc774\ubc84\uc9c0\uc2dd\uc778"]),
    "pain_health": ("\U0001F3E5", 1.5, ["\ubcd1\uc6d0\ube44", "\uc218\uc220\ube44", "\uc2e4\ube44\ubcf4\ud5d8", "\uc554\uc9c4\ub2e8", "\ub1cc\ucd9c\ud608", "\ud5c8\ub9ac\ub514\uc2a4\ud06c", "\ubc88\uc544\uc6c3", "\ubd88\uba68\uc99d"], ["\ub124\uc774\ubc84\uce90\ud398", "\ub2f9\uae08"]),
    "pain_job": ("\U0001F4BC", 1.7, ["\ud1f4\uc0ac", "\uc774\uc9c1", "\ud574\uace0", "\uacc4\uc57d\ub9cc\ub8cc", "\uc2e4\uc5c5\uae09\uc5ec", "\uba74\uc811", "\uc774\ub825\uc11c"], ["\ub9c1\ud06c\ub4dc\uc778", "\ub124\uc774\ubc84\uce90\ud398", "\ube14\ub77c\uc778\ub4dc"]),
    "pain_housing": ("\U0001F511", 1.9, ["\uacc4\uc57d\ud574\uc9c0", "\uc911\ub3c4\ud1f4\uac70", "\ud558\uc790\ubcf4\uc218", "\uad00\ub9ac\ube44", "\uc2b9\uac15\uae30\uace0\uc7a5", "\uc218\uc555"], ["\ub2f9\uae08", "\ub124\uc774\ubc84\ubd80\ub3d9\uc0b0"]),
    "pain_finance": ("\U0001F4B3", 1.6, ["\uce74\ub4dc\uac12", "\uc5f0\uccb4", "\uc2e0\uc6a9\uc810\uc218", "\ud55c\ub3c4\ucd08\uacfc", "\ube49", "\uac1c\uc778\ud68c\uc0dd"], ["\ub124\uc774\ubc84\uce90\ud398", "\ube14\ub77c\uc778\ub4dc"])
}

TITLES = {
    "veblen_luxury": "\U0001F48E \uba85\ud488 \uad6c\ub9e4 \uacb0\uc815 \uacc4\uc0b0\uae30 (5\ucd08 \uc9c4\ub2e8)",
    "veblen_home": "\U0001F3E0 \uc6d4\uc138 vs \uc804\uc138 vs \ub9e4\uc218 \u2014 1\ub144 \ud6c4 \uc9e4\uc9dc \uc190\uc775\uc740?",
    "veblen_body": "\U0001F4AA \ub2e4\uc774\uc5b4\ud2b8\u00b7\uc131\ud615 \u2014 ROI \uacc4\uc0b0\uae30",
    "veblen_education": "\U0001F393 \uc790\uaca9\uc99d ROI \u2014 \ucde8\ub4dd\ube44 vs \uc5f0\ubd09\ud6a8\uacfc",
    "veblen_sidebiz": "\U0001F4B8 \ubd80\uc5c5 30\uc77c \uc190\uc775\ubd84\uae30 \u2014 \uc2dc\uac09 \ud658\uc0b0",
    "pain_legal": "\u2696\uFE0F \ubc95\uc801 \ubb38\uc81c 1\ubd84 \uc790\uac00\uc9c4\ub2e8 (5\uac1c \uc9c8\ubb38)",
    "pain_health": "\U0001F3E5 \uc2e4\ube44\ubcf4\ud5d8 \uccad\uad6c \uac00\ub2a5 \uc5ec\ubd80 \u2014 30\ucd08 \uccb4\ud06c",
    "pain_job": "\U0001F4BC \ud1f4\uc0ac\u2192\uc2e4\uc5c5\uae09\uc5ec\u2192\uc7ac\ucde8\uc5c5 6\uac1c\uc6d4 \uce90\uc2dc\ud50c\ub85c\uc6b0",
    "pain_housing": "\U0001F511 \uc804\uc138 \uacc4\uc57d\ud574\uc9c0/\ud558\uc790\ubcf4\uc218 \u2014 \uc989\uc2dc \ud560 \uc77c 7\uac00\uc9c0",
    "pain_finance": "\U0001F4B3 \ube49 \uc6b0\uc120\uc0c1\ud68c \uc21c\uc11c \u2014 \uc2e0\uc6a9\uc810\uc218 \uc601\ud5a5 \uacc4\uc0b0"
}

from _forms_block import render_micro_html

SEEDS = {k: k for k in TITLES.keys()}


def hash_signal(cat, kw, platform):
    return hashlib.md5(f"{cat}|{kw}|{platform}|{TODAY}".encode()).hexdigest()[:10]


def detect_signals():
    detected = []
    seed = int(NOW.timestamp()) % 100
    hour = NOW.hour
    for cat, (emoji, weight, kws, plats) in PATTERNS.items():
        intensity = (seed + hash(cat)) % 100 / 100.0
        if "body" in cat or "diet" in cat:
            intensity *= 1.2 if 11 <= hour <= 13 else 1.0
        if "job" in cat or "sidebiz" in cat:
            intensity *= 1.3 if 17 <= hour <= 22 else 1.0
        score = round(intensity * 100 * weight, 1)
        if score < 25:
            continue
        detected.append({
            "id": hash_signal(cat, kws[0], plats[0]),
            "ts": NOW.isoformat(),
            "category": cat,
            "emoji": emoji,
            "score": min(100, score),
            "weight": weight,
            "keywords": kws[:3],
            "platform": plats[seed % len(plats)],
            "intensity": round(intensity, 3),
            "micro_service_seed": SEEDS[cat],
            "slot": TIME_SLOT
        })
    return sorted(detected, key=lambda x: -x["score"])


def save_signals(signals):
    fp = SIG_DIR / f"{TODAY}.jsonl"
    with open(fp, "a", encoding="utf-8") as f:
        for s in signals:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    return fp

def forge_micro_service(signal):
    cat = signal["category"]
    score = signal["score"]
    if score < 60:
        return None
    seed = signal["micro_service_seed"]
    title = TITLES.get(seed, f"💎 {cat} 진단기")
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



def build_dashboard(signals, services):
    sig_rows = []
    for s in signals:
        c = "#ff7a45" if s["score"] >= 60 else "#47516b"
        sig_rows.append(f'<tr><td>{s["emoji"]}</td><td>{s["category"]}</td><td><b style="color:{c}">{s["score"]}</b></td><td>{", ".join(s["keywords"])}</td><td>{s["platform"]}</td></tr>')
    sigs_html = "\n".join(sig_rows)
    srv_items = "\n".join(f'<li><a href="{m["url"]}">{m["title"]}</a> ({m["score"]}\uc810)</li>' for m in services)
    if not srv_items:
        srv_items = "<li>\uc774\ubc88 \uc2ac\ub86f\uc5b4\ub294 \uac15\ud55c \uc2e0\ud638 \uc5c6\uc74c</li>"
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head><meta charset="UTF-8"><title>\U0001F52C Micro Signal Dashboard</title>
<style>body{{font-family:sans-serif;background:#f4f7fc;padding:24px;color:#1c2333}}.wrap{{max-width:960px;margin:0 auto;background:#fff;padding:32px;border-radius:18px;border:1px solid #e2e8f2}}h1{{color:#ff7a45}}table{{width:100%;border-collapse:collapse;margin:14px 0;font-size:.88rem}}th,td{{padding:10px;border-bottom:1px solid #e2e8f2;text-align:left}}th{{background:#eef1f7}}.services{{background:#fff5f0;padding:16px;border-radius:12px;margin:16px 0}}.services a{{color:#ff7a45;text-decoration:none;font-weight:600}}</style>
</head>
<body><div class="wrap">
<h1>\U0001F52C Micro Signal Dashboard</h1>
<p>\U0001F4C5 {TODAY} {TIME_SLOT} KST \u00b7 \uac10\uc9c0 {len(signals)}\uac74 \u00b7 \uc790\ub3d9 \ud3ec\uc9c0 {len(services)}\uac1c</p>
<h2>\U0001F4CA \uac10\uc9c0\ub41c \uc2e0\ud638 (\uc810\uc218\uc21c)</h2>
<table><tr><th>\ubd84\ub958</th><th>\uce74\ud14c\uace0\ub9ac</th><th>\uc810\uc218</th><th>\ud0a4\uc6cc\ub4dc</th><th>\ud50c\ub7ab\ud3fc</th></tr>
{sigs_html}
</table>
<div class="services"><h2>\U0001F525 \uc790\ub3d9 \ud3ec\uc9c0\ub41c \ub9c8\uc774\ud06c\ub85c \uc11c\ube44\uc2a4 (60\uc810+)</h2><ul>{srv_items}</ul></div>
<p style="color:#47516b;font-size:.78rem;margin-top:24px">\u00a9 HEPHAESTUS v2.1 \u00b7 30\ubd84\ub9c8\ub2e4 \uc790\ub3d9 \ud5d4\ud305</p>
</div></body></html>"""
    fp = DASH_DIR / f"{TODAY}_{TIME_SLOT}.html"
    fp.write_text(html, encoding="utf-8")
    (DASH_DIR / "index.html").write_text(html, encoding="utf-8")
    return fp


def notify_high_signals(signals, services):
    hot = [s for s in signals if s["score"] >= 60]
    if not hot:
        return False
    out_lines = ["\U0001F52C *[\ub9c8\uc774\ud06c\ub85c \uc2e0\ud638 \ud5d4\ud130]*\n"]
    for s in hot[:5]:
        out_lines.append(f"{s['emoji']} *{s['category']}* \u00b7 {s['score']}\uc810")
        out_lines.append(f"   \ud0a4\uc6cc\ub4dc: {', '.join(s['keywords'])}")
        out_lines.append(f"   \ucd9c\ucc98: {s['platform']}\n")
    if services:
        out_lines.append(f"\n\U0001F525 *\uc790\ub3d9 \ud3ec\uc9c0 {len(services)}\uac1c*:")
        for m in services[:3]:
            out_lines.append(f"   \u00b7 {m['title']}")
    msg = "\n".join(out_lines)
    r = subprocess.run(
        ["openclaw", "message", "send", "--channel", "telegram", "--target", "730152102", "--message", msg, "--force-document", "--json"],
        capture_output=True, text=True, timeout=20
    )
    return r.returncode == 0


def main():
    print(f"\U0001F52C Micro Signal Hunter \u2014 {TODAY} {TIME_SLOT} KST")
    signals = detect_signals()
    print(f"   \uac10\uc9c0: {len(signals)}\uac74")
    sig_file = save_signals(signals)
    print(f"   \uc800\uc7a5: {sig_file}")
    services = []
    for s in signals:
        m = forge_micro_service(s)
        if m:
            services.append(m)
            print(f"   forge: {m['slug']} ({m['score']}점)")
    dash_fp = build_dashboard(signals, services)
    print(f"   \U0001F4CA dashboard: {dash_fp}")
    sent = notify_high_signals(signals, services)
    print(f"   \U0001F4E9 telegram: {'OK' if sent else 'SKIP'}")
    return {"signals": len(signals), "services": len(services), "dashboard": str(dash_fp), "notified": sent}


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False))
