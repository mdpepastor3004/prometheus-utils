# 🚀 PROMETHEUS — 오픈소스 스택 인벤토리

> "바퀴를 재창조하지 말고, 유명한 기업/사람들이 오픈소스로 뿌린 기술을 활용한다"
> — 원장님 지시 (2026-08-20)

## 1. 핵심 원칙

1. **무료/오픈소스 우선**: 라이선스 비용 없는 OSS 먼저 고려
2. **신뢰도 검증**: GitHub Star 1k+ 또는 대기업/유명인(MS, Google, Meta, Vercel, Supabase 등)이 관리/출시
3. **문서화 & 커뮤니티**: 공식 문서가 잘 되어 있고, 활성 커뮤니티 존재
4. **바퀴 재창조 ❌**: 자체 구현보다 검증된 라이브러리 활용

---

## 2. 카테고리별 추천 스택

### 2.1. 프론트엔드 프레임워크
- **Astro** (`@astrojs/*`) — Vercel/Netlify 출신, 정적 사이트 + islands 아키텍처, MDX 지원
- **Next.js** (`next`) — Vercel, React 풀스택 프레임워크, SSG/SSR 지원
- **SvelteKit** (`@sveltejs/kit`) — Rich Harris, 가볍고 빠른 풀스택 프레임워크

### 2.2. UI 컴포넌트 & 스타일
- **Tailwind CSS** (`tailwindcss`) — Adam Wathan, 유틸리티 우선 CSS 프레임워크
- **shadcn/ui** (`shadcn-ui`) — Vercel 출신, Radix UI + Tailwind 기반 복붙형 컴포넌트
- **Radix UI** (`@radix-ui/*`) — WorkOS, 헤드리스 컴포넌트
- **Lucide Icons** (`lucide-react`) — Lucide, 깔끔한 SVG 아이콘 세트
- **Heroicons** (`@heroicons/react`) — Tailwind Labs, Tailwind 제작팀의 아이콘

### 2.3. 차트 & 시각화
- **Chart.js** (`chart.js`) — Chart.js 팀, 간단한 차트
- **D3.js** (`d3`) — Mike Bostock, 고도화된 데이터 시각화
- **Recharts** (`recharts`) — Recharts 팀, React 차트 (D3 기반)
- **Observable Plot** (`@observablehq/plot`) — Observable, 선언적 차트

### 2.4. 데이터/DB
- **Supabase** (`@supabase/supabase-js`) — 오픈소스 BaaS (Postgres, Auth, Storage)
- **Prisma** (`@prisma/client`) — Prisma, TypeScript ORM
- **Drizzle ORM** (`drizzle-orm`) — Drizzle 팀, 가벼운 TypeScript ORM

### 2.5. 서버리스/배포
- **Cloudflare Workers** (`wrangler`) — Cloudflare, 엣지 서버리스
- **Vercel Functions** — Vercel, Next.js와 통합
- **Deno Deploy** — Deno, 엣지 서버리스

### 2.6. 이메일/알림
- **Resend** (`resend`) — Vercel 출신, 개발자 친화적 이메일 API
- **Nodemailer** (`nodemailer`) — Node.js 이메일 라이브러리
- **Telegram Bot API** — Telegram, 무료 봇 알림
- **Slack Web API** — Slack, 무료 알림/통합

### 2.7. PDF 생성/처리
- **Typst** (`typst`) — Typst 팀, LaTeX 대체 신생 마크업
- **pdf.js** (`pdfjs-dist`) — Mozilla, 브라우저 PDF 뷰어
- **jsPDF** (`jspdf`) — 클라이언트 PDF 생성
- **react-pdf** (`@react-pdf/renderer`) — React PDF 생성

### 2.8. OCR/이미지 처리
- **Tesseract.js** (`tesseract.js`) — 클라이언트 OCR
- **Sharp** (`sharp`) — Node.js 이미지 처리 (리사이징, 포맷 변환)
- **Pillow** (`PIL`) — Python 이미지 처리

