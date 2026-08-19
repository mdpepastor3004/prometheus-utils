#!/usr/bin/env bash
# build_from_template.sh — 템플릿 시스템으로 유틸리티 빌드
# Usage: bash build_from_template.sh [slug]
#   slug: gradecalc | wordforge | all

set -euo pipefail
cd "$(dirname "$0")/.."
BASE="$PWD"
TPL="$BASE/templates/p-template.html"
SPEC="$BASE/specs/v2_utilities.json"
OUTDIR="$BASE"

if ! command -v jq &>/dev/null; then echo "❌ jq 필요함"; exit 1; fi

build_one() {
  local slug="$1"
  local spec
  spec=$(jq -r ".[] | select(.slug==\"$slug\")" "$SPEC")
  [[ -z "$spec" || "$spec" == "null" ]] && echo "❌ 명세서 없음: $slug" && return 1

  # 필드 추출
  TITLE=$(echo "$spec" | jq -r '.title')
  TITLE_SHORT=$(echo "$spec" | jq -r '.title_short')
  EMOJI=$(echo "$spec" | jq -r '.emoji')
  SUBTITLE=$(echo "$spec" | jq -r '.subtitle')
  DESC=$(echo "$spec" | jq -r '.desc')
  KEYWORDS=$(echo "$spec" | jq -r '.keywords')
  LEAD_SOURCE=$(echo "$spec" | jq -r '.lead_source')
  LEAD_BENEFITS=$(echo "$spec" | jq -r '.lead_benefits')
  LEAD_PDF=$(echo "$spec" | jq -r '.lead_pdf')
  FUNNEL_TAG=$(echo "$spec" | jq -r '.funnel_tag')
  FUNNEL_TEXT=$(echo "$spec" | jq -r '.funnel_text')
  FUNNEL_BTN=$(echo "$spec" | jq -r '.funnel_btn')
  FUNNEL_SUB=$(echo "$spec" | jq -r '.funnel_sub')
  OG_URL="https://mdpepastor3004.github.io/prometheus-utils/$slug/"

  # 과목별 스크립트 파일 읽기
  SCRIPT_FILE="$BASE/scripts/${slug}_script.js"
  SCRIPT=""
  STYLE_EXTRA=""
  BODY_FILE="$BASE/scripts/${slug}_body.html"

  if [[ -f "$SCRIPT_FILE" ]]; then
    SCRIPT=$(cat "$SCRIPT_FILE")
  fi
  if [[ -f "$BASE/scripts/${slug}_style.html" ]]; then
    STYLE_EXTRA=$(cat "$BASE/scripts/${slug}_style.html")
  fi
  if [[ -f "$BODY_FILE" ]]; then
    BODY=$(cat "$BODY_FILE")
  fi

  # 대상 경로
  TARGET="$OUTDIR/$slug"
  mkdir -p "$TARGET"

  # 템플릿 치환
  sed \
    -e "/{{STYLE_EXTRA}}/{r /dev/stdin" -e "d" -e "}" \
    "$TPL" <<<"$STYLE_EXTRA" \
  | sed \
    -e "s|{{TITLE}}|$TITLE|g" \
    -e "s|{{TITLE_SHORT}}|$TITLE_SHORT|g" \
    -e "s|{{EMOJI}}|$EMOJI|g" \
    -e "s|{{SUBTITLE}}|$SUBTITLE|g" \
    -e "s|{{DESC}}|$DESC|g" \
    -e "s|{{KEYWORDS}}|$KEYWORDS|g" \
    -e "s|{{LEAD_SOURCE}}|$LEAD_SOURCE|g" \
    -e "s|{{LEAD_BENEFITS}}|$LEAD_BENEFITS|g" \
    -e "s|{{LEAD_PDF}}|$LEAD_PDF|g" \
    -e "s|{{FUNNEL_TAG}}|$FUNNEL_TAG|g" \
    -e "s|{{FUNNEL_TEXT}}|$FUNNEL_TEXT|g" \
    -e "s|{{FUNNEL_BTN}}|$FUNNEL_BTN|g" \
    -e "s|{{FUNNEL_SUB}}|$FUNNEL_SUB|g" \
    -e "s|{{OG_URL}}|$OG_URL|g" \
    -e "/{{BODY}}/{r /dev/stdin" -e "d" -e "}" \
    <(echo "$BODY") \
  | sed \
    -e "/{{SCRIPT}}/{r /dev/stdin" -e "d" -e "}" \
    <(echo "$SCRIPT") \
  > "$TARGET/index.html"

  echo "✅ $slug → $TARGET/index.html ($(wc -c < "$TARGET/index.html") bytes)"
}

if [[ "$1" == "all" ]]; then
  for slug in $(jq -r '.[].slug' "$SPEC"); do
    build_one "$slug"
  done
else
  build_one "$1"
fi
