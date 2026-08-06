import re
import json

with open('gen_python_basics.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. ADD TAB BAR BUTTON
old_tab_bar = """  <nav class="tab-bar">
    <button class="tab-btn active" id="tabExplore" data-tab="explore">🚀 행성 탐험</button>
    <button class="tab-btn" id="tabProblems" data-tab="problems">🧠 생각하는 응용문제</button>
  </nav>"""
new_tab_bar = """  <nav class="tab-bar">
    <button class="tab-btn active" id="tabExplore" data-tab="explore">🚀 행성 탐험</button>
    <button class="tab-btn" id="tabProblems" data-tab="problems">🧠 생각하는 응용문제</button>
    <button class="tab-btn" id="tabTest" data-tab="test">💯 실력 평가</button>
  </nav>"""
content = content.replace(old_tab_bar, new_tab_bar)

# 2. ADD TEST VIEW HTML
test_view_html = """
  <!-- SCORE TEST TAB VIEW -->
  <div class="test-view" id="testView" style="display:none;">
    <div class="problem-card">
      <div class="lesson-head">
        <div class="emoji">💯</div>
        <h2>실력 평가 테스트 (20문제)</h2>
      </div>
      <div class="speech">🐍 모든 문제를 풀고 맨 아래의 <b>'답안 제출하기'</b> 버튼을 누르면 채점됩니다! 100점에 도전해봐요!</div>
      
      <div id="testList" style="margin-top:20px;"></div>
      
      <div class="test-submit-area" style="text-align:center; margin-top:30px;">
        <button class="next-btn ready" id="submitTestBtn" style="font-size:18px; padding:15px 30px;">답안 제출하기</button>
      </div>
      <div id="testResultArea" style="display:none; text-align:center; margin-top:20px; padding:20px; background:var(--bg-panel-2); border-radius:12px; border:2px solid var(--accent-gold);">
        <h2 style="color:var(--accent-gold); font-size:32px; margin-bottom:10px;" id="testScoreDisplay"></h2>
        <div class="speech" id="testFeedbackMsg" style="font-size:18px;"></div>
      </div>
    </div>
  </div>
"""

content = content.replace('  <!-- TROPHY VIEW -->', test_view_html + '\n  <!-- TROPHY VIEW -->')

# 3. ADD CSS
css_to_add = """
.test-view{display:none;}
.test-view.show{display:block; animation: pop-in .25s ease;}
.test-q-card{
  background:var(--bg-panel-2); border:1px solid var(--border-soft); border-radius:12px;
  padding:16px; margin-bottom:16px;
}
.test-q-text{
  font-size:16px; font-weight:600; color:var(--text-light); margin-bottom:12px;
}
.test-choice-btn{
  display:block; width:100%; text-align:left; background:var(--bg-deep);
  border:1px solid var(--border-soft); border-radius:8px; padding:12px;
  color:var(--text-muted); cursor:pointer; font-size:14px; margin-bottom:8px;
  transition:all 0.2s; font-family:'Gowun Dodum',sans-serif;
}
.test-choice-btn:hover{ border-color:var(--accent-blue); color:var(--text-light); }
.test-choice-btn.selected{
  background:rgba(75,139,255,0.15); border-color:var(--accent-blue); color:var(--text-light);
}
.test-choice-btn.correct-ans{
  background:rgba(67,229,180,0.15); border-color:var(--accent-mint); color:var(--text-light);
}
.test-choice-btn.wrong-ans{
  background:rgba(255,107,107,0.15); border-color:var(--accent-coral); color:var(--text-light);
  text-decoration: line-through;
}
"""
content = content.replace('/* ===== TAB BAR ===== */', css_to_add + '\n/* ===== TAB BAR ===== */')


# 4. JS LOGIC (switchTab, event listener, state, test problems, render, submit)
# Add to switchTab
content = content.replace("document.getElementById('tabProblems').classList.toggle('active', tab==='problems');",
                          "document.getElementById('tabProblems').classList.toggle('active', tab==='problems');\n  document.getElementById('tabTest').classList.toggle('active', tab==='test');")
content = content.replace("document.getElementById('problemsView').classList.toggle('show', name==='problems');",
                          "document.getElementById('problemsView').classList.toggle('show', name==='problems');\n  document.getElementById('testView').classList.toggle('show', name==='test');")

content = content.replace("document.getElementById('tabProblems').addEventListener('click', ()=>switchTab('problems'));",
                          "document.getElementById('tabProblems').addEventListener('click', ()=>switchTab('problems'));\ndocument.getElementById('tabTest').addEventListener('click', ()=>switchTab('test'));")


# Generate 20 test problems
test_problems = [
    {"q": "파이썬에서 화면에 글자를 보여주기 위해 사용하는 명령어는?", "choices": ["print()", "say()", "show()", "write()"], "answer": 0},
    {"q": "다음 중 파이썬에서 글자(문자열)를 감쌀 때 사용하는 기호는?", "choices": ["따옴표 (\" \")", "괄호 ( )", "대괄호 [ ]", "별표 * *"], "answer": 0},
    {"q": "다음 코드를 실행하면 어떤 결과가 나올까요?\\nprint('10' + '5')", "choices": ["105", "15", "10 + 5", "오류 발생"], "answer": 0},
    {"q": "변수 `age`에 숫자 10을 넣으려고 합니다. 알맞은 코드는?", "choices": ["age = 10", "age == 10", "10 = age", "age <- 10"], "answer": 0},
    {"q": "파이썬에서 '같다'를 의미하는 기호는?", "choices": ["==", "=", "!=", ">="], "answer": 0},
    {"q": "리스트를 만들 때 사용하는 괄호 모양은?", "choices": ["[ ]", "( )", "{ }", "< >"], "answer": 0},
    {"q": "리스트 `colors = ['빨', '주', '노']`에서 첫 번째 값인 '빨'을 꺼내는 코드는?", "choices": ["colors[0]", "colors[1]", "colors.first()", "colors['빨']"], "answer": 0},
    {"q": "리스트의 길이나 크기(들어있는 개수)를 재는 명령어는?", "choices": ["len()", "size()", "count()", "length()"], "answer": 0},
    {"q": "파이썬에서 '만약 날씨가 맑다면' 이라는 조건을 쓸 때 사용하는 키워드는?", "choices": ["if", "for", "while", "else"], "answer": 0},
    {"q": "if문의 조건이 거짓일 때 실행되는 부분은?", "choices": ["else", "if", "for", "def"], "answer": 0},
    {"q": "10을 3으로 나눈 '나머지'를 구하는 연산자는?", "choices": ["%", "/", "//", "mod"], "answer": 0},
    {"q": "두 조건이 '모두 참'일 때만 참이 되게 하는 키워드는?", "choices": ["and", "or", "both", "all"], "answer": 0},
    {"q": "리스트의 맨 끝에 새로운 값을 추가할 때 사용하는 명령어는?", "choices": ["append()", "add()", "insert()", "push()"], "answer": 0},
    {"q": "정해진 횟수만큼 반복할 때 주로 사용하는 반복문은?", "choices": ["for문", "while문", "if문", "def문"], "answer": 0},
    {"q": "for i in range(3): 은 몇 번 반복될까요?", "choices": ["3번", "4번", "2번", "반복되지 않음"], "answer": 0},
    {"q": "조건이 참인 동안 '계속해서' 반복하는 반복문은?", "choices": ["while문", "for문", "loop문", "continue"], "answer": 0},
    {"q": "while문 안에서 값이 변하지 않아 영원히 반복되는 현상을 무엇이라고 할까요?", "choices": ["무한 반복", "에러", "무한 출력", "타임아웃"], "answer": 0},
    {"q": "나만의 새로운 명령어를 만들고 싶을 때 사용하는 키워드는?", "choices": ["def", "function", "make", "create"], "answer": 0},
    {"q": "함수를 선언할 때, 함수 안으로 전달해주는 값을 담는 통을 무엇이라고 할까요?", "choices": ["매개변수", "결과값", "리스트", "조건문"], "answer": 0},
    {"q": "파이썬에서 '참'을 의미하는 특별한 단어는 무엇일까요?", "choices": ["True", "true", "Yes", "O"], "answer": 0},
]

js_test_problems = "const TEST_PROBLEMS = [\n"
for q in test_problems:
    js_test_problems += f"  {{ q:`{q['q']}`, choices:[`{q['choices'][0]}`, `{q['choices'][1]}`, `{q['choices'][2]}`, `{q['choices'][3]}`], answer: {q['answer']} }},\n"
js_test_problems += "];\n"

js_test_logic = """
const testState = {
  answers: new Array(20).fill(-1),
  submitted: false
};

function renderTest(){
  const list = document.getElementById('testList');
  list.innerHTML = '';
  TEST_PROBLEMS.forEach((q, qi)=>{
    const qDiv = document.createElement('div');
    qDiv.className = 'test-q-card';
    qDiv.innerHTML = `<div class="test-q-text">Q${qi+1}. ${q.q}</div>
                      <div class="test-choices" id="test-choices-${qi}"></div>`;
    const cWrap = qDiv.querySelector('.test-choices');
    q.shuffledChoices.forEach((choiceObj, ci)=>{
      const btn = document.createElement('button');
      btn.className = 'test-choice-btn';
      btn.textContent = `${['①','②','③','④'][ci]} ${choiceObj.text}`;
      btn.addEventListener('click', ()=>{
        if(testState.submitted) return;
        testState.answers[qi] = ci;
        cWrap.querySelectorAll('.test-choice-btn').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
      });
      cWrap.appendChild(btn);
    });
    list.appendChild(qDiv);
  });
}

document.getElementById('submitTestBtn').addEventListener('click', ()=>{
  if(testState.submitted) return;
  if(testState.answers.includes(-1)){
    alert("아직 풀지 않은 문제가 있습니다. 모든 문제를 풀어주세요!");
    return;
  }
  
  testState.submitted = true;
  document.getElementById('submitTestBtn').style.display = 'none';
  
  let correctCount = 0;
  TEST_PROBLEMS.forEach((q, qi)=>{
    const selectedIdx = testState.answers[qi];
    const cWrap = document.getElementById(`test-choices-${qi}`);
    const btns = cWrap.querySelectorAll('.test-choice-btn');
    
    let isCorrect = q.shuffledChoices[selectedIdx].isCorrect;
    if(isCorrect) correctCount++;
    
    q.shuffledChoices.forEach((choiceObj, ci)=>{
      if(choiceObj.isCorrect) {
        btns[ci].classList.add('correct-ans');
      } else if (ci === selectedIdx && !choiceObj.isCorrect) {
        btns[ci].classList.add('wrong-ans');
      }
    });
  });
  
  const score = correctCount * 5;
  const resultArea = document.getElementById('testResultArea');
  resultArea.style.display = 'block';
  document.getElementById('testScoreDisplay').textContent = `🎉 내 점수: ${score}점 (${correctCount}/20)`;
  
  let msg = '';
  if(score === 100) msg = '만점입니다! 파이썬 마스터 칭호를 획득했어요! 🏆';
  else if(score >= 80) msg = '정말 훌륭해요! 파이썬의 핵심을 아주 잘 이해하고 있군요! 👍';
  else if(score >= 60) msg = '좋아요! 틀린 문제를 다시 확인해 보세요. 😊';
  else msg = '조금 더 연습이 필요해요. 파이썬 행성들을 다시 복습해 볼까요? 💪';
  
  document.getElementById('testFeedbackMsg').textContent = msg;
  window.scrollTo({top: document.getElementById('testResultArea').offsetTop - 50, behavior: 'smooth'});
});
"""

# Insert js_test_problems and js_test_logic right before `function updateProblemsProgress()`
content = content.replace('function updateProblemsProgress(){', js_test_problems + '\n' + js_test_logic + '\nfunction updateProblemsProgress(){')

# Add shuffle logic for TEST_PROBLEMS in init
shuffle_test = """
if (typeof TEST_PROBLEMS !== 'undefined') {
  TEST_PROBLEMS.forEach(q => {
    let objs = q.choices.map((text, i) => ({ text, isCorrect: i === q.answer }));
    shuffleArray(objs);
    q.shuffledChoices = objs;
  });
}
"""
content = content.replace("if (typeof PROBLEMS !== 'undefined') {", shuffle_test + "\nif (typeof PROBLEMS !== 'undefined') {")

content = content.replace("renderProblems();\n</script>", "renderProblems();\nrenderTest();\n</script>")

with open('gen_python_basics.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Score test successfully generated.")