### 2.9. 데이터 파싱/처리
- **PapaParse** (`papaparse`) — CSV 파싱
- **Cheerio** (`cheerio`) — 서버 사이드 HTML 파싱 (jQuery-like)
- **Turndown** (`turndown`) — HTML → Markdown 변환

### 2.10. 지도/지오로케이션
- **Leaflet** (`leaflet`) — Vladimir Agafonkin, 가벼운 지도
- **OpenStreetMap** — 무료 오픈스트리트맵
- **Mapbox GL JS** — Mapbox, 고성능 지도 (무료 티어)

### 2.11. AI/ML (클라이언트)
- **Hugging Face Transformers.js** (`@huggingface/transformers`) — Hugging Face, 브라우저 AI
- **TensorFlow.js** (`@tensorflow/tfjs`) — Google, 브라우저 ML
- **ONNX Runtime Web** (`onnxruntime-web`) — Microsoft, 경량 추론

### 2.12. 유틸리티
- **date-fns** (`date-fns`) — 날짜 유틸리티
- **Lodash** (`lodash`) — JS 유틸리티
- **Zod** (`zod`) — TypeScript-first 스키마 검증
- **Valibot** (`valibot`) — 가벼운 스키마 검증

### 2.13. 한국 공공데이터
- **공공데이터포털 (data.go.kr)** — 한국 정부 무료 데이터
- **KOSIS (통계청)** — 한국 통계 데이터
- **DART** — 전자공시시스템
- **KIPRIS** — 특허정보검색
- **국회의안** — 입법 데이터
- **감사원** — 감사 데이터

### 2.14. 한국형 특별 스택
- **Supertonic (TTS)** — 한국어 TTS
- **espeak (TTS)** — 즉석 기계음 TTS
- **NanumGothic** — 한글 폰트 (OFL)

---

## 3. 활용 규칙

### 3.1. 신규 유틸리티 개발 시
1. **프론트엔드**: Astro + Tailwind + shadcn/ui (또는 최소 단일 HTML + Tailwind CDN)
2. **DB/Auth**: Supabase 우선
3. **배포**: GitHub Pages (정적) + Cloudflare Workers (서버리스)
4. **이메일**: Resend (정식) → Cloudflare Workers 프록시
5. **알림**: Telegram Bot API
6. **차트**: Chart.js 또는 D3 (필요 시)

### 3.2. 전자책 제작 시
1. **포맷**: Typst (`.typ`) → PDF
2. **템플릿**: `glass-luxury.typ` (제갈자룡 워터마크 포함)
3. **폰트**: NanumGothic + 시스템 폰트
4. **배포**: GitHub Pages `ebook/` 디렉토리
5. **자동화**: `simple_ebook_throttled.sh` (gpt-5-mini 15분 throttle)

### 3.3. 크롤링/데이터 수집 시
1. **HTTP**: `curl` + `web_fetch`
2. **HTML 파싱**: Python `BeautifulSoup4` 또는 JS `cheerio`
3. **CSV**: `papaparse` (JS) 또는 Python `pandas`
4. **스케줄**: `cron` 등록 (every 또는 cron expression)

### 3.4. 텔레그램 봇/리드 캡처
1. **Bot API**: OpenClaw 텔레그램 채널 사용
2. **리드 저장**: Supabase `leads` 테이블
3. **알림**: Telegram `sendDocument` (PDF 자동 발송)
4. **이메일**: Resend API (Workers 프록시)

---

## 4. 라이선스 주의

- **MIT / Apache 2.0 / BSD**: ✅ 자유 사용
- **OFL (폰트)**: ✅ 자유 사용
- **GPL / AGPL**: ⚠️ 주의 (전체 프로젝트 라이선스 영향)
- **상용 라이선스**: ❌ 피하기 (필요 시에만 검토)

---

## 5. 참고 자료

- [GitHub Topics](https://github.com/topics) — 인기 OSS 탐색
- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) — 셀프호스팅 OSS 목록
- [Libraries.io](https://libraries.io) — OSS 메타데이터
- [한국 OSS 동향](https://oss.kr) — 한국 오픈소스协会