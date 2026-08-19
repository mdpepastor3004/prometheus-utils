# coding: utf-8
"""호갱백신 퀴즈 3개 시드 (v1). 5라운드 게임화 + AI 대비 코멘트."""

QUIZZES = {
    "veblen_luxury": {
        "sub": "5라운드 · AI가 당신을 호구로 만들 명품 결정 체험",
        "emoji": "💎",
        "rounds": [
            {
                "situation": "백화점 매장에서 셀러가 '오늘만 30% 할인, 30분 뒤 끝나요' 합니다",
                "options": [
                    ("30% 할인이라면 일단 질러야지", "bad", "충동구매의 시작. '마감 압박'은 셀러의 가장 흔한 수법입니다."),
                    ("비슷한 다른 매장도 비교해본다", "good", "이 한 마디면 셀러의 90% 수법이 무력화됩니다."),
                    ("일단 카드를 꺼내본다 (결제는 나중에)", "bad", "카드 제시 = 심리적 계약. 안 사기로 해도 다음에 또 옵니다."),
                ],
                "ai_would": "AI 추천 봇은 보통 '30%면 7만원 아끼는 셈, 3일 후엔 후회 없을 듯'이라고 답합니다. 그게 함정입니다."
            },
            {
                "situation": "지인이 '이 가방 진짜야, 50만 원에 내줄게' 합니다. 정가 200만 원",
                "options": [
                    ("정가 대비 75% 할인, 대박 사자", "bad", "지인 사기(친족 사기)의 단골 수법. 50만 원 받고 사라집니다."),
                    ("정가 확인 + 시리얼/영수증 요구", "good", "구매 전 진위 확인은 기본 중의 기본입니다."),
                    ("일단 맡기고 내일 답할게", "ok", "미루기는 좋지만, '내일 생각할게'는 거절로 통하지 않을 수 있습니다."),
                ],
                "ai_would": "AI는 '정가 대비 75% 할인은 의심해볼 만하다' 정도로 답하지만, 위험 신호는 직접 짚어주지 않습니다."
            },
            {
                "situation": "한정판 '○○○ 1,000개 한정' SNS 광고, 10분 뒤 품절",
                "options": [
                    ("한정이라면 지금 질러야지", "bad", "한정 트리거는 충동구매 1위. 대부분 재고 풀려 있습니다."),
                    ("브랜드 공식몰/오프라인 동시 확인", "good", "검증 가능한 채널에서만 구매하는 게 안전합니다."),
                    ("리셀 가치 있을지 시세 확인", "ok", "리셀은 본전도 못 건질 확률 70%."),
                ],
                "ai_would": "AI는 '리셀 가치는 변동성 크다' 정도. 진짜 한정판은 광고 없이도 3초 만에 품절입니다."
            },
            {
                "situation": "중고 명품 거래, 판매자가 '지갑 들고 인증샷 보내줄게' 합니다",
                "options": [
                    ("인증샷 봤으니 안심", "bad", "인증샷은 위조 가능. 사진 한 장으로 진위 판별 불가."),
                    ("공식 매장/감정사 동행 요청", "good", "직접 감정 받으면 100% 안전. 비용 1~2만 원."),
                    ("가격이 정가 대비 50% 이하면 의심한다", "good", "50% 이하 = 99% 가품. 가격 자체가 신호입니다."),
                ],
                "ai_would": "AI는 '감정 서비스를 권장합니다'라고 답하지만, 지금 이 사람이 99% 가품 팔이라는 경고는 안 합니다."
            },
            {
                "situation": "한 번 산 명품, 3일 후 후회. 환불 요청할까요?",
                "options": [
                    ("3일 지났으니 포기", "bad", "전자상거래법상 7일 청약철구 가능. 포기 = 손해 확정."),
                    ("판매자에게 먼저 연락", "ok", "가능하지만, 판매자 응 거부 시 2차 피해 가능."),
                    ("플랫폼 소비자센터에 동시 접수", "good", "공식 채널 동시 접수 = 압박 효과 + 증거 확보."),
                ],
                "ai_would": "AI는 '판매자와의 관계를 고려하세요' 정도로 답하지만, 법적 권리는 구체적으로 짚어주지 않습니다."
            },
        ],
    },
    "pain_legal": {
        "sub": "5라운드 · AI 법률 조언의 한계 체험",
        "emoji": "⚖️",
        "rounds": [
            {
                "situation": "AI 법률 봇이 '전세사기 시 내용증명 보내면 됩니다' (실제 증거 없음)",
                "options": [
                    ("AI 말대로 내용증명 보낸다", "bad", "증거 없이 내용증명 = 법적 효과 없음 + 상대 경계심만 높임."),
                    ("증거 확보 후 법률구조공단 상담", "good", "증거 = 모든 법적 조치의 시작점입니다."),
                    ("AI 더 물어본다", "ok", "더 물어보는 건 좋지만, AI는 변호사 아님."),
                ],
                "ai_would": "AI는 '법적 조치를 권장합니다'라고 답하지만, 증거 없이는 무의미라고 짚어주진 않습니다."
            },
            {
                "situation": "계약 분쟁, AI가 '여기 조항이 유리합니다'라고 조언",
                "options": [
                    ("AI가 유리하면 그대로 진행", "bad", "계약 해석은 사안별, AI 일반론 ≠ 내 사건."),
                    ("변호사 상담 30분 무료 활용", "good", "법률구조공단 30분 무료 상담 = 기본 권리입니다."),
                    ("다른 AI로 다시 물어본다", "ok", "다중 검증은 좋지만, 변호사 상담이 답."),
                ],
                "ai_would": "AI는 '개별 상담을 권장합니다'라고 답하지만, 법률구조공단 무료 상담은 짚어주지 않습니다."
            },
            {
                "situation": "이혼 상담, AI가 '위자료 5,000만 원 가능'이라고 답",
                "options": [
                    ("AI가 5,000만 원 가능하다고 함", "bad", "위자료 = 사안별, AI 추측은 근거 없음."),
                    ("판례 검색 + 변호사 검토", "good", "유사 판례 = 위자료 예측의 기준입니다."),
                    ("다른 AI로 다시 물어본다", "ok", "검증은 좋지만, 판례·변호사가 답."),
                ],
                "ai_would": "AI는 '개별 사안이 다르다'고 답하지만, 5,000만 원 가능이라는 추측에 대한 근거는 제시하지 않습니다."
            },
            {
                "situation": "직장 내 harassment, AI가 '녹음해두면 됩니다' 조언",
                "options": [
                    ("녹음은 도청죄 우려", "ok", "정확한 이해. 통신비밀보호법 적용 가능."),
                    ("녹음 + 제보 + 노동부 신고 동시", "good", "녹음만으론 약함, 공식 채널 병행이 핵심입니다."),
                    ("녹음만으로 충분하다고 믿는다", "bad", "녹음 단독 = 법적 효력 약함, 추가 증거 필요."),
                ],
                "ai_would": "AI는 '녹음은 신중히'라고 답하지만, 노동부 신고·제보 등 구체적 채널은 짚어주지 않습니다."
            },
            {
                "situation": "소액 분쟁, AI가 '소송 비용 100만 원 예상'이라고 함",
                "options": [
                    ("100만 원 들여 소송한다", "bad", "소송 비용 > 분쟁액 = 손해 확정."),
                    ("조정·중재 + 소액사건심판 검토", "good", "소액 분쟁은 조정·중재가 90% 유리합니다."),
                    ("AI 다시 물어본다", "ok", "검증은 좋지만, 조정·중재는 기본."),
                ],
                "ai_would": "AI는 '비용을 고려하세요'라고 답하지만, 조정·중재 등 무료/저비용 대안은 짚어주지 않습니다."
            },
        ],
    },
    "veblen_sidebiz": {
        "sub": "5라운드 · 부업·N잡 모집의 진짜 수익률 체험",
        "emoji": "💸",
        "rounds": [
            {
                "situation": "부업 모집 '월 300만 원 부업, 하루 2시간. 100만 원 교육비'",
                "options": [
                    ("300만 - 100만 = 200만 순수익", "bad", "월 300만 = 상위 5%, 하루 2시간 = 거의 불가."),
                    ("수익 후기 + 평균 수익 분포 확인", "good", "평균과 분포 모두 봐야 진짜 그림이 나옵니다."),
                    ("3일만 미뤄본다", "ok", "미루기 좋지만, 검증은 별도."),
                ],
                "ai_would": "AI는 '개인이 다르다'고 답하지만, 월 300만 = 상위 5%라고 짚어주진 않습니다."
            },
            {
                "situation": "스마트스토어 교육 '6개월 월 500만 원 보장. 등록비 200만 원'",
                "options": [
                    ("500만 보장 + 200만 = 5개월 회수", "bad", "보장 문구 = 마케팅, 실제 회수 기간 검증 필수."),
                    ("3개월 후기 + 손익 시뮬레이션", "good", "3개월 후기 = 진짜 데이터입니다."),
                    ("무료 자료로 먼저 학습", "ok", "무료 학습 후 판단은 좋지만, 교육 등록은 별도."),
                ],
                "ai_would": "AI는 '노력이 중요하다'고 답하지만, 보장 문구의 허상은 짚어주지 않습니다."
            },
            {
                "situation": "N잡 크리에이터 '인스타 1만 팔로워 = 월 100만 원. 50만 원 강의'",
                "options": [
                    ("1만 팔로워면 100만 원 가능", "bad", "팔로워 ≠ 수익. 광고 단가·전환율 별개."),
                    ("강의자 실제 수익 공개 자료 확인", "good", "수익 공개 = 신뢰의 시작입니다."),
                    ("무료로 검증할 수 있는지 본다", "ok", "무료 검증은 좋지만, 강의 등록은 별도."),
                ],
                "ai_would": "AI는 '콘텐츠 품질이 핵심'이라고 답하지만, 1만 팔로워 ≠ 100만 원이라는 함정은 짚어주지 않습니다."
            },
            {
                "situation": "부업 모집 '투자금 50만 원으로 일 5만 원 자동 수익'. 7일 체험",
                "options": [
                    ("7일 무료니까 해본다", "bad", "자동 수익 = 사기 단골, 체험 후 카드 청구 패턴."),
                    ("자동 수익 구조 + 사업자 등록 확인", "good", "자동 수익은 한국에서 사업자 등록 필수입니다."),
                    ("수익 구조 이해 전 결제 안 함", "good", "이해 없는 결제는 도박."),
                ],
                "ai_would": "AI는 '주의가 필요하다'고 답하지만, 자동 수익 = 사기 단골이라고 짚어주진 않습니다."
            },
            {
                "situation": "부업 시작 3개월, 월 30만 원밖에 안 벌임. 교육료 200만 원",
                "options": [
                    ("더 열심히 하면 늘겠지", "bad", "수익 정체 = 구조적 한계 가능성."),
                    ("중단 + 다른 부업 검토", "good", "손절 시점 = 6개월 전이 일반적입니다."),
                    ("일단 1년 더 해본다", "ok", "1년은 길지만, 검증은 가능."),
                ],
                "ai_would": "AI는 '도전을 응원합니다'라고 답하지만, 손절 기준은 짚어주지 않습니다."
            },
        ],
    },
}


