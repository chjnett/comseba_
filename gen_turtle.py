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
  <span>유치원생과 함께하는 신나는 파이썬 거북이 그림 교실</span>
</div>

<div class="wrap">

  <section class="hero">
    <div class="eyebrow">부모님과 함께해요</div>
    <h1>거북이 친구와 함께<br><em>그림 그리기!</em> 🐢</h1>
    <p class="lede">
      거북이 친구에게 명령을 내려서 그림을 그리게 하는 놀이를 통해 파이썬을 배워요.
      아이는 <b>"어떤 명령을 넣을지 결정하는 사람"</b>, 어른은 <b>"타이핑을 도와주는 조수"</b> 역할을 맡으면 좋아요.
    </p>
  </section>

  <!-- 0. 준비물 -->
  <section class="fig" style="--accent:var(--c-var)">
    <div class="fig-head">
      <div class="fig-emoji">🎒</div>
      <h2 class="fig-title">0. 준비물</h2>
    </div>
    <div class="board-card">
      <ul>
        <li><b>컴퓨터</b> (Windows 또는 Mac)</li>
        <li><b>인터넷 연결</b> (설치할 때만 필요)</li>
        <li><b>30분 정도의 시간</b> (설치는 어른이 미리 해두는 걸 추천해요!)</li>
      </ul>
    </div>
  </section>

  <!-- 1. 파이썬 설치하기 -->
  <section class="fig" style="--accent:var(--c-loop)">
    <div class="fig-head">
      <div class="fig-emoji">⚙️</div>
      <h2 class="fig-title">1. 파이썬 설치하기</h2>
    </div>
    <div class="board-card">
      <h3>💻 Windows</h3>
      <ol>
        <li>브라우저에서 <b>python.org</b> 접속 → 상단 메뉴 <b>Downloads</b> 클릭</li>
        <li>노란색 <b>"Download Python 3.x.x"</b> 버튼 클릭 (자동으로 최신 버전 다운로드)</li>
        <li>다운로드된 설치 파일 실행</li>
        <li>⚠️ <span style="color:var(--warn); font-weight:bold;">가장 중요한 단계</span>: 설치 창 맨 아래 <b>"Add python.exe to PATH"</b> 체크박스를 <b>꼭 체크하세요!</b></li>
        <li><b>"Install Now"</b> 클릭 → 설치 완료까지 기다리기</li>
        <li>설치가 끝나면 <b>"Disable path length limit"</b>이 뜨면 클릭 (없으면 그냥 닫기)</li>
      </ol>

      <h3 style="margin-top:24px;">🍎 Mac</h3>
      <ol>
        <li>브라우저에서 <b>python.org</b> 접속 → <b>Downloads</b> → <b>macOS</b> 클릭</li>
        <li><code>.pkg</code> 파일 다운로드 후 실행</li>
        <li>화면 안내에 따라 계속 <b>Continue → Agree → Install</b> 클릭</li>
        <li>설치 완료!</li>
      </ol>

      <div class="callout">
        <b>✅ 설치 확인하기</b><br>
        Windows: 시작 메뉴에서 <b>cmd</b> 검색 → 명령 프롬프트 실행<br>
        Mac: <b>Spotlight(⌘+Space)</b> → <b>terminal</b> 검색 → 터미널 실행<br><br>
        터미널에 <code>python --version</code> (또는 <code>python3 --version</code>)을 입력했을 때 <code>Python 3.12.x</code> 같은 글자가 나오면 성공! 🎉
      </div>
    </div>
  </section>

  <!-- 2. VS Code 설치하기 -->
  <section class="fig" style="--accent:var(--c-list)">
    <div class="fig-head">
      <div class="fig-emoji">📝</div>
      <h2 class="fig-title">2. VS Code (편집기) 설치하기</h2>
    </div>
    <div class="board-card">
      <ol>
        <li>브라우저에서 <b>code.visualstudio.com</b> 접속</li>
        <li>파란색 <b>"Download"</b> 버튼 클릭 (내 컴퓨터에 맞는 버전 자동 추천됨)</li>
        <li>다운로드된 파일 실행 → 계속 <b>Next → I Agree → Next → Install</b></li>
        <li>설치 완료 후 VS Code 실행</li>
      </ol>
      <h3 style="margin-top:24px;">🧩 파이썬 확장 프로그램 설치</h3>
      <ol>
        <li>VS Code 왼쪽 세로 아이콘 중 <b>네모 4개 모양(Extensions)</b> 클릭</li>
        <li>검색창에 <b>"Python"</b> 입력</li>
        <li>Microsoft에서 만든 <b>Python</b> 확장(파란/노란 로고) 찾아서 <b>Install</b> 클릭</li>
      </ol>
      <p style="margin-top:14px; text-align:center; font-weight:bold;">이제 진짜 준비 끝! 🎈</p>
    </div>
  </section>

  <!-- 3. 첫 코드 실행해보기 -->
  <section class="fig" style="--accent:var(--c-math)">
    <div class="fig-head">
      <div class="fig-emoji">🚀</div>
      <h2 class="fig-title">3. 첫 코드 실행해보기</h2>
    </div>
    <div class="board-card">
      <ol>
        <li>VS Code에서 <b>File → Open Folder</b>로 바탕화면에 만든 폴더(예: <code>파이썬거북이</code>) 열기</li>
        <li>왼쪽 파일 목록에서 <b>새 파일</b> 아이콘 클릭 → 파일명을 <code>hello.py</code> 로 저장 (반드시 <code>.py</code>로 끝나야 해요!)</li>
        <li>아래 코드를 입력:</li>
      </ol>
      <div class="code-block" style="margin:8px 0;">
