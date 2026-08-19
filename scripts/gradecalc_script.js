// GradeCalc — 수능 등급 계산 엔진
// 2027학년도 기준 예상 컷 (실제와 다를 수 있음, 참고용)

const GRADE_TABLE = {
  // [원점수 하한]: { std: 표준점수, pct: 백분위, grade: 등급 }
  // 국어/수학 (100점 만점)
  kor: {
    100:{std:142,pct:99,g:1},97:{std:138,pct:96,g:1},95:{std:136,pct:95,g:1},
    92:{std:133,pct:91,g:2},88:{std:129,pct:88,g:2},85:{std:127,pct:85,g:2},
    80:{std:123,pct:80,g:3},75:{std:120,pct:75,g:3},70:{std:117,pct:70,g:3},
    65:{std:114,pct:65,g:4},60:{std:111,pct:60,g:4},55:{std:108,pct:55,g:4},
    50:{std:105,pct:50,g:5},45:{std:102,pct:45,g:5},40:{std:98,pct:40,g:5},
    35:{std:95,pct:35,g:6},30:{std:92,pct:30,g:6},25:{std:88,pct:25,g:7},
    20:{std:85,pct:20,g:7},15:{std:82,pct:15,g:8},10:{std:78,pct:10,g:8},
    5:{std:75,pct:5,g:9},0:{std:70,pct:1,g:9}
  },
  math: {
    100:{std:148,pct:99,g:1},97:{std:144,pct:96,g:1},95:{std:142,pct:95,g:1},
    92:{std:139,pct:91,g:2},88:{std:135,pct:88,g:2},84:{std:131,pct:84,g:2},
    80:{std:127,pct:80,g:3},75:{std:123,pct:75,g:3},70:{std:120,pct:70,g:3},
    65:{std:116,pct:65,g:4},60:{std:113,pct:60,g:4},55:{std:109,pct:55,g:4},
    50:{std:105,pct:50,g:5},45:{std:101,pct:45,g:5},40:{std:97,pct:40,g:5},
    35:{std:93,pct:35,g:6},30:{std:89,pct:30,g:6},25:{std:85,pct:25,g:7},
    20:{std:81,pct:20,g:7},15:{std:77,pct:15,g:8},10:{std:73,pct:10,g:8},
    5:{std:69,pct:5,g:9},0:{std:65,pct:1,g:9}
  },
  // 영어 (100점 만점, 절대평가)
  eng: {
    90:{std:140,pct:90,g:1},80:{std:130,pct:80,g:2},70:{std:120,pct:70,g:3},
    60:{std:110,pct:60,g:4},50:{std:100,pct:50,g:5},40:{std:90,pct:40,g:6},
    30:{std:80,pct:30,g:7},20:{std:70,pct:20,g:8},0:{std:60,pct:1,g:9}
  },
  // 탐구 (50점 만점)
  sci: {
    50:{std:70,pct:99,g:1},47:{std:67,pct:96,g:1},45:{std:65,pct:94,g:1},
    42:{std:63,pct:90,g:2},40:{std:61,pct:87,g:2},37:{std:59,pct:83,g:2},
    35:{std:57,pct:79,g:3},32:{std:55,pct:74,g:3},30:{std:53,pct:70,g:3},
    27:{std:51,pct:65,g:4},25:{std:49,pct:60,g:4},22:{std:47,pct:54,g:4},
    20:{std:45,pct:50,g:5},17:{std:43,pct:44,g:5},15:{std:41,pct:39,g:5},
    12:{std:39,pct:33,g:6},10:{std:37,pct:28,g:6},7:{std:35,pct:22,g:7},
    5:{std:33,pct:17,g:7},2:{std:31,pct:11,g:8},0:{std:30,pct:5,g:9}
  },
  // 한국사 (50점 만점, 절대평가)
  hist: {
    40:{std:50,pct:80,g:1},35:{std:47,pct:70,g:2},30:{std:45,pct:60,g:3},
    25:{std:43,pct:50,g:4},20:{std:40,pct:40,g:5},15:{std:37,pct:30,g:6},
    10:{std:35,pct:20,g:7},5:{std:32,pct:10,g:8},0:{std:30,pct:1,g:9}
  }
};

// 대학별 권장 등급표 (정시 기준 예시)
const UNIV_TABLE = [
  {n:"서울대 인문",r:1.2},{n:"서울대 자연",r:1.3},
  {n:"연세대 인문",r:1.5},{n:"연세대 자연",r:1.7},
  {n:"고려대 인문",r:1.5},{n:"고려대 자연",r:1.7},
  {n:"서강대 인문",r:2.0},{n:"서강대 자연",r:2.3},
  {n:"성균관대 인문",r:2.0},{n:"성균관대 자연",r:2.3},
  {n:"한양대 인문",r:2.3},{n:"한양대 자연",r:2.5},
  {n:"중앙대 인문",r:2.5},{n:"중앙대 자연",r:3.0},
  {n:"경희대 인문",r:3.0},{n:"경희대 자연",r:3.3},
  {n:"한국외대",r:3.0},{n:"시립대",r:2.7},
  {n:"건국대 인문",r:3.5},{n:"건국대 자연",r:3.7},
  {n:"동국대",r:3.5},{n:"홍익대",r:3.7},
  {n:"숭실대",r:3.7},{n:"국민대",r:4.0},
  {n:"인하대",r:4.0},{n:"아주대",r:4.0},
  {n:"세종대",r:4.3},{n:"단국대",r:4.5}
];

function getGradeForScore(subject, score) {
  const table = GRADE_TABLE[subject];
  if (!table) return {std:0,pct:0,g:9};
  const keys = Object.keys(table).map(Number).sort((a,b)=>b-a);
  for (const k of keys) {
    if (score >= k) return table[k];
  }
  return table[0];
}

