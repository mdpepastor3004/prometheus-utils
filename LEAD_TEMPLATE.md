# 리드 캡처 템플릿 — GitHub Pages + Supabase + Telegram

## 구조

```
새로운 유틸리티/index.html
  ├ 무료 유틸리티 기능 (사용자 가치 제공)
  └ 리드 캡처 모달 (푸터 CTA)
      ├ 이름 / 전화번호 / 이메일
      ├ → Supabase (DB 저장)
      └ → Telegram fallback (Bot API)
```

## 1. Supabase 설정

### 테이블 생성

```sql
CREATE TABLE leads (
  id BIGSERIAL PRIMARY KEY,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  name TEXT NOT NULL,
  phone TEXT NOT NULL,
  email TEXT NOT NULL,
  source TEXT DEFAULT '',
  score TEXT DEFAULT '',
  device TEXT DEFAULT '',
  page TEXT DEFAULT ''
);
```

### Row Level Security (RLS)

```sql
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;

-- 누구나 INSERT 가능 (익명 사용자)
CREATE POLICY "Anyone can insert leads"
  ON leads FOR INSERT
  TO anon
  WITH CHECK (true);

-- 관리자만 SELECT 가능
CREATE POLICY "Admins can view leads"
  ON leads FOR SELECT
  USING (auth.role() = 'service_role');
```

## 2. HTML에 포함할 JS 코드

Supabase URL과 Anon Key는 `hephaestus/SUPABASE_CONFIG.js`에서 관리.

### `hephaestus/SUPABASE_CONFIG.js`

```js
const SUPABASE_URL = 'https://YOUR_PROJECT.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_YOUR_KEY';
```

### 모달 HTML (복붙용)

```html
<!-- 리드 캡처 모달 -->
<div class="modal-overlay" id="leadM">
<div class="modal">
<button class="close" onclick="closeLead()">✕</button>
<div id="mf">
<h2>📩 프리미엄 리포트</h2>
<p class="desc">정보 입력 후 무료 다운로드</p>
<div class="benefit"><b>🎁 혜택</b>✅ 항목1<br>✅ 항목2<br>✅ 항목3</div>
<div class="field"><input type="text" id="lName" placeholder="이름"></div>
<div class="field"><input type="tel" id="lPhone" placeholder="전화번호"></div>
<div class="field"><input type="email" id="lEmail" placeholder="이메일"></div>
<div class="error-msg" id="lErr">모든 항목을 입력해주세요</div>
<button class="btn" onclick="sLead()">📩 받기 (무료)</button>
</div>
<div class="success" id="ms">
<div class="icon">🎉</div>
<h3>신청 완료!</h3>
<p>프리미엄 리포트를 보내드렸습니다</p>
<a class="dl-btn" href="../ebook/YOUR_REPORT.pdf" target="_blank">📕 다운로드</a>
</div>
</div>
</div>
```

### JS 함수 (복붙용)

```js
// Supabase 연동
function supabaseInsert(payload) {
  return fetch(SUPABASE_URL + '/rest/v1/leads', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'apikey': SUPABASE_ANON_KEY,
      'Authorization': 'Bearer ' + SUPABASE_ANON_KEY,
      'Prefer': 'return=minimal'
    },
    body: JSON.stringify(payload)
  });
}

// Telegram fallback
function telegramSend(text) {
  return fetch('https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({chat_id: CHAT_ID, text: text})
  });
}

async function sLead() {
  const n = document.getElementById('lName').value.trim();
  const p = document.getElementById('lPhone').value.trim();
  const em = document.getElementById('lEmail').value.trim();
  document.getElementById('lErr').style.display = 'none';
  if (!n || !p || !em) { document.getElementById('lErr').style.display = 'block'; return; }

  const btn = document.querySelector('.modal .btn');
  btn.disabled = true;
  btn.textContent = '처리 중...';

  const dv = /Mobi|Android/i.test(navigator.userAgent) ? 'mobile' : 'pc';
  const payload = {
    name: n,
    phone: p,
    email: em,
    source: 'YOUR_PAGE_SOURCE', // ← 변경 필요
    score: 'YOUR_SCORE',         // ← 변경 필요
    device: dv,
    page: window.location.href
  };

  let ok = false;
  // 1차: Supabase 저장
  try {
    const r = await supabaseInsert(payload);
    ok = r.ok || r.status === 201;
  } catch(e) { ok = false; }

  // 2차 fallback: Telegram
  if (!ok) {
    try {
      const tg = '🆕 [리드] SOURCE\n━━━\n👤 ' + n + '\n📞 ' + p + '\n📧 ' + em + '\n🎯 ' + payload.score + '\n📱 ' + dv + '\n🕐 ' + new Date().toLocaleString('ko-KR', {timeZone:'Asia/Seoul'});
      const r2 = await telegramSend(tg);
      ok = r2.ok;
    } catch(e2) { ok = false; }
  }

  if (ok) {
    document.getElementById('mf').style.display = 'none';
    document.getElementById('ms').classList.add('active');
    st('✅ 신청 완료!');
  } else {
    st('⚠️ 오류가 발생했습니다. 다시 시도해주세요.', 'error');
    btn.disabled = false;
    btn.textContent = '📩 받기 (무료)';
  }
}
```

## 3. 새 페이지 만들 때마다

1. 이 템플릿 복사
2. `YOUR_PAGE_SOURCE` → 페이지 식별자 (예: `gradecalc`, `wordforge`)
3. `YOUR_SCORE` → 유틸리티 결과값 변수
4. `YOUR_REPORT.pdf` → 프리미엄 PDF 경로
5. `혜택 항목` → 해당 리포트에 맞는 혜택 3개

## 4. 리드 데이터 확인

- **Supabase**: `https://supabase.com/dashboard/project/YOUR_PROJECT_ID/table/leads`
- **텔레그램** (Supabase 실패 시): 봇 메시지