<pre><span class="fn">print</span>(<span class="str">"안녕! 나는 파이썬이야!"</span>)</pre>
      </div>
      <ol start="4">
        <li>화면 오른쪽 위 <b>▶ (실행, Run)</b> 삼각형 버튼 클릭</li>
        <li>아래쪽 터미널 창에 <b>"안녕! 나는 파이썬이야!"</b>라는 글자가 뜨면 성공! 🎉</li>
      </ol>
      <div class="callout" style="background:#eaf5ec; border-color:var(--c-loop);">
        <b style="color:var(--c-loop);">💡 팁</b>: 아이에게 <i>"우리가 쓴 글자가 진짜로 화면에 나왔어! 이게 바로 프로그래밍이야!"</i> 라고 말해주면 눈이 반짝여요.
      </div>
    </div>
  </section>

  <!-- 4. 문법 -->
  <section class="fig" style="--accent:var(--c-if)">
    <div class="fig-head">
      <div class="fig-emoji">🐢</div>
      <h2 class="fig-title">4. 재미있는 거북이 문법 배우기</h2>
    </div>
    <p class="fig-note">
      터틀(turtle)은 화면 위를 기어다니며 그림을 그리는 파이썬 거북이 친구예요.<br>
      모든 거북이 예제는 항상 아래 3줄로 시작해요! (거북이를 화면에 불러오는 "주문"이라고 알려주세요)
    </p>
    <div class="board-card">
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()
<span class="cm"># ... 여기에 거북이 명령을 적어요 ...</span>
turtle.<span class="fn">done</span>()  <span class="cm"># ← 이건 맨 마지막 줄에!</span></pre>
      </div>
      
      <h3 style="margin-top:16px;">🚶 4-1. 거북이 움직이기 (순차 명령)</h3>
      <table>
        <tr><th>명령어</th><th>뜻</th><th>비유</th></tr>
        <tr><td><code>t.forward(100)</code></td><td>100만큼 앞으로 걷기</td><td>"앞으로 100걸음!"</td></tr>
        <tr><td><code>t.backward(50)</code></td><td>뒤로 걷기</td><td>"뒤로 뒷걸음질!"</td></tr>
        <tr><td><code>t.left(90)</code></td><td>왼쪽으로 90도 돌기</td><td>"왼쪽으로 빙글!"</td></tr>
        <tr><td><code>t.right(90)</code></td><td>오른쪽으로 90도 돌기</td><td>"오른쪽으로 빙글!"</td></tr>
      </table>

      <h3 style="margin-top:24px;">🎨 4-2. 색깔과 굵기 (팔레트 놀이)</h3>
      <div class="code-block">
<pre>t.<span class="fn">color</span>(<span class="str">"red"</span>)       <span class="cm"># 빨간색 선</span>
t.<span class="fn">pensize</span>(<span class="num">5</span>)         <span class="cm"># 붓을 굵게!</span></pre>
      </div>

      <h3 style="margin-top:24px;">🪄 4-3. 반복문 — "얍얍얍! 마법 주문"</h3>
      <p>같은 동작을 여러 번 하고 싶을 때 쓰는 <b>마법 주문</b>이라고 알려주세요.</p>
      <div class="code-block">
<pre><span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">4</span>):
    t.<span class="fn">forward</span>(<span class="num">100</span>)
    t.<span class="fn">right</span>(<span class="num">90</span>)</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px;">→ <i>"얍! 하고 4번 외치면 거북이가 4번 앞으로 가고 4번 돌아!"</i> 라고 설명하면 이해가 쉬워요.</p>

      <h3 style="margin-top:24px;">✏️ 4-4. 이름표 쓰기 — <code>write()</code></h3>
      <div class="code-block">
