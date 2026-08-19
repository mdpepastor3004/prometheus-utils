# 🔥 HEPHAESTUS — 마이크로 유틸리티 주조 공장
> Prometheus v2.0 · Template-Driven Micro-Utility Forge

---

## 📐 아키텍처 (v2.0)

```
hephaestus/
├── templates/
│   └── p-template.html          ← 공통 뼈대 (CSS, GA, 모달, 리드캡처, 공유바, 토스트)
├── specs/
│   └── v2_utilities.json        ← 유틸리티 명세서 (JSON 메타데이터)
├── scripts/
│   ├── build_prometheus.py      ← 빌드 엔진 (JSON+템플릿 → HTML 생성)
│   ├── {slug}_body.html         ← 각 유틸 고유 UI 바디
│   ├── {slug}_script.js         ← 각 유틸 계산/동작 로직
│   └── {slug}_style.html        ← 선택적 추가 CSS
├── cheongyakcalc/               ← ✅ 빌드 결과물 1
├── jeonseguard/                 ← ✅ 빌드 결과물 2
├── gradecalc/                   ← ✅ 빌드 결과물 3
├── wordforge/                   ← ✅ 빌드 결과물 4
└── SYSTEM.md                    ← 이 파일
```

## 🏗️ 새 유틸리티 만드는 법 (STEP-BY-STEP)

### Step 1: 명세서 등록
`specs/v2_utilities.json`에 엔트리 추가:
```json
{
  "slug": "myutil",
  "title": "내 유틸리티 이름",
  "title_short": "짧은제목",
  "emoji": "🎯",
  "subtitle": "설명 한 줄",
  "desc": "메타 설명",
  "keywords": "키워드1, 키워드2",
  "lead_source": "myutil",
  "lead_benefits": "혜택<br>목록",
  "lead_pdf": "../ebook/report.pdf",
  "funnel_tag": "프리미엄 리포트",
  "funnel_text": "CTA 문구",
  "funnel_btn": "무료로 받기",
  "funnel_sub": "보너스 안내"
}
```

### Step 2: BODy + SCRIPT 작성
- `scripts/myutil_body.html` — 유틸 고유 UI (HTML 구조만)
- `scripts/myutil_script.js` — 계산 로직 및 상호작용 (JS 함수만)
- `scripts/myutil_style.html` — 필요하면 추가 CSS (선택)

### Step 3: 빌드 실행
```bash
python3 scripts/build_prometheus.py all     # 전체
python3 scripts/build_prometheus.py myutil  # 하나만
```

결과물: `myutil/index.html` (단일 HTML 파일)

---

## 템플릿 시스템의 핵심 설계

### `p-template.html`이 제공하는 것
1. **테마 시스템** — CSS 변수 기반 Glass Luxury Dark (`:root`)
2. **공통 컴포넌트**:
   - 슬라이더 + 숫자입력 듀얼 UI
   - SVG 링 게이지 (원형 프로그레스)
   - 점수 대시보드 (분해 그리드)
   - 바 차트
   - 결과 표 (pass/fail 커틀라인)
   - 판정 배너 (grade별 색상은별 상태)
   - 공유 버튼 (링크복사/캡처/카톡)
   - 리드 캡처 모달 (Supabase POST → Telegram 알림)
   - 토스트 알림
   - localStorage 저장/복원 헬퍼
3. **퍼널 통합** — 하단 CTA → 리드 캡처 → PDF 제공 → 텔레그램 알림
4. **SEO** — title, meta, OG 태그 자동 삽입
5. **GA4 스니펫** — placeholder 포함

