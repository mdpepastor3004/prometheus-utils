#!/usr/bin/env bash
# HEPHAESTUS deploy utility — policy-aware micro-signal/service/manifest push.
#
# 정책 (PR #6 / 2026-08-19 확정):
#   ✅ 마이크로 신호/서비스/매니페스트 → 자동 푸시 (GitHub Pages → PROMETHEUS)
#   ❌ RPG(P10/흙수저/multiverse_*) 절대 푸시 ❌
#   🛡️ staging에서 RPG 패턴 발견 시 자동 ABORT
#
# Usage: bash hephaestus/scripts/deploy_utils.sh '🔬 헌터 자동 디플로이'
set -euo pipefail

MSG="${1:-🔬 헌터 자동 디플로이}"
cd "$(dirname "$0")/.."  # repo root (hephaestus/)

echo "🛡️ RPG 패턴 가드 검사..."
if git status --porcelain | grep -E "(P10|흙수저|multiverse_)" >/dev/null 2>&1; then
  echo "🛑 ABORT: staging에 RPG 패턴(P10/흙수저/multiverse_*) 발견 → 푸시 금지"
  exit 1
fi
if git diff --cached --name-only | grep -E "(P10|흙수저|multiverse_)" >/dev/null 2>&1; then
  echo "🛑 ABORT: index에 RPG 패턴 → 푸시 금지"
  exit 1
fi
echo "✅ RPG 가드 통과"

# micro_signals 디렉토리만 staging에 포함되어 있는지 확인
STAGED=$(git status --porcelain | awk '{print $2}' | grep -v "^micro_signals/" | grep -v "^$" || true)
if [ -n "$STAGED" ]; then
  echo "⚠️ micro_signals 외 변경 감지: $STAGED"
  echo "    헌터 자동 디플로이 범위 외 — 수동 검토 필요. 마이크로만 푸시합니다."
fi

# 변경된 micro_signals 파일만 add
git add micro_signals/ 2>/dev/null || true

if git diff --cached --quiet; then
  echo "ℹ️ 커밋할 micro_signals 변경 없음 — 푸시 스킵"
  exit 0
fi

git commit -m "$MSG" --no-verify
BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "🚀 푸시: origin/$BRANCH"
git push origin "$BRANCH"
echo "✅ 디플로이 완료: origin/$BRANCH"
