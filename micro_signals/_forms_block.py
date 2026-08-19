# coding: utf-8
FORMS = {
    "veblen_luxury": {
        "sub": "충동구매인지 진짜 필요인지 5초 안에 판단하세요",
        "qs": [
            ("이번 구매, 예산 대비 비중은?", [("한 달 생활비 이하", 1), ("한 달 생활비 수준", 2), ("몇 달치 생활비", 3)]),
            ("6개월 후에도 쓸 것 같나요?", [("매일 쓸 것 같음", 1), ("가끔 쓸 듯", 2), ("모르겠음", 3)]),
            ("대체할 수 있는 물건이 이미 있나요?", [("이미 있음", 3), ("비슷한 게 있음", 2), ("없음", 1)]),
        ],
        "advice": [(7, "충동구매 위험. 3일만 미뤄보세요."), (4, "애매합니다. 예산을 다시 짜보세요."), (0, "계획된 소비로 보입니다.")],
    },
    "veblen_home": {
        "sub": "거주 형태별 1년 손익을 직접 계산해보세요",
        "qs": [
            ("예상 거주 기간은?", [("1년 이하", 1), ("1~3년", 2), ("3년 이상", 3)]),
            ("보유 현금(전세/매수 자금)은?", [("부족함", 1), ("어느 정도 있음", 2), ("충분함", 3)]),
            ("금리·집값 하락 리스크를 감당할 수 있나요?", [("부담됨", 1), ("보통", 2), ("여유 있음", 3)]),
        ],
        "advice": [(7, "매수/전세 장기 관점 유리."), (4, "월세로 유연성 확보 고려."), (0, "무리한 결정은 피하세요.")],
    },
    "veblen_body": {
        "sub": "다이어트·시술 투자 전 현실적인 회수 가능성 체크",
        "qs": [
            ("목표 기간은?", [("1개월 이내", 1), ("3개월", 2), ("6개월 이상", 3)]),
            ("예산 대비 부담 수준은?", [("가벼움", 3), ("보통", 2), ("부담됨", 1)]),
            ("과거 비슷한 시도 지속률은?", [("항상 포기함", 1), ("반반", 2), ("잘 지킴", 3)]),
        ],
        "advice": [(7, "투자 대비 성공 가능성 높음."), (4, "작은 목표로 나눠서 시작하세요."), (0, "지금은 무리한 투자입니다.")],
    },
    "veblen_education": {
        "sub": "자격증·교육 투자, 숫자로 따져보는 회수 가능성",
        "qs": [
            ("취득까지 걸리는 기간은?", [("6개월 이내", 3), ("1년", 2), ("1년 이상", 1)]),
            ("취득 후 예상 소득 변화는?", [("확실히 오름", 3), ("불확실", 2), ("변화 없을 듯", 1)]),
            ("현재 직무와 연관성은?", [("직결됨", 3), ("어느 정도", 2), ("무관함", 1)]),
        ],
        "advice": [(7, "투자 회수 가능성 높음."), (4, "좀 더 알아보고 결정하세요."), (0, "다른 대안을 먼저 검토하세요.")],
    },
    "veblen_sidebiz": {
        "sub": "부업 시작 전, 진짜 손익분기 시점을 계산하세요",
        "qs": [
            ("주당 투입 가능 시간은?", [("5시간 이내", 1), ("5~15시간", 2), ("15시간 이상", 3)]),
            ("초기 투자 비용 수준은?", [("거의 없음", 3), ("소액", 2), ("상당함", 1)]),
            ("관련 경험이 있나요?", [("전혀 없음", 1), ("어느 정도", 2), ("전문가급", 3)]),
        ],
        "advice": [(7, "30일 내 손익분기 가능성 높음."), (4, "3개월은 각오하세요."), (0, "시간·비용 재검토가 필요합니다.")],
    },
    "pain_legal": {
        "sub": "법적 문제, 지금 얼마나 긴급한지 5개 질문으로 진단",
        "qs": [
            ("문제 발생 후 경과 시간은?", [("1주 이내", 3), ("1개월 이내", 2), ("그 이상", 1)]),
            ("관련 증거·서류를 보유하고 있나요?", [("충분히 있음", 1), ("일부 있음", 2), ("거의 없음", 3)]),
            ("상대방과 연락이 되나요?", [("됨", 1), ("가끔 됨", 2), ("안 됨", 3)]),
        ],
        "advice": [(7, "긴급 — 법률 전문가 상담을 서두르세요."), (4, "증거를 먼저 정리하세요."), (0, "여유를 갖고 준비하세요.")],
    },
    "pain_health": {
        "sub": "실비보험 청구 가능 여부, 30초 자가진단",
        "qs": [
            ("실비보험에 가입되어 있나요?", [("가입됨", 3), ("모르겠음", 2), ("미가입", 1)]),
            ("진료비 영수증을 보관하고 있나요?", [("있음", 3), ("일부", 2), ("없음", 1)]),
            ("진료 후 경과 기간은?", [("3년 이내", 3), ("3~5년", 2), ("5년 이상", 1)]),
        ],
        "advice": [(7, "청구 가능성 높음 — 보험사에 바로 문의하세요."), (4, "서류를 보완하면 청구 가능할 수 있습니다."), (0, "청구 기한을 확인해보세요.")],
    },
    "pain_job": {
        "sub": "퇴사 결정 전, 6개월 캐시플로우를 미리 확인하세요",
        "qs": [
            ("현재 재직 기간(고용보험 가입)은?", [("1년 이상", 3), ("6개월~1년", 2), ("6개월 미만", 1)]),
            ("생활비 대비 저축 여유는?", [("6개월치 이상", 3), ("3개월치", 2), ("1개월치 이하", 1)]),
            ("재취업 준비 상태는?", [("이미 준비됨", 3), ("일부 준비", 2), ("전혀 없음", 1)]),
        ],
        "advice": [(7, "퇴사 후 안정적으로 버틸 수 있습니다."), (4, "3개월치 생활비를 더 모으고 결정하세요."), (0, "재직하며 준비 기간을 더 가지세요.")],
    },
    "pain_housing": {
        "sub": "전세 계약 문제, 지금 해야 할 일을 순서대로 확인",
        "qs": [
            ("계약 만료까지 남은 기간은?", [("3개월 이내", 3), ("3~6개월", 2), ("6개월 이상", 1)]),
            ("집주인과 연락·협의가 되나요?", [("원만함", 1), ("어느 정도", 2), ("전혀 안 됨", 3)]),
            ("보증금 규모 대비 자산 상황은?", [("여유 있음", 1), ("보통", 2), ("절박함", 3)]),
        ],
        "advice": [(7, "임차권등기명령 등 법적 조치를 서두르세요."), (4, "내용증명 발송부터 시작하세요."), (0, "여유 있게 협의하세요.")],
    },
    "pain_finance": {
        "sub": "여러 개 빚, 어떤 것부터 갚아야 손해가 적을까요",
        "qs": [
            ("가장 이자율이 높은 대출은?", [("20% 이상", 3), ("10~20%", 2), ("10% 이하", 1)]),
            ("연체 중인 대출이 있나요?", [("있음", 3), ("곧 연체 예정", 2), ("없음", 1)]),
            ("신용점수 관리가 중요한가요?", [("매우 중요", 2), ("보통", 1), ("상관없음", 1)]),
        ],
        "advice": [(7, "고금리·연체 대출부터 우선 상환하세요."), (4, "이자율 순으로 상환 계획을 세우세요."), (0, "현재 상환 순서가 합리적입니다.")],
    },
}


