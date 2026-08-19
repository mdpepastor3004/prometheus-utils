#!/usr/bin/env bash
# 🔥 PROMETHEUS v3.1 — 유틸리티 자동 디플로이 스크립트
# 규칙: 유틸/마이크로/헌터/전자책 → 자동 push
#       RPG(P10/흙수저/multiverse_*) → ❌ 절대 push 안 함
#       workspace 루트의 rpg/, multiverse_rpg/, heuksujeo-rpg/ 등 절대 추가 안 됨

set -e

cd "$(dirname "$0")/.."

echo "🔍 Push 직전 안전 가드: RPG 디렉토리 staging area 확인..."
FORBIDDEN=$(git status --porcelain | grep -E '\s(rpg|multiverse_rpg|heuksujeo-rpg|multiverse_p[0-9]+|P10_하이브리드)' || true)
if [ -n "$FORBIDDEN" ]; then
  echo "❌ ABORT: RPG 파일이 staging area에 감지됨"
  echo "$FORBIDDEN"
  exit 1
fi

# P10 RPG PDF 파일명 패턴이 anywhere에 있는지도 확인
if [ -n "$(git status --porcelain | grep -iE 'P10|하이브리드|multiverse_p' || true)" ]; then
  echo "❌ ABORT: P10/멀티버스 RPG 파일명 감지됨"
  git status --porcelain | grep -iE 'P10|하이브리드|multiverse_p'
  exit 1
fi

echo "✅ 안전 가드 통과 — RPG 흔적 0건"
echo "--- 변경 파일 (안전) ---"
git status --short | head -30
echo "--- commit + push ---"
git add -A
MSG="${1:-🔥 auto: 유틸/마이크로 자동 디플로이 $(date +%Y-%m-%d_%H%M) KST}"
git commit -m "$MSG" || { echo "⚠️ 변경 없음 — skip"; exit 0; }
BR=$(git rev-parse --abbrev-ref HEAD)
if [ "$BR" = "main" ]; then
  git push origin main
  echo "✅ main에 push 완료 → GitHub Pages 자동 배포"
else
  echo "ℹ️ feature 브랜치($BR) — push만"
  git push origin "$BR"
fi
