# 🔥 HEPHAESTUS — 마이크로 유틸리티 주조 공장
> Prometheus v2.0 · Micro-Utility Forge

---

## 설치된 유틸리티

| # | 유틸리티 | 경로 | 용량 | 상태 |
|---|---------|------|------|------|
| 1 | CheongyakCalc | `hephaestus/cheongyakcalc/index.html` | 12KB | ✅ 완료 |
| 2 | JeonseGuard | `hephaestus/jeonseguard/index.html` | 11KB | ✅ 완료 |

---

## CheongyakCalc — 청약 가점 계산기

**해결하는 마찰:** "청약 가점 계산 복잡해요"

**기능:**
- 무주택기간 (1년 2점, 최대 32점)
- 부양가족수 (1명 5점, 최대 35점)
- 청약통장 가입기간 (1년 1점, 최대 17점)
- 총점 84점 만점 실시간 계산
- 지역별 당첨 가능성 표 (강남~지방 10개 권역)
- 특별공급 자격 확인 (신혼부부/생애최초/다자녀/노부모)
- 당첨 커트라인 예측

**스택:** 단일 HTML + CSS + JS (제로 의존성)

---

## JeonseGuard — 전세 안전도 분석기

**해결하는 마찰:** "전세금 안전한지 확인하기 어려워요"

**기능:**
- 전세가율 계산 (전세금 / 매매가 × 100)
- 위험 점수 1~10점 산출
- 건물 유형별 위험도 (아파트 < 단독 < 오피스텔 < 빌라)
- 건물 연식 반영
- 등기부등본 체크리스트 생성
- 깡통전세 위험 경고
- 맞춤형 액션 아이템 제공

**스택:** 단일 HTML + CSS + JS (제로 의존성)

---

## 배포 경로

### GitHub Pages (권장)
```bash
# 1. GitHub repo 생성
# 2. 각 유틸리티 폴더 통째로 push
# 3. GitHub Pages → root → `hephaestus/cheongyakcalc/`
# 4. 커스텀 도메인 연결

### Vercel (무료)
Each folder = independent deployment

### 로컬 (Termux)
python3 -m http.server 8080
# 브라우저에서 http://localhost:8080/hephaestus/cheongyakcalc/
```

---

## 향후 로드맵

### Priority 1 (이번 주)
- [x] CheongyakCalc — 청약 가점 계산기
- [x] JeonseGuard — 전세 안전도 분석기
- [ ] GradeCalc — 수능 등급 계산기
- [ ] WordForge — 망각곡선 영단어 카드

### Priority 2 (다음 주)
- [ ] ExamPlanner — 시험 D-day 학습 플래너
- [ ] RentVsBuy — 월세 vs 전세 손익 계산기
- [ ] RealPriceMap — 실거래가 트렌드 차트

### Priority 3 (3주차)
- [ ] Dev Legion — 자동 코드 생성 파이프라인 구축
- [ ] Synapse — 마찰 데이터 수집 → 명세서 자동 생성 루프

---

## 퍼널 전략

유틸리티 → 무료 사용 → 신뢰 획득 → 전자책/리포트 링크 → 구매 전환

각 유틸리티 하단에는 `funnel` 섹션이 내장되어 있음.
추가할 링크:
- `/ebook_daily/` 경로의 전세사기/AI/저임금 전자책
- 구독 폼 (이메일 수집)
- 관련 HEO 콘텐츠

© 자룡봇 AI Research · Prometheus v2.0