def render_quiz_html(cat, title):
    """호갱백신 퀴즈 HTML 생성. 5라운드 게임화 + AI 대비 코멘트 + 공유 CTA."""
    quiz = QUIZZES.get(cat)
    if not quiz:
        return None
    rounds = quiz["rounds"]
    n = len(rounds)
    parts = []
    parts.append('<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">')
    parts.append('<title>' + title + ' | Prometheus Utils</title>')
    parts.append('<meta name="description" content="AI가 당신을 호구로 만들 결정을 미리 체험하는 5라운드 퀴즈">')
    parts.append('<style>:root{--bg:#f4f7fc;--glass:#fff;--border:#e2e8f2;--text:#1c2333;--sec:#47516b;--accent:#ff7a45;--good:#10b981;--bad:#ef4444;--ok:#3b82f6;--warn:#f59e0b}*{margin:0;padding:0;box-sizing:border-box}body{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans KR",sans-serif;line-height:1.7;padding:16px;min-height:100vh}.container{max-width:520px;margin:0 auto}h1{font-size:1.4rem;margin-bottom:4px;text-align:center}.sub{color:var(--sec);font-size:.85rem;text-align:center;margin-bottom:16px}.progress{background:#e2e8f2;border-radius:99px;height:8px;margin:12px 0;overflow:hidden}.pbar{background:linear-gradient(90deg,var(--accent),var(--warn));height:100%;border-radius:99px;transition:width .4s}.step{font-size:.72rem;color:var(--sec);text-align:center;margin-bottom:6px}.card{background:var(--glass);border:1px solid var(--border);border-radius:16px;padding:24px 20px;box-shadow:0 4px 24px rgba(0,0,0,.06);margin-bottom:14px}.situation{font-size:1rem;font-weight:600;margin-bottom:14px;line-height:1.5}.opt{display:block;width:100%;text-align:left;background:#fff;border:2px solid var(--border);border-radius:12px;padding:12px 14px;margin:8px 0;cursor:pointer;font-size:.92rem;transition:all .15s}.opt:hover{border-color:var(--accent);transform:translateY(-1px)}.opt.sel-good{border-color:var(--good);background:#d1fae5}.opt.sel-bad{border-color:var(--bad);background:#fee2e2}.opt.sel-ok{border-color:var(--warn);background:#fef3c7}.opt:disabled{opacity:.6;cursor:not-allowed}.feedback{margin-top:12px;padding:14px;border-radius:10px;font-size:.85rem;display:none;line-height:1.6}.feedback.show{display:block}.feedback.good{background:#d1fae5;border:1px solid #6ee7b7;color:#065f46}.feedback.bad{background:#fee2e2;border:1px solid #fca5a5;color:#991b1b}.feedback.ok{background:#fef3c7;border:1px solid #fcd34d;color:#78350f}.ai-warn{margin-top:10px;padding:10px 12px;background:#1e293b;color:#a7f3d0;border-radius:8px;font-size:.78rem;line-height:1.5}.ai-warn b{color:#fbbf24}.btn{width:100%;background:var(--accent);color:#fff;border:none;padding:13px;border-radius:10px;font-size:1rem;font-weight:600;cursor:pointer;margin-top:12px}.btn:hover{background:#e86435}.btn:disabled{background:#aaa;cursor:not-allowed}.share{background:var(--ok)}.share:hover{background:#059669}.final{display:none;text-align:center;padding:20px;border-radius:14px;background:linear-gradient(135deg,#fff5f0,#fff);border:2px solid var(--accent)}.final.show{display:block}.score-big{font-size:3rem;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--warn));-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:8px 0}.score-lbl{font-size:.85rem;color:var(--sec);margin-bottom:6px}.verdict{font-size:1.05rem;font-weight:700;margin:12px 0}.verdict.hoo{color:var(--bad)}.verdict.mid{color:var(--warn)}.verdict.safe{color:var(--good)}.coda{font-size:.78rem;color:var(--sec);margin:8px 0 16px}footer{text-align:center;margin-top:16px;color:var(--sec);font-size:.7rem}footer a{color:var(--accent);text-decoration:none}</style></head><body>')
    parts.append('<div class="container">')
    parts.append('<h1>' + quiz["emoji"] + ' ' + title + '</h1>')
    parts.append('<p class="sub">' + quiz["sub"] + '</p>')
    parts.append('<div class="step" id="step">1 / ' + str(n) + ' 라운드</div>')
    parts.append('<div class="progress"><div class="pbar" id="pbar" style="width:' + str(100 // n) + '%"></div></div>')
    parts.append('<div id="quiz"></div>')
    parts.append('<div class="final" id="final"></div>')
    parts.append('</div>')
    parts.append('<footer>© Prometheus Utils · <a href="../../">더 많은 호갱백신 퀴즈</a></footer>')

    # rounds data
    import json as _json
    rounds_json = _json.dumps(rounds, ensure_ascii=False)
    parts.append('<script>')
    parts.append('var rounds = ' + rounds_json + ';')
    parts.append('var n = rounds.length;')
    parts.append('var idx = 0;')
    parts.append('var score = 0;')
    parts.append('var goodCount = 0;')
    parts.append('var badCount = 0;')
    parts.append('var okCount = 0;')
    parts.append('function showRound() {')
    parts.append('  if (idx >= n) { return showFinal(); }')
    parts.append('  var r = rounds[idx];')
    parts.append('  document.getElementById("step").textContent = (idx + 1) + " / " + n + " 라운드";')
    parts.append('  document.getElementById("pbar").style.width = Math.round(((idx + 1) / n) * 100) + "%";')
    parts.append('  var html = "<div class=\"card\"><div class=\"situation\">" + r.situation + "</div>";')
    parts.append('  for (var i = 0; i < r.options.length; i++) {')
    parts.append('    var o = r.options[i];')
    parts.append('    html += "<button class=\"opt\" data-i=\"" + i + "\" onclick=\"pick(this)\">" + o[0] + "</button>";')
    parts.append('  }')
    parts.append('  html += "</div>";')
    parts.append('  document.getElementById("quiz").innerHTML = html;')
    parts.append('}')
    parts.append('function pick(btn) {')
    parts.append('  var i = parseInt(btn.dataset.i);')
    parts.append('  var r = rounds[idx];')
    parts.append('  var o = r.options[i];')
    parts.append('  var kind = o[1];')
    parts.append('  var comment = o[2];')
    parts.append('  if (kind === "good") { goodCount++; btn.classList.add("sel-good"); }')
    parts.append('  else if (kind === "bad") { badCount++; btn.classList.add("sel-bad"); }')
    parts.append('  else { okCount++; btn.classList.add("sel-ok"); }')
    parts.append('  var btns = document.querySelectorAll(".opt");')
    parts.append('  for (var j = 0; j < btns.length; j++) { btns[j].disabled = true; }')
    parts.append('  var fb = document.createElement("div");')
    parts.append('  fb.className = "feedback show " + kind;')
    parts.append('  fb.innerHTML = "<b>" + (kind === "good" ? "✅ 냉수 한잔!" : kind === "bad" ? "⚠️ 호구 신호" : "🤔 애매했어요") + "</b><br>" + comment;')
    parts.append('  var ai = document.createElement("div");')
    parts.append('  ai.className = "ai-warn";')
    parts.append('  ai.innerHTML = "<b>🤖 AI는 이렇게 답했을 겁니다:</b><br>" + r.ai_would;')
    parts.append('  btn.parentNode.appendChild(fb);')
    parts.append('  btn.parentNode.appendChild(ai);')
    parts.append('  var nb = document.createElement("button");')
    parts.append('  nb.className = "btn";')
    parts.append('  nb.textContent = (idx + 1 < n) ? "다음 라운드 →" : "결과 보기 →";')
    parts.append('  nb.onclick = function() { idx++; showRound(); };')
    parts.append('  btn.parentNode.appendChild(nb);')
    parts.append('}')
    parts.append('function showFinal() {')
    parts.append('  document.getElementById("step").textContent = "완료";')
    parts.append('  document.getElementById("pbar").style.width = "100%";')
    parts.append('  document.getElementById("quiz").style.display = "none";')
    parts.append('  var pct = Math.round((goodCount / n) * 100);')
    parts.append('  var verdict = "";')
    parts.append('  var verdictClass = "";')
    parts.append('  var coda = "";')
    parts.append('  if (pct >= 80) { verdict = "🛡️ 호구 면역 완료"; verdictClass = "safe"; coda = "위험 신호 즉시 감지. AI보다 한 수 위. 주변에 공유하세요."; }')
    parts.append('  else if (pct >= 50) { verdict = "⚠️ 면역 중 — 한 수만 더"; verdictClass = "mid"; coda = "AI 함정 절반은 피했지만, 결정적 순간에 흔들릴 수 있습니다."; }')
    parts.append('  else { verdict = "🚨 호구 고위험군"; verdictClass = "hoo"; coda = "AI 답변을 그대로 믿으면 큰 손해. 다른 사람의 체크리스트로 검증하세요."; }')
    parts.append('  var shareTxt = encodeURIComponent("' + quiz["emoji"] + ' 호갱백신 퀴즈 결과: " + verdict + " (" + pct + "점) — AI가 호구로 만들 결정을 미리 체험");')
    parts.append('  var shareUrl = "https://mdpepastor3004.github.io/prometheus-utils/micro_signals/services/";')
    parts.append('  var tg = "https://t.me/share/url?url=" + shareUrl + "&text=" + shareTxt;')
    parts.append('  var html = "<div class=\"score-lbl\">냉수 한잔 점수</div><div class=\"score-big\">" + pct + "점</div>";')
    parts.append('  html += "<div class=\"verdict " + verdictClass + "\">" + verdict + "</div>";')
    parts.append('  html += "<div class=\"coda\">" + coda + "</div>";')
    parts.append('  html += "<div style=\"font-size:.78rem;color:var(--sec);margin:14px 0\"><b>내 점수:</b> 냉수 " + goodCount + " · 애매 " + okCount + " · 호구신호 " + badCount + "</div>";')
    parts.append('  html += "<a class=\"btn share\" href=\"\" + tg + "" target=\"_blank\" style=\"display:block;text-decoration:none;text-align:center\">📤 텔레그램으로 공유 — 친구 1명 호구 예방</a>";')
    parts.append('  html += "<a class=\"btn\" href=\"../../\" style=\"display:block;text-decoration:none;text-align:center;margin-top:8px;background:var(--high)\">🔬 다른 호갱백신 퀴즈 풀기</a>";')
    parts.append('  document.getElementById("final").innerHTML = html;')
    parts.append('  document.getElementById("final").classList.add("show");')
    parts.append('}')
    parts.append('showRound();')
    parts.append('</script>')
    parts.append('</body></html>')
    return ''.join(parts)