<pre>t.<span class="fn">write</span>(<span class="str">"민준"</span>)</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px;">→ 아이 이름을 화면에 쓰게 하면 정말 좋아해요!</p>
    </div>
  </section>

  <!-- 5. 프로젝트 -->
  <section class="fig" style="--accent:var(--water)">
    <div class="fig-head">
      <div class="fig-emoji">⭐</div>
      <h2 class="fig-title">5. 단계별 프로젝트 (쉬운 것 → 신나는 것)</h2>
    </div>
    <p class="fig-note">각 프로젝트는 새 <code>.py</code> 파일로 만들어서 실행 버튼(▶)을 누르면 화면에 그림 창이 뜨며 바로 결과가 보여요.</p>

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
      <p style="color:var(--ink-soft); font-size:15px;">→ <i>"똑같은 걸 4번 썼지? 다음엔 마법 주문으로 줄여보자!"</i></p>

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
      <p style="color:var(--ink-soft); font-size:15px;">→ 각도만 바꿨는데 완전히 다른 모양! <i>"144도로 돌면 별이 돼요!"</i> 신기함 포인트.</p>

      <h3 style="margin-top:24px;">🟠 프로젝트 5. 무지개 나선 그리기</h3>
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">speed</span>(<span class="num">0</span>)
t.<span class="fn">pensize</span>(<span class="num">3</span>)

colors = [<span class="str">"red"</span>, <span class="str">"orange"</span>, <span class="str">"yellow"</span>, <span class="str">"green"</span>, <span class="str">"blue"</span>, <span class="str">"purple"</span>]

<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">60</span>):
    t.<span class="fn">color</span>(colors[i % <span class="num">6</span>])
    t.<span class="fn">forward</span>(i * <span class="num">3</span>)
    t.<span class="fn">right</span>(<span class="num">59</span>)

turtle.<span class="fn">done</span>()</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px;">→ 알록달록 소용돌이가 그려져서 아이들이 제일 좋아하는 프로젝트예요.</p>

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

<span class="cm"># 가운데로 이동해서 이름 쓰기</span>
t.<span class="fn">penup</span>()
t.<span class="fn">goto</span>(-<span class="num">100</span>, -<span class="num">20</span>)
t.<span class="fn">pendown</span>()
t.<span class="fn">color</span>(<span class="str">"purple"</span>)
t.<span class="fn">write</span>(<span class="str">"민준이의 그림"</span>, font=(<span class="str">"Arial"</span>, <span class="num">24</span>, <span class="str">"bold"</span>))

turtle.<span class="fn">done</span>()</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px;">→ 발표회 날 이 코드를 열어서 아이가 직접 이름 부분만 자기 이름으로 바꾸고 ▶ 버튼을 누르게 해주세요!</p>
    </div>
  </section>

  <!-- 6. 실행 & 에러 해결 -->
  <section class="fig" style="--accent:var(--c-print)">
    <div class="fig-head">
      <div class="fig-emoji">💡</div>
      <h2 class="fig-title">6. 실행하는 법 & 에러 고치기</h2>
    </div>
    <div class="board-card">
      <h3>▶ 다시 한번 정리하는 실행 방법</h3>
      <ol>
        <li>VS Code에서 <code>.py</code> 파일 열기</li>
        <li>오른쪽 위 <b>▶ 삼각형 버튼</b> 클릭</li>
        <li>새 창(터틀 그래픽 창)이 뜨면서 거북이가 그림을 그려요</li>
        <li>창을 닫으려면 그림 창을 클릭 후 <b>아무 키나 누르거나 X 버튼</b></li>
      </ol>

      <h3 style="margin-top:24px;">😅 흔한 에러, 같이 웃으며 고치기</h3>
      <table>
        <tr><th>에러 메시지</th><th>원인</th><th>해결</th></tr>
        <tr><td><code>NameError</code></td><td>오타 (예: <code>Turtel</code>)</td><td>철자 다시 확인</td></tr>
        <tr><td><code>IndentationError</code></td><td>들여쓰기(공백) 안 맞음</td><td><code>for</code> 문 안쪽 줄은 <b>꼭 4칸 띄우기</b></td></tr>
        <tr><td>창이 바로 사라짐</td><td>맨 끝에 <code>turtle.done()</code> 빠짐</td><td>마지막 줄에 추가</td></tr>
      </table>
      <div class="callout" style="margin-top:16px;">
        <b style="color:var(--c-var);">💡 아이에게:</b> <i>"컴퓨터가 삐졌나 봐! 우리 뭘 잘못 말했는지 같이 찾아볼까?"</i> 라고 하면 에러도 놀이가 돼요.
      </div>
    </div>
  </section>

  <!-- 8. 다음 단계 -->
  <section class="fig" style="--accent:var(--warn)">
    <div class="fig-head">
      <div class="fig-emoji">🚀</div>
      <h2 class="fig-title">7. 다음 단계로 넘어가고 싶다면</h2>
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
    <div class="footer-title">🐢 거북이와 즐거운 코딩 시간 되세요! 🎉</div>
  </footer>

</div>

</body>
</html>
"""

with open('/Users/cheonhyeonjun/com_gui/public/python_turtle.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated python_turtle.html")