function computeGrade() {
  const kor = parseInt(gId('kor').value)||0;
  const math = parseInt(gId('math').value)||0;
  const eng = parseInt(gId('eng').value)||0;
  const sci = parseInt(gId('sci').value)||0;
  const hist = parseInt(gId('hist').value)||0;

  const rKor = getGradeForScore('kor', kor);
  const rMath = getGradeForScore('math', math);
  const rEng = getGradeForScore('eng', eng);
  const rSci = getGradeForScore('sci', sci);
  const rHist = getGradeForScore('hist', hist);

  // Badge updates
  gId('gsKor').textContent = rKor.g + '등급';
  gId('gsMath').textContent = rMath.g + '등급';
  gId('gsEng').textContent = rEng.g + '등급';
  gId('gsSci').textContent = rSci.g + '등급';
  gId('gsHist').textContent = rHist.g + '등급';

  // Breakdown
  gId('gsBkor').textContent = kor;
  gId('gsBmath').textContent = math;
  gId('gsBeng').textContent = eng;
  gId('gsBsci').textContent = sci;
  gId('gsBhist').textContent = hist;
  gId('gsBkorG').textContent = rKor.g+'등급';
  gId('gsBmathG').textContent = rMath.g+'등급';
  gId('gsBengG').textContent = rEng.g+'등급';
  gId('gsBsciG').textContent = rSci.g+'등급';
  gId('gsBhistG').textContent = rHist.g+'등급';

  // Average grade (for ring + banner)
  const avgG = (rKor.g + rMath.g + rEng.g + rSci.g + rHist.g) / 5;
  const gsTotal = gId('gsTotal');
  const gsArc = gId('gsArc');
  const gsGradeTxt = gId('gsGradeTxt');
  const gsBanner = gId('gsBanner');

  const arcCirc = 377;
  const pct = Math.max(5, Math.min(100, 100 - (avgG-1)*12));
  const off = arcCirc - (pct/100)*arcCirc;
  gsArc.setAttribute('stroke-dashoffset', off);

  // Color
  let color='var(--low)', gradeLabel='', bannerClass='low';
  if (avgG <= 1.5) { color='var(--vhigh)'; gradeLabel='최상위권'; bannerClass='god'; }
  else if (avgG <= 2.5) { color='var(--high)'; gradeLabel='상위권'; bannerClass='high'; }
  else if (avgG <= 4.0) { color='var(--mid)'; gradeLabel='중위권'; bannerClass='mid'; }
  else if (avgG <= 6.0) { color='var(--warn)'; gradeLabel='하위권'; bannerClass='mid'; }
  else { color='var(--low)'; gradeLabel='기초 부족'; bannerClass='low'; }
  gsArc.style.stroke = color;
  gsGradeTxt.textContent = gradeLabel;
  gsGradeTxt.className = 'grade grade-'+bannerClass;

  gsTotal.textContent = avgG.toFixed(1);
  gsTotal.style.color = color;

  gsBanner.className = 'verdict-banner '+bannerClass;
  gsBanner.innerHTML = '<span>'+gradeLabel+': 평균 '+avgG.toFixed(1)+'등급</span><div class="detail">국어:'+rKor.g+' 수학:'+rMath.g+' 영어:'+rEng.g+' 탐구:'+rSci.g+' 한국사:'+rHist.g+'</div>';

  // University table
  const univBody = gId('gsUnivBody');
  let h = '';
  UNIV_TABLE.forEach(u => {
    const pass = avgG <= u.r;
    const gradeDiff = (avgG - u.r).toFixed(1);
    h += '<div class="r-row"><span class="r-name">'+u.n+'</span><span class="r-cut">'+u.r.toFixed(1)+'등급↑</span><span class="r-result '+(pass?'pass':'fail')+'">'+(pass?'✅ 가능':'❌ '+(gradeDiff>0?'+'+gradeDiff:gradeDiff)+'등급차')+'</span></div>';
  });
  univBody.innerHTML = h;

  // Save to localStorage
  svls('gradecalc', {kor,math,eng,sci,hist});
}

function leadScore() {
  const kor = parseInt(gId('kor').value)||0;
  const math = parseInt(gId('math').value)||0;
  const eng = parseInt(gId('eng').value)||0;
  const sci = parseInt(gId('sci').value)||0;
  const hist = parseInt(gId('hist').value)||0;
  return kor+'점|'+math+'점|'+eng+'점|'+sci+'점|'+hist+'점';
}

const subjMapGS = {kor:'kor',math:'math',eng:'eng',sci:'sci',hist:'hist'};
const subjMaxGS = {kor:100,math:100,eng:100,sci:50,hist:50};

function syncNumGS(id, max) {
  let v = parseInt(gId(id+'Num').value)||0;
  v = Math.max(0, Math.min(v, max));
  gId(id+'Num').value = v;
  gId(id).value = v;
  fillGS(id, max);
  computeGrade();
}
function syncSldGS(id, max) {
  const s = gId(id);
  gId(id+'Num').value = s.value;
  fillGS(id, max);
  computeGrade();
}
function fillGS(id, max) {
  const p = (parseInt(gId(id).value)/max)*100;
  gId('fill'+id.charAt(0).toUpperCase()+id.slice(1)).style.width = p+'%';
}

// Load saved
window.addEventListener('DOMContentLoaded', () => {
  const d = ldls('gradecalc', null);
  if (d) {
    Object.keys(subjMapGS).forEach(k => {
      if (d[k] !== undefined) {
        gId(k).value = d[k];
        gId(k+'Num').value = d[k];
        fillGS(k, subjMaxGS[k]);
      }
    });
    computeGrade();
  }
});
