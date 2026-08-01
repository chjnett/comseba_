import re

with open('gen_python_basics.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS
css_addition = """
  /* ===== TAB BAR ===== */
  .tab-bar{
    display:flex; gap:8px; margin-bottom:22px;
    border-bottom:1px solid var(--border-soft); padding-bottom:0;
  }
  .tab-btn{
    background:none; border:none; color:var(--text-muted);
    font-family:'Jua',sans-serif; font-size:14.5px; padding:10px 6px 12px;
    cursor:pointer; position:relative; border-bottom:3px solid transparent;
  }
  .tab-btn:hover{color:var(--text-light);}
  .tab-btn.active{color:var(--accent-gold); border-bottom-color:var(--accent-gold);}

  /* ===== PROBLEMS TAB ===== */
  .problems-view{display:none;}
  .problems-view.show{display:block; animation: pop-in .25s ease;}

  .problem-card{
    background:var(--bg-panel); border:1px solid var(--border-soft); border-radius:18px;
    margin-bottom:16px; overflow:hidden;
  }
  .problem-head{
    display:flex; align-items:center; gap:14px; padding:18px 20px; cursor:pointer;
  }
  .problem-head .pnum{
    font-family:'Jua',sans-serif; font-size:13px; color:var(--bg-deep);
    background:var(--accent-blue); width:30px;height:30px;border-radius:50%;
    display:flex;align-items:center;justify-content:center; flex-shrink:0;
  }
  .problem-card.solved .problem-head .pnum{background:var(--accent-mint);}
  .problem-head .ptitle{flex:1;}
  .problem-head .ptitle .pname{font-family:'Jua',sans-serif; font-size:15.5px;}
  .problem-head .ptitle .ptag{font-size:11.5px; color:var(--text-muted); margin-top:2px;}
  .problem-head .pchev{color:var(--text-muted); font-size:13px; transition: transform .2s;}
  .problem-card.open .pchev{transform:rotate(180deg);}
  .problem-card.solved .problem-head{background:rgba(67,229,180,.06);}

  .problem-body{display:none; padding:0 20px 22px;}
  .problem-card.open .problem-body{display:block; animation: pop-in .2s ease;}
  .problem-scenario{
    font-size:14.5px; line-height:1.75; color:var(--text-light); margin-bottom:14px;
    background:var(--bg-panel-2); border-radius:12px; padding:14px 16px;
  }
  .problem-body .explain-box{
    display:none; margin-top:12px; font-size:13.5px; line-height:1.7;
    background:rgba(75,139,255,.08); border:1px solid rgba(75,139,255,.25);
    border-radius:12px; padding:12px 16px; color:#BFD6FF;
  }

  /* ===== MAP VIEW ===== */"""
content = content.replace("  /* ===== MAP VIEW ===== */", css_addition, 1)

# 2. Media query
content = content.replace("  @media(max-width:520px){\n    .planet-info .desc{display:none;}\n    .lesson-card{padding:18px;}\n  }", "  @media(max-width:520px){\n    .planet-info .desc{display:none;}\n    .lesson-card{padding:18px;}\n    .tab-btn{font-size:12.5px; padding:8px 4px 10px;}\n  }")

# 3. HTML Tab bar
html_tabs = """
  <nav class="tab-bar">
    <button class="tab-btn active" id="tabExplore" data-tab="explore">🚀 행성 탐험</button>
    <button class="tab-btn" id="tabProblems" data-tab="problems">🧠 생각하는 응용문제</button>
  </nav>

  <!-- MAP VIEW -->"""
content = content.replace("  <!-- MAP VIEW -->", html_tabs, 1)

# 4. HTML Problems View
html_problems_view = """  <!-- TROPHY VIEW -->
  <div id="trophyView" class="lesson-view"></div>

  <!-- APPLIED PROBLEMS TAB VIEW -->
  <div id="problemsView" class="problems-view">
    <div class="map-intro">
      <div class="mascot">🧠</div>
      <p>여기서는 배운 걸 그대로 따라 쓰는 게 아니라, <b>직접 생각해서</b> 풀어보는 문제들이 있어요.<br>정답이 바로 안 보여도 괜찮아요. 코드를 천천히 읽고 무슨 일이 일어날지 상상해보세요! 🔍</p>
    </div>
    <div class="stat-pill" id="problemsProgressPill" style="width:fit-content;margin:0 0 18px;">🧩 해결한 문제 <span id="probSolvedCount">0</span> / <span id="probTotalCount">0</span></div>
    <div id="problemsList"></div>
  </div>
</div>"""
content = content.replace('  <!-- TROPHY VIEW -->\n  <div id="trophyView" class="lesson-view"></div>\n</div>', html_problems_view, 1)

# 5. JS showView & switchTab
js_show_view = """function showView(name){
  document.getElementById('mapView').style.display = name==='map' ? '' : 'none';
  document.getElementById('lessonView').classList.toggle('show', name==='lesson');
  document.getElementById('trophyView').classList.toggle('show', name==='trophy');
  document.getElementById('problemsView').classList.toggle('show', name==='problems');
  window.scrollTo({top:0, behavior:'smooth'});
}

/* ---------------- tab switching ---------------- */
function switchTab(tab){
  document.getElementById('tabExplore').classList.toggle('active', tab==='explore');
  document.getElementById('tabProblems').classList.toggle('active', tab==='problems');
  if(tab==='explore'){
    showView('map');
  } else {
    showView('problems');
  }
}
document.getElementById('tabExplore').addEventListener('click', ()=>switchTab('explore'));
document.getElementById('tabProblems').addEventListener('click', ()=>switchTab('problems'));"""

old_js_show_view = """function showView(name){
  document.getElementById('mapView').style.display = name==='map' ? '' : 'none';
  document.getElementById('lessonView').classList.toggle('show', name==='lesson');
  document.getElementById('trophyView').classList.toggle('show', name==='trophy');
  window.scrollTo({top:0, behavior:'smooth'});
}"""
content = content.replace(old_js_show_view, js_show_view, 1)

# 6. JS Problems
js_problems = """/* ---------------- APPLIED THINKING PROBLEMS ---------------- */
const PROBLEMS = [
  {
    emoji:'🍬', title:'사탕 나누기', tag:'문제해결 · 쉬움',
    scenario:'민준이는 사탕 12개를 가지고 있어요. 친구 3명에게 <b>똑같이</b> 나누어 주려고 해요.<br>한 명이 사탕을 몇 개씩 받게 될지 알려주는 코드는 무엇일까요?',
    code:null,
    choices:[
      {text:'print(12 / 3)', correct:true, feedback:'✅ 정답이에요! 12개를 3명이 똑같이 나누면 한 명당 4개씩 받아요. "나눈다"는 나누기(/) 연산이에요.'},
      {text:'print(12 - 3)', correct:false, feedback:'🤔 빼기를 하면 "나눠준다"는 뜻이 되지 않아요. 똑같이 나눌 땐 나누기(/)를 사용해야 해요.'},
      {text:'print(12 * 3)', correct:false, feedback:'🤔 곱하기를 하면 사탕이 오히려 더 늘어나버려요! 나누기(/)를 사용해야 해요.'}
    ]
  },
  {
    emoji:'🐞', title:'오류 찾기', tag:'디버깅 · 쉬움',
    scenario:'다음 코드를 실행하면 오류가 나요. 무엇이 문제일까요?',
    code:'print(안녕하세요)',
    choices:[
      {text:'따옴표(" ")가 빠졌어요', correct:true, feedback:'✅ 맞아요! 글자(문자열)는 반드시 따옴표로 감싸야 해요. print("안녕하세요") 라고 써야 해요.'},
      {text:'print라는 단어가 틀렸어요', correct:false, feedback:'🤔 print는 정확한 명령어예요. 문제는 다른 곳에 있어요.'},
      {text:'괄호가 필요 없어요', correct:false, feedback:'🤔 아니에요, 괄호는 꼭 필요해요! 괄호 안의 내용을 다시 살펴보세요.'}
    ]
  },
  {
    emoji:'🔮', title:'출력 예측하기', tag:'예측하기 · 보통',
    scenario:'다음 코드를 실행하면 화면에 무엇이 나올까요? 코드를 천천히 읽고 먼저 머릿속으로 계산해보세요.',
    code:'score = 72\\nif score >= 90:\\n    print("최우수")\\nelif score >= 70:\\n    print("우수")\\nelse:\\n    print("노력")',
    choices:[
      {text:'최우수', correct:false, feedback:'🤔 score(72)는 90 이상이 아니에요. 다음 조건도 확인해보세요.'},
      {text:'우수', correct:true, feedback:'✅ 정답! 72는 90 이상은 아니지만 70 이상이라서 elif 조건에 걸려요.'},
      {text:'노력', correct:false, feedback:'🤔 72는 70 이상이니까 elif 조건에서 이미 걸려요. else까지 가지 않아요.'},
      {text:'아무것도 안 나온다', correct:false, feedback:'🤔 if / elif / else 중 반드시 하나는 실행돼요.'}
    ]
  },
  {
    emoji:'🔁', title:'몇 번 출력될까?', tag:'반복 추론 · 보통',
    scenario:'아래 코드를 실행하면 숫자가 몇 번 출력될까요? 0부터 5까지 하나씩 손가락으로 짚어가며 세어보세요.',
    code:'for i in range(6):\\n    if i % 2 == 0:\\n        print(i)',
    choices:[
      {text:'3번 (0, 2, 4)', correct:true, feedback:'✅ 맞아요! range(6)은 0~5까지 반복하고, 그중 짝수(0,2,4)만 출력돼요.'},
      {text:'6번', correct:false, feedback:'🤔 if 조건 때문에 짝수일 때만 출력돼요. 전부 다 출력되는 게 아니에요.'},
      {text:'2번', correct:false, feedback:'🤔 0도 짝수라는 걸 잊지 마세요! 0, 2, 4 이렇게 3번이에요.'},
      {text:'0번', correct:false, feedback:'🤔 조건을 만족하는 숫자가 분명히 있어요. 하나씩 다시 세어보세요.'}
    ]
  },
  {
    emoji:'🧩', title:'순서를 맞춰라', tag:'논리적 사고 · 보통',
    scenario:'이름을 저장하고 인사말을 출력하는 프로그램을 만들려고 해요.<br><br>① <code>print(name + "야, 반가워!")</code><br>② <code>name = "하늘"</code><br><br>①과 ② 중 어떤 순서로 실행해야 올바르게 동작할까요?',
    code:null,
    choices:[
      {text:'② 먼저 실행하고, 그다음 ①', correct:true, feedback:'✅ 정답이에요! 변수는 반드시 값을 먼저 저장(②)해야, 그 값을 사용(①)할 수 있어요.'},
      {text:'① 먼저 실행하고, 그다음 ②', correct:false, feedback:'🤔 name이라는 변수가 아직 만들어지기 전에 사용하면 오류가 나요!'},
      {text:'순서는 상관없다', correct:false, feedback:'🤔 아니에요, 파이썬은 코드를 위에서 아래로 순서대로 실행해요. 순서가 중요해요!'}
    ]
  },
  {
    emoji:'🏆', title:'가장 큰 키 찾기', tag:'개념 이해 · 보통',
    scenario:'친구들의 키가 담긴 리스트 <code>[132, 145, 128, 150]</code> 에서 가장 큰 키를 컴퓨터는 어떻게 찾아낼까요?',
    code:null,
    choices:[
      {text:'가장 큰 값을 저장할 변수를 만들고, 하나씩 비교하면서 더 큰 값이 나오면 바꿔준다', correct:true, feedback:'✅ 맞아요! 컴퓨터는 사람처럼 한눈에 보지 못해서, 하나씩 순서대로 비교하며 "지금까지 가장 큰 값"을 계속 갱신해요.'},
      {text:'리스트의 첫 번째 값이 항상 가장 크다고 생각한다', correct:false, feedback:'🤔 첫 번째 값(132)은 가장 작은 값이에요! 모든 값을 비교해봐야 알 수 있어요.'},
      {text:'리스트를 무작위로 섞은 뒤 아무 값이나 고른다', correct:false, feedback:'🤔 그러면 정확한 답을 찾을 수 없어요. 하나씩 순서대로 비교해야 해요.'}
    ]
  },
  {
    emoji:'🧠', title:'멈추지 않는 코드', tag:'디버깅 · 어려움',
    scenario:'다음 코드를 실행하면 어떤 일이 벌어질까요?',
    code:'n = 5\\nwhile n > 0:\\n    print(n)',
    choices:[
      {text:'n 값이 줄어들지 않아서 무한히 반복된다', correct:true, feedback:'✅ 정답이에요! n을 줄이는 코드(n = n - 1)가 없어서 n은 계속 5로 남아있고, 조건 n > 0 은 영원히 참이 돼요.'},
      {text:'5부터 1까지 출력되고 멈춘다', correct:false, feedback:'🤔 n 값을 줄여주는 코드가 어디에도 없어요! n이 줄어들지 않으면 조건은 계속 참이에요.'},
      {text:'한 번만 실행되고 끝난다', correct:false, feedback:'🤔 while은 조건이 거짓이 될 때까지 계속 반복해요. 조건이 바뀌지 않으면 멈추지 않아요.'}
    ]
  },
  {
    emoji:'🎨', title:'알맞은 도구 고르기', tag:'개념 이해 · 어려움',
    scenario:'구슬치기에서 이긴 친구에게 "축하해!"라는 메시지를 <b>정확히 5번</b> 출력하고 싶어요.<br><code>for</code>와 <code>while</code> 중 어떤 것이 더 어울릴까요?',
    code:null,
    choices:[
      {text:'for - 반복 횟수(5번)가 미리 정해져 있으니까', correct:true, feedback:'✅ 맞아요! 반복 횟수를 미리 알고 있을 땐 for가 더 간단하고 실수도 적어요.'},
      {text:'while - 조건 없이 무조건 쓰는 게 좋으니까', correct:false, feedback:'🤔 while은 조건에 따라 반복 횟수가 달라질 때 유용해요. 정해진 횟수엔 for가 더 어울려요.'},
      {text:'둘 다 어울리지 않는다', correct:false, feedback:'🤔 사실 둘 다 사용은 가능하지만, 이 상황엔 더 알맞은 도구가 있어요!'}
    ]
  }
];
const problemState = PROBLEMS.map(()=>false);

function updateProblemsProgress(){
  const solved = problemState.filter(Boolean).length;
  document.getElementById('probSolvedCount').textContent = solved;
  document.getElementById('probTotalCount').textContent = PROBLEMS.length;
}

function renderProblems(){
  const list = document.getElementById('problemsList');
  list.innerHTML = '';
  PROBLEMS.forEach((p, idx)=>{
    const card = document.createElement('div');
    card.className = 'problem-card';
    card.innerHTML = `
      <div class="problem-head">
        <div class="pnum">${idx+1}</div>
        <div class="ptitle">
          <div class="pname">${p.emoji} ${p.title}</div>
          <div class="ptag">${p.tag}</div>
        </div>
        <div class="pchev">▼</div>
      </div>
      <div class="problem-body">
        <div class="problem-scenario">${p.scenario}</div>
        ${p.code ? `<div class="code-block">${escapeHtml(p.code)}</div>` : ''}
        <div class="mission-choices"></div>
        <div class="explain-box"></div>
      </div>
    `;
    const head = card.querySelector('.problem-head');
    head.addEventListener('click', ()=>{ card.classList.toggle('open'); });

    const choicesWrap = card.querySelector('.mission-choices');
    const explainBox = card.querySelector('.explain-box');
    p.choices.forEach(c=>{
      const btn = document.createElement('button');
      btn.className = 'choice-btn';
      btn.style.fontFamily = "'Gowun Dodum',sans-serif";
      btn.textContent = c.text;
      btn.addEventListener('click', (e)=>{
        e.stopPropagation();
        explainBox.style.display = 'block';
        explainBox.textContent = c.feedback;
        if(c.correct){
          btn.classList.add('correct');
          choicesWrap.querySelectorAll('.choice-btn').forEach(x=>x.disabled=true);
          if(!problemState[idx]){
            problemState[idx] = true;
            card.classList.add('solved');
            const rect = btn.getBoundingClientRect();
            burstConfetti(rect.left, rect.top);
            updateProblemsProgress();
          }
        } else {
          btn.classList.add('wrong');
          setTimeout(()=>btn.classList.remove('wrong'), 400);
        }
      });
      choicesWrap.appendChild(btn);
    });

    list.appendChild(card);
  });
  updateProblemsProgress();
}

/* ---------------- init ---------------- */
renderMap();
renderProblems();
</script>"""

content = content.replace("/* ---------------- init ---------------- */\nrenderMap();\n</script>", js_problems)

with open('gen_python_basics.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("gen_python_basics.py updated successfully!")