### 치환 가능한 슬롯 (`{{SLUG}}`)
| 슬롯 | 설명 | 예시 |
|------|------|------|
| `{{TITLE}}` | 페이지 제목 | 수능 등급 계산기 2027 |
| `{{TITLE_SHORT}}` | 헤더 제목 | 수능 등급컷 계산기 |
| `{{EMOJI}}` | 헤더 이모지 | 🎓 |
| `{{SUBTITLE}}` | 부제 | 원점수 입력시 예상 등급 확인 |
| `{{DESC}}` | 메타 설명 | … |
| `{{KEYWORDS}}` | 메타 키워드 | 수능등급계산기, 등급컷… |
| `{{OG_URL}}` | OG URL | https://.../gradecalc/ |
| `{{LEAD_SOURCE}}` | 리드 소스 식별 | gradecalc |
| `{{LEAD_BENEFITS}}` | 리드 혜택 | … |
| `{{LEAD_PDF}}` | 다운로드 경로 | ../ebook/2027_grade_report.pdf |
| `{{FUNNEL_TAG}}` | CTA 뱃지 | 🚀 정시 합격 예측 |
| `{{FUNNEL_TEXT}}` | CTA 본문 | 내 점수로 갈 수 있는 대학은? |
| `{{FUNNEL_BTN}}` | 버튼 텍스트 | 지금 바로 확인하기 |
| `{{FUNNEL_SUB}}` | 버튼 아래 글 | ✔ 주요 15개 대학 합격선 포함 |
| `{{BODY}}` | 유틸 고유 HTML | body.html 내용 삽입 |
| `{{SCRIPT}}` | 유틸 JS | script.js 내용 삽입 |
| `{{STYLE_EXTRA}}` | 추가 CSS | style.html 내용 삽입 |

### 공통 JS API (모든 유틸에서 사용 가능)
```javascript
gId(id)       // document.getElementById
st(msg, err?) // 토스트 알림
svls(key,obj) // localStorage 저장 (try/catch)
ldls(key,def) // localStorage 읽기

// 리드캡처 함수들 (자동 정의됨)
openLead(), closeLead()
sLead() // Supabase → Telegram fallback

// 공유 함수들 (자동 정의됨)
cpLink(), screenShot(), shareKakao()
```

---

## 현재 유틸리티 목록

| # | 유틸리티 | 경로 | 용량 | 상태 |
|---|---------|------|------|------|
| 1 | CheongyakCalc | `cheongyakcalc/` | ~16KB | ✅ 완료 (v1 레거시, 추후 템플릿으로 마이그레이션) |
| 2 | JeonseGuard | `jeonseguard/` | ~15KB | ✅ 완료 (v1 레거시) |
| 3 | GradeCalc | `gradecalc/` | ~29KB | ✅ 템플릿 v2 |
| 4 | WordForge | `wordforge/` | ~29KB | ✅ 템플릿 v2 |

---

## 퍼널 전략

유틸리티 → 무료 사용 → 신뢰 획득 → 전자책/리포트 링크 → 구매 전환

**리드 흐름:**
1. 사용자 유틸리티 사용 중
2. 하단 CTA 클릭 → 모달 표시
3. 이름/전화/이메일 입력
4. **Supabase POST** (leads 테이블) → 실패 시 **Telegram 알림** fallback
5. 성공 시 PDF 제공 + "신청 완료!" 토스트
6. 리드 데이터는 `source`(예: gradecalc), `score`(사용 데이터), `device`(mobile/pc) 포함

---

## 향후 로드맵

### Priority 1
- [x] GradeCalc — 수능 등급 계산기 (템플릿 v2)
- [x] WordForge — 망각곡선 영단어 카드 (템플릿 v2)
- [ ] 기존 유틸리티(v1)를 템플릿 v2로 마이그레이션

### Priority 2 (다음 프로젝트 준비)
- [ ] ExamPlanner — 시험 D-day 학습 플래너
- [ ] RentVsBuy — 월세 vs 전세 손익 계산기
- [ ] RealPriceMap — 실거래가 트렌드 차트

### Priority 3 (자동화)
- [ ] Synapse — 커뮤니티 고통(OCULUS) → 명세서(JSON) 자동 생성
- [ ] Dev Legion — 명세서 → 템플릿 코드 자동 생성

© 자룡봇 AI Research · Prometheus v2.0 · 템플릿 시스템 탑재
