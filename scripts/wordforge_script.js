// WordForge — 망각곡선 기반 영단어 암기 (SRS)
// 에빙하우스 간격: 10분 → 1일 → 3일 → 7일 → 14일 → 30일

const SRS_INTERVALS = [0, 1/1440, 1, 3, 7, 14, 30]; // days: 0=just added, 1/1440=~1min (first review same session)

// Priority-based sample words
const SAMPLE_WORDS = [
  {w:"ephemeral",m:"덧없는, 일시적인",e:"The beauty of cherry blossoms is ephemeral."},
  {w:"ubiquitous",m:"어디에나 있는",e:"Smartphones have become ubiquitous in modern life."},
  {w:"pragmatic",m:"실용적인, 현실적인",e:"We need a pragmatic approach to this problem."},
  {w:"ambiguous",m:"모호한, 애매한",e:"His answer was deliberately ambiguous."},
  {w:"resilient",m:"회복력 있는, 강한",e:"Children are remarkably resilient."},
  {w:"meticulous",m:"세심한, 꼼꼼한",e:"She is meticulous about her work."},
  {w:"eloquent",m:"웅변적인, 달변의",e:"He gave an eloquent speech."},
  {w:"tenacious",m:"집요한, 끈질긴",e:"Her tenacious spirit led to success."},
  {w:"candid",m:"솔직한, 숨김없는",e:"I appreciate your candid opinion."},
  {w:"paradox",m:"역설, 모순",e:"It's a paradox that less is more."},
  {w:"complacent",m:"자기만족에 빠진",e:"We cannot become complacent about our success."},
  {w:"scrutiny",m:"정밀 조사, 면밀한 검토",e:"The plan came under intense scrutiny."},
  {w:"conundrum",m:"난문제, 수수께끼",e:"This is a real conundrum."},
  {w:"exacerbate",m:"악화시키다",e:"The drought exacerbated the food shortage."},
  {w:"alleviate",m:"완화하다, 경감시키다",e:"This medicine will alleviate the pain."},
];

function wordForgeInit() {
  let data = ldls('wordforge', null);
  if (!data || !data.words) {
    // Fresh start
    data = {
      words: [],
      dailyNew: 10,
      lastReviewDate: '',
      todayCount: 0
    };
  }
  window.wfData = data;
  
  // Check day reset
  const today = new Date().toDateString();
  if (data.lastReviewDate !== today) {
    data.lastReviewDate = today;
    data.todayCount = 0;
  }
  
  updateWFStats();
  showNextCard();
}

function getDueWords() {
  const now = Date.now();
  return window.wfData.words.filter(w => {
    if (w.srsLevel >= SRS_INTERVALS.length) return false;
    const nextReview = w.lastReview + SRS_INTERVALS[w.srsLevel] * 86400000;
    return nextReview <= now;
  });
}

function showNextCard() {
  const due = getDueWords();
  const emptyEl = gId('wfEmpty');
  const cardEl = gId('wfCard');
  
  if (due.length === 0) {
    emptyEl.style.display = 'block';
    cardEl.style.display = 'none';
    updateWFStats();
    saveWF();
    return;
  }
  
  emptyEl.style.display = 'none';
  cardEl.style.display = 'block';
  
  window.wfCurrentCard = due[0];
  window.wfCurrentIdx = window.wfData.words.indexOf(due[0]);
  window.wfFlipped = false;
  
  gId('wfCardInfo').textContent = '단어 ' + (due.indexOf(due[0])+1) + '/' + due.length;
  gId('wfFront').textContent = due[0].w;
  gId('wfFrontSub').textContent = '뜻을 보려면 탭하세요';
  gId('wfMeaning').textContent = due[0].m;
  gId('wfExample').textContent = due[0].e || '—';
  gId('wfBack').style.display = 'none';
  gId('wfCardBody').style.borderColor = 'var(--border)';
}

function flipCard() {
  if (window.wfFlipped) return;
  window.wfFlipped = true;
  gId('wfFrontSub').textContent = '';
  gId('wfBack').style.display = 'block';
  gId('wfCardBody').style.borderColor = 'var(--accent)';
}

