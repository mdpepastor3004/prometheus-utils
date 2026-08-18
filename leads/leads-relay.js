#!/usr/bin/env node
// leads-relay.js — Termux 로컬 리드 수집 서버 v2
// 실제 bot token 포함 버전
const http = require('http');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const PORT = parseInt(process.argv[2]) || 3737;
const DB_PATH = path.join(__dirname, 'leads.db');
const CONFIG_PATH = path.join(__dirname, 'supabase_config.sh');

// 실제 텔레그램 봇 토큰 (openclaw config에서 추출)
const TG_BOT_TOKEN = '8268734337:AAEwMDqDzv6J4QtEGpeat6sShv-rdI0k2k0';
const TG_CHAT_ID = '730152102';

let SUPABASE_URL = null, SUPABASE_ANON_KEY = null;
if (fs.existsSync(CONFIG_PATH)) {
  const content = fs.readFileSync(CONFIG_PATH, 'utf8');
  const urlMatch = content.match(/SUPABASE_URL="([^"]+)"/);
  const keyMatch = content.match(/SUPABASE_ANON_KEY="([^"]+)"/);
  if (urlMatch) SUPABASE_URL = urlMatch[1];
  if (keyMatch) SUPABASE_ANON_KEY = keyMatch[1];
}

function saveToLocalSQLite(lead) {
  try {
    const safe = (s) => (s || '').replace(/'/g, "''");
    const sql = `INSERT INTO leads (name, phone, email, source, score, device) VALUES ('${safe(lead.name)}', '${safe(lead.phone)}', '${safe(lead.email)}', '${safe(lead.source)}', '${safe(lead.score)}', '${safe(lead.device)}');`;
    execSync(`sqlite3 "${DB_PATH}" "${sql}"`, { stdio: 'pipe' });
    return true;
  } catch (e) {
    console.error('SQLite error:', e.message);
    return false;
  }
}

async function forwardToTelegram(lead) {
  const msg = `🆕 [릴레이] ${lead.source}
━━━
👤 ${lead.name}
📞 ${lead.phone}
📧 ${lead.email}
🎯 ${lead.score || '-'}
📱 ${lead.device}
🕐 ${new Date().toLocaleString('ko-KR', {timeZone: 'Asia/Seoul'})}
#릴레이 #${lead.source}`;
  try {
    const res = await fetch(`https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chat_id: TG_CHAT_ID, text: msg }),
    });
    return res.ok;
  } catch (e) { return false; }
}

async function forwardToSupabase(lead) {
  if (!SUPABASE_URL || !SUPABASE_ANON_KEY) return false;
  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/leads`, {
      method: 'POST',
      headers: {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(lead),
    });
    return res.ok;
  } catch (e) { return false; }
}

const server = http.createServer(async (req, res) => {
  const cors = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST, GET, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type' };
  if (req.method === 'OPTIONS') { res.writeHead(204, cors); res.end(); return; }
  
  if (req.method === 'GET' && req.url === '/health') {
    const total = execSync(`sqlite3 "${DB_PATH}" "SELECT COUNT(*) FROM leads;"`, { encoding: 'utf8' }).trim() || '0';
    res.writeHead(200, { ...cors, 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', port: PORT, total, supabase: !!SUPABASE_URL }));
    return;
  }
  
  if (req.method === 'GET' && req.url === '/stats') {
    try {
      const total = execSync(`sqlite3 "${DB_PATH}" "SELECT COUNT(*) FROM leads;"`, { encoding: 'utf8' }).trim();
      const today = execSync(`sqlite3 "${DB_PATH}" "SELECT COUNT(*) FROM leads WHERE date(created_at) = date('now');"`, { encoding: 'utf8' }).trim();
      const bySource = execSync(`sqlite3 "${DB_PATH}" "SELECT source || '|' || COUNT(*) FROM leads GROUP BY source;"`, { encoding: 'utf8' }).trim();
      res.writeHead(200, { ...cors, 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ total, today, bySource }));
    } catch (e) { res.writeHead(500); res.end('Error'); }
    return;
  }
  
  if (req.method === 'GET' && req.url === '/export') {
    try {
      const data = execSync(`sqlite3 -header -csv "${DB_PATH}" "SELECT * FROM leads ORDER BY created_at DESC;"`, { encoding: 'utf8' });
      const fileName = `leads_${new Date().toISOString().slice(0,10)}.csv`;
      res.writeHead(200, { ...cors, 'Content-Type': 'text/csv', 'Content-Disposition': `attachment; filename="${fileName}"` });
      res.end(data);
    } catch (e) { res.writeHead(500); res.end('Error'); }
    return;
  }
  
  if (req.method === 'POST' && req.url === '/leads') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      try {
        const lead = JSON.parse(body);
        if (!lead.name || !lead.phone || !lead.email) {
          res.writeHead(400, cors); res.end('Missing fields');
          return;
        }
        const localOK = saveToLocalSQLite(lead);
        const tgOK = await forwardToTelegram(lead);
        const supOK = await forwardToSupabase(lead);
        res.writeHead(200, { ...cors, 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ ok: true, local: localOK, telegram: tgOK, supabase: supOK }));
      } catch (e) {
        res.writeHead(400, cors); res.end('Invalid JSON: ' + e.message);
      }
    });
    return;
  }
  
  res.writeHead(404, cors); res.end('Not Found');
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`🔥 Leads relay server v2 on port ${PORT}`);
  console.log(`   ${TG_BOT_TOKEN.slice(0,15)}...`);
  console.log(`   Supabase: ${SUPABASE_URL ? '✅' : '⚠️  not configured'}`);
  console.log(`   SQLite: ${DB_PATH}`);
  console.log('   Endpoints: /health /stats /export /leads (POST)');
  console.log('   Tunnel: ssh -R 80:localhost:' + PORT + ' serveo.net');
});