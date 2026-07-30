import os

html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>파이썬이랑 놀아보자!</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans+KR:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{
    --paper:#efeae0;
    --paper-2:#e6e0d1;
    --ink:#182623;
    --ink-soft:#4d5c56;
    --water:#1f7a8c;
    --water-deep:#0b4f63;
    --land-soft:#e4d7a3;
    --foam:#bfe9e4;
    --rule:#c9c2b2;
    --warn:#b8531d;

    --c-var:#1f7a8c;
    --c-print:#c9a227;
    --c-math:#b8531d;
    --c-if:#5b3a8e;
    --c-loop:#2e7d32;
    --c-list:#0b4f63;
    --c-dict:#0c8599;
    --c-def:#d9480f;
    --c-input:#c92a2a;

    --mono:'IBM Plex Mono', ui-monospace, monospace;
    --sans:'IBM Plex Sans KR','IBM Plex Sans', sans-serif;
    --display:'Space Grotesk', var(--sans);
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{ background:var(--paper); color:var(--ink); font-family:var(--sans); line-height:1.6; -webkit-font-smoothing:antialiased; overflow-x:hidden; }
  ::selection{ background:var(--foam); }
  .wrap{ max-width:940px; margin:0 auto; padding:0 24px; }

  .topbar{ display:flex; justify-content:space-between; align-items:center; padding:16px 24px; border-bottom:1px solid var(--rule);
    font-family:var(--mono); font-size:12px; letter-spacing:.06em; color:var(--ink-soft); text-transform:uppercase; flex-wrap:wrap; gap:10px; }
  .topbar strong{ color:var(--ink); }
  .topbar .dot{ color:var(--water); }

  /* progress badges */
  .badge-bar{ display:flex; align-items:center; justify-content:center; gap:12px; padding:20px 24px; flex-wrap:wrap; }
  .badge{ width:52px; height:52px; border-radius:50%; background:#fff; border:2px solid var(--rule);
    display:flex; align-items:center; justify-content:center; font-size:24px; opacity:.45; transition:all .35s ease; }
  .badge.done{ opacity:1; box-shadow:0 0 0 4px rgba(0,0,0,.05), 0 4px 10px rgba(0,0,0,.12); animation:badgePop .5s ease; }
  @keyframes badgePop{ 0%{ transform:scale(.6); } 60%{ transform:scale(1.18); } 100%{ transform:scale(1); } }
  .progress-text{ font-family:var(--mono); font-size:12px; color:var(--ink-soft); text-align:center; margin-top:2px; }

  .hero{ padding:44px 0 40px; text-align:center; }
  .eyebrow{ font-family:var(--mono); font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--water-deep);
    display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:18px; }
  .eyebrow::before, .eyebrow::after{ content:''; width:22px; height:1px; background:var(--water-deep); }
  h1{ font-family:var(--display); font-weight:700; font-size:clamp(32px,7vw,52px); line-height:1.15; margin:0 0 18px; letter-spacing:-0.01em; }
  h1 em{ font-style:normal; color:var(--water-deep); }
  .lede{ font-size:18px; color:var(--ink-soft); max-width:52ch; margin:0 auto; }
  .lede b{ color:var(--ink); font-weight:600; }

  .fig{ padding:52px 0; border-top:1px solid var(--rule); }
  .fig-head{ display:flex; align-items:center; gap:14px; margin-bottom:18px; flex-wrap:wrap; }
  .fig-emoji{ font-size:30px; width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center;
    background:var(--accent); flex:0 0 auto; color:#fff; }
  .fig-title{ font-family:var(--display); font-weight:700; font-size:24px; margin:0; color:var(--ink); }
  .fig-note{ color:var(--ink-soft); font-size:16px; max-width:64ch; margin:0 0 20px; }
  .fig-note b{ color:var(--ink); }

  .board-card{ background:#fff; border:2px solid var(--rule); border-radius:16px; padding:26px;
    display:flex; flex-direction:column; align-items:center; gap:18px; }

  .row{ display:flex; gap:12px; flex-wrap:wrap; justify-content:center; align-items:center; }

  .emoji-btn{ font-size:34px; background:#fbfaf4; border:3px solid var(--rule); border-radius:16px; padding:10px 16px;
    cursor:pointer; transition:transform .15s ease, border-color .15s ease, box-shadow .15s ease; }
  .emoji-btn:hover{ transform:translateY(-3px) scale(1.05); }
  .emoji-btn:active{ transform:translateY(1px) scale(.97); }
  .emoji-btn.selected{ border-color:var(--accent); box-shadow:0 0 0 4px var(--accent); opacity:.92; }

  .kid-btn{ font-family:var(--display); font-weight:600; font-size:16px; padding:13px 24px; border-radius:999px; border:none;
    color:#fff; cursor:pointer; box-shadow:0 4px 0 rgba(0,0,0,.15); transition:transform .12s ease, box-shadow .12s ease;
    background:var(--accent); }
  .kid-btn:hover{ filter:brightness(1.06); }
  .kid-btn:active{ transform:translateY(4px); box-shadow:0 0 0 rgba(0,0,0,.15); }
  .kid-btn.ghost{ background:#fff; color:var(--ink); border:2px solid var(--rule); box-shadow:none; }
  .kid-btn.ghost:active{ transform:translateY(2px); }
  .kid-btn:disabled{ opacity:.35; cursor:not-allowed; }

  .num-btn{ font-family:var(--mono); font-weight:600; font-size:20px; width:48px; height:48px; border-radius:12px;
    border:3px solid var(--rule); background:#fbfaf4; cursor:pointer; transition:all .15s ease; }
  .num-btn:hover{ transform:translateY(-2px); }
  .num-btn.selected{ border-color:var(--accent); background:var(--accent); color:#fff; }

  /* box visual for variables */
  .box-visual{ width:150px; height:150px; border-radius:20px; background:var(--paper-2); border:4px dashed var(--rule);
    display:flex; flex-direction:column; align-items:center; justify-content:center; gap:6px; transition:all .3s ease; }
  .box-visual .content{ font-size:48px; transition:transform .25s ease; }
  .box-visual .label{ font-family:var(--mono); font-size:12px; color:var(--ink-soft); }
  .box-visual.filled{ border-style:solid; border-color:var(--accent); background:#fff; }
  @keyframes dropIn{ 0%{ transform:translateY(-30px) scale(.5); opacity:0; } 60%{ transform:translateY(4px) scale(1.1); opacity:1;} 100%{ transform:translateY(0) scale(1); } }
  .box-visual .content.animate{ animation:dropIn .4s ease; }

  /* speech / console */
  .console{ width:100%; min-height:70px; background:var(--ink); color:var(--foam); border-radius:12px;
    padding:16px 20px; font-family:var(--mono); font-size:16px; display:flex; align-items:center; flex-wrap:wrap; gap:8px; }
  .console .placeholder{ opacity:.4; font-style:italic; }
  .bubble{ background:#fff; color:var(--ink); border-radius:14px; padding:6px 14px; font-family:var(--sans); font-weight:600;
    animation:pop .25s ease; }
  @keyframes pop{ from{ transform:scale(.5); opacity:0;} to{ transform:scale(1); opacity:1; } }

  /* code block (same family as BFS pages) */
  .code-block{ font-family:var(--mono); font-size:14px; background:#132321; color:#dce8e4; border-radius:12px;
    padding:18px 22px; width:100%; overflow-x:auto; }
  .code-block pre{ margin:0; white-space:pre; }
  .code-block .kw{ color:#7fc8ff; }
  .code-block .fn{ color:#ffd580; }
  .code-block .str{ color:#a9e5c9; }
  .code-block .num{ color:#f5a97f; }
  .code-block .cm{ color:#7a938d; font-style:italic; }
  .code-line{ display:block; padding:2px 6px; border-radius:5px; transition:background-color .3s ease; }
  .code-line.active{ background:rgba(255,255,255,.1); box-shadow:0 0 0 1px rgba(255,255,255,.15) inset; }

  .result-banner{ font-family:var(--display); font-weight:700; font-size:20px; padding:14px 22px; border-radius:12px;
    text-align:center; width:100%; transition:all .25s ease; }
  .result-banner.even{ background:#eaf5ec; color:var(--c-loop); }
  .result-banner.odd{ background:#fdeeea; color:var(--c-math); }
  .result-banner.empty{ background:var(--paper-2); color:var(--ink-soft); font-weight:500; font-size:15px; }

  /* bag / list slots */
  .bag{ display:flex; gap:10px; flex-wrap:wrap; justify-content:center; }
  .slot{ width:56px; height:56px; border-radius:12px; background:var(--paper-2); border:2px dashed var(--rule);
    display:flex; align-items:center; justify-content:center; font-size:28px; position:relative; transition:all .25s ease; }
  .slot.filled{ border-style:solid; background:#fff; }
  .slot.picked{ box-shadow:0 0 0 4px var(--accent); border-color:var(--accent); }
  .slot .idx{ position:absolute; bottom:-20px; font-family:var(--mono); font-size:10px; color:var(--ink-soft); }

  .status-row{ display:flex; gap:22px; flex-wrap:wrap; width:100%; font-family:var(--mono); font-size:12.5px; justify-content:center; }
  .status-item{ text-align:center; }
  .status-item .k{ color:var(--ink-soft); display:block; font-size:10.5px; text-transform:uppercase; letter-spacing:.08em; }
  .status-item .v{ font-size:16px; color:var(--ink); font-family:var(--display); font-weight:700; }

  footer{ border-top:1px solid var(--rule); padding:40px 0 60px; text-align:center; }
  .footer-title{ font-family:var(--display); font-weight:700; font-size:22px; margin-bottom:14px; }
  .recap-grid{ display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:14px; margin-top:20px; }
  .recap-card{ background:#fff; border:2px solid var(--rule); border-radius:14px; padding:16px; text-align:left; }
  .recap-card .e{ font-size:26px; }
  .recap-card .t{ font-family:var(--display); font-weight:700; font-size:14px; margin:6px 0 4px; }
  .recap-card .d{ font-family:var(--sans); font-size:12.5px; color:var(--ink-soft); }

  .confetti{ position:fixed; top:-20px; width:10px; height:10px; border-radius:2px; z-index:999; pointer-events:none; }
  @keyframes fall{ to{ transform:translateY(110vh) rotate(720deg); opacity:.3; } }

  @media (max-width:600px){
    .box-visual{ width:120px; height:120px; }
    .box-visual .content{ font-size:38px; }
  }
</style>
</head>
<body>

<div class="topbar">
  <span><strong>🐍 PYTHON PLAYGROUND</strong></span>
  <span>눌러보면서 배우는 파이썬</span>
</div>

<div class="badge-bar" id="badgeBar"></div>
<div class="progress-text" id="progressText">0 / 9개 배지를 모아보세요!</div>

<div class="wrap">

  <section class="hero">
    <div class="eyebrow">누구나 할 수 있어요</div>
    <h1>파이썬이랑<br><em>같이 놀아볼까?</em> 🎈</h1>
    <p class="lede">
      버튼을 <b>꾹 눌러보세요.</b> 누를 때마다 컴퓨터가 어떻게 생각하는지 눈으로 볼 수 있어요.
      아래로 내려가면서 하나씩 눌러보면, 아홉 개의 배지를 다 모을 수 있어요!
    </p>
  </section>

  <!-- 01 변수 -->
  <section class="fig" style="--accent:var(--c-var)">
    <div class="fig-head">
      <div class="fig-emoji">📦</div>
      <h2 class="fig-title">변수는 이름표 붙은 상자예요</h2>
    </div>
    <p class="fig-note">상자 안에 물건을 넣으면, 나중에 이름표만 보고도 뭐가 들었는지 알 수 있어요. 눌러서 상자를 채워보세요!</p>
    <div class="board-card">
      <div class="row">
        <button class="emoji-btn" data-word="사과" data-emoji="🍎">🍎</button>
        <button class="emoji-btn" data-word="별" data-emoji="⭐">⭐</button>
        <button class="emoji-btn" data-word="로봇" data-emoji="🤖">🤖</button>
      </div>
      <div class="box-visual" id="varBox">
        <div class="content" id="varContent">?</div>
        <div class="label">my_box</div>
      </div>
      <div class="code-block">
<pre><span class="code-line" id="varLine1"><span class="kw">my_box</span> = <span class="str" id="varStrCode">"?"</span></span>
<span class="code-line" id="varLine2"><span class="fn">print</span>(<span class="kw">my_box</span>)</span></pre>
      </div>
      <div class="console"><span id="varOutput" class="placeholder">여기에 결과가 나와요</span></div>
    </div>
  </section>

  <!-- 02 print -->
  <section class="fig" style="--accent:var(--c-print)">
    <div class="fig-head">
      <div class="fig-emoji">💬</div>
      <h2 class="fig-title">print()는 이야기해주는 거예요</h2>
    </div>
    <p class="fig-note"><code>print()</code>는 컴퓨터가 우리한테 말을 걸어주는 방법이에요. 버튼을 누르면 컴퓨터가 말해줘요!</p>
    <div class="board-card">
      <div class="row">
        <button class="kid-btn" data-msg="안녕!">안녕! 눌러보기</button>
        <button class="kid-btn" data-msg="나는 파이썬이야!">나는 파이썬이야!</button>
        <button class="kid-btn" data-msg="같이 놀자!">같이 놀자!</button>
      </div>
      <div class="code-block">
<pre><span class="fn">print</span>(<span class="str" id="printStrCode">"..."</span>)</pre>
      </div>
      <div class="console" id="printConsole"><span class="placeholder">버튼을 누르면 여기서 말해요</span></div>
    </div>
  </section>

  <!-- 03 사칙연산 -->
  <section class="fig" style="--accent:var(--c-math)">
    <div class="fig-head">
      <div class="fig-emoji">➕</div>
      <h2 class="fig-title">숫자 계산 놀이</h2>
    </div>
    <p class="fig-note">숫자 두 개를 고르고, 계산 방법을 골라서 <b>계산하기</b>를 눌러보세요.</p>
    <div class="board-card">
      <div class="row">
        <div style="text-align:center">
          <div style="font-family:var(--mono);font-size:11px;color:var(--ink-soft);margin-bottom:6px">첫번째 숫자</div>
          <div class="row" style="gap:6px">
            <button class="kid-btn ghost" id="numADown" style="padding:8px 14px">−</button>
            <div class="num-btn" style="cursor:default;display:flex;align-items:center;justify-content:center" id="numADisplay">3</div>
            <button class="kid-btn ghost" id="numAUp" style="padding:8px 14px">+</button>
          </div>
        </div>
        <div style="font-size:30px;font-family:var(--display);color:var(--ink-soft)" id="opDisplay">+</div>
        <div style="text-align:center">
          <div style="font-family:var(--mono);font-size:11px;color:var(--ink-soft);margin-bottom:6px">두번째 숫자</div>
          <div class="row" style="gap:6px">
            <button class="kid-btn ghost" id="numBDown" style="padding:8px 14px">−</button>
            <div class="num-btn" style="cursor:default;display:flex;align-items:center;justify-content:center" id="numBDisplay">5</div>
            <button class="kid-btn ghost" id="numBUp" style="padding:8px 14px">+</button>
          </div>
        </div>
      </div>
      <div class="row">
        <button class="num-btn op-btn selected" data-op="+">+</button>
        <button class="num-btn op-btn" data-op="-">−</button>
        <button class="num-btn op-btn" data-op="*">×</button>
        <button class="num-btn op-btn" data-op="/">÷</button>
      </div>
      <button class="kid-btn" id="btnCalc">계산하기 🧮</button>
      <div class="code-block">
<pre><span class="fn">print</span>(<span class="num" id="mathCodeA">3</span> <span id="mathCodeOp">+</span> <span class="num" id="mathCodeB">5</span>)</pre>
      </div>
      <div class="console"><span id="mathOutput" class="placeholder">계산하기를 눌러보세요</span></div>
    </div>
  </section>

  <!-- 04 if/else -->
  <section class="fig" style="--accent:var(--c-if)">
    <div class="fig-head">
      <div class="fig-emoji">🔀</div>
      <h2 class="fig-title">만약 ~라면 (if/else)</h2>
    </div>
    <p class="fig-note">숫자를 하나 고르면, 컴퓨터가 <b>짝수인지 홀수인지</b> 알려줘요. 규칙에 따라 다른 문이 열려요!</p>
    <div class="board-card">
      <div class="row" id="numberPicker"></div>
      <div class="code-block">
<pre><span class="code-line" id="ifLine"><span class="kw">if</span> num % <span class="num">2</span> == <span class="num">0</span>:</span>
    <span class="fn">print</span>(<span class="str">"짝수예요! 😊"</span>)
<span class="code-line" id="elseLine"><span class="kw">else</span>:</span>
    <span class="fn">print</span>(<span class="str">"홀수예요! 🙂"</span>)</pre>
      </div>
      <div class="result-banner empty" id="ifResult">숫자를 골라보세요</div>
    </div>
  </section>

  <!-- 05 for loop -->
  <section class="fig" style="--accent:var(--c-loop)">
    <div class="fig-head">
      <div class="fig-emoji">🔁</div>
      <h2 class="fig-title">반복문은 노래를 여러 번 부르는 거예요</h2>
    </div>
    <p class="fig-note">몇 번 부를지 고르고, <b>한 걸음씩</b> 눌러서 노래가 어떻게 반복되는지 봐요.</p>
    <div class="board-card">
      <div class="row" id="loopCountPicker"></div>
      <div class="row" id="loopStage" style="min-height:60px"></div>
      <div class="code-block">
<pre><span class="code-line" id="forLine"><span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num" id="loopN">3</span>):</span>
    <span class="fn">print</span>(<span class="str">"안녕! 🙌"</span>)</pre>
      </div>
      <div class="status-row">
        <div class="status-item"><span class="k">진행</span><span class="v" id="loopProgress">0 / 3</span></div>
      </div>
      <div class="row">
        <button class="kid-btn" id="btnLoopStep">한 걸음 진행 →</button>
        <button class="kid-btn ghost" id="btnLoopPlay">자동 재생</button>
        <button class="kid-btn ghost" id="btnLoopReset">처음부터</button>
      </div>
    </div>
  </section>

  <!-- 06 list -->
  <section class="fig" style="--accent:var(--c-list)">
    <div class="fig-head">
      <div class="fig-emoji">🎒</div>
      <h2 class="fig-title">리스트는 가방이에요</h2>
    </div>
    <p class="fig-note">가방에 물건을 여러 개 담을 수 있어요. 번호(순서)로 물건을 꺼내볼 수도 있어요!</p>
    <div class="board-card">
      <div class="row">
        <button class="emoji-btn" data-item="🍭">🍭</button>
        <button class="emoji-btn" data-item="🍇">🍇</button>
        <button class="emoji-btn" data-item="🚗">🚗</button>
        <button class="emoji-btn" data-item="🎈">🎈</button>
        <button class="emoji-btn" data-item="🐟">🐟</button>
      </div>
      <div class="bag" id="bag"></div>
      <div class="code-block">
<pre><span class="kw">my_bag</span> = [<span id="bagCode"></span>]</pre>
      </div>
      <div class="row" id="indexPicker"></div>
      <div class="code-block">
<pre><span class="fn">print</span>(<span class="kw">my_bag</span>[<span class="num" id="idxCode">0</span>])</pre>
      </div>
      <div class="console"><span id="bagOutput" class="placeholder">가방에 담고, 번호를 눌러보세요</span></div>
    </div>
  </section>

  <!-- 07 dictionary -->
  <section class="fig" style="--accent:var(--c-dict)">
    <div class="fig-head">
      <div class="fig-emoji">🗂️</div>
      <h2 class="fig-title">딕셔너리는 이름표가 붙은 가방이에요</h2>
    </div>
    <p class="fig-note">리스트가 순서대로 담는 가방이라면, 딕셔너리는 '이름표'를 달아둬서 바로바로 찾을 수 있어요!</p>
    <div class="board-card">
      <div class="row">
        <button class="kid-btn ghost" id="dictBtn1">"사과" 꺼내기</button>
        <button class="kid-btn ghost" id="dictBtn2">"바나나" 꺼내기</button>
        <button class="kid-btn ghost" id="dictBtn3">"포도" 꺼내기</button>
      </div>
      <div class="code-block">
<pre><span class="kw">my_dict</span> = {<span class="str">"사과"</span>: <span class="str">"🍎"</span>, <span class="str">"바나나"</span>: <span class="str">"🍌"</span>, <span class="str">"포도"</span>: <span class="str">"🍇"</span>}
<span class="fn">print</span>(<span class="kw">my_dict</span>[<span class="str" id="dictCodeKey">"..."</span>])</pre>
      </div>
      <div class="console"><span id="dictOutput" class="placeholder">이름표를 눌러서 과일을 꺼내보세요</span></div>
    </div>
  </section>

  <!-- 08 function -->
  <section class="fig" style="--accent:var(--c-def)">
    <div class="fig-head">
      <div class="fig-emoji">🪄</div>
      <h2 class="fig-title">함수는 나만의 마법 주문이에요</h2>
    </div>
    <p class="fig-note">자주 쓰는 행동을 마법 주문 하나로 묶어둘 수 있어요. 괄호 안에 다른 단어를 넣으면 마법이 다르게 걸려요!</p>
    <div class="board-card">
      <div class="code-block">
<pre><span class="kw">def</span> <span class="fn">magic_spell</span>(word):
    <span class="fn">print</span>(<span class="str">"수리수리 마수리! "</span> + word)</pre>
      </div>
      <div class="row">
        <button class="kid-btn ghost" id="defBtn1">magic_spell("얍!")</button>
        <button class="kid-btn ghost" id="defBtn2">magic_spell("짠!")</button>
        <button class="kid-btn ghost" id="defBtn3">magic_spell("뿅!")</button>
      </div>
      <div class="code-block">
<pre><span class="fn" id="defCallCode">magic_spell</span>(<span class="str" id="defCallArg">"..."</span>)</pre>
      </div>
      <div class="console"><span id="defOutput" class="placeholder">마법 주문을 외워보세요</span></div>
    </div>
  </section>

  <!-- 09 input -->
  <section class="fig" style="--accent:var(--c-input)">
    <div class="fig-head">
      <div class="fig-emoji">⌨️</div>
      <h2 class="fig-title">input()은 컴퓨터에게 대답하는 거예요</h2>
    </div>
    <p class="fig-note">컴퓨터가 물어보는 말에 우리가 직접 키보드로 대답해서 컴퓨터에게 알려줄 수 있어요.</p>
    <div class="board-card">
      <div class="row" style="width: 100%; justify-content: center; gap: 8px;">
        <input type="text" id="inputField" placeholder="여기에 이름을 적어보세요" style="padding:12px; border-radius:12px; border:2px solid var(--rule); font-family:var(--sans); font-size:16px; outline:none; max-width:200px;">
        <button class="kid-btn" id="inputSubmitBtn">대답하기</button>
      </div>
      <div class="code-block">
<pre><span class="kw">name</span> = <span class="fn">input</span>(<span class="str">"이름이 뭔가요? "</span>)
<span class="fn">print</span>(<span class="str">"안녕, "</span> + <span class="kw">name</span> + <span class="str">"!"</span>)</pre>
      </div>
      <div class="console"><span id="inputOutput" class="placeholder">이름을 적고 대답하기를 눌러주세요</span></div>
    </div>
  </section>

  <footer>
    <div class="footer-title">오늘 배운 것 🎉</div>
    <div class="recap-grid">
      <div class="recap-card"><div class="e">📦</div><div class="t">변수</div><div class="d">이름표 붙은 상자에 값을 담아요</div></div>
      <div class="recap-card"><div class="e">💬</div><div class="t">print()</div><div class="d">컴퓨터가 우리에게 말해줘요</div></div>
      <div class="recap-card"><div class="e">➕</div><div class="t">사칙연산</div><div class="d">+ − × ÷ 로 계산해요</div></div>
      <div class="recap-card"><div class="e">🔀</div><div class="t">if / else</div><div class="d">조건에 따라 다르게 행동해요</div></div>
      <div class="recap-card"><div class="e">🔁</div><div class="t">for 반복문</div><div class="d">같은 일을 여러 번 반복해요</div></div>
      <div class="recap-card"><div class="e">🎒</div><div class="t">리스트</div><div class="d">여러 개를 순서대로 담아요</div></div>
      <div class="recap-card"><div class="e">🗂️</div><div class="t">딕셔너리</div><div class="d">이름표와 값을 세트로 담아요</div></div>
      <div class="recap-card"><div class="e">🪄</div><div class="t">함수 (def)</div><div class="d">나만의 마법 주문을 만들어요</div></div>
      <div class="recap-card"><div class="e">⌨️</div><div class="t">입력 (input)</div><div class="d">컴퓨터에게 키보드로 알려줘요</div></div>
    </div>
  </footer>

</div>

<script>
(function(){
  // ---------- progress badges ----------
  const badgeIcons = ['📦','💬','➕','🔀','🔁','🎒', '🗂️', '🪄', '⌨️'];
  const badgeBar = document.getElementById('badgeBar');
  const progressText = document.getElementById('progressText');
  const done = [false,false,false,false,false,false,false,false,false];
  
  const badgeEls = badgeIcons.map((icon) => {
    const el = document.createElement('div');
    el.className = 'badge';
    el.textContent = icon;
    badgeBar.appendChild(el);
    return el;
  });

  function markDone(i){
    if (done[i]) return;
    done[i] = true;
    badgeEls[i].classList.add('done');
    const count = done.filter(Boolean).length;
    progressText.textContent = count + ' / 9개 배지를 모았어요!';
    if (count === 9) {
      progressText.textContent = '🎉 전부 다 모았어요! 완벽해요! 🎉';
      confettiBurst();
    }
  }

  function confettiBurst(){
    const colors = ['#1f7a8c','#c9a227','#b8531d','#5b3a8e','#2e7d32','#0b4f63', '#0c8599', '#d9480f', '#c92a2a'];
    for (let i=0;i<60;i++){
      const c = document.createElement('div');
      c.className = 'confetti';
      c.style.left = Math.random()*100 + 'vw';
      c.style.background = colors[Math.floor(Math.random()*colors.length)];
      c.style.animation = `fall ${1.6+Math.random()*1.4}s ease-in forwards`;
      c.style.animationDelay = (Math.random()*0.4)+'s';
      document.body.appendChild(c);
      setTimeout(()=>c.remove(), 3500);
    }
  }

  // ---------- 01 variables ----------
  const varBox = document.getElementById('varBox');
  const varContent = document.getElementById('varContent');
  const varStrCode = document.getElementById('varStrCode');
  const varOutput = document.getElementById('varOutput');
  document.querySelectorAll('.fig[style*="c-var"] .emoji-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.fig[style*="c-var"] .emoji-btn').forEach(b=>b.classList.remove('selected'));
      btn.classList.add('selected');
      const word = btn.dataset.word;
      const emoji = btn.dataset.emoji;
      varBox.classList.add('filled');
      varContent.textContent = emoji;
      varContent.classList.remove('animate');
      void varContent.offsetWidth;
      varContent.classList.add('animate');
      varStrCode.textContent = '"' + word + '"';
      varOutput.innerHTML = '<span class="bubble">' + word + '</span>';
      markDone(0);
    });
  });

  // ---------- 02 print ----------
  const printStrCode = document.getElementById('printStrCode');
  const printConsole = document.getElementById('printConsole');
  document.querySelectorAll('.fig[style*="c-print"] .kid-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const msg = btn.dataset.msg;
      printStrCode.textContent = '"' + msg + '"';
      printConsole.innerHTML = '<span class="bubble">🐍 ' + msg + '</span>';
      markDone(1);
    });
  });

  // ---------- 03 math ----------
  let numA = 3, numB = 5, op = '+';
  const numADisplay = document.getElementById('numADisplay');
  const numBDisplay = document.getElementById('numBDisplay');
  const opDisplay = document.getElementById('opDisplay');
  const mathCodeA = document.getElementById('mathCodeA');
  const mathCodeB = document.getElementById('mathCodeB');
  const mathCodeOp = document.getElementById('mathCodeOp');
  const mathOutput = document.getElementById('mathOutput');
  const opSymbols = {'+':'+', '-':'−', '*':'×', '/':'÷'};

  function refreshMathDisplay(){
    numADisplay.textContent = numA;
    numBDisplay.textContent = numB;
    opDisplay.textContent = opSymbols[op];
    mathCodeA.textContent = numA;
    mathCodeB.textContent = numB;
    mathCodeOp.textContent = opSymbols[op];
  }
  document.getElementById('numAUp').addEventListener('click', ()=>{ numA = Math.min(20, numA+1); refreshMathDisplay(); });
  document.getElementById('numADown').addEventListener('click', ()=>{ numA = Math.max(0, numA-1); refreshMathDisplay(); });
  document.getElementById('numBUp').addEventListener('click', ()=>{ numB = Math.min(20, numB+1); refreshMathDisplay(); });
  document.getElementById('numBDown').addEventListener('click', ()=>{ numB = Math.max(0, numB-1); refreshMathDisplay(); });
  document.querySelectorAll('.op-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      document.querySelectorAll('.op-btn').forEach(b=>b.classList.remove('selected'));
      btn.classList.add('selected');
      op = btn.dataset.op;
      refreshMathDisplay();
    });
  });
  document.getElementById('btnCalc').addEventListener('click', ()=>{
    let result;
    if (op === '+') result = numA + numB;
    else if (op === '-') result = numA - numB;
    else if (op === '*') result = numA * numB;
    else { result = numB === 0 ? '앗, 0으로는 못 나눠요!' : Math.round((numA / numB) * 100) / 100; }
    mathOutput.innerHTML = '<span class="bubble">' + result + '</span>';
    markDone(2);
  });
  refreshMathDisplay();

  // ---------- 04 if/else ----------
  const numberPicker = document.getElementById('numberPicker');
  const ifResult = document.getElementById('ifResult');
  const ifLine = document.getElementById('ifLine');
  const elseLine = document.getElementById('elseLine');
  for (let n=1; n<=10; n++){
    const b = document.createElement('button');
    b.className = 'num-btn';
    b.textContent = n;
    b.addEventListener('click', ()=>{
      document.querySelectorAll('#numberPicker .num-btn').forEach(x=>x.classList.remove('selected'));
      b.classList.add('selected');
      const isEven = n % 2 === 0;
      ifLine.classList.toggle('active', isEven);
      elseLine.classList.toggle('active', !isEven);
      ifResult.className = 'result-banner ' + (isEven ? 'even' : 'odd');
      ifResult.textContent = n + '은(는) ' + (isEven ? '짝수예요! 😊' : '홀수예요! 🙂');
      markDone(3);
    });
    numberPicker.appendChild(b);
  }

  // ---------- 05 for loop ----------
  let loopN = 3, loopI = 0, loopTimer = null;
  const loopCountPicker = document.getElementById('loopCountPicker');
  const loopStage = document.getElementById('loopStage');
  const loopNEl = document.getElementById('loopN');
  const loopProgress = document.getElementById('loopProgress');
  const forLine = document.getElementById('forLine');
  const btnLoopStep = document.getElementById('btnLoopStep');
  const btnLoopPlay = document.getElementById('btnLoopPlay');
  const btnLoopReset = document.getElementById('btnLoopReset');

  for (let n=1; n<=5; n++){
    const b = document.createElement('button');
    b.className = 'num-btn' + (n===3 ? ' selected' : '');
    b.textContent = n;
    b.addEventListener('click', ()=>{
      document.querySelectorAll('#loopCountPicker .num-btn').forEach(x=>x.classList.remove('selected'));
      b.classList.add('selected');
      loopN = n;
      resetLoop();
    });
    loopCountPicker.appendChild(b);
  }

  function renderLoop(){
    loopNEl.textContent = loopN;
    loopProgress.textContent = loopI + ' / ' + loopN;
    btnLoopStep.disabled = loopI >= loopN;
    btnLoopPlay.disabled = loopI >= loopN;
  }
  function resetLoop(){
    loopI = 0;
    loopStage.innerHTML = '';
    clearInterval(loopTimer); loopTimer = null;
    btnLoopPlay.textContent = '자동 재생';
    renderLoop();
  }
  function loopStep(){
    if (loopI >= loopN) return;
    loopI++;
    const bub = document.createElement('span');
    bub.className = 'bubble';
    bub.textContent = '안녕! 🙌';
    loopStage.appendChild(bub);
    forLine.classList.add('active');
    setTimeout(()=>forLine.classList.remove('active'), 250);
    renderLoop();
    if (loopI >= loopN){
      clearInterval(loopTimer); loopTimer = null;
      btnLoopPlay.textContent = '자동 재생';
      markDone(4);
    }
  }
  btnLoopStep.addEventListener('click', loopStep);
  btnLoopReset.addEventListener('click', resetLoop);
  btnLoopPlay.addEventListener('click', ()=>{
    if (loopTimer){ clearInterval(loopTimer); loopTimer=null; btnLoopPlay.textContent='자동 재생'; return; }
    btnLoopPlay.textContent = '일시 정지';
    loopTimer = setInterval(()=>{
      if (loopI >= loopN){ clearInterval(loopTimer); loopTimer=null; btnLoopPlay.textContent='자동 재생'; return; }
      loopStep();
    }, 500);
  });
  renderLoop();

  // ---------- 06 list ----------
  const bagEl = document.getElementById('bag');
  const bagCode = document.getElementById('bagCode');
  const indexPicker = document.getElementById('indexPicker');
  const idxCode = document.getElementById('idxCode');
  const bagOutput = document.getElementById('bagOutput');
  const bagItems = [null,null,null,null,null];
  const slotEls = [];

  for (let i=0;i<5;i++){
    const slot = document.createElement('div');
    slot.className = 'slot';
    const idx = document.createElement('div');
    idx.className = 'idx';
    idx.textContent = i;
    slot.appendChild(idx);
    bagEl.appendChild(slot);
    slotEls.push(slot);

    const ib = document.createElement('button');
    ib.className = 'num-btn';
    ib.textContent = i;
    ib.addEventListener('click', ()=>{
      document.querySelectorAll('#indexPicker .num-btn').forEach(x=>x.classList.remove('selected'));
      ib.classList.add('selected');
      slotEls.forEach(s=>s.classList.remove('picked'));
      idxCode.textContent = i;
      if (bagItems[i]){
        slotEls[i].classList.add('picked');
        bagOutput.innerHTML = '<span class="bubble">' + bagItems[i] + '</span>';
        markDone(5);
      } else {
        bagOutput.innerHTML = '<span class="placeholder">그 칸은 아직 비어있어요!</span>';
      }
    });
    indexPicker.appendChild(ib);
  }

  function refreshBagCode(){
    bagCode.textContent = bagItems.filter(Boolean).map(x=>'"'+x+'"').join(', ');
  }

  document.querySelectorAll('.fig[style*="c-list"] .emoji-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      const emptyIdx = bagItems.indexOf(null);
      if (emptyIdx === -1) return;
      bagItems[emptyIdx] = btn.dataset.item;
      slotEls[emptyIdx].classList.add('filled');
      slotEls[emptyIdx].textContent = btn.dataset.item;
      const idx = document.createElement('div');
      idx.className = 'idx';
      idx.textContent = emptyIdx;
      slotEls[emptyIdx].appendChild(idx);
      refreshBagCode();
    });
  });

  // ---------- 07 dictionary ----------
  const dictCodeKey = document.getElementById('dictCodeKey');
  const dictOutput = document.getElementById('dictOutput');
  const dictDict = {"사과": "🍎", "바나나": "🍌", "포도": "🍇"};
  
  document.getElementById('dictBtn1').addEventListener('click', ()=>{ dictCodeKey.textContent = '"사과"'; dictOutput.innerHTML = '<span class="bubble">🍎</span>'; markDone(6); });
  document.getElementById('dictBtn2').addEventListener('click', ()=>{ dictCodeKey.textContent = '"바나나"'; dictOutput.innerHTML = '<span class="bubble">🍌</span>'; markDone(6); });
  document.getElementById('dictBtn3').addEventListener('click', ()=>{ dictCodeKey.textContent = '"포도"'; dictOutput.innerHTML = '<span class="bubble">🍇</span>'; markDone(6); });

  // ---------- 08 function ----------
  const defCallArg = document.getElementById('defCallArg');
  const defOutput = document.getElementById('defOutput');
  
  document.getElementById('defBtn1').addEventListener('click', ()=>{ defCallArg.textContent = '"얍!"'; defOutput.innerHTML = '<span class="bubble">수리수리 마수리! 얍!</span>'; markDone(7); });
  document.getElementById('defBtn2').addEventListener('click', ()=>{ defCallArg.textContent = '"짠!"'; defOutput.innerHTML = '<span class="bubble">수리수리 마수리! 짠!</span>'; markDone(7); });
  document.getElementById('defBtn3').addEventListener('click', ()=>{ defCallArg.textContent = '"뿅!"'; defOutput.innerHTML = '<span class="bubble">수리수리 마수리! 뿅!</span>'; markDone(7); });

  // ---------- 09 input ----------
  const inputField = document.getElementById('inputField');
  const inputSubmitBtn = document.getElementById('inputSubmitBtn');
  const inputOutput = document.getElementById('inputOutput');

  inputSubmitBtn.addEventListener('click', ()=>{
    const val = inputField.value.trim();
    if (val === '') {
      inputOutput.innerHTML = '<span class="placeholder">이름을 먼저 적어주세요!</span>';
      return;
    }
    inputOutput.innerHTML = '<span class="bubble">안녕, ' + val + '!</span>';
    markDone(8);
  });
  inputField.addEventListener('keypress', (e)=>{
    if (e.key === 'Enter') inputSubmitBtn.click();
  });

})();
</script>

</body>
</html>
"""

with open('/Users/cheonhyeonjun/com_gui/public/python_playground.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated new python_playground.html")
