html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>신나는 파이썬 거북이 그림 교실</title>
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

  .hero{ padding:60px 0 40px; text-align:center; }
  .eyebrow{ font-family:var(--mono); font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--water-deep);
    display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:18px; }
  .eyebrow::before, .eyebrow::after{ content:''; width:22px; height:1px; background:var(--water-deep); }
  h1{ font-family:var(--display); font-weight:700; font-size:clamp(32px,6vw,48px); line-height:1.15; margin:0 0 18px; letter-spacing:-0.01em; }
  h1 em{ font-style:normal; color:var(--water-deep); }
  .lede{ font-size:18px; color:var(--ink-soft); max-width:60ch; margin:0 auto; }
  .lede b{ color:var(--ink); font-weight:600; }

  .fig{ padding:52px 0; border-top:1px solid var(--rule); }
  .fig-head{ display:flex; align-items:center; gap:14px; margin-bottom:18px; flex-wrap:wrap; }
  .fig-emoji{ font-size:30px; width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center;
    background:var(--accent, var(--water)); flex:0 0 auto; color:#fff; }
  .fig-title{ font-family:var(--display); font-weight:700; font-size:24px; margin:0; color:var(--ink); }
  .fig-note{ color:var(--ink-soft); font-size:16px; max-width:68ch; margin:0 0 20px; }
  .fig-note b{ color:var(--ink); }

  .board-card{ background:#fff; border:2px solid var(--rule); border-radius:16px; padding:26px;
    display:flex; flex-direction:column; gap:18px; }

  /* code block */
  .code-block{ font-family:var(--mono); font-size:14px; background:#132321; color:#dce8e4; border-radius:12px;
    padding:18px 22px; width:100%; overflow-x:auto; }
  .code-block pre{ margin:0; white-space:pre; }
  .code-block .kw{ color:#7fc8ff; }
  .code-block .fn{ color:#ffd580; }
  .code-block .str{ color:#a9e5c9; }
  .code-block .num{ color:#f5a97f; }
  .code-block .cm{ color:#7a938d; font-style:italic; }

  .callout{ background:#fff3e9; border:1px solid var(--warn); border-left-width:4px; border-radius:6px;
    padding:14px 18px; font-size:14.5px; color:var(--ink); margin:16px 0; }
  .callout b{ color:var(--warn); }

  .grammar-badge { display:inline-block; font-family:var(--mono); font-size:11px; padding:4px 8px; border-radius:4px; background:var(--paper-2); color:var(--ink-soft); margin-bottom:6px; letter-spacing:0.04em; }

  ul, ol { padding-left: 24px; margin: 0; }
  li { margin-bottom: 8px; }
  
  table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 15px; }
  th, td { border: 1px solid var(--rule); padding: 10px 14px; text-align: left; }
  th { background: var(--paper-2); font-weight: 600; font-family: var(--display); }

  footer{ border-top:1px solid var(--rule); padding:40px 0 60px; text-align:center; }
  .footer-title{ font-family:var(--display); font-weight:700; font-size:22px; margin-bottom:14px; }
</style>
</head>
<body>

<div class="topbar">
  <span><strong>🐢 TURTLE GRAPHICS</strong></span>
  <span>기초 문법 프리뷰 & 신나는 거북이 그림 교실</span>
</div>

<div class="wrap">

  <section class="hero">
    <div class="eyebrow">부모님과 함께해요</div>
    <h1>문법을 쏙쏙! <br><em>거북이 그림 놀이!</em> 🐢</h1>
    <p class="lede">
      코딩의 뼈대가 되는 '기초 문법'을 먼저 가볍게 살펴본 다음,
      거북이에게 명령을 내리면서 배운 문법을 눈으로 직접 확인해봐요!
      아이는 <b>"결정하는 사람"</b>, 어른은 <b>"타이핑 조수"</b> 역할을 맡아주세요.
    </p>
  </section>

  <!-- 1. 준비물 및 환경설정 -->
  <section class="fig" style="--accent:var(--c-var)">
    <div class="fig-head">
      <div class="fig-emoji">🎒</div>
      <h2 class="fig-title">1. 코딩할 준비를 해요</h2>
    </div>
    <div class="board-card">
      <h3>💻 파이썬 & VS Code 설치</h3>
      <ol>
        <li><b>python.org</b>에서 파이썬을 설치해요. (Windows는 <b>"Add python.exe to PATH"</b> 꼭 체크!)</li>
        <li><b>code.visualstudio.com</b>에서 편집기(VS Code)를 설치해요.</li>
        <li>VS Code를 열고 왼쪽 블록 아이콘(Extensions)에서 <b>Python</b>을 검색해서 설치해요.</li>
        <li>바탕화면에 새 폴더를 만들고 VS Code로 열어주세요.</li>
      </ol>

      <h3 style="margin-top:24px;">🚀 첫 번째 코드 실행해보기</h3>
      <ol>
        <li>VS Code에서 <code>hello.py</code>라는 새 파일을 만들어요.</li>
        <li>아래 코드를 입력하세요.</li>
      </ol>
      <div class="code-block" style="margin:8px 0;">
<pre><span class="fn">print</span>(<span class="str">"안녕! 나는 파이썬이야!"</span>)</pre>
      </div>
      <ol start="3">
        <li>화면 오른쪽 위의 <b>▶ (실행)</b> 버튼을 누르면 아래쪽 터미널에 글자가 뿅! 하고 나와요.</li>
      </ol>
      <div class="callout" style="background:#eaf5ec; border-color:var(--c-loop);">
        <b style="color:var(--c-loop);">💡 아이에게:</b> <i>"우리가 쓴 글자가 진짜로 화면에 나왔어! 컴퓨터랑 처음으로 대화한 거야!"</i> 라고 알려주세요.
      </div>
    </div>
  </section>

  <!-- 2. 파이썬 기초 문법 맛보기 (프리뷰) -->
  <section class="fig" style="--accent:var(--c-print)">
    <div class="fig-head">
      <div class="fig-emoji">🔍</div>
      <h2 class="fig-title">2. 파이썬 기초 문법 맛보기 (프리뷰)</h2>
    </div>
    <p class="fig-note">거북이를 만나기 전에, 파이썬이 어떤 규칙으로 움직이는지 미리 살짝 살펴볼까요?</p>

    <div class="board-card">
      <h3>📦 변수 (Variable): "이름표가 붙은 상자"</h3>
      <p>값을 담아두고 언제든 꺼내 쓸 수 있는 상자예요.</p>
      <div class="code-block">
<pre><span class="cm"># '민준'이라는 글자를 name 상자에 담기</span>
name = <span class="str">"민준"</span>
<span class="fn">print</span>(name)</pre>
      </div>

      <h3 style="margin-top:24px;">🅰️ 숫자와 글자 (Data Types): "따옴표의 마법"</h3>
      <p>컴퓨터는 숫자는 계산할 수 있지만, 글자는 그냥 모양으로만 봐요. 그래서 <b>글자에는 꼭 따옴표(" ")</b> 옷을 입혀야 해요.</p>
      <div class="code-block">
<pre><span class="fn">print</span>(<span class="num">3</span> + <span class="num">5</span>)       <span class="cm"># 숫자 계산! (결과: 8)</span>
<span class="fn">print</span>(<span class="str">"안녕 파이썬"</span>) <span class="cm"># 글자 출력!</span></pre>
      </div>

      <h3 style="margin-top:24px;">🎒 리스트 (List): "한 상자에 여러 개 담기"</h3>
      <p>여러 가지 물건을 한꺼번에 보관하는 가방(배열)이에요.</p>
      <div class="code-block">
<pre>colors = [<span class="str">"red"</span>, <span class="str">"blue"</span>, <span class="str">"yellow"</span>]
<span class="fn">print</span>(colors[<span class="num">0</span>])   <span class="cm"># 컴퓨터는 0번부터 세어요! (결과: red)</span></pre>
      </div>

      <h3 style="margin-top:24px;">🔁 반복문 (for loop): "똑같은 일 쉽게 하기"</h3>
      <p>같은 행동을 여러 번 할 때 쓰는 <b>마법 주문</b>이에요. 파이썬은 묶음을 표현할 때 <b>들여쓰기(띄어쓰기 4칸)</b>를 꼭 해야 해요.</p>
      <div class="code-block">
<pre><span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">3</span>):
    <span class="fn">print</span>(<span class="str">"야호!"</span>)   <span class="cm"># 4칸 띄어쓰기를 한 이 문장이 3번 반복돼요.</span></pre>
      </div>
    </div>
  </section>

  <!-- 3. 거북이 설명 -->
  <section class="fig" style="--accent:var(--water)">
    <div class="fig-head">
      <div class="fig-emoji">🐢</div>
      <h2 class="fig-title">3. 자, 이제 거북이와 그림을 그려볼까요?</h2>
    </div>
    <p class="fig-note">
      터틀(turtle)은 화면 위를 기어다니며 그림을 그리는 파이썬 거북이 친구예요.<br>
      방금 배운 기초 문법들을 거북이에게 쓰면 거북이가 어떻게 움직일까요?
    </p>

    <div class="board-card">
      <div class="callout" style="margin-top:0; border-left-color:var(--water); background:#eff8f9;">
        거북이를 불러오는 모든 예제는 <b>항상 아래 3줄로 시작</b>해요! 
      </div>
      <div class="code-block" style="margin-top:8px;">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()  <span class="cm"># 방금 배운 '변수' t에 거북이를 담았어요!</span>
<span class="cm"># ... 여기에 거북이 명령을 적어요 ...</span>
turtle.<span class="fn">done</span>()        <span class="cm"># 맨 마지막 줄에 이걸 꼭 적어주세요!</span></pre>
      </div>

      <h3 style="margin-top:24px;">🚶 3-1. 거북이 움직이기 (순차 명령)</h3>
      <table>
        <tr><th>명령어</th><th>뜻</th><th>비유</th></tr>
        <tr><td><code>t.forward(100)</code></td><td>100만큼 앞으로 걷기</td><td>"앞으로 100걸음!" (숫자를 줬죠?)</td></tr>
        <tr><td><code>t.backward(50)</code></td><td>뒤로 걷기</td><td>"뒤로 뒷걸음질!"</td></tr>
        <tr><td><code>t.left(90)</code></td><td>왼쪽으로 90도 돌기</td><td>"왼쪽으로 빙글!"</td></tr>
        <tr><td><code>t.right(90)</code></td><td>오른쪽으로 90도 돌기</td><td>"오른쪽으로 빙글!"</td></tr>
      </table>

      <h3 style="margin-top:24px;">🎨 3-2. 색깔과 굵기 (글자와 숫자)</h3>
      <div class="code-block">
<pre>t.<span class="fn">color</span>(<span class="str">"red"</span>)       <span class="cm"># 색깔 이름은 '글자'니까 따옴표 옷을!</span>
t.<span class="fn">pensize</span>(<span class="num">5</span>)         <span class="cm"># 굵기는 '숫자'니까 그냥 써요!</span></pre>
      </div>

      <h3 style="margin-top:24px;">🪄 3-3. 반복문으로 거북이 춤추게 하기</h3>
      <p>방금 프리뷰에서 배운 <b>마법 주문(들여쓰기 4칸)</b>을 거북이에게 써봐요.</p>
      <div class="code-block">
<pre><span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">4</span>):
    t.<span class="fn">forward</span>(<span class="num">100</span>)   <span class="cm"># 들여쓰기 4칸!</span>
    t.<span class="fn">right</span>(<span class="num">90</span>)      <span class="cm"># 들여쓰기 4칸!</span></pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px;">→ <i>"얍! 하고 4번 외치면 거북이가 4번 앞으로 가고 4번 돌아!"</i></p>

      <h3 style="margin-top:24px;">✏️ 3-4. 이름표 쓰기 — <code>write()</code></h3>
      <div class="code-block">
<pre>t.<span class="fn">write</span>(<span class="str">"민준"</span>)        <span class="cm"># 거북이가 화면에 글자를 써줘요. 따옴표 필수!</span></pre>
      </div>
    </div>
  </section>

  <!-- 4. 프로젝트 -->
  <section class="fig" style="--accent:var(--c-loop)">
    <div class="fig-head">
      <div class="fig-emoji">⭐</div>
      <h2 class="fig-title">4. 단계별 프로젝트 (쉬운 것 → 신나는 것)</h2>
    </div>
    <p class="fig-note">
      각 프로젝트는 새 <code>.py</code> 파일로 만들어서 실행 버튼(▶)을 누르면 바로 창이 뜨며 결과가 보여요.
    </p>

    <div class="board-card">
      <h3>🟢 프로젝트 1. 선 하나 긋기 (첫 그림!)</h3>
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()

t.<span class="fn">forward</span>(<span class="num">150</span>)

turtle.<span class="fn">done</span>()</pre>
      </div>

      <h3 style="margin-top:24px;">🟢 프로젝트 2. 네모 그리기 (하나하나 명령)</h3>
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()

t.<span class="fn">forward</span>(<span class="num">100</span>)
t.<span class="fn">right</span>(<span class="num">90</span>)
t.<span class="fn">forward</span>(<span class="num">100</span>)
t.<span class="fn">right</span>(<span class="num">90</span>)
t.<span class="fn">forward</span>(<span class="num">100</span>)
t.<span class="fn">right</span>(<span class="num">90</span>)
t.<span class="fn">forward</span>(<span class="num">100</span>)
t.<span class="fn">right</span>(<span class="num">90</span>)

turtle.<span class="fn">done</span>()</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px; margin-top:8px;">→ <i>"똑같은 걸 4번 썼지? 배운 대로 마법 주문으로 줄여보자!"</i></p>

      <h3 style="margin-top:24px;">🟡 프로젝트 3. 마법 주문으로 네모 그리기</h3>
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">color</span>(<span class="str">"blue"</span>)
t.<span class="fn">pensize</span>(<span class="num">3</span>)

<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">4</span>):
    t.<span class="fn">forward</span>(<span class="num">100</span>)
    t.<span class="fn">right</span>(<span class="num">90</span>)

turtle.<span class="fn">done</span>()</pre>
      </div>

      <h3 style="margin-top:24px;">🟡 프로젝트 4. 반짝반짝 별 그리기</h3>
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">color</span>(<span class="str">"gold"</span>)
t.<span class="fn">pensize</span>(<span class="num">3</span>)

<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">5</span>):
    t.<span class="fn">forward</span>(<span class="num">150</span>)
    t.<span class="fn">right</span>(<span class="num">144</span>)

turtle.<span class="fn">done</span>()</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px; margin-top:8px;">→ 각도만 바꿨는데 완전히 다른 모양! <i>"144도로 돌면 별이 돼요!"</i></p>

      <h3 style="margin-top:24px;">🟠 프로젝트 5. 무지개 나선 그리기 (리스트 활용!)</h3>
      <p>아까 배운 '리스트(상자 묶음)'를 여기서 진짜로 써봐요!</p>
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">speed</span>(<span class="num">0</span>)
t.<span class="fn">pensize</span>(<span class="num">3</span>)

<span class="cm"># 6가지 색깔이 담긴 리스트 가방</span>
colors = [<span class="str">"red"</span>, <span class="str">"orange"</span>, <span class="str">"yellow"</span>, <span class="str">"green"</span>, <span class="str">"blue"</span>, <span class="str">"purple"</span>]

<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">60</span>):
    t.<span class="fn">color</span>(colors[i % <span class="num">6</span>])  <span class="cm"># 가방에서 하나씩 꺼내 써요</span>
    t.<span class="fn">forward</span>(i * <span class="num">3</span>)
    t.<span class="fn">right</span>(<span class="num">59</span>)

turtle.<span class="fn">done</span>()</pre>
      </div>

      <h3 style="margin-top:24px;">🔴 프로젝트 6. 꽃 그리기 (동그라미 반복)</h3>
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">speed</span>(<span class="num">0</span>)
t.<span class="fn">color</span>(<span class="str">"hotpink"</span>)
t.<span class="fn">pensize</span>(<span class="num">2</span>)

<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">36</span>):
    t.<span class="fn">circle</span>(<span class="num">50</span>)
    t.<span class="fn">left</span>(<span class="num">10</span>)

turtle.<span class="fn">done</span>()</pre>
      </div>

      <h3 style="margin-top:24px;">🎁 프로젝트 7. 완성작 — 나만의 이름 그림</h3>
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">speed</span>(<span class="num">0</span>)

<span class="cm"># 배경에 별 그리기</span>
t.<span class="fn">color</span>(<span class="str">"gold"</span>)
<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">5</span>):
    t.<span class="fn">forward</span>(<span class="num">100</span>)
    t.<span class="fn">right</span>(<span class="num">144</span>)

<span class="cm"># 글자(문자열)를 화면에 쓰기</span>
t.<span class="fn">penup</span>()
t.<span class="fn">goto</span>(-<span class="num">100</span>, -<span class="num">20</span>)
t.<span class="fn">pendown</span>()
t.<span class="fn">color</span>(<span class="str">"purple"</span>)
t.<span class="fn">write</span>(<span class="str">"민준이의 그림"</span>, font=(<span class="str">"Arial"</span>, <span class="num">24</span>, <span class="str">"bold"</span>))

turtle.<span class="fn">done</span>()</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px; margin-top:8px;">→ 아이가 직접 이름 부분만 자기 이름으로 바꾸고 ▶ 버튼을 누르게 해주세요!</p>
    </div>
  </section>

  <!-- 5. 에러 대처법 -->
  <section class="fig" style="--accent:var(--c-print)">
    <div class="fig-head">
      <div class="fig-emoji">💡</div>
      <h2 class="fig-title">5. 에러 대처법 (흔한 실수들)</h2>
    </div>
    <div class="board-card">
      <table>
        <tr><th>에러 메시지</th><th>원인</th><th>해결 방법</th></tr>
        <tr><td><code>NameError</code></td><td>오타 (예: <code>Turtel</code>)</td><td>철자 다시 확인하기</td></tr>
        <tr><td><code>SyntaxError</code></td><td>글자(문자열)인데 <code>" "</code>를 빼먹음</td><td>글자 양쪽에 따옴표를 잘 썼나 확인하기</td></tr>
        <tr><td><code>IndentationError</code></td><td>들여쓰기(공백) 안 맞음</td><td><code>for</code> 문 안쪽 줄은 꼭 <b>4칸 띄우기</b></td></tr>
        <tr><td>창이 바로 사라짐</td><td>맨 끝에 <code>turtle.done()</code> 빠짐</td><td>마지막 줄에 추가하기</td></tr>
      </table>
      <div class="callout" style="margin-top:16px;">
        <b style="color:var(--c-var);">💡 부모님 팁:</b> <i>"컴퓨터가 들여쓰기를 빼먹어서 삐졌나 봐! 우리 띄어쓰기 4칸이 잘 되었는지 탐정처럼 찾아볼까?"</i> 라고 놀이처럼 접근해주세요.
      </div>
    </div>
  </section>

  <!-- 6. 다음 단계 -->
  <section class="fig" style="--accent:var(--warn)">
    <div class="fig-head">
      <div class="fig-emoji">🚀</div>
      <h2 class="fig-title">6. 다음 단계로 넘어가고 싶다면</h2>
    </div>
    <div class="board-card">
      <ul>
        <li><code>t.circle()</code>, <code>t.dot()</code> 등 다른 도형 명령어 탐험하기</li>
        <li>조건문(<code>if</code>)으로 "특정 색이면 다르게 그리기" 도전</li>
        <li><code>turtle.bgcolor("skyblue")</code> 로 배경색 바꾸기</li>
        <li>여러 마리 거북이(<code>turtle.Turtle()</code> 여러 개)로 그림 대결하기</li>
      </ul>
      <div class="callout" style="margin-top:20px; background:#f9f9f9; border-color:var(--c-math);">
        <b style="color:var(--c-math);">👩‍🏫 진행 팁</b><br>
        한 프로젝트당 10~15분, 프로젝트 하나 끝날 때마다 화면 캡처해서 모아두면 나중에 성장 앨범이 돼요.<br>
        아이가 직접 <b>숫자(각도, 길이, 색깔 이름)</b>만 바꿔보게 하는 것만으로도 "내가 만들었다"는 성취감을 크게 느껴요.
      </div>
    </div>
  </section>

  <footer>
    <div class="footer-title">🐢 거북이와 함께 파이썬의 기초를 정복했어요! 🎉</div>
  </footer>

</div>

</body>
</html>
"""

with open('/Users/cheonhyeonjun/com_gui/public/python_turtle.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated python_turtle.html")