def render_micro_html(cat, title):
    """카테고리별 실제 자가진단 HTML 생성 — 신호/점수/키워드/내부로직 절대 미노출."""
    form = FORMS.get(cat)
    if not form:
        return None
    qs = form["qs"]
    advice = form["advice"]
    parts = []
    parts.append('<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">')
    parts.append('<title>' + title + ' | Prometheus Utils</title>')
    parts.append('<style>:root{--bg:#f4f7fc;--glass:#fff;--border:#e2e8f2;--text:#1c2333;--sec:#47516b;--accent:#ff7a45}*{margin:0;padding:0;box-sizing:border-box}body{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans KR",sans-serif;line-height:1.7;padding:24px 16px}.card{max-width:480px;margin:0 auto;background:var(--glass);border:1px solid var(--border);border-radius:16px;padding:28px 22px;box-shadow:0 4px 24px rgba(0,0,0,.06)}h1{font-size:1.3rem;margin-bottom:6px}.sub{color:var(--sec);font-size:.85rem;margin-bottom:20px}.q{margin:16px 0}.qlabel{display:block;font-weight:600;font-size:.92rem;margin-bottom:8px}.opt{display:block;padding:9px 12px;border:1px solid var(--border);border-radius:8px;margin-bottom:6px;font-size:.88rem;cursor:pointer}.opt:hover{border-color:var(--accent)}.opt input{margin-right:8px}.btn{width:100%;background:var(--accent);color:#fff;border:none;padding:13px;border-radius:10px;font-size:1rem;font-weight:600;cursor:pointer;margin-top:12px}.btn:hover{background:#e86435}.result{display:none;text-align:center;margin-top:20px;padding:18px;border-radius:12px;background:#fff5f0}.result.show{display:block}.advice{font-size:1rem;font-weight:700;margin-top:6px}footer{text-align:center;margin-top:20px;color:var(--sec);font-size:.7rem}footer a{color:var(--accent);text-decoration:none}</style></head><body><div class="card">')
    parts.append('<h1>' + title + '</h1>')
    parts.append('<p class="sub">' + form["sub"] + '</p>')
    parts.append('<form id="qForm">')
    for qi, (label, opts) in enumerate(qs, start=1):
        parts.append('<div class="q"><label class="qlabel">' + str(qi) + '. ' + label + '</label>')
        for oi, (otext, oval) in enumerate(opts):
            req = ' required' if oi == 0 else ''
            parts.append('<label class="opt"><input type="radio" name="q' + str(qi) + '" value="' + str(oval) + '"' + req + '> ' + otext + '</label>')
        parts.append('</div>')
    parts.append('<button type="button" class="btn" onclick="calc()">🎯 진단하기</button></form>')
    parts.append('<div id="res" class="result"><div class="advice" id="advice"></div></div>')
    # JS: 사용자 입력 총합 기준, 신호 점수/가중치 절대 사용 안 함
    expr = '"진단 완료"'
    for th, msg in reversed(advice):
        expr = '(t>=' + str(th) + '?"' + msg + '":' + expr + ')'
    js = '<script>function calc(){var inputs=document.querySelectorAll("input:checked");if(inputs.length<' + str(len(qs)) + '){alert("모든 질문에 답해주세요");return}var t=0;inputs.forEach(function(i){t+=+i.value});var a=' + expr + ';document.getElementById("advice").textContent=a;document.getElementById("res").classList.add("show")}</script>'
    parts.append(js)
    parts.append('<footer>© Prometheus Utils · <a href="../../">더 많은 무료 진단 도구</a></footer>')
    parts.append('</div></body></html>')
    return ''.join(parts)
