html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>파이썬 게임 만들기 (Pygame)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans+KR:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{
    --paper:#12121a;
    --paper-2:#1e1e2c;
    --ink:#f0f0f5;
    --ink-soft:#8a8a9e;
    --water:#00ffcc;
    --water-deep:#00ccaa;
    --rule:#2c2c3e;
    
    --c-var:#ff00ff;
    --c-loop:#00ffcc;
    --c-list:#ffcc00;
    --c-def:#ff3366;

    --mono:'IBM Plex Mono', ui-monospace, monospace;
    --sans:'IBM Plex Sans KR','IBM Plex Sans', sans-serif;
    --display:'Space Grotesk', var(--sans);
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  /* Arcade Dark theme */
  body{ background:var(--paper); color:var(--ink); font-family:var(--sans); line-height:1.6; -webkit-font-smoothing:antialiased; overflow-x:hidden; }
  ::selection{ background:var(--c-var); color:#fff; }
  .wrap{ max-width:940px; margin:0 auto; padding:0 24px; }

  .topbar{ display:flex; justify-content:space-between; align-items:center; padding:16px 24px; border-bottom:1px solid var(--rule);
    font-family:var(--mono); font-size:12px; letter-spacing:.06em; color:var(--ink-soft); text-transform:uppercase; flex-wrap:wrap; gap:10px; }
  .topbar strong{ color:var(--ink); }

  .hero{ padding:60px 0 40px; text-align:center; }
  .eyebrow{ font-family:var(--mono); font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--c-var);
    display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:18px; }
  .eyebrow::before, .eyebrow::after{ content:''; width:22px; height:1px; background:var(--c-var); }
  h1{ font-family:var(--display); font-weight:700; font-size:clamp(32px,6vw,48px); line-height:1.15; margin:0 0 18px; letter-spacing:-0.01em; color:#fff; }
  h1 em{ font-style:normal; color:var(--water); text-shadow: 0 0 15px rgba(0,255,204,0.4); }
  .lede{ font-size:18px; color:var(--ink-soft); max-width:60ch; margin:0 auto; }
  .lede b{ color:var(--ink); font-weight:600; }

  .fig{ padding:52px 0; border-top:1px solid var(--rule); }
  .fig-head{ display:flex; align-items:center; gap:14px; margin-bottom:18px; flex-wrap:wrap; }
  .fig-emoji{ font-size:30px; width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center;
    background:var(--accent); flex:0 0 auto; color:#12121a; box-shadow: 0 0 15px var(--accent); }
  .fig-title{ font-family:var(--display); font-weight:700; font-size:24px; margin:0; color:#fff; }
  .fig-note{ color:var(--ink-soft); font-size:16px; max-width:68ch; margin:0 0 20px; }

  .board-card{ background:var(--paper-2); border:1px solid var(--rule); border-radius:16px; padding:26px;
    display:flex; flex-direction:column; gap:18px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }

  /* code block neon optimized */
  .code-block{ font-family:var(--mono); font-size:14px; background:#0c0c11; border:1px solid #000; color:#dce8e4; border-radius:12px;
    padding:18px 22px; width:100%; overflow-x:auto; }
  .code-block pre{ margin:0; white-space:pre; }
  .code-block .kw{ color:#ff79c6; font-weight:bold; }
  .code-block .fn{ color:#50fa7b; }
  .code-block .str{ color:#f1fa8c; }
  .code-block .num{ color:#bd93f9; }
  .code-block .cm{ color:#6272a4; font-style:italic; }
  .copy-btn { position:absolute; top:12px; right:12px; background:var(--paper-2); color:var(--ink-soft); border:1px solid var(--rule); border-radius:6px; padding:4px 10px; font-size:11px; font-family:var(--sans); cursor:pointer; transition:all 0.2s; z-index:10;}
  .copy-btn:hover { background:var(--rule); color:#fff; }

  .grammar-badge { display:inline-block; font-family:var(--mono); font-size:11px; padding:4px 8px; border-radius:4px; background:#12121a; color:var(--ink-soft); margin-bottom:6px; letter-spacing:0.04em; border: 1px solid var(--rule); }

  ul, ol { padding-left: 24px; margin: 0; }
  li { margin-bottom: 8px; }
  
  footer{ border-top:1px solid var(--rule); padding:40px 0 60px; text-align:center; }
  .footer-title{ font-family:var(--display); font-weight:700; font-size:22px; margin-bottom:14px; color:#fff; }
</style>
</head>
<body>

<div class="topbar">
  <span><strong>🕹️ PYGAME CLASS</strong></span>
  <span>진짜 게임을 만들어보자!</span>
</div>

<div class="wrap">

  <section class="hero">
    <div class="eyebrow">Level 3. 게임 마스터</div>
    <h1>파이썬으로 만드는<br><em>나만의 오락실 게임!</em> 👾</h1>
    <p class="lede">
      터틀 그래픽을 넘어, 진짜 상용 게임도 만들 수 있는 <b>Pygame(파이게임)</b>의 세계로 오신 것을 환영합니다!<br>
      초당 수십 번 화면을 다시 그리며 부드럽게 움직이는 2D 게임의 기초를 배워보아요.
    </p>
  </section>

  <!-- 0. 설치 -->
  <section class="fig" style="--accent:var(--water)">
    <div class="fig-head">
      <div class="fig-emoji">📦</div>
      <h2 class="fig-title">0. 게임 만들기 준비물 (Pygame 설치)</h2>
    </div>
    <div class="board-card">
      <p>Pygame은 파이썬에 기본으로 들어있지 않아서 한 번만 따로 설치해줘야 해요. VS Code 하단의 <b>터미널(Terminal)</b> 창을 열고 아래 명령어를 입력해 주세요.</p>
      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre>pip install pygame</pre>
      </div>
      <p style="color:var(--ink-soft); font-size:14px; margin-top:0;">* <b>맥(Mac)</b> 사용자는 <code>pip3 install pygame</code>이라고 입력해야 할 수도 있어요!</p>
    </div>
  </section>

  <!-- 1. 파이게임의 심장 -->
  <section class="fig" style="--accent:var(--c-var)">
    <div class="fig-head">
      <div class="fig-emoji">❤️</div>
      <h2 class="fig-title">1. 게임의 심장 (게임 루프 만들기)</h2>
    </div>
    <div class="board-card">
      <div class="grammar-badge">핵심 개념: pygame.init(), while 루프, Event</div>
      <p>모든 게임은 "화면 지우기 👉 그림 그리기 👉 키보드 입력 받기"를 1초에 60번씩 엄청나게 빠르게 반복합니다. 이것을 <b>게임 루프(Game Loop)</b>라고 불러요!</p>
      
      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre><span class="kw">import</span> pygame
<span class="kw">import</span> sys

pygame.<span class="fn">init</span>()  <span class="cm"># 파이게임 엔진 시동 걸기!</span>

<span class="cm"># 1. 화면(도화지) 설정</span>
screen = pygame.<span class="fn">display</span>.<span class="fn">set_mode</span>((<span class="num">800</span>, <span class="num">600</span>)) <span class="cm"># 가로 800, 세로 600</span>
pygame.<span class="fn">display</span>.<span class="fn">set_caption</span>(<span class="str">"내 첫 번째 게임 창"</span>)
clock = pygame.time.<span class="fn">Clock</span>()  <span class="cm"># 시간 관리자</span>

<span class="cm"># 2. 게임 루프 (심장 박동)</span>
<span class="kw">while True</span>:
    <span class="cm"># (1) 이벤트 처리: 플레이어가 무엇을 했는지 확인</span>
    <span class="kw">for</span> event <span class="kw">in</span> pygame.event.<span class="fn">get</span>():
        <span class="kw">if</span> event.type == pygame.<span class="fn">QUIT</span>: <span class="cm"># 창 닫기[X] 버튼을 눌렀다면?</span>
            pygame.<span class="fn">quit</span>()
            sys.<span class="fn">exit</span>()              <span class="cm"># 게임 완전 종료!</span>

    <span class="cm"># (2) 화면 그리기 (일단 까만색으로 채우기)</span>
    screen.<span class="fn">fill</span>((<span class="num">0</span>, <span class="num">0</span>, <span class="num">0</span>)) <span class="cm"># (R, G, B) 색상 코드: 까만색</span>

    <span class="cm"># (3) 새로 그린 화면 업데이트해서 보여주기</span>
    pygame.<span class="fn">display</span>.<span class="fn">update</span>()
    
    <span class="cm"># (4) 1초에 60번만 실행되도록 속도 조절 (60 FPS)</span>
    clock.<span class="fn">tick</span>(<span class="num">60</span>)</pre>
      </div>
    </div>
  </section>

  <!-- 2. 캐릭터 그리기 -->
  <section class="fig" style="--accent:var(--c-loop)">
    <div class="fig-head">
      <div class="fig-emoji">🛸</div>
      <h2 class="fig-title">2. 화면에 내 캐릭터 나타나기!</h2>
    </div>
    <div class="board-card">
      <div class="grammar-badge">핵심 개념: pygame.draw, RGB 색상상</div>
      <p>아무것도 없는 까만 창에 멋진 형광색 우주선(동그라미)을 그려볼까요? 화면을 채우고(`fill`) 업데이트(`update`) 하는 사이에 코드를 넣어야 해요!</p>

      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre><span class="kw">import</span> pygame, sys
pygame.<span class="fn">init</span>()
screen = pygame.<span class="fn">display</span>.<span class="fn">set_mode</span>((<span class="num">800</span>, <span class="num">600</span>))
clock = pygame.time.<span class="fn">Clock</span>()

<span class="kw">while True</span>:
    <span class="kw">for</span> event <span class="kw">in</span> pygame.event.<span class="fn">get</span>():
        <span class="kw">if</span> event.type == pygame.<span class="fn">QUIT</span>:
            pygame.<span class="fn">quit</span>(); sys.<span class="fn">exit</span>()

    <span class="cm"># 1. 배경을 먼저 까맣게 칠하기</span>
    screen.<span class="fn">fill</span>((<span class="num">0</span>, <span class="num">0</span>, <span class="num">0</span>))

    <span class="cm"># 2. 형광 청록색 원 그리기!</span>
    <span class="cm"># pygame.draw.circle(어디에, 무슨색, (x, y 좌표), 크기)</span>
    pygame.draw.<span class="fn">circle</span>(screen, (<span class="num">0</span>, <span class="num">255</span>, <span class="num">204</span>), (<span class="num">400</span>, <span class="num">300</span>), <span class="num">50</span>)
    
    <span class="cm"># 3. 빨간색 네모 그리기!</span>
    <span class="cm"># pygame.draw.rect(어디에, 무슨색, [x, y, 가로, 세로])</span>
    pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">255</span>, <span class="num">50</span>, <span class="num">50</span>), [<span class="num">100</span>, <span class="num">100</span>, <span class="num">40</span>, <span class="num">40</span>])

    pygame.<span class="fn">display</span>.<span class="fn">update</span>()
    clock.<span class="fn">tick</span>(<span class="num">60</span>)</pre>
      </div>
    </div>
  </section>

  <!-- 3. 키보드로 조종하기 -->
  <section class="fig" style="--accent:var(--c-list)">
    <div class="fig-head">
      <div class="fig-emoji">🎮</div>
      <h2 class="fig-title">3. 방향키로 내 캐릭터 조종하기</h2>
    </div>
    <div class="board-card">
      <div class="grammar-badge">핵심 개념: 변수 활용, pygame.key.get_pressed()</div>
      <p>도형이 멈춰있으면 재미가 없죠! 플레이어의 `x` 좌표, `y` 좌표를 <b>변수</b>로 만들고, 방향키를 누를 때마다 이 좌표를 5씩 바꿔주면 캐릭터가 움직입니다.</p>

      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre><span class="kw">import</span> pygame, sys
pygame.<span class="fn">init</span>()
screen = pygame.<span class="fn">display</span>.<span class="fn">set_mode</span>((<span class="num">800</span>, <span class="num">600</span>))
clock = pygame.time.<span class="fn">Clock</span>()

<span class="cm"># (게임 루프 밖) 캐릭터의 시작 위치 변수</span>
player_x = <span class="num">400</span>
player_y = <span class="num">300</span>
player_speed = <span class="num">5</span>

<span class="kw">while True</span>:
    <span class="kw">for</span> event <span class="kw">in</span> pygame.event.<span class="fn">get</span>():
        <span class="kw">if</span> event.type == pygame.<span class="fn">QUIT</span>:
            pygame.<span class="fn">quit</span>(); sys.<span class="fn">exit</span>()

    <span class="cm"># ★ 키보드 눌림 확인하기 ★</span>
    keys = pygame.key.<span class="fn">get_pressed</span>()
    <span class="kw">if</span> keys[pygame.<span class="fn">K_LEFT</span>]:  <span class="cm"># 왼쪽 화살표</span>
        player_x -= player_speed
    <span class="kw">if</span> keys[pygame.<span class="fn">K_RIGHT</span>]: <span class="cm"># 오른쪽 화살표</span>
        player_x += player_speed
    <span class="kw">if</span> keys[pygame.<span class="fn">K_UP</span>]:    <span class="cm"># 위쪽 화살표</span>
        player_y -= player_speed
    <span class="kw">if</span> keys[pygame.<span class="fn">K_DOWN</span>]:  <span class="cm"># 아래쪽 화살표</span>
        player_y += player_speed

    screen.<span class="fn">fill</span>((<span class="num">0</span>, <span class="num">0</span>, <span class="num">0</span>))
    
    <span class="cm"># 변수 player_x, player_y를 위치로 사용해 그리기!</span>
    pygame.draw.<span class="fn">circle</span>(screen, (<span class="num">0</span>, <span class="num">255</span>, <span class="num">204</span>), (player_x, player_y), <span class="num">30</span>)
    
    pygame.<span class="fn">display</span>.<span class="fn">update</span>()
    clock.<span class="fn">tick</span>(<span class="num">60</span>)</pre>
      </div>
    </div>
  </section>

  <!-- 4. 마스터 프로젝트 (별 잡기 게임) -->
  <section class="fig" style="--accent:var(--c-def)">
    <div class="fig-head">
      <div class="fig-emoji">⭐</div>
      <h2 class="fig-title">4. 게임 마스터 프로젝트: 별 잡기!</h2>
    </div>
    
    <div class="board-card">
      <p>드디어 완성된 하나의 게임입니다! 좌우 방향키로 플레이어(초록색 네모)를 움직여 하늘에서 떨어지는 진짜 별(⭐) 모양을 잡으세요. 10점을 모으면 승리!</p>
      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre><span class="kw">import</span> pygame, sys, random

pygame.<span class="fn">init</span>()
screen = pygame.<span class="fn">display</span>.<span class="fn">set_mode</span>((<span class="num">600</span>, <span class="num">800</span>))
clock = pygame.time.<span class="fn">Clock</span>()
font = pygame.font.<span class="fn">SysFont</span>(<span class="str">"malgungothic"</span>, <span class="num">36</span>) <span class="cm"># 글꼴 설정</span>

<span class="cm"># 별(⭐)을 예쁘게 그리는 마법 함수</span>
<span class="kw">def</span> <span class="fn">draw_star</span>(surface, x, y):
    <span class="cm"># 꼭짓점 10개의 좌표 계산</span>
    points = [
        (x+<span class="num">25</span>, y), (x+<span class="num">33</span>, y+<span class="num">17</span>), (x+<span class="num">50</span>, y+<span class="num">17</span>),
        (x+<span class="num">35</span>, y+<span class="num">30</span>), (x+<span class="num">40</span>, y+<span class="num">50</span>), (x+<span class="num">25</span>, y+<span class="num">37</span>),
        (x+<span class="num">10</span>, y+<span class="num">50</span>), (x+<span class="num">15</span>, y+<span class="num">30</span>), (x, y+<span class="num">17</span>), (x+<span class="num">17</span>, y+<span class="num">17</span>)
    ]
    pygame.draw.<span class="fn">polygon</span>(surface, (<span class="num">255</span>, <span class="num">255</span>, <span class="num">0</span>), points)

<span class="cm"># 플레이어(바구니) 설정</span>
player_x = <span class="num">250</span>
player_y = <span class="num">700</span>
score = <span class="num">0</span>

<span class="cm"># 떨어지는 별 설정</span>
star_x = random.<span class="fn">randint</span>(<span class="num">0</span>, <span class="num">550</span>)
star_y = -<span class="num">50</span>

<span class="kw">while True</span>:
    <span class="kw">for</span> event <span class="kw">in</span> pygame.event.<span class="fn">get</span>():
        <span class="kw">if</span> event.type == pygame.<span class="fn">QUIT</span>:
            pygame.<span class="fn">quit</span>(); sys.<span class="fn">exit</span>()

    <span class="cm"># 1. 플레이어 이동</span>
    keys = pygame.key.<span class="fn">get_pressed</span>()
    <span class="kw">if</span> keys[pygame.<span class="fn">K_LEFT</span>] <span class="kw">and</span> player_x &gt; <span class="num">0</span>:
        player_x -= <span class="num">7</span>
    <span class="kw">if</span> keys[pygame.<span class="fn">K_RIGHT</span>] <span class="kw">and</span> player_x &lt; <span class="num">500</span>:
        player_x += <span class="num">7</span>

    <span class="cm"># 2. 별 떨어지기</span>
    star_y += <span class="num">5</span>
    <span class="kw">if</span> star_y &gt; <span class="num">800</span>: <span class="cm"># 바닥에 닿으면 다시 위로</span>
        star_y = -<span class="num">50</span>
        star_x = random.<span class="fn">randint</span>(<span class="num">0</span>, <span class="num">550</span>)

    <span class="cm"># 3. 별을 잡았는지(충돌) 확인</span>
    <span class="kw">if</span> player_y &lt; star_y+<span class="num">50</span> <span class="kw">and</span> player_x-<span class="num">50</span> &lt; star_x &lt; player_x+<span class="num">100</span>:
        score += <span class="num">1</span>
        star_y = -<span class="num">50</span>
        star_x = random.<span class="fn">randint</span>(<span class="num">0</span>, <span class="num">550</span>)

    <span class="cm"># 4. 화면 그리기</span>
    screen.<span class="fn">fill</span>((<span class="num">20</span>, <span class="num">20</span>, <span class="num">40</span>)) <span class="cm"># 남색 밤하늘</span>
    
    <span class="cm"># 플레이어(초록 네모)와 별(⭐) 그리기</span>
    pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">0</span>, <span class="num">255</span>, <span class="num">100</span>), [player_x, player_y, <span class="num">100</span>, <span class="num">20</span>])
    <span class="fn">draw_star</span>(screen, star_x, star_y)
    
    <span class="cm"># 점수 텍스트 표시</span>
    score_text = font.<span class="fn">render</span>(<span class="str">f"점수: {score}"</span>, <span class="kw">True</span>, (<span class="num">255</span>, <span class="num">255</span>, <span class="num">255</span>))
    screen.<span class="fn">blit</span>(score_text, (<span class="num">10</span>, <span class="num">10</span>))

    pygame.<span class="fn">display</span>.<span class="fn">update</span>()
    clock.<span class="fn">tick</span>(<span class="num">60</span>)</pre>
      </div>
    </div>
  </section>

  <!-- 5. 프로젝트: 점핑 버드 -->
  <section class="fig" style="--accent:var(--c-var)">
    <div class="fig-head">
      <div class="fig-emoji">🦅</div>
      <h2 class="fig-title">5. 프로젝트: 점핑 버드 (중력과 점프)</h2>
    </div>
    
    <div class="board-card">
      <p>스페이스바를 누르면 새(플레이어)가 위로 점프하고, 가만히 있으면 중력 때문에 아래로 떨어집니다. 오른쪽에서 다가오는 기둥을 피하며 최대한 오래 살아남아 보세요!</p>
      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre><span class="kw">import</span> pygame, sys, random
pygame.<span class="fn">init</span>()
screen = pygame.<span class="fn">display</span>.<span class="fn">set_mode</span>((<span class="num">800</span>, <span class="num">600</span>))
clock = pygame.time.<span class="fn">Clock</span>()
font = pygame.font.<span class="fn">SysFont</span>(<span class="str">"malgungothic"</span>, <span class="num">36</span>)

<span class="cm"># 플레이어(새) 설정</span>
player_x = <span class="num">100</span>
player_y = <span class="num">300</span>
player_velocity = <span class="num">0</span>    <span class="cm"># 현재 떨어지는 속도</span>
gravity = <span class="num">0.5</span>          <span class="cm"># 중력 (계속 아래로 당기는 힘)</span>

<span class="cm"># 장애물(기둥) 설정</span>
pipe_x = <span class="num">800</span>
pipe_gap = <span class="num">150</span>         <span class="cm"># 기둥 사이의 빈 공간 크기</span>
pipe_top_height = random.<span class="fn">randint</span>(<span class="num">100</span>, <span class="num">350</span>)
score = <span class="num">0</span>

<span class="kw">while True</span>:
    <span class="kw">for</span> event <span class="kw">in</span> pygame.event.<span class="fn">get</span>():
        <span class="kw">if</span> event.type == pygame.<span class="fn">QUIT</span>:
            pygame.<span class="fn">quit</span>(); sys.<span class="fn">exit</span>()
        <span class="kw">if</span> event.type == pygame.<span class="fn">KEYDOWN</span>:
            <span class="kw">if</span> event.key == pygame.<span class="fn">K_SPACE</span>: <span class="cm"># 스페이스바를 누르면</span>
                player_velocity = -<span class="num">8</span>       <span class="cm"># 위로 점프! (y가 줄어들면 위로 감)</span>

    <span class="cm"># 1. 중력 적용 및 새 이동</span>
    player_velocity += gravity
    player_y += player_velocity

    <span class="cm"># 2. 기둥 이동</span>
    pipe_x -= <span class="num">5</span>
    <span class="kw">if</span> pipe_x &lt; -<span class="num">50</span>:  <span class="cm"># 기둥이 화면 왼쪽 밖으로 나가면 다시 오른쪽에서 등장</span>
        pipe_x = <span class="num">800</span>
        pipe_top_height = random.<span class="fn">randint</span>(<span class="num">100</span>, <span class="num">350</span>)
        score += <span class="num">1</span>

    <span class="cm"># 3. 충돌 검사 (바닥에 닿거나 기둥에 부딪히면 끝!)</span>
    <span class="kw">if</span> player_y &gt; <span class="num">600</span> <span class="kw">or</span> player_y &lt; <span class="num">0</span>:
        score = <span class="num">0</span>; player_y = <span class="num">300</span>; pipe_x = <span class="num">800</span> <span class="cm"># 리셋</span>
    
    <span class="cm"># 윗 기둥과 충돌</span>
    <span class="kw">if</span> pipe_x &lt; player_x + <span class="num">30</span> <span class="kw">and</span> pipe_x + <span class="num">50</span> &gt; player_x <span class="kw">and</span> player_y &lt; pipe_top_height:
        score = <span class="num">0</span>; player_y = <span class="num">300</span>; pipe_x = <span class="num">800</span>
    <span class="cm"># 아래 기둥과 충돌</span>
    <span class="kw">if</span> pipe_x &lt; player_x + <span class="num">30</span> <span class="kw">and</span> pipe_x + <span class="num">50</span> &gt; player_x <span class="kw">and</span> player_y + <span class="num">30</span> &gt; pipe_top_height + pipe_gap:
        score = <span class="num">0</span>; player_y = <span class="num">300</span>; pipe_x = <span class="num">800</span>

    <span class="cm"># 4. 화면 그리기</span>
    screen.<span class="fn">fill</span>((<span class="num">135</span>, <span class="num">206</span>, <span class="num">235</span>)) <span class="cm"># 하늘색 배경</span>
    
    <span class="cm"># 플레이어(새) 그리기</span>
    pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">255</span>, <span class="num">200</span>, <span class="num">0</span>), [player_x, player_y, <span class="num">30</span>, <span class="num">30</span>])
    <span class="cm"># 기둥 그리기 (위, 아래)</span>
    pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">34</span>, <span class="num">139</span>, <span class="num">34</span>), [pipe_x, <span class="num">0</span>, <span class="num">50</span>, pipe_top_height])
    pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">34</span>, <span class="num">139</span>, <span class="num">34</span>), [pipe_x, pipe_top_height + pipe_gap, <span class="num">50</span>, <span class="num">600</span>])
    
    screen.<span class="fn">blit</span>(font.<span class="fn">render</span>(<span class="str">f"점수: {score}"</span>, <span class="kw">True</span>, (<span class="num">0</span>, <span class="num">0</span>, <span class="num">0</span>)), (<span class="num">10</span>, <span class="num">10</span>))
    pygame.<span class="fn">display</span>.<span class="fn">update</span>()
    clock.<span class="fn">tick</span>(<span class="num">60</span>)</pre>
      </div>
    </div>
  </section>

  <!-- 6. 프로젝트: 마우스 핑퐁 -->
  <section class="fig" style="--accent:var(--water-deep)">
    <div class="fig-head">
      <div class="fig-emoji">🏓</div>
      <h2 class="fig-title">6. 프로젝트: 마우스 핑퐁 (반사각과 마우스)</h2>
    </div>
    
    <div class="board-card">
      <p>키보드 대신 <b>마우스</b>로 패들(막대기)을 움직여 튕겨 다니는 공을 살려내는 게임입니다. 공이 벽이나 막대기에 부딪히면 반대로 튕겨 나가는 수학 로직이 핵심입니다!</p>
      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre><span class="kw">import</span> pygame, sys
pygame.<span class="fn">init</span>()
screen = pygame.<span class="fn">display</span>.<span class="fn">set_mode</span>((<span class="num">800</span>, <span class="num">600</span>))
clock = pygame.time.<span class="fn">Clock</span>()
pygame.mouse.<span class="fn">set_visible</span>(<span class="kw">False</span>) <span class="cm"># 진짜 마우스 커서 숨기기</span>

<span class="cm"># 공 설정</span>
ball_x = <span class="num">400</span>; ball_y = <span class="num">300</span>
ball_dx = <span class="num">5</span>;  ball_dy = -<span class="num">5</span>    <span class="cm"># 공이 이동하는 방향과 속도</span>

<span class="kw">while True</span>:
    <span class="kw">for</span> event <span class="kw">in</span> pygame.event.<span class="fn">get</span>():
        <span class="kw">if</span> event.type == pygame.<span class="fn">QUIT</span>:
            pygame.<span class="fn">quit</span>(); sys.<span class="fn">exit</span>()

    <span class="cm"># 1. 마우스 위치 가져와서 패들 움직이기</span>
    mouse_x, mouse_y = pygame.mouse.<span class="fn">get_pos</span>()
    paddle_x = mouse_x - <span class="num">50</span> <span class="cm"># 마우스가 패들의 중앙에 오게 조정</span>

    <span class="cm"># 2. 공 움직이기</span>
    ball_x += ball_dx
    ball_y += ball_dy

    <span class="cm"># 3. 벽에 부딪히면 튕기기 (방향 반전)</span>
    <span class="kw">if</span> ball_x &lt;= <span class="num">0</span> <span class="kw">or</span> ball_x &gt;= <span class="num">780</span>: <span class="cm"># 왼쪽/오른쪽 벽</span>
        ball_dx = -ball_dx
    <span class="kw">if</span> ball_y &lt;= <span class="num">0</span>:                  <span class="cm"># 천장</span>
        ball_dy = -ball_dy
    <span class="kw">if</span> ball_y &gt;= <span class="num">600</span>:                <span class="cm"># 바닥에 떨어지면 게임 오버(초기화)</span>
        ball_x = <span class="num">400</span>; ball_y = <span class="num">300</span>
        ball_dy = -<span class="num">5</span>
        pygame.time.<span class="fn">delay</span>(<span class="num">1000</span>)      <span class="cm"># 1초 쉬고 시작</span>

    <span class="cm"># 4. 패들(막대기)에 공이 닿으면 튕기기</span>
    <span class="kw">if</span> ball_y + <span class="num">20</span> &gt;= <span class="num">550</span> <span class="kw">and</span> paddle_x &lt; ball_x + <span class="num">20</span> <span class="kw">and</span> paddle_x + <span class="num">100</span> &gt; ball_x:
        ball_dy = -ball_dy           <span class="cm"># 위로 튕겨내기!</span>

    <span class="cm"># 5. 화면 그리기</span>
    screen.<span class="fn">fill</span>((<span class="num">30</span>, <span class="num">30</span>, <span class="num">30</span>)) <span class="cm"># 어두운 배경</span>
    
    <span class="cm"># 패들(하늘색)과 공(빨간색) 그리기</span>
    pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">0</span>, <span class="num">200</span>, <span class="num">255</span>), [paddle_x, <span class="num">550</span>, <span class="num">100</span>, <span class="num">20</span>], border_radius=<span class="num">10</span>)
    pygame.draw.<span class="fn">ellipse</span>(screen, (<span class="num">255</span>, <span class="num">50</span>, <span class="num">50</span>), [ball_x, ball_y, <span class="num">20</span>, <span class="num">20</span>])

    pygame.<span class="fn">display</span>.<span class="fn">update</span>()
    clock.<span class="fn">tick</span>(<span class="num">60</span>)</pre>
      </div>
    </div>
  </section>


  <!-- 7. 프로젝트: 뱀 꼬리잡기 -->
  <section class="fig" style="--accent:var(--c-list)">
    <div class="fig-head">
      <div class="fig-emoji">🐍</div>
      <h2 class="fig-title">7. 프로젝트: 뱀 꼬리잡기 (리스트 활용)</h2>
    </div>
    
    <div class="board-card">
      <p>사과를 먹을 때마다 뱀의 꼬리가 하나씩 길어지는 고전 명작 <b>스네이크 게임</b>입니다. 뱀의 몸통 전체 좌표를 '리스트'에 담아서 관리하는 것이 이 게임의 핵심 원리예요!</p>
      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre><span class="kw">import</span> pygame, sys, random
pygame.<span class="fn">init</span>()
screen = pygame.<span class="fn">display</span>.<span class="fn">set_mode</span>((<span class="num">600</span>, <span class="num">600</span>))
clock = pygame.time.<span class="fn">Clock</span>()
font = pygame.font.<span class="fn">SysFont</span>(<span class="str">"malgungothic"</span>, <span class="num">36</span>)

<span class="cm"># 뱀과 사과 설정</span>
snake = [[<span class="num">300</span>, <span class="num">300</span>]]  <span class="cm"># 뱀 몸통 좌표들이 들어있는 리스트 (처음엔 머리 하나)</span>
dx, dy = <span class="num">0</span>, -<span class="num">20</span>      <span class="cm"># 처음에는 위로 이동</span>
apple_x = random.<span class="fn">randrange</span>(<span class="num">0</span>, <span class="num">30</span>) * <span class="num">20</span>
apple_y = random.<span class="fn">randrange</span>(<span class="num">0</span>, <span class="num">30</span>) * <span class="num">20</span>
score = <span class="num">0</span>

<span class="kw">while True</span>:
    <span class="kw">for</span> event <span class="kw">in</span> pygame.event.<span class="fn">get</span>():
        <span class="kw">if</span> event.type == pygame.<span class="fn">QUIT</span>:
            pygame.<span class="fn">quit</span>(); sys.<span class="fn">exit</span>()
        <span class="kw">if</span> event.type == pygame.<span class="fn">KEYDOWN</span>:
            <span class="kw">if</span> event.key == pygame.<span class="fn">K_UP</span> <span class="kw">and</span> dy == <span class="num">0</span>:    dx, dy = <span class="num">0</span>, -<span class="num">20</span>
            <span class="kw">if</span> event.key == pygame.<span class="fn">K_DOWN</span> <span class="kw">and</span> dy == <span class="num">0</span>:  dx, dy = <span class="num">0</span>, <span class="num">20</span>
            <span class="kw">if</span> event.key == pygame.<span class="fn">K_LEFT</span> <span class="kw">and</span> dx == <span class="num">0</span>:  dx, dy = -<span class="num">20</span>, <span class="num">0</span>
            <span class="kw">if</span> event.key == pygame.<span class="fn">K_RIGHT</span> <span class="kw">and</span> dx == <span class="num">0</span>: dx, dy = <span class="num">20</span>, <span class="num">0</span>

    <span class="cm"># 1. 뱀 머리 이동</span>
    new_head = [snake[<span class="num">0</span>][<span class="num">0</span>] + dx, snake[<span class="num">0</span>][<span class="num">1</span>] + dy]
    snake.<span class="fn">insert</span>(<span class="num">0</span>, new_head) <span class="cm"># 리스트 맨 앞에 새 머리 추가</span>

    <span class="cm"># 2. 사과 먹기 검사</span>
    <span class="kw">if</span> new_head[<span class="num">0</span>] == apple_x <span class="kw">and</span> new_head[<span class="num">1</span>] == apple_y:
        score += <span class="num">10</span>
        apple_x = random.<span class="fn">randrange</span>(<span class="num">0</span>, <span class="num">30</span>) * <span class="num">20</span>
        apple_y = random.<span class="fn">randrange</span>(<span class="num">0</span>, <span class="num">30</span>) * <span class="num">20</span>
    <span class="kw">else</span>:
        snake.<span class="fn">pop</span>() <span class="cm"># 사과를 안 먹었으면 맨 뒤 꼬리를 지워서 길이를 유지</span>

    <span class="cm"># 3. 벽에 부딪히거나 자기 몸에 부딪히면 끝!</span>
    <span class="kw">if</span> new_head[<span class="num">0</span>] &lt; <span class="num">0</span> <span class="kw">or</span> new_head[<span class="num">0</span>] &gt;= <span class="num">600</span> <span class="kw">or</span> new_head[<span class="num">1</span>] &lt; <span class="num">0</span> <span class="kw">or</span> new_head[<span class="num">1</span>] &gt;= <span class="num">600</span> <span class="kw">or</span> new_head <span class="kw">in</span> snake[<span class="num">1</span>:]:
        pygame.time.<span class="fn">delay</span>(<span class="num">1500</span>)
        snake = [[<span class="num">300</span>, <span class="num">300</span>]]; dx, dy = <span class="num">0</span>, -<span class="num">20</span>; score = <span class="num">0</span>

    <span class="cm"># 4. 화면 그리기</span>
    screen.<span class="fn">fill</span>((<span class="num">40</span>, <span class="num">40</span>, <span class="num">40</span>))
    
    <span class="cm"># 사과 그리기 (빨간색)</span>
    pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">255</span>, <span class="num">50</span>, <span class="num">50</span>), [apple_x, apple_y, <span class="num">20</span>, <span class="num">20</span>], border_radius=<span class="num">5</span>)
    
    <span class="cm"># 뱀 그리기 (초록색)</span>
    <span class="kw">for</span> part <span class="kw">in</span> snake:
        pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">50</span>, <span class="num">255</span>, <span class="num">50</span>), [part[<span class="num">0</span>], part[<span class="num">1</span>], <span class="num">20</span>, <span class="num">20</span>], border_radius=<span class="num">3</span>)

    screen.<span class="fn">blit</span>(font.<span class="fn">render</span>(<span class="str">f"점수: {score}"</span>, <span class="kw">True</span>, (<span class="num">255</span>, <span class="num">255</span>, <span class="num">255</span>)), (<span class="num">10</span>, <span class="num">10</span>))
    pygame.<span class="fn">display</span>.<span class="fn">update</span>()
    clock.<span class="fn">tick</span>(<span class="num">12</span>) <span class="cm"># 뱀 게임은 조금 천천히 움직이게 (1초에 12프레임)</span></pre>
      </div>
    </div>
  </section>

  <!-- 8. 프로젝트: 스페이스 슈팅 -->
  <section class="fig" style="--accent:var(--c-var)">
    <div class="fig-head">
      <div class="fig-emoji">🛸</div>
      <h2 class="fig-title">8. 프로젝트: 스페이스 슈팅 (레이저와 다중 충돌)</h2>
    </div>
    
    <div class="board-card">
      <p>스페이스바를 눌러 레이저를 쏘고 하늘에서 떨어지는 운석(적)을 격추하는 비행기 슈팅 게임입니다! 여러 개의 총알과 여러 개의 운석을 동시에 관리하는 법을 배울 수 있어요.</p>
      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre><span class="kw">import</span> pygame, sys, random
pygame.<span class="fn">init</span>()
screen = pygame.<span class="fn">display</span>.<span class="fn">set_mode</span>((<span class="num">600</span>, <span class="num">800</span>))
clock = pygame.time.<span class="fn">Clock</span>()
font = pygame.font.<span class="fn">SysFont</span>(<span class="str">"malgungothic"</span>, <span class="num">36</span>)

player_x = <span class="num">275</span>
bullets = []   <span class="cm"># 발사된 총알들을 담을 리스트 (예: [[x, y], [x, y], ...])</span>
enemies = []   <span class="cm"># 떨어지는 적들을 담을 리스트 (예: [[x, y], [x, y], ...])</span>
score = <span class="num">0</span>
enemy_timer = <span class="num">0</span>

<span class="kw">while True</span>:
    <span class="kw">for</span> event <span class="kw">in</span> pygame.event.<span class="fn">get</span>():
        <span class="kw">if</span> event.type == pygame.<span class="fn">QUIT</span>:
            pygame.<span class="fn">quit</span>(); sys.<span class="fn">exit</span>()
        <span class="kw">if</span> event.type == pygame.<span class="fn">KEYDOWN</span>:
            <span class="kw">if</span> event.key == pygame.<span class="fn">K_SPACE</span>:
                bullets.<span class="fn">append</span>([player_x + <span class="num">20</span>, <span class="num">700</span>]) <span class="cm"># 비행기 중앙에서 총알 발사</span>

    <span class="cm"># 1. 플레이어 이동</span>
    keys = pygame.key.<span class="fn">get_pressed</span>()
    <span class="kw">if</span> keys[pygame.<span class="fn">K_LEFT</span>] <span class="kw">and</span> player_x &gt; <span class="num">0</span>:   player_x -= <span class="num">6</span>
    <span class="kw">if</span> keys[pygame.<span class="fn">K_RIGHT</span>] <span class="kw">and</span> player_x &lt; <span class="num">550</span>: player_x += <span class="num">6</span>

    <span class="cm"># 2. 적 생성 (조금씩 자주 나타나게)</span>
    enemy_timer += <span class="num">1</span>
    <span class="kw">if</span> enemy_timer &gt; <span class="num">40</span>:
        enemies.<span class="fn">append</span>([random.<span class="fn">randint</span>(<span class="num">0</span>, <span class="num">550</span>), -<span class="num">50</span>])
        enemy_timer = <span class="num">0</span>

    <span class="cm"># 3. 총알 이동</span>
    <span class="kw">for</span> b <span class="kw">in</span> bullets:
        b[<span class="num">1</span>] -= <span class="num">10</span> <span class="cm"># 위로 빠르게 이동</span>

    <span class="cm"># 4. 적 이동</span>
    <span class="kw">for</span> e <span class="kw">in</span> enemies:
        e[<span class="num">1</span>] += <span class="num">4</span>  <span class="cm"># 아래로 떨어짐</span>

    <span class="cm"># 5. 충돌 검사 (총알이 적을 맞췄을 때)</span>
    <span class="cm"># 리스트 안의 요소를 지워야 해서 뒤집어서 반복합니다.</span>
    <span class="kw">for</span> e <span class="kw">in</span> enemies[:]:
        <span class="kw">for</span> b <span class="kw">in</span> bullets[:]:
            <span class="cm"># 사각형 충돌 계산 (간단하게 중심 좌표로 비교)</span>
            <span class="kw">if</span> e[<span class="num">0</span>] &lt; b[<span class="num">0</span>] &lt; e[<span class="num">0</span>]+<span class="num">40</span> <span class="kw">and</span> e[<span class="num">1</span>] &lt; b[<span class="num">1</span>] &lt; e[<span class="num">1</span>]+<span class="num">40</span>:
                score += <span class="num">10</span>
                <span class="kw">if</span> b <span class="kw">in</span> bullets: bullets.<span class="fn">remove</span>(b)
                <span class="kw">if</span> e <span class="kw">in</span> enemies: enemies.<span class="fn">remove</span>(e)
                <span class="kw">break</span>
                
        <span class="cm"># 적이 바닥에 닿거나 나를 치면 게임 오버로 할 수도 있지만, 여기선 그냥 삭제</span>
        <span class="kw">if</span> e[<span class="num">1</span>] &gt; <span class="num">850</span> <span class="kw">and</span> e <span class="kw">in</span> enemies:
            enemies.<span class="fn">remove</span>(e)

    <span class="cm"># 6. 화면 그리기</span>
    screen.<span class="fn">fill</span>((<span class="num">10</span>, <span class="num">10</span>, <span class="num">30</span>))
    
    pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">0</span>, <span class="num">255</span>, <span class="num">255</span>), [player_x, <span class="num">700</span>, <span class="num">50</span>, <span class="num">50</span>]) <span class="cm"># 비행기</span>
    <span class="kw">for</span> b <span class="kw">in</span> bullets:
        pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">255</span>, <span class="num">255</span>, <span class="num">0</span>), [b[<span class="num">0</span>], b[<span class="num">1</span>], <span class="num">5</span>, <span class="num">15</span>]) <span class="cm"># 총알</span>
    <span class="kw">for</span> e <span class="kw">in</span> enemies:
        pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">255</span>, <span class="num">50</span>, <span class="num">50</span>), [e[<span class="num">0</span>], e[<span class="num">1</span>], <span class="num">40</span>, <span class="num">40</span>]) <span class="cm"># 적</span>

    screen.<span class="fn">blit</span>(font.<span class="fn">render</span>(<span class="str">f"점수: {score}"</span>, <span class="kw">True</span>, (<span class="num">255</span>, <span class="num">255</span>, <span class="num">255</span>)), (<span class="num">10</span>, <span class="num">10</span>))
    pygame.<span class="fn">display</span>.<span class="fn">update</span>()
    clock.<span class="fn">tick</span>(<span class="num">60</span>)</pre>
      </div>
    </div>
  </section>

  <!-- 9. 프로젝트: 두더지 잡기 -->
  <section class="fig" style="--accent:var(--water-deep)">
    <div class="fig-head">
      <div class="fig-emoji">🔨</div>
      <h2 class="fig-title">9. 프로젝트: 두더지 잡기 (마우스 클릭)</h2>
    </div>
    
    <div class="board-card">
      <p>이번엔 키보드가 아니라 <b>마우스 클릭</b>을 사용하는 게임입니다! `MOUSEBUTTONDOWN` 이벤트를 이용해 화면 여기저기서 나타나는 네모 두더지를 빠르게 클릭해 보세요.</p>
      <div class="code-block" style="position:relative;">
        <button class="copy-btn" onclick="copyCode(this)">복사 📋</button>
<pre><span class="kw">import</span> pygame, sys, random
pygame.<span class="fn">init</span>()
screen = pygame.<span class="fn">display</span>.<span class="fn">set_mode</span>((<span class="num">800</span>, <span class="num">600</span>))
clock = pygame.time.<span class="fn">Clock</span>()
font = pygame.font.<span class="fn">SysFont</span>(<span class="str">"malgungothic"</span>, <span class="num">36</span>)

<span class="cm"># 두더지 정보 (위치와 크기)</span>
mole_x = random.<span class="fn">randint</span>(<span class="num">50</span>, <span class="num">700</span>)
mole_y = random.<span class="fn">randint</span>(<span class="num">150</span>, <span class="num">500</span>)
mole_size = <span class="num">80</span>
score = <span class="num">0</span>
timer = <span class="num">60</span> <span class="cm"># 두더지가 위치를 바꿀 때까지 세는 타이머</span>

<span class="kw">while True</span>:
    <span class="kw">for</span> event <span class="kw">in</span> pygame.event.<span class="fn">get</span>():
        <span class="kw">if</span> event.type == pygame.<span class="fn">QUIT</span>:
            pygame.<span class="fn">quit</span>(); sys.<span class="fn">exit</span>()
            
        <span class="cm"># 마우스를 클릭했을 때 발생하는 이벤트!</span>
        <span class="kw">if</span> event.type == pygame.<span class="fn">MOUSEBUTTONDOWN</span>:
            <span class="cm"># event.pos는 클릭한 마우스의 (x, y) 좌표예요.</span>
            mouse_x, mouse_y = event.pos
            
            <span class="cm"># 클릭한 위치가 두더지 네모 영역 안에 있는지 확인</span>
            <span class="kw">if</span> mole_x &lt; mouse_x &lt; mole_x + mole_size <span class="kw">and</span> mole_y &lt; mouse_y &lt; mole_y + mole_size:
                score += <span class="num">10</span>
                <span class="cm"># 잡았으면 즉시 위치를 이동</span>
                mole_x = random.<span class="fn">randint</span>(<span class="num">50</span>, <span class="num">700</span>)
                mole_y = random.<span class="fn">randint</span>(<span class="num">150</span>, <span class="num">500</span>)
                timer = <span class="num">60</span>

    <span class="cm"># 시간이 흐르면 두더지가 도망감</span>
    timer -= <span class="num">1</span>
    <span class="kw">if</span> timer &lt; <span class="num">0</span>:
        mole_x = random.<span class="fn">randint</span>(<span class="num">50</span>, <span class="num">700</span>)
        mole_y = random.<span class="fn">randint</span>(<span class="num">150</span>, <span class="num">500</span>)
        timer = <span class="num">60</span>

    <span class="cm"># 화면 그리기</span>
    screen.<span class="fn">fill</span>((<span class="num">120</span>, <span class="num">200</span>, <span class="num">100</span>)) <span class="cm"># 잔디밭 배경색</span>
    
    <span class="cm"># 갈색 두더지 그리기</span>
    pygame.draw.<span class="fn">rect</span>(screen, (<span class="num">139</span>, <span class="num">69</span>, <span class="num">19</span>), [mole_x, mole_y, mole_size, mole_size], border_radius=<span class="num">20</span>)

    <span class="cm"># 마우스 커서 위치에 망치 모양(흰 동그라미) 따라다니게 하기</span>
    mx, my = pygame.mouse.<span class="fn">get_pos</span>()
    pygame.draw.<span class="fn">circle</span>(screen, (<span class="num">255</span>, <span class="num">255</span>, <span class="num">255</span>), (mx, my), <span class="num">15</span>)

    <span class="cm"># 점수 텍스트 </span>
    screen.<span class="fn">blit</span>(font.<span class="fn">render</span>(<span class="str">f"잡은 점수: {score}"</span>, <span class="kw">True</span>, (<span class="num">0</span>, <span class="num">0</span>, <span class="num">0</span>)), (<span class="num">20</span>, <span class="num">20</span>))
    
    pygame.<span class="fn">display</span>.<span class="fn">update</span>()
    clock.<span class="fn">tick</span>(<span class="num">60</span>)</pre>
      </div>
    </div>
  </section>

  <footer>
    <div class="footer-title">👾 훌륭한 게임 개발자가 되셨어요!</div>
    <p style="color:var(--ink-soft);">이제 직접 코드를 수정해서 속도를 높이거나, 장애물을 추가해 보세요.</p>
  </footer>

</div>

<script>
function copyCode(btn) {
  const code = btn.nextElementSibling.innerText;
  navigator.clipboard.writeText(code).then(() => {
    const originalText = btn.innerText;
    btn.innerText = "복사 완료! ✅";
    setTimeout(() => btn.innerText = originalText, 2000);
  });
}
</script>
</body>
</html>
"""

with open('/Users/cheonhyeonjun/com_gui/public/python_pygame.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated python_pygame.html")
