// leads.js — Supabase + Telegram 이중 전송 모듈
// Supabase URL/Key가 설정되면 Supabase가 메인, Telegram이 알림용
// Supabase 미설정 시 Telegram이 메인 (기존 방식)

const LEAD_CONFIG = {
  // ⚡ 아래 값을 실제 Supabase 프로젝트 값으로 교체
  supabaseUrl: localStorage.getItem('supabase_url') || null,
  supabaseAnonKey: localStorage.getItem('supabase_anon_key') || null,
  
  // Telegram (항상 활성, 폴백용)
  botToken: '***',
  chatId: '730152102',
  
  // 로컬 릴레이 (Termux Node.js 서버, 있으면 사용)
  relayUrl: localStorage.getItem('relay_url') || null,
};

async function submitLead({ name, phone, email, source, score }) {
  const errors = [];
  const device = /Mobi|Android/i.test(navigator.userAgent) ? 'mobile' : 'pc';
  const payload = { name, phone, email, source, score: score || '', device };
  
  // 1. Supabase 전송 (메인)
  if (LEAD_CONFIG.supabaseUrl && LEAD_CONFIG.supabaseAnonKey) {
    try {
      const res = await fetch(`${LEAD_CONFIG.supabaseUrl}/rest/v1/leads`, {
        method: 'POST',
        headers: {
          'apikey': LEAD_CONFIG.supabaseAnonKey,
          'Authorization': `Bearer ${LEAD_CONFIG.supabaseAnonKey}`,
          'Content-Type': 'application/json',
          'Prefer': 'return=minimal',
        },
        body: JSON.stringify(payload),
      });
      if (res.ok) {
        console.log('✅ Supabase: lead saved');
      } else {
        throw new Error(`Supabase ${res.status}`);
      }
    } catch (e) {
      errors.push(`Supabase: ${e.message}`);
    }
  }
  
  // 2. 로컬 릴레이 전송 (있으면)
  if (LEAD_CONFIG.relayUrl) {
    try {
      const res = await fetch(LEAD_CONFIG.relayUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      if (res.ok) console.log('✅ Relay: lead saved');
      else throw new Error(`Relay ${res.status}`);
    } catch (e) {
      errors.push(`Relay: ${e.message}`);
    }
  }
  
  // 3. Telegram 알림 (항상, 실시간 알림)
  const tgMsg = `🆕 [리드] ${source}
━━━
👤 ${name}
📞 ${phone}
📧 ${email}
🎯 ${score || '-'}
📱 ${device}
🕐 ${new Date().toLocaleString('ko-KR', {timeZone: 'Asia/Seoul'})}
#리드 #${source}`;
  
  try {
    const res = await fetch(`https://api.telegram.org/bot${LEAD_CONFIG.botToken}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chat_id: LEAD_CONFIG.chatId, text: tgMsg }),
    });
    if (res.ok) console.log('✅ Telegram: notification sent');
    else errors.push(`Telegram: ${res.status}`);
  } catch (e) {
    errors.push(`Telegram: ${e.message}`);
  }
  
  return { success: errors.length === 0, errors };
}