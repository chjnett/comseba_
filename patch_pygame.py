import re

with open('gen_pygame.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_games_html = """
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
"""

content = content.replace("  <footer>", new_games_html + "\n  <footer>")

with open('gen_pygame.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("gen_pygame.py updated with 3 new games.")
