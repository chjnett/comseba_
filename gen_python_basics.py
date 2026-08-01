html_content = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>파이썬 행성 탐험대</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jua&family=Gowun+Dodum&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root{
    --bg-deep:#0B1226;
    --bg-panel:#131B36;
    --bg-panel-2:#1B2547;
    --accent-gold:#FFD43B;
    --accent-blue:#4B8BFF;
    --accent-mint:#43E5B4;
    --accent-coral:#FF6B6B;
    --text-light:#EAF0FF;
    --text-muted:#8B96B8;
    --border-soft: rgba(234,240,255,0.08);
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background:
      radial-gradient(ellipse at 20% -10%, rgba(75,139,255,0.18), transparent 55%),
      radial-gradient(ellipse at 90% 10%, rgba(255,212,59,0.10), transparent 45%),
      var(--bg-deep);
    color:var(--text-light);
    font-family:'Gowun Dodum', sans-serif;
    min-height:100vh;
    overflow-x:hidden;
    position:relative;
  }
  /* twinkling stars background */
  .stars{position:fixed;inset:0;z-index:0;pointer-events:none;}
  .stars span{
    position:absolute;width:2px;height:2px;background:#fff;border-radius:50%;
    opacity:.5; animation: twinkle 3.5s ease-in-out infinite;
  }
  @keyframes twinkle{0%,100%{opacity:.15;}50%{opacity:.9;}}
  @keyframes float-y{0%,100%{transform:translateY(0);}50%{transform:translateY(-8px);}}
  @keyframes pop-in{from{transform:scale(.85);opacity:0;}to{transform:scale(1);opacity:1;}}
  @keyframes shake{10%,90%{transform:translateX(-2px)}20%,80%{transform:translateX(3px)}30%,50%,70%{transform:translateX(-5px)}40%,60%{transform:translateX(5px)}}
  @keyframes burst{0%{transform:scale(0) rotate(0);opacity:1;}100%{transform:scale(1.6) rotate(60deg);opacity:0;}}

  .app{position:relative;z-index:1;max-width:920px;margin:0 auto;padding:20px 16px 60px;}

  header.top{
    display:flex;align-items:center;justify-content:space-between;
    padding:10px 4px 18px;
  }
  .brand{display:flex;align-items:center;gap:10px;}
  .brand .rocket-icon{font-size:26px; animation: float-y 2.6s ease-in-out infinite;}
  .brand h1{
    font-family:'Jua',sans-serif; font-size:22px; margin:0; letter-spacing:.5px;
    color:var(--text-light);
  }
  .brand small{display:block;color:var(--text-muted);font-size:12px;margin-top:2px;}
  .stat-pill{
    display:flex;align-items:center;gap:6px;
    background:var(--bg-panel); border:1px solid var(--border-soft);
    padding:8px 14px;border-radius:999px; font-family:'Jua',sans-serif;
    font-size:15px; color:var(--accent-gold);
    box-shadow:0 4px 14px rgba(0,0,0,.25);
  }

  /* ===== MAP VIEW ===== */
  .map-intro{
    background:linear-gradient(135deg, var(--bg-panel), var(--bg-panel-2));
    border:1px solid var(--border-soft); border-radius:20px;
    padding:20px 22px; margin-bottom:26px;
    display:flex; align-items:center; gap:16px;
  }
  .map-intro .mascot{font-size:40px; flex-shrink:0; animation: float-y 3s ease-in-out infinite;}
  .map-intro p{margin:0;line-height:1.6;font-size:15px;color:var(--text-light);}
  .map-intro b{color:var(--accent-gold);}

  .path-wrap{position:relative; padding:10px 0 20px;}
  .planet-row{
    display:flex; align-items:center; gap:16px; margin-bottom:6px; position:relative;
  }
  .planet-row.right{flex-direction:row-reverse; text-align:right;}
  .connector{
    position:absolute; left:34px; top:74px; width:2px; height:56px;
    background-image: linear-gradient(var(--border-soft) 60%, transparent 0%);
    background-size: 2px 12px; background-repeat: repeat-y;
  }
  .planet-row.right .connector{left:auto; right:34px;}

  .planet-node{
    position:relative; flex-shrink:0;
    width:68px;height:68px;border-radius:50%;
    display:flex;align-items:center;justify-content:center;
    font-size:28px; cursor:pointer; border:none;
    transition: transform .15s ease;
    font-family:'Jua',sans-serif;
  }
  .planet-node:hover{transform:scale(1.07);}
  .planet-node:active{transform:scale(.96);}
  .planet-node.locked{
    background:var(--bg-panel); border:2px dashed var(--border-soft); color:var(--text-muted);
    cursor:not-allowed;
  }
  .planet-node.locked:hover{transform:none;}
  .planet-node.available{
    background: radial-gradient(circle at 30% 25%, #6FA6FF, var(--accent-blue));
    box-shadow: 0 0 0 4px rgba(75,139,255,0.18), 0 8px 20px rgba(75,139,255,.35);
  }
  .planet-node.done{
    background: radial-gradient(circle at 30% 25%, #FFE477, var(--accent-gold));
    box-shadow: 0 0 0 4px rgba(255,212,59,0.18), 0 8px 20px rgba(255,212,59,.3);
    color:#3a2b00;
  }
  .planet-node .badge-check{
    position:absolute; top:-6px; right:-6px; background:var(--accent-mint);
    width:22px;height:22px;border-radius:50%; display:flex;align-items:center;justify-content:center;
    font-size:12px; border:2px solid var(--bg-deep); color:#03291d;
  }
  .planet-info{flex:1;}
  .planet-info .idx{font-size:12px;color:var(--text-muted);font-family:'JetBrains Mono',monospace;}
  .planet-info .name{font-family:'Jua',sans-serif;font-size:17px;margin:2px 0;}
  .planet-info .desc{font-size:13px;color:var(--text-muted);}
  .stars-earned{font-size:12px;color:var(--accent-gold);margin-top:3px;}

  .boss-row .planet-node{width:80px;height:80px;font-size:34px;}

  /* ===== LESSON VIEW ===== */
  .lesson-view{display:none;}
  .lesson-view.show{display:block; animation: pop-in .25s ease;}
  .back-btn{
    background:none;border:1px solid var(--border-soft); color:var(--text-light);
    padding:8px 14px;border-radius:10px;font-family:'Gowun Dodum',sans-serif;font-size:13px;
    cursor:pointer; margin-bottom:14px; display:inline-flex; align-items:center; gap:6px;
  }
  .back-btn:hover{border-color:var(--accent-blue); color:var(--accent-blue);}

  .lesson-card{
    background:var(--bg-panel); border:1px solid var(--border-soft); border-radius:20px;
    padding:24px; margin-bottom:18px;
  }
  .lesson-head{display:flex;align-items:center;gap:14px;margin-bottom:14px;}
  .lesson-head .emoji{font-size:36px;}
  .lesson-head h2{font-family:'Jua',sans-serif;font-size:21px;margin:0;color:var(--text-light);}

  .speech{
    background:var(--bg-panel-2); border-radius:14px; padding:16px 18px;
    line-height:1.75; font-size:15.5px; position:relative; margin-bottom:4px;
  }
  .speech b{color:var(--accent-gold);}
  .speech code{
    background:rgba(75,139,255,0.15); color:#9FC1FF; padding:1px 6px; border-radius:6px;
    font-family:'JetBrains Mono',monospace; font-size:.92em;
  }

  .section-label{
    font-family:'Jua',sans-serif; font-size:14px; color:var(--accent-blue);
    display:flex; align-items:center; gap:6px; margin:22px 0 10px;
  }

  .code-block{
    background:#0D1428; border:1px solid var(--border-soft); border-radius:12px;
    padding:16px 18px; font-family:'JetBrains Mono',monospace; font-size:13.5px;
    line-height:1.7; color:#D7E2FF; white-space:pre; overflow-x:auto;
  }
  .code-block .cm{color:#6B7FA6;}
  .code-block .str{color:#8FE3A3;}
  .code-block .kw{color:#FF9BC4;}
  .code-block .num{color:#FFD43B;}
  .code-block .fn{color:#7FC8FF;}

  .run-btn{
    margin-top:10px; background:var(--accent-blue); color:#fff; border:none;
    padding:9px 18px; border-radius:10px; font-family:'Jua',sans-serif; font-size:13px;
    cursor:pointer; display:inline-flex; align-items:center; gap:6px;
  }
  .run-btn:hover{filter:brightness(1.1);}
  .output-box{
    margin-top:10px; background:#04140E; border:1px solid rgba(67,229,180,.25); border-radius:12px;
    padding:14px 18px; font-family:'JetBrains Mono',monospace; font-size:13.5px; color:var(--accent-mint);
    display:none; white-space:pre-line;
  }
  .output-box .tag{color:var(--text-muted); font-size:11px; display:block; margin-bottom:6px; font-family:'Gowun Dodum',sans-serif;}

  .mission-choices{display:flex;flex-direction:column;gap:10px;margin-top:10px;}
  .choice-btn{
    text-align:left; background:#0D1428; border:1px solid var(--border-soft); color:var(--text-light);
    border-radius:12px; padding:12px 16px; font-family:'JetBrains Mono',monospace; font-size:13px;
    cursor:pointer; white-space:pre; line-height:1.6;
  }
  .choice-btn:hover{border-color:var(--accent-blue);}
  .choice-btn.correct{border-color:var(--accent-mint); background:rgba(67,229,180,.1); color:var(--accent-mint);}
  .choice-btn.wrong{border-color:var(--accent-coral); background:rgba(255,107,107,.1); color:#FFB3B3; animation: shake .4s;}
  .choice-btn:disabled{cursor:default;}
  .hint-box{
    margin-top:8px; font-size:13px; color:var(--accent-coral); display:none;
    font-family:'Gowun Dodum',sans-serif;
  }

  .quiz-q{margin-bottom:20px;}
  .quiz-q .qtext{font-size:15px; margin-bottom:10px; font-family:'Gowun Dodum',sans-serif;}
  .quiz-q .qtext b{color:var(--accent-gold); font-family:'JetBrains Mono',monospace;}

  .status-row{
    display:flex; gap:10px; margin:18px 0 6px; flex-wrap:wrap;
  }
  .status-chip{
    font-size:12px; padding:6px 12px; border-radius:999px; border:1px solid var(--border-soft);
    color:var(--text-muted); display:flex; align-items:center; gap:5px;
  }
  .status-chip.done{color:var(--accent-mint); border-color:rgba(67,229,180,.3); background:rgba(67,229,180,.08);}

  .next-btn{
    display:block; width:100%; margin-top:20px; padding:14px; border:none; border-radius:14px;
    background:var(--text-muted); color:var(--bg-deep); font-family:'Jua',sans-serif; font-size:16px;
    cursor:not-allowed; transition: all .2s;
  }
  .next-btn.ready{
    background:linear-gradient(135deg, var(--accent-gold), #FFB84B); cursor:pointer; color:#3a2b00;
    box-shadow:0 8px 20px rgba(255,212,59,.3);
  }
  .next-btn.ready:hover{filter:brightness(1.05);}

  .confetti{position:fixed; inset:0; pointer-events:none; z-index:50;}
  .confetti span{
    position:absolute; font-size:20px; animation: burst 1s ease-out forwards;
  }

  .trophy-screen{
    text-align:center; padding:50px 20px; background:var(--bg-panel); border-radius:20px;
    border:1px solid var(--border-soft);
  }
  .trophy-screen .big{font-size:64px; animation: float-y 2.4s ease-in-out infinite;}
  .trophy-screen h2{font-family:'Jua',sans-serif; font-size:24px; margin:14px 0 6px; color:var(--accent-gold);}
  .trophy-screen p{color:var(--text-muted); margin-bottom:20px;}
  .restart-btn{
    background:var(--accent-blue); color:#fff; border:none; padding:12px 24px; border-radius:12px;
    font-family:'Jua',sans-serif; cursor:pointer; font-size:14px;
  }

  @media(max-width:520px){
    .planet-info .desc{display:none;}
    .lesson-card{padding:18px;}
  }
</style>
</head>
<body>

<div class="stars" id="starsBg"></div>

<div class="app">
  <header class="top">
    <div class="brand">
      <span class="rocket-icon">🚀</span>
      <div>
        <h1>파이썬 행성 탐험대</h1>
        <small>재미있게 배우는 파이썬 기초 문법</small>
      </div>
    </div>
    <div class="stat-pill">⭐ <span id="starCount">0</span> / <span id="starTotal">0</span></div>
  </header>

  <!-- MAP VIEW -->
  <div id="mapView">
    <div class="map-intro">
      <div class="mascot">🐍</div>
      <p>안녕! 나는 <b>파이</b>야. 우주선을 타고 행성을 하나씩 탐험하면서<br>파이썬 코딩을 배워보자! 아래 행성을 눌러서 시작해볼까? 🌟</p>
    </div>
    <div class="path-wrap" id="pathWrap"></div>
  </div>

  <!-- LESSON VIEW -->
  <div id="lessonView" class="lesson-view"></div>

  <!-- TROPHY VIEW -->
  <div id="trophyView" class="lesson-view"></div>
</div>

<div class="confetti" id="confetti"></div>

<script>
/* ---------------- background stars ---------------- */
(function(){
  const el = document.getElementById('starsBg');
  let html = '';
  for(let i=0;i<80;i++){
    const x = Math.random()*100, y = Math.random()*100, d = (Math.random()*3+2).toFixed(1);
    html += `<span style="left:${x}%;top:${y}%;animation-duration:${d}s;animation-delay:${(Math.random()*3).toFixed(1)}s;"></span>`;
  }
  el.innerHTML = html;
})();

/* ---------------- lesson data ---------------- */
const LESSONS = [
  {
    id:0, emoji:'🐍', name:'파이썬 마을', desc:'print()로 말해보기',
    explain:`파이썬은 우리가 <b>컴퓨터에게 명령을 내리는 말</b>이에요.<br>
    <code>print()</code>는 화면에 글자를 보여주는 마법 주문이랍니다. 괄호 안에 보여주고 싶은 말을 <b>따옴표(" ")</b>로 감싸서 넣어주면 돼요!`,
    code:[
      {t:'kw',v:'print'},{t:'p',v:'('},{t:'str',v:'"안녕, 파이썬!"'},{t:'p',v:')'},{t:'nl'},
      {t:'kw',v:'print'},{t:'p',v:'('},{t:'str',v:'"나는 코딩을 배우고 있어요"'},{t:'p',v:')'}
    ],
    output:'안녕, 파이썬!\n나는 코딩을 배우고 있어요',
    mission:{
      goal:'화면에 "안녕하세요!" 를 출력하는 코드는 무엇일까요?',
      choices:[
        {code:'print("안녕하세요!")', correct:true, out:'안녕하세요!'},
        {code:'print(안녕하세요!)', correct:false, hint:'글자는 따옴표(" ")로 꼭 감싸야 해요!'},
        {code:'print "안녕하세요!"', correct:false, hint:'print 뒤에는 괄호 ( )가 필요해요!'}
      ]
    },
    quiz:[
      {q:'print() 의 역할은 무엇일까요?', choices:['화면에 글자를 보여준다','숫자를 지운다','컴퓨터를 끈다','그림을 그린다'], answer:0},
      {q:'다음 코드의 출력 결과는? <b>print("Hello")</b>', choices:['Hello','print','"Hello"','오류가 난다'], answer:0}
    ]
  },
  {
    id:1, emoji:'📦', name:'상자 행성', desc:'변수 만들기',
    explain:`<b>변수</b>는 이름표가 붙은 상자예요. 숫자나 글자를 넣어뒀다가 나중에 꺼내 쓸 수 있어요.<br>
    <code>이름 = 값</code> 처럼 <b>=</b> 기호를 사용해서 상자에 물건을 넣어줍니다.`,
    code:[
      {t:'fn',v:'name'},{t:'p',v:' = '},{t:'str',v:'"지민"'},{t:'nl'},
      {t:'fn',v:'age'},{t:'p',v:' = '},{t:'num',v:'11'},{t:'nl'},
      {t:'kw',v:'print'},{t:'p',v:'('},{t:'fn',v:'name'},{t:'p',v:')'},{t:'nl'},
      {t:'kw',v:'print'},{t:'p',v:'('},{t:'fn',v:'age'},{t:'p',v:')'}
    ],
    output:'지민\n11',
    mission:{
      goal:'변수 age에 12를 저장하고 출력하는 코드는?',
      choices:[
        {code:'age = 12\nprint(age)', correct:true, out:'12'},
        {code:'age == 12\nprint(age)', correct:false, hint:'값을 저장할 땐 =(등호) 한 개만 사용해요!'},
        {code:'12 = age\nprint(age)', correct:false, hint:'변수 이름은 왼쪽에, 값은 오른쪽에 와야 해요!'}
      ]
    },
    quiz:[
      {q:'변수는 무엇과 비슷한가요?', choices:['이름표 붙은 상자','지우개','창문','신발'], answer:0},
      {q:'<b>age = 11</b> 에서 age 안에 들어있는 값은?', choices:['11','age','"11"','아무것도 없다'], answer:0}
    ]
  },
  {
    id:2, emoji:'🧮', name:'계산기 행성', desc:'사칙연산 배우기',
    explain:`파이썬은 계산기처럼 <b>더하기(+) 빼기(-) 곱하기(*) 나누기(/)</b>를 할 수 있어요.<br>
    변수끼리도 계산해서 새로운 변수에 담을 수 있답니다!`,
    code:[
      {t:'fn',v:'apple'},{t:'p',v:' = '},{t:'num',v:'3'},{t:'nl'},
      {t:'fn',v:'banana'},{t:'p',v:' = '},{t:'num',v:'5'},{t:'nl'},
      {t:'fn',v:'total'},{t:'p',v:' = '},{t:'fn',v:'apple'},{t:'p',v:' + '},{t:'fn',v:'banana'},{t:'nl'},
      {t:'kw',v:'print'},{t:'p',v:'('},{t:'fn',v:'total'},{t:'p',v:')'}
    ],
    output:'8',
    mission:{
      goal:'10 - 4의 결과를 출력하는 코드는?',
      choices:[
        {code:'print(10 - 4)', correct:true, out:'6'},
        {code:'print(10 + 4)', correct:false, hint:'빼기는 - 기호를 사용해요!'},
        {code:'print(10 4)', correct:false, hint:'숫자 사이에 연산 기호(+, -, *, /)가 빠졌어요!'}
      ]
    },
    quiz:[
      {q:'곱하기를 나타내는 기호는 무엇인가요?', choices:['*','x','^','&'], answer:0},
      {q:'10 을 4로 나누는 코드로 옳은 것은?', choices:['print(10 / 4)','print(10 + 4)','print(10 * 4)','print(10 - 4)'], answer:0}
    ]
  },
  {
    id:3, emoji:'🔤', name:'글자 행성', desc:'문자열 다루기',
    explain:`글자들을 <b>" "</b> 로 감싸면 <b>문자열</b>이 돼요.<br>
    문자열끼리는 <b>+</b> 기호로 이어 붙일 수도 있어요. 마치 블록을 연결하듯이요!`,
    code:[
      {t:'fn',v:'first'},{t:'p',v:' = '},{t:'str',v:'"안녕"'},{t:'nl'},
      {t:'fn',v:'second'},{t:'p',v:' = '},{t:'str',v:'"친구야"'},{t:'nl'},
      {t:'kw',v:'print'},{t:'p',v:'('},{t:'fn',v:'first'},{t:'p',v:' + '},{t:'str',v:'" "'},{t:'p',v:' + '},{t:'fn',v:'second'},{t:'p',v:')'}
    ],
    output:'안녕 친구야',
    mission:{
      goal:'"잘" 과 "가" 를 합쳐서 "잘가"를 출력하는 코드는?',
      choices:[
        {code:'print("잘" + "가")', correct:true, out:'잘가'},
        {code:'print("잘" - "가")', correct:false, hint:'문자열을 합칠 땐 - 가 아니라 + 를 사용해요!'},
        {code:'print(잘 + 가)', correct:false, hint:'문자열은 반드시 따옴표로 감싸야 해요!'}
      ]
    },
    quiz:[
      {q:'문자열을 만들 때 감싸는 기호는?', choices:['따옴표 " "','괄호 ( )','중괄호 { }','대괄호 [ ]'], answer:0},
      {q:'<b>"가" + "나"</b> 의 결과는 무엇일까요?', choices:['가나','가 나','나가','오류가 난다'], answer:0}
    ]
  },
  {
    id:4, emoji:'🔀', name:'선택 행성', desc:'조건문 if / else',
    explain:`<code>if</code>는 "만약 ~라면" 이라는 뜻이에요. 조건이 맞으면 실행하고,<br>
    아니면 <code>else</code>(그렇지 않으면) 부분을 실행해요. <b>콜론(:)</b>과 <b>들여쓰기</b>를 꼭 기억하세요!`,
    code:[
      {t:'fn',v:'score'},{t:'p',v:' = '},{t:'num',v:'90'},{t:'nl'},
      {t:'kw',v:'if'},{t:'p',v:' score >= '},{t:'num',v:'80'},{t:'p',v:':'},{t:'nl'},
      {t:'p',v:'    '},{t:'kw',v:'print'},{t:'p',v:'('},{t:'str',v:'"참 잘했어요!"'},{t:'p',v:')'},{t:'nl'},
      {t:'kw',v:'else'},{t:'p',v:':'},{t:'nl'},
      {t:'p',v:'    '},{t:'kw',v:'print'},{t:'p',v:'('},{t:'str',v:'"조금 더 힘내요!"'},{t:'p',v:')'}
    ],
    output:'참 잘했어요!',
    mission:{
      goal:'나이가 10살 이상이면 "어린이"를 출력하는 올바른 코드는?',
      choices:[
        {code:'if age >= 10:\n    print("어린이")', correct:true, out:'어린이'},
        {code:'if age >= 10\n    print("어린이")', correct:false, hint:'if 조건 뒤에는 콜론(:)이 꼭 필요해요!'},
        {code:'if age => 10:\n    print("어린이")', correct:false, hint:'"이상"은 >= 순서로 써야 해요!'}
      ]
    },
    quiz:[
      {q:'if 는 무슨 뜻일까요?', choices:['만약 ~라면','반복해서','멈춰라','더하기'], answer:0},
      {q:'score = 70 일 때, 예제 코드의 출력 결과는?', choices:['조금 더 힘내요!','참 잘했어요!','70','오류가 난다'], answer:0}
    ]
  },
  {
    id:5, emoji:'🔁', name:'반복 행성', desc:'for 반복문',
    explain:`<code>for</code>는 같은 일을 여러 번 반복시킬 때 써요.<br>
    <code>range(3)</code>은 <b>0, 1, 2</b> 이렇게 <b>3번</b> 반복하라는 뜻이에요.`,
    code:[
      {t:'kw',v:'for'},{t:'p',v:' i in '},{t:'fn',v:'range'},{t:'p',v:'('},{t:'num',v:'3'},{t:'p',v:'):'},{t:'nl'},
      {t:'p',v:'    '},{t:'kw',v:'print'},{t:'p',v:'('},{t:'str',v:'"코딩 화이팅!"'},{t:'p',v:')'}
    ],
    output:'코딩 화이팅!\n코딩 화이팅!\n코딩 화이팅!',
    mission:{
      goal:'"화이팅!" 을 3번 출력하는 올바른 코드는?',
      choices:[
        {code:'for i in range(3):\n    print("화이팅!")', correct:true, out:'화이팅!\n화이팅!\n화이팅!'},
        {code:'for i in range(3)\n    print("화이팅!")', correct:false, hint:'for 문도 마지막에 콜론(:)이 필요해요!'},
        {code:'for i in range(3):\nprint("화이팅!")', correct:false, hint:'print 앞에 들여쓰기(공백 4칸)가 있어야 해요!'}
      ]
    },
    quiz:[
      {q:'range(3) 은 몇 번 반복할까요?', choices:['3번','2번','4번','1번'], answer:0},
      {q:'for문을 사용하는 이유는 무엇일까요?', choices:['같은 일을 여러 번 반복하려고','그림을 그리려고','소리를 내려고','변수를 지우려고'], answer:0}
    ]
  },
  {
    id:6, emoji:'📋', name:'목록 행성', desc:'리스트로 여러 개 담기',
    explain:`<b>리스트</b>는 여러 개의 물건을 한 줄로 담는 상자예요. <b>[ ]</b> 대괄호를 사용해요.<br>
    그리고 파이썬은 순서를 셀 때 <b>0부터</b> 시작한다는 걸 꼭 기억하세요!`,
    code:[
      {t:'fn',v:'fruits'},{t:'p',v:' = '},{t:'p',v:'['},{t:'str',v:'"사과"'},{t:'p',v:', '},{t:'str',v:'"바나나"'},{t:'p',v:', '},{t:'str',v:'"포도"'},{t:'p',v:']'},{t:'nl'},
      {t:'kw',v:'print'},{t:'p',v:'('},{t:'fn',v:'fruits'},{t:'p',v:'[0])'},{t:'nl'},
      {t:'kw',v:'print'},{t:'p',v:'('},{t:'fn',v:'fruits'},{t:'p',v:'[1])'}
    ],
    output:'사과\n바나나',
    mission:{
      goal:'fruits = ["사과","바나나","포도"] 에서 "바나나"를 출력하는 코드는?',
      choices:[
        {code:'print(fruits[1])', correct:true, out:'바나나'},
        {code:'print(fruits[2])', correct:false, hint:'파이썬은 0부터 세요! 두 번째 자리는 번호 1이에요.'},
        {code:'print(fruits(1))', correct:false, hint:'리스트에서 값을 꺼낼 땐 대괄호 [ ]를 사용해요!'}
      ]
    },
    quiz:[
      {q:'리스트를 만들 때 사용하는 기호는?', choices:['[ ] 대괄호','( ) 소괄호','{ } 중괄호','< > 부등호'], answer:0},
      {q:'fruits[0] 은 리스트의 몇 번째 것을 가리킬까요?', choices:['첫 번째','두 번째','마지막','세 번째'], answer:0}
    ]
  }
];

const BOSS = {
  id:7, emoji:'👾', name:'보스 행성', desc:'종합 실력 점검!',
  quiz:[
    {q:'화면에 글자를 보여주는 명령어는?', choices:['print()','input()','list()','sum()'], answer:0},
    {q:'변수를 만들 때 사용하는 기호는?', choices:['=','==','+','?'], answer:0},
    {q:'"만약 ~라면"을 뜻하는 파이썬 키워드는?', choices:['if','for','while','and'], answer:0},
    {q:'같은 동작을 여러 번 반복할 때 쓰는 것은?', choices:['for 반복문','print문','변수','리스트'], answer:0},
    {q:'파이썬에서 리스트의 첫 번째 값의 번호는?', choices:['0','1','2','시작 번호 없음'], answer:0}
  ]
};

/* ---------------- state ---------------- */
const state = {
  progress: LESSONS.map(()=>({mission:false, q0:false, q1:false})),
  bossProgress: BOSS.quiz.map(()=>false),
  bossDone:false,
  currentLessonId: null
};
const TOTAL_STARS = LESSONS.length*3 + BOSS.quiz.length;

function earnedStars(){
  let s=0;
  state.progress.forEach(p=>{ if(p.mission)s++; if(p.q0)s++; if(p.q1)s++; });
  state.bossProgress.forEach(b=>{ if(b)s++; });
  return s;
}
function isLessonDone(i){ const p = state.progress[i]; return p.mission && p.q0 && p.q1; }
function isUnlocked(i){ if(i===0) return true; return isLessonDone(i-1); }
function bossUnlocked(){ return LESSONS.every((_,i)=>isLessonDone(i)); }

function updateStarUI(){
  document.getElementById('starCount').textContent = earnedStars();
  document.getElementById('starTotal').textContent = TOTAL_STARS;
}

/* ---------------- confetti ---------------- */
function burstConfetti(x,y){
  const box = document.getElementById('confetti');
  const emojis = ['⭐','✨','🎉','💫'];
  for(let i=0;i<10;i++){
    const s = document.createElement('span');
    s.textContent = emojis[Math.floor(Math.random()*emojis.length)];
    s.style.left = (x + (Math.random()*80-40))+'px';
    s.style.top = (y + (Math.random()*40-20))+'px';
    s.style.animationDelay = (Math.random()*.15)+'s';
    box.appendChild(s);
    setTimeout(()=>s.remove(),1100);
  }
}

/* ---------------- code render ---------------- */
function renderCode(tokens){
  return tokens.map(tok=>{
    if(tok.t==='nl') return '\n';
    if(tok.t==='p') return escapeHtml(tok.v);
    return `<span class="${tok.t}">${escapeHtml(tok.v)}</span>`;
  }).join('');
}
function escapeHtml(s){
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

/* ---------------- map render ---------------- */
function renderMap(){
  const wrap = document.getElementById('pathWrap');
  let html = '';
  LESSONS.forEach((l,i)=>{
    const unlocked = isUnlocked(i);
    const done = isLessonDone(i);
    const cls = done ? 'done' : (unlocked ? 'available' : 'locked');
    const side = i%2===0 ? '' : 'right';
    const starsGot = (state.progress[i].mission?1:0)+(state.progress[i].q0?1:0)+(state.progress[i].q1?1:0);
    html += `
    <div class="planet-row ${side}">
      ${i<LESSONS.length ? `<div class="connector"></div>` : ''}
      <button class="planet-node ${cls}" data-id="${i}" ${unlocked?'':'disabled'}>
        ${done ? `<span class="badge-check">✓</span>` : ''}
        ${unlocked ? l.emoji : '🔒'}
      </button>
      <div class="planet-info">
        <div class="idx">STAGE 0${i+1}</div>
        <div class="name">${l.name}</div>
        <div class="desc">${l.desc}</div>
        <div class="stars-earned">${unlocked ? `⭐ ${starsGot}/3` : '잠겨있어요'}</div>
      </div>
    </div>`;
  });
  // boss
  const bUnlocked = bossUnlocked();
  const bDone = state.bossDone;
  const bCls = bDone ? 'done' : (bUnlocked ? 'available' : 'locked');
  const bStars = state.bossProgress.filter(Boolean).length;
  html += `
  <div class="planet-row boss-row">
    <div class="connector"></div>
    <button class="planet-node ${bCls}" data-boss="1" ${bUnlocked?'':'disabled'}>
      ${bDone ? `<span class="badge-check">✓</span>` : ''}
      ${bUnlocked ? BOSS.emoji : '🔒'}
    </button>
    <div class="planet-info">
      <div class="idx">FINAL STAGE</div>
      <div class="name">${BOSS.name}</div>
      <div class="desc">${BOSS.desc}</div>
      <div class="stars-earned">${bUnlocked ? `⭐ ${bStars}/${BOSS.quiz.length}` : '모든 행성을 완료하면 열려요'}</div>
    </div>
  </div>`;
  wrap.innerHTML = html;

  wrap.querySelectorAll('.planet-node[data-id]').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      if(btn.disabled) return;
      openLesson(parseInt(btn.dataset.id));
    });
  });
  const bossBtn = wrap.querySelector('.planet-node[data-boss]');
  if(bossBtn){
    bossBtn.addEventListener('click', ()=>{
      if(bossBtn.disabled) return;
      openBoss();
    });
  }
  updateStarUI();
}

/* ---------------- lesson view ---------------- */
function showView(name){
  document.getElementById('mapView').style.display = name==='map' ? '' : 'none';
  document.getElementById('lessonView').classList.toggle('show', name==='lesson');
  document.getElementById('trophyView').classList.toggle('show', name==='trophy');
  window.scrollTo({top:0, behavior:'smooth'});
}

function openLesson(id){
  state.currentLessonId = id;
  const l = LESSONS[id];
  const p = state.progress[id];
  const view = document.getElementById('lessonView');

  view.innerHTML = `
    <button class="back-btn" id="backBtn">← 행성 지도로 돌아가기</button>

    <div class="lesson-card">
      <div class="lesson-head">
        <div class="emoji">${l.emoji}</div>
        <h2>${l.name}</h2>
      </div>
      <div class="speech">🐍 <span>${l.explain}</span></div>

      <div class="section-label">📖 예제 코드</div>
      <div class="code-block">${renderCode(l.code)}</div>
      <button class="run-btn" id="runBtn">▶ 실행결과 보기</button>
      <div class="output-box" id="outBox"><span class="tag">실행 결과</span></div>

      <div class="section-label">🎯 미니미션</div>
      <div class="speech" style="font-size:14px;">${l.mission.goal}</div>
      <div class="mission-choices" id="missionChoices"></div>
      <div class="hint-box" id="missionHint"></div>

      <div class="section-label">📝 퀴즈</div>
      <div id="quizArea"></div>

      <div class="status-row">
        <span class="status-chip ${p.mission?'done':''}" id="chipMission">${p.mission?'✅':'⬜'} 미니미션</span>
        <span class="status-chip ${p.q0?'done':''}" id="chipQ0">${p.q0?'✅':'⬜'} 퀴즈 1</span>
        <span class="status-chip ${p.q1?'done':''}" id="chipQ1">${p.q1?'✅':'⬜'} 퀴즈 2</span>
      </div>

      <button class="next-btn" id="nextBtn">다음 행성으로 이동하기 🚀</button>
    </div>
  `;

  document.getElementById('backBtn').addEventListener('click', ()=>{ renderMap(); showView('map'); });

  // run example
  document.getElementById('runBtn').addEventListener('click', (e)=>{
    const box = document.getElementById('outBox');
    box.style.display = 'block';
    box.innerHTML = `<span class="tag">실행 결과</span>` + escapeHtml(l.output);
  });

  // mission choices
  const mc = document.getElementById('missionChoices');
  l.mission.choices.forEach((c, idx)=>{
    const btn = document.createElement('button');
    btn.className = 'choice-btn';
    btn.textContent = c.code;
    btn.addEventListener('click', ()=>{
      const hintBox = document.getElementById('missionHint');
      if(c.correct){
        btn.classList.add('correct');
        mc.querySelectorAll('.choice-btn').forEach(b=>b.disabled=true);
        hintBox.style.display='block';
        hintBox.style.color='var(--accent-mint)';
        hintBox.textContent = `✅ 실행 결과: ${c.out}`;
        if(!p.mission){
          p.mission = true;
          const rect = btn.getBoundingClientRect();
          burstConfetti(rect.left, rect.top);
          refreshLessonStatus(id);
        }
      } else {
        btn.classList.add('wrong');
        setTimeout(()=>btn.classList.remove('wrong'), 400);
        hintBox.style.display='block';
        hintBox.style.color='var(--accent-coral)';
        hintBox.textContent = `🤔 ${c.hint}`;
      }
    });
    mc.appendChild(btn);
  });

  // quiz
  const qArea = document.getElementById('quizArea');
  l.quiz.forEach((q, qi)=>{
    const qDiv = document.createElement('div');
    qDiv.className = 'quiz-q';
    qDiv.innerHTML = `<div class="qtext">Q${qi+1}. ${q.q}</div><div class="mission-choices" style="font-family:'Gowun Dodum',sans-serif;"></div>`;
    const choicesWrap = qDiv.querySelector('.mission-choices');
    q.choices.forEach((choiceText, ci)=>{
      const b = document.createElement('button');
      b.className = 'choice-btn';
      b.style.fontFamily = "'Gowun Dodum',sans-serif";
      b.textContent = `${['①','②','③','④'][ci]} ${choiceText}`;
      b.addEventListener('click', ()=>{
        if(ci===q.answer){
          b.classList.add('correct');
          choicesWrap.querySelectorAll('.choice-btn').forEach(x=>x.disabled=true);
          const key = qi===0?'q0':'q1';
          if(!p[key]){
            p[key]=true;
            const rect=b.getBoundingClientRect();
            burstConfetti(rect.left, rect.top);
            refreshLessonStatus(id);
          }
        } else {
          b.classList.add('wrong');
          setTimeout(()=>b.classList.remove('wrong'),400);
        }
      });
      choicesWrap.appendChild(b);
    });
    qArea.appendChild(qDiv);
  });

  document.getElementById('nextBtn').addEventListener('click', ()=>{
    if(!isLessonDone(id)) return;
    renderMap(); showView('map');
  });

  showView('lesson');
}

function refreshLessonStatus(id){
  const p = state.progress[id];
  document.getElementById('chipMission').className = 'status-chip ' + (p.mission?'done':'');
  document.getElementById('chipMission').textContent = (p.mission?'✅':'⬜') + ' 미니미션';
  document.getElementById('chipQ0').className = 'status-chip ' + (p.q0?'done':'');
  document.getElementById('chipQ0').textContent = (p.q0?'✅':'⬜') + ' 퀴즈 1';
  document.getElementById('chipQ1').className = 'status-chip ' + (p.q1?'done':'');
  document.getElementById('chipQ1').textContent = (p.q1?'✅':'⬜') + ' 퀴즈 2';
  const nextBtn = document.getElementById('nextBtn');
  if(isLessonDone(id)){ nextBtn.classList.add('ready'); }
  updateStarUI();
}

/* ---------------- boss view ---------------- */
function openBoss(){
  const view = document.getElementById('lessonView');
  view.innerHTML = `
    <button class="back-btn" id="backBtn">← 행성 지도로 돌아가기</button>
    <div class="lesson-card">
      <div class="lesson-head">
        <div class="emoji">👾</div>
        <h2>보스 행성 - 종합 실력 점검!</h2>
      </div>
      <div class="speech">🐍 지금까지 배운 모든 것을 총동원해서 문제를 풀어봐! 5문제를 모두 맞히면 <b>파이썬 탐험대 졸업장</b>을 받을 수 있어요!</div>
      <div class="section-label">📝 최종 퀴즈</div>
      <div id="bossQuizArea"></div>
      <button class="next-btn" id="bossNextBtn">탐험 완료하기 🏆</button>
    </div>
  `;
  document.getElementById('backBtn').addEventListener('click', ()=>{ renderMap(); showView('map'); });

  const area = document.getElementById('bossQuizArea');
  BOSS.quiz.forEach((q,qi)=>{
    const qDiv = document.createElement('div');
    qDiv.className='quiz-q';
    qDiv.innerHTML = `<div class="qtext">Q${qi+1}. ${q.q}</div><div class="mission-choices"></div>`;
    const wrap = qDiv.querySelector('.mission-choices');
    q.choices.forEach((choiceText,ci)=>{
      const b = document.createElement('button');
      b.className='choice-btn';
      b.style.fontFamily = "'Gowun Dodum',sans-serif";
      b.textContent = `${['①','②','③','④'][ci]} ${choiceText}`;
      b.addEventListener('click', ()=>{
        if(ci===q.answer){
          b.classList.add('correct');
          wrap.querySelectorAll('.choice-btn').forEach(x=>x.disabled=true);
          if(!state.bossProgress[qi]){
            state.bossProgress[qi]=true;
            const rect=b.getBoundingClientRect();
            burstConfetti(rect.left, rect.top);
            updateStarUI();
            checkBossReady();
          }
        } else {
          b.classList.add('wrong');
          setTimeout(()=>b.classList.remove('wrong'),400);
        }
      });
      wrap.appendChild(b);
    });
    area.appendChild(qDiv);
  });

  document.getElementById('bossNextBtn').addEventListener('click', ()=>{
    if(!state.bossProgress.every(Boolean)) return;
    state.bossDone = true;
    showTrophy();
  });

  showView('lesson');
}
function checkBossReady(){
  if(state.bossProgress.every(Boolean)){
    document.getElementById('bossNextBtn').classList.add('ready');
  }
}

/* ---------------- trophy view ---------------- */
function showTrophy(){
  const view = document.getElementById('trophyView');
  view.innerHTML = `
    <div class="trophy-screen">
      <div class="big">🏆</div>
      <h2>축하합니다, 파이썬 탐험대장님!</h2>
      <p>모든 행성을 탐험하고 파이썬 기초 문법을 마스터했어요.<br>
      총 획득한 별: ⭐ ${earnedStars()} / ${TOTAL_STARS}</p>
      <button class="restart-btn" id="restartBtn">처음부터 다시 탐험하기</button>
    </div>
  `;
  document.getElementById('restartBtn').addEventListener('click', ()=>{
    state.progress = LESSONS.map(()=>({mission:false,q0:false,q1:false}));
    state.bossProgress = BOSS.quiz.map(()=>false);
    state.bossDone = false;
    renderMap();
    showView('map');
  });
  showView('trophy');
}

/* ---------------- init ---------------- */
renderMap();
</script>
</body>
</html>
"""

with open('/Users/cheonhyeonjun/com_gui/public/python_basic_reference.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated python_basic_reference.html")