function rateCard(quality) {
  // quality: 0=forgot, 1=hard, 2=good
  if (window.wfCurrentIdx < 0) return;
  const w = window.wfData.words[window.wfCurrentIdx];
  if (!w) return;
  
  const now = Date.now();
  w.lastReview = now;
  w.reviewCount = (w.reviewCount || 0) + 1;
  
  if (quality === 0) {
    // Forgot: reset to level 1
    w.srsLevel = 1;
  } else if (quality === 1) {
    // Hard: keep same level but reset timer
    if (w.srsLevel < 1) w.srsLevel = 1;
  } else {
    // Good: advance
    w.srsLevel = Math.min(w.srsLevel + 1, SRS_INTERVALS.length - 1);
  }
  
  // Today count (only count first review of the day for each word)
  const today = new Date().toDateString();
  if (w.lastReviewDate !== today) {
    w.lastReviewDate = today;
    window.wfData.todayCount++;
  }
  
  saveWF();
  updateWFStats();
  showNextCard();
}

function addWord() {
  const word = gId('wfNewWord').value.trim();
  const meaning = gId('wfNewMean').value.trim();
  if (!word || !meaning) { st('단어와 의미를 입력하세요'); return; }
  
  const exist = window.wfData.words.find(w => w.w.toLowerCase() === word.toLowerCase());
  if (exist) { st('이미 있는 단어입니다'); return; }
  
  window.wfData.words.push({
    w: word,
    m: meaning,
    e: gId('wfNewEx').value.trim(),
    srsLevel: 0,
    lastReview: 0,
    reviewCount: 0,
    lastReviewDate: '',
    added: Date.now()
  });
  
  gId('wfNewWord').value = '';
  gId('wfNewMean').value = '';
  gId('wfNewEx').value = '';
  saveWF();
  updateWFStats();
  st('✅ ' + word + ' 추가 완료!');
}

function addSampleWords() {
  // Add up to 5 sample words that don't exist yet
  let count = 0;
  for (const sw of SAMPLE_WORDS) {
    if (count >= 5) break;
    const exist = window.wfData.words.find(w => w.w.toLowerCase() === sw.w.toLowerCase());
    if (exist) continue;
    window.wfData.words.push({
      w: sw.w,
      m: sw.m,
      e: sw.e,
      srsLevel: 0,
      lastReview: Date.now() - 86400000, // Due immediately (was added yesterday)
      reviewCount: 0,
      lastReviewDate: '',
      added: Date.now()
    });
    count++;
  }
  saveWF();
  updateWFStats();
  st('✅ 샘플 ' + count + '개 추가됨');
}

function updateWFStats() {
  const due = getDueWords();
  const total = window.wfData.words.length;
  
  gId('wfDue').textContent = due.length;
  gId('wfDone').textContent = window.wfData.todayCount || 0;
  gId('wfTotal').textContent = total;
  
  const pct = total > 0 ? Math.round((window.wfData.todayCount / Math.max(total, window.wfData.dailyNew)) * 100) : 0;
  gId('wfProgBar').style.width = Math.min(pct, 100) + '%';
  gId('wfProgLbl').textContent = Math.min(pct, 100) + '%';
}

function updateSettings() {
  const v = parseInt(gId('wfDailyNew').value) || 10;
  window.wfData.dailyNew = Math.max(1, Math.min(50, v));
  gId('wfDailyNew').value = window.wfData.dailyNew;
  saveWF();
  st('✅ 설정 저장됨');
}

function exportWords() {
  const blob = new Blob([JSON.stringify(window.wfData, null, 2)], {type:'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'wordforge_backup_' + new Date().toISOString().slice(0,10) + '.json';
  a.click();
  st('💾 내보내기 완료');
}

function importWords(e) {
  const file = e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = function(ev) {
    try {
      const data = JSON.parse(ev.target.result);
      if (!data.words || !Array.isArray(data.words)) throw new Error('Invalid format');
      // Merge: overwrite existing by word
      data.words.forEach(nw => {
        const idx = window.wfData.words.findIndex(w => w.w.toLowerCase() === nw.w.toLowerCase());
        if (idx >= 0) {
          window.wfData.words[idx] = nw;
        } else {
          window.wfData.words.push(nw);
        }
      });
      saveWF();
      updateWFStats();
      st('✅ ' + data.words.length + '개 단어 가져오기 완료');
    } catch(err) {
      st('⚠️ 파일 형식 오류');
    }
  };
  reader.readAsText(file);
}

function resetAll() {
  window.wfData = { words: [], dailyNew: 10, lastReviewDate: '', todayCount: 0 };
  saveWF();
  updateWFStats();
  gId('wfEmpty').style.display = 'block';
  gId('wfCard').style.display = 'none';
  st('🗑️ 초기화 완료');
}

function saveWF() {
  svls('wordforge', window.wfData);
}

function leadScore() {
  return gId('wfDue').textContent + '개 복습중';
}

// Init
window.addEventListener('DOMContentLoaded', wordForgeInit);
