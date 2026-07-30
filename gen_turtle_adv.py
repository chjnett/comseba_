html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>파이썬 거북이 아트 클래스 (심화편)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans+KR:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{
    --paper:#1a1a24;
    --paper-2:#2a2a35;
    --ink:#f0f0f5;
    --ink-soft:#a0a0b0;
    --water:#ff3366;
    --water-deep:#ff0044;
    --rule:#3a3a45;
    --warn:#ffb347;

    --c-var:#00e5ff;
    --c-print:#ffea00;
    --c-math:#ff3366;
    --c-if:#b000ff;
    --c-loop:#00ff88;
    --c-list:#3366ff;

    --mono:'IBM Plex Mono', ui-monospace, monospace;
    --sans:'IBM Plex Sans KR','IBM Plex Sans', sans-serif;
    --display:'Space Grotesk', var(--sans);
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  /* Dark theme for advanced art class */
  body{ background:var(--paper); color:var(--ink); font-family:var(--sans); line-height:1.6; -webkit-font-smoothing:antialiased; overflow-x:hidden; }
  ::selection{ background:var(--water); color:#fff; }
  .wrap{ max-width:940px; margin:0 auto; padding:0 24px; }

  .topbar{ display:flex; justify-content:space-between; align-items:center; padding:16px 24px; border-bottom:1px solid var(--rule);
    font-family:var(--mono); font-size:12px; letter-spacing:.06em; color:var(--ink-soft); text-transform:uppercase; flex-wrap:wrap; gap:10px; }
  .topbar strong{ color:var(--ink); }

  .hero{ padding:60px 0 40px; text-align:center; }
  .eyebrow{ font-family:var(--mono); font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--c-var);
    display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:18px; }
  .eyebrow::before, .eyebrow::after{ content:''; width:22px; height:1px; background:var(--c-var); }
  h1{ font-family:var(--display); font-weight:700; font-size:clamp(32px,6vw,48px); line-height:1.15; margin:0 0 18px; letter-spacing:-0.01em; color:#fff; }
  h1 em{ font-style:normal; color:var(--water); text-shadow: 0 0 15px rgba(255,51,102,0.4); }
  .lede{ font-size:18px; color:var(--ink-soft); max-width:60ch; margin:0 auto; }
  .lede b{ color:var(--ink); font-weight:600; }

  .fig{ padding:52px 0; border-top:1px solid var(--rule); }
  .fig-head{ display:flex; align-items:center; gap:14px; margin-bottom:18px; flex-wrap:wrap; }
  .fig-emoji{ font-size:30px; width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center;
    background:var(--accent, var(--water)); flex:0 0 auto; color:#fff; box-shadow: 0 0 15px var(--accent); }
  .fig-title{ font-family:var(--display); font-weight:700; font-size:24px; margin:0; color:#fff; }
  .fig-note{ color:var(--ink-soft); font-size:16px; max-width:68ch; margin:0 0 20px; }

  .board-card{ background:var(--paper-2); border:1px solid var(--rule); border-radius:16px; padding:26px;
    display:flex; flex-direction:column; gap:18px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }

  /* code block dark optimized */
  .code-block{ font-family:var(--mono); font-size:14px; background:#121218; border:1px solid #000; color:#dce8e4; border-radius:12px;
    padding:18px 22px; width:100%; overflow-x:auto; }
  .code-block pre{ margin:0; white-space:pre; }
  .code-block .kw{ color:#ff79c6; font-weight:bold; }
  .code-block .fn{ color:#50fa7b; }
  .code-block .str{ color:#f1fa8c; }
  .code-block .num{ color:#bd93f9; }
  .code-block .cm{ color:#6272a4; font-style:italic; }

  .grammar-badge { display:inline-block; font-family:var(--mono); font-size:11px; padding:4px 8px; border-radius:4px; background:#1a1a24; color:var(--ink-soft); margin-bottom:6px; letter-spacing:0.04em; border: 1px solid var(--rule); }

  ul, ol { padding-left: 24px; margin: 0; }
  li { margin-bottom: 8px; }
  
  footer{ border-top:1px solid var(--rule); padding:40px 0 60px; text-align:center; }
  .footer-title{ font-family:var(--display); font-weight:700; font-size:22px; margin-bottom:14px; color:#fff; }
</style>
</head>
<body>

<div class="topbar">
  <span><strong>🐢 TURTLE ART CLASS</strong></span>
  <span>거북이 그래픽 심화 과정 & 마스터 프로젝트</span>
</div>

<div class="wrap">

  <section class="hero">
    <div class="eyebrow">Level 2. 거북이 마스터</div>
    <h1>거북이와 함께 그리는<br><em>화려한 파이썬 아트!</em> 🎨</h1>
    <p class="lede">
      기초를 마친 분들을 위한 <b>조금 더 매운맛!</b> 거북이 그래픽 클래스입니다.<br>
      함수 만들기, 랜덤 기능, 마우스 클릭 이벤트 등 진짜 "프로그래밍"다운 기술을 사용해 화려하고 멋진 그래픽 작품을 만들어봐요!
    </p>
  </section>

  <!-- 1. 나만의 마법 주문 만들기 (함수) -->
  <section class="fig" style="--accent:var(--c-var)">
    <div class="fig-head">
      <div class="fig-emoji">🪄</div>
      <h2 class="fig-title">1. 나만의 마법 주문 만들기 (함수 정의)</h2>
    </div>
    <div class="board-card">
      <div class="grammar-badge">핵심 문법: def 키워드와 매개변수</div>
      <p>매번 별을 그릴 때마다 코드를 길게 쓰기 귀찮지 않나요? <code>def</code>를 사용하면 <b>나만의 마법 주문(함수)</b>을 만들 수 있어요!</p>
      
      <div class="code-block">
<pre><span class="kw">import</span> turtle
t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">speed</span>(<span class="num">0</span>)

<span class="cm"># 'draw_star'라는 나만의 별 그리기 주문을 만들어요!</span>
<span class="cm"># 괄호 안의 'size'는 별의 크기를 조절하는 다이얼이에요.</span>
<span class="kw">def</span> <span class="fn">draw_star</span>(size):
    <span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">5</span>):
        t.<span class="fn">forward</span>(size)
        t.<span class="fn">right</span>(<span class="num">144</span>)

<span class="cm"># 이제 내가 만든 주문을 사용해볼까요?</span>
t.<span class="fn">color</span>(<span class="str">"yellow"</span>)
<span class="fn">draw_star</span>(<span class="num">100</span>)   <span class="cm"># 크기가 100인 별 뿅!</span>

t.<span class="fn">penup</span>(); t.<span class="fn">forward</span>(<span class="num">150</span>); t.<span class="fn">pendown</span>()
t.<span class="fn">color</span>(<span class="str">"pink"</span>)
<span class="fn">draw_star</span>(<span class="num">50</span>)    <span class="cm"># 크기가 50인 작은 별 뿅!</span>

turtle.<span class="fn">done</span>()</pre>
      </div>
    </div>
  </section>

  <!-- 2. 무작위의 마법 (Random) -->
  <section class="fig" style="--accent:var(--c-loop)">
    <div class="fig-head">
      <div class="fig-emoji">🎲</div>
      <h2 class="fig-title">2. 예상할 수 없는 재미! (Random 모듈)</h2>
    </div>
    <div class="board-card">
      <div class="grammar-badge">핵심 문법: import random, random.randint(), random.choice()</div>
      <p>항상 똑같이 그리면 지루하죠. 주사위를 굴리듯 컴퓨터가 <b>마음대로 색깔이나 크기를 고르게</b> 해볼까요?</p>

      <div class="code-block">
<pre><span class="kw">import</span> turtle
<span class="kw">import</span> random      <span class="cm"># 무작위 마법 모듈을 불러와요!</span>

t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">speed</span>(<span class="num">0</span>)
colors = [<span class="str">"red"</span>, <span class="str">"orange"</span>, <span class="str">"gold"</span>, <span class="str">"green"</span>, <span class="str">"blue"</span>, <span class="str">"purple"</span>]

<span class="cm"># 20개의 선을 무작위로 그려봐요</span>
<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">20</span>):
    <span class="cm"># 1. 색깔을 아무거나 뽑기</span>
    pick_color = random.<span class="fn">choice</span>(colors)
    t.<span class="fn">color</span>(pick_color)
    
    <span class="cm"># 2. 길이를 50에서 150 사이로 아무거나 뽑기</span>
    length = random.<span class="fn">randint</span>(<span class="num">50</span>, <span class="num">150</span>)
    t.<span class="fn">forward</span>(length)
    
    <span class="cm"># 3. 뒤로 돌아오고, 각도도 아무거나 틀어보기</span>
    t.<span class="fn">backward</span>(length)
    angle = random.<span class="fn">randint</span>(<span class="num">10</span>, <span class="num">350</span>)
    t.<span class="fn">right</span>(angle)

turtle.<span class="fn">done</span>()</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px; margin-top:8px;">→ 실행할 때마다 거북이가 완전히 다른 불꽃놀이를 그려낼 거예요!</p>
    </div>
  </section>

  <!-- 3. 마우스 클릭 (Event) -->
  <section class="fig" style="--accent:var(--c-list)">
    <div class="fig-head">
      <div class="fig-emoji">🖱️</div>
      <h2 class="fig-title">3. 거북이와 상호작용하기 (마우스 이벤트)</h2>
    </div>
    <div class="board-card">
      <div class="grammar-badge">핵심 문법: 화면 이벤트 처리 (onscreenclick)</div>
      <p>그냥 보기만 하는 건 끝! 이제 <b>우리가 마우스를 클릭하는 곳</b>으로 거북이가 순간이동해서 그림을 그리게 만들 수 있어요.</p>

      <div class="code-block">
<pre><span class="kw">import</span> turtle
<span class="kw">import</span> random

screen = turtle.<span class="fn">Screen</span>()
screen.<span class="fn">bgcolor</span>(<span class="str">"black"</span>)  <span class="cm"># 밤하늘처럼 배경을 까맣게!</span>

t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">speed</span>(<span class="num">0</span>)
t.<span class="fn">hideturtle</span>()         <span class="cm"># 거북이 몸통은 숨겨요</span>

<span class="cm"># 클릭할 때 실행될 마법 주문(함수) - (x, y) 좌표를 받아요!</span>
<span class="kw">def</span> <span class="fn">draw_stamp</span>(x, y):
    t.<span class="fn">penup</span>()
    t.<span class="fn">goto</span>(x, y)       <span class="cm"># 마우스를 클릭한 (x, y) 위치로 순간이동!</span>
    t.<span class="fn">pendown</span>()
    
    colors = [<span class="str">"#ff3366"</span>, <span class="str">"#00e5ff"</span>, <span class="str">"#00ff88"</span>, <span class="str">"#ffea00"</span>]
    t.<span class="fn">color</span>(random.<span class="fn">choice</span>(colors))
    
    <span class="cm"># 무작위 크기의 예쁜 나선 그리기</span>
    size = random.<span class="fn">randint</span>(<span class="num">10</span>, <span class="num">40</span>)
    <span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(size):
        t.<span class="fn">forward</span>(i * <span class="num">2</span>)
        t.<span class="fn">right</span>(<span class="num">89</span>)

<span class="cm"># 화면을 클릭하면 'draw_stamp' 주문을 실행해달라고 등록해요</span>
screen.<span class="fn">onscreenclick</span>(draw_stamp)

<span class="cm"># 거북이가 마우스를 기다리도록 하는 마법 (done 대신 사용)</span>
screen.<span class="fn">mainloop</span>()</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:15px; margin-top:8px;">→ 이제 까만 창이 뜨면 <b>아무 곳이나 마우스로 콕콕 클릭</b>해보세요. 네온사인 아트가 그려집니다!</p>
    </div>
  </section>

  <!-- 4. 마스터 프로젝트 -->
  <section class="fig" style="--accent:var(--water)">
    <div class="fig-head">
      <div class="fig-emoji">💎</div>
      <h2 class="fig-title">4. 아트 마스터 프로젝트</h2>
    </div>
    
    <div class="board-card">
      <h3>🌀 프로젝트 1: 신비로운 만다라 (Spirograph)</h3>
      <p>조금씩 각도를 틀어가며 원을 수십 번 겹쳐 그리면, 수학적으로 완벽하고 아름다운 무늬가 탄생합니다.</p>
      <div class="code-block">
<pre><span class="kw">import</span> turtle

t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">speed</span>(<span class="num">0</span>)
t.<span class="fn">pensize</span>(<span class="num">2</span>)
turtle.<span class="fn">bgcolor</span>(<span class="str">"black"</span>)

colors = [<span class="str">"#ff0044"</span>, <span class="str">"#ff3366"</span>, <span class="str">"#ff6699"</span>, <span class="str">"#ff99cc"</span>, <span class="str">"#ffccff"</span>, <span class="str">"#ffffff"</span>]

<span class="cm"># 36번 반복해서 둥근 만다라 완성</span>
<span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="num">36</span>):
    t.<span class="fn">color</span>(colors[i % <span class="num">6</span>])
    t.<span class="fn">circle</span>(<span class="num">100</span>)      <span class="cm"># 반지름 100인 원 그리기</span>
    t.<span class="fn">right</span>(<span class="num">10</span>)        <span class="cm"># 10도씩 살짝 비틀기</span>

turtle.<span class="fn">done</span>()</pre>
      </div>

      <h3 style="margin-top:40px;">🌲 프로젝트 2: 프랙탈 눈꽃송이 (Fractal)</h3>
      <p>코딩의 꽃! 규칙을 반복해서 얼음 결정 같은 복잡한 기하학적 도형을 그려봐요.</p>
      <div class="code-block">
<pre><span class="kw">import</span> turtle

t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">speed</span>(<span class="num">0</span>)
turtle.<span class="fn">bgcolor</span>(<span class="str">"#001133"</span>) <span class="cm"># 깊은 밤하늘 색</span>
t.<span class="fn">color</span>(<span class="str">"#00e5ff"</span>)       <span class="cm"># 형광 하늘색</span>

<span class="cm"># 눈꽃의 한쪽 가지를 그리는 마법 주문</span>
<span class="kw">def</span> <span class="fn">draw_branch</span>(length):
    <span class="kw">if</span> length &lt; <span class="num">10</span>:      <span class="cm"># 가지가 너무 짧아지면 멈춰! (조건문)</span>
        <span class="kw">return</span>
    
    t.<span class="fn">forward</span>(length)
    
    t.<span class="fn">left</span>(<span class="num">30</span>)
    <span class="fn">draw_branch</span>(length * <span class="num">0.7</span>) <span class="cm"># 자기 자신을 더 작은 크기로 다시 부름! (재귀)</span>
    
    t.<span class="fn">right</span>(<span class="num">60</span>)
    <span class="fn">draw_branch</span>(length * <span class="num">0.7</span>)
    
    t.<span class="fn">left</span>(<span class="num">30</span>)
    t.<span class="fn">backward</span>(length)

<span class="cm"># 화면 정중앙 아래로 내려와서 시작</span>
t.<span class="fn">penup</span>()
t.<span class="fn">goto</span>(<span class="num">0</span>, -<span class="num">150</span>)
t.<span class="fn">pendown</span>()
t.<span class="fn">left</span>(<span class="num">90</span>)

<span class="cm"># 6개의 거대한 가지를 그려 눈꽃을 완성해요</span>
<span class="kw">for</span> _ <span class="kw">in</span> <span class="fn">range</span>(<span class="num">6</span>):
    <span class="fn">draw_branch</span>(<span class="num">80</span>)
    t.<span class="fn">right</span>(<span class="num">60</span>)

t.<span class="fn">hideturtle</span>()
turtle.<span class="fn">done</span>()</pre>
      </div>

      <h3 style="margin-top:40px;">🎨 프로젝트 3: 나만의 거북이 그림판</h3>
      <p>마우스를 드래그해서 자유롭게 그림을 그려봐요! 파이썬 터틀을 진짜 마우스 그림판처럼 사용할 수 있습니다.</p>
      <div class="code-block">
<pre><span class="kw">import</span> turtle

<span class="cm"># 1. 화면 및 터틀 기본 설정</span>
screen = turtle.<span class="fn">Screen</span>()
screen.<span class="fn">title</span>(<span class="str">"마우스 따라 그리기"</span>)

t = turtle.<span class="fn">Turtle</span>()
t.<span class="fn">shape</span>(<span class="str">"circle"</span>)  <span class="cm"># 마우스 포인터 모양</span>
t.<span class="fn">pensize</span>(<span class="num">3</span>)       <span class="cm"># 선 굵기</span>
t.<span class="fn">speed</span>(<span class="num">0</span>)         <span class="cm"># 그리기 속도 (0은 최고 속도)</span>

<span class="cm"># 2. 화면의 빈 곳을 클릭했을 때 실행할 함수 (펜을 들고 이동)</span>
<span class="kw">def</span> <span class="fn">move_to</span>(x, y):
    t.<span class="fn">penup</span>()      <span class="cm"># 선이 그려지지 않게 펜 들기</span>
    t.<span class="fn">goto</span>(x, y)   <span class="cm"># 클릭한 좌표로 이동</span>
    t.<span class="fn">pendown</span>()    <span class="cm"># 펜 내리기</span>

<span class="cm"># 3. 마우스를 드래그할 때 실행할 함수 (선을 그리며 이동)</span>
<span class="kw">def</span> <span class="fn">draw</span>(x, y):
    t.<span class="fn">goto</span>(x, y)   <span class="cm"># 마우스가 움직이는 좌표로 터틀 이동</span>

<span class="cm"># 4. 오른쪽 클릭 시 화면을 지우는 함수</span>
<span class="kw">def</span> <span class="fn">clear_screen</span>(x, y):
    t.<span class="fn">clear</span>()

<span class="cm"># 5. 마우스 이벤트 연결</span>
screen.<span class="fn">onscreenclick</span>(move_to, <span class="num">1</span>)  <span class="cm"># 왼쪽 클릭(1): 해당 위치로 이동</span>
t.<span class="fn">ondrag</span>(draw)                    <span class="cm"># 터틀 드래그: 선 그리기</span>
screen.<span class="fn">onscreenclick</span>(clear_screen, <span class="num">3</span>) <span class="cm"># 오른쪽 클릭(3): 화면 지우기</span>

<span class="cm"># 프로그램 유지</span>
screen.<span class="fn">mainloop</span>()</pre>
      </div>
    </div>
  </section>

  <footer>
    <div class="footer-title">🎨 멋진 파이썬 아티스트가 되신 것을 축하합니다!</div>
    <p style="color:var(--ink-soft);">기초부터 심화까지, 거북이로 그리지 못할 그림은 없어요.</p>
  </footer>

</div>

</body>
</html>
"""

with open('/Users/cheonhyeonjun/com_gui/public/python_turtle_adv.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated python_turtle_adv.html")
