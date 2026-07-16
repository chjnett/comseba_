import os

with open('/Users/cheonhyeonjun/com_gui/public/bfs_dfs.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replacements for UI texts
html = html.replace('BFS 탐사 기록', 'DFS 탐사 기록')
html = html.replace('BFS가 어떻게', 'DFS가 어떻게')
html = html.replace('BFS 탐사 시뮬레이터', 'DFS 탐사 시뮬레이터')
html = html.replace('BFS 내부 동작', 'DFS 내부 동작')
html = html.replace('BFS로 호수 전체 방문', 'DFS로 호수 전체 방문')
html = html.replace('큐 (대기 중인 호수 칸)', '콜 스택 (재귀 호출 대기)')
html = html.replace('queueCount', 'stackCount')
html = html.replace('queue-panel', 'stack-panel')
html = html.replace('queue-label', 'stack-label')

# Replace shift with pop for LIFO (stack behavior)
html = html.replace('queue.shift()', 'queue.pop()')

# Reverse the loop for DFS to match recursion order (d=0 first)
old_loop = "for (const [dr, dc, name, isDiag] of DIRS) {"
new_loop = """for (let i = DIRS.length - 1; i >= 0; i--) {
        const [dr, dc, name, isDiag] = DIRS[i];"""
html = html.replace(old_loop, new_loop)

# Update the track label for stack
old_track = """trackEl.innerHTML = '<span class="flow-label">먼저 나감</span>' +
        queue.map(q => `<span class="chip">(${q[0]+1}, ${q[1]+1})</span>`).join('') +
        '<span class="flow-label">← 나중에 들어옴</span>';"""
new_track = """trackEl.innerHTML = '<span class="flow-label">스택 바닥</span>' +
        queue.map(q => `<span class="chip">(${q[0]+1}, ${q[1]+1})</span>`).join('') +
        '<span class="flow-label">← 맨 위 (Pop)</span>';"""
html = html.replace(old_track, new_track)

# Replace code snippet
old_bfs = """<span class="tag">꺼내기 — BFS로 호수 전체 방문 (8방향)</span>
<pre><span class="kw">int</span> dr[<span class="num">8</span>] = {-<span class="num">1</span>,-<span class="num">1</span>,-<span class="num">1</span>, <span class="num">0</span>,<span class="num">0</span>, <span class="num">1</span>,<span class="num">1</span>,<span class="num">1</span>};
<span class="kw">int</span> dc[<span class="num">8</span>] = {-<span class="num">1</span>, <span class="num">0</span>, <span class="num">1</span>,-<span class="num">1</span>,<span class="num">1</span>,-<span class="num">1</span>,<span class="num">0</span>,<span class="num">1</span>};

<span class="kw">void</span> <span class="fn">bfs</span>(<span class="kw">int</span> sr, <span class="kw">int</span> sc) {
    queue.push({sr, sc});
    visited[sr][sc] = <span class="kw">true</span>;

    <span class="kw">while</span> (!queue.empty()) {
        <span class="kw">auto</span> [r, c] = queue.front(); queue.pop();

        <span class="kw">for</span> (<span class="kw">int</span> d = <span class="num">0</span>; d &lt; <span class="num">8</span>; d++) {   <span class="cm">// 4 -> 8</span>
            <span class="kw">int</span> nr = r + dr[d], nc = c + dc[d];
            <span class="kw">if</span> (nr&lt;0 || nr&gt;=h || nc&lt;0 || nc&gt;=w) <span class="kw">continue</span>;
            <span class="kw">if</span> (visited[nr][nc] || board[nr][nc]!=<span class="num">'L'</span>) <span class="kw">continue</span>;

            visited[nr][nc] = <span class="kw">true</span>;
            queue.push({nr, nc});
        }
    }
}</pre>"""
new_dfs = """<span class="tag">파고들기 — DFS 재귀로 호수 전체 방문 (8방향)</span>
<pre><span class="kw">int</span> dr[<span class="num">8</span>] = {-<span class="num">1</span>,-<span class="num">1</span>,-<span class="num">1</span>, <span class="num">0</span>,<span class="num">0</span>, <span class="num">1</span>,<span class="num">1</span>,<span class="num">1</span>};
<span class="kw">int</span> dc[<span class="num">8</span>] = {-<span class="num">1</span>, <span class="num">0</span>, <span class="num">1</span>,-<span class="num">1</span>,<span class="num">1</span>,-<span class="num">1</span>,<span class="num">0</span>,<span class="num">1</span>};

<span class="kw">void</span> <span class="fn">dfs</span>(<span class="kw">int</span> r, <span class="kw">int</span> c) {
    visited[r][c] = <span class="kw">true</span>;

    <span class="kw">for</span> (<span class="kw">int</span> d = <span class="num">0</span>; d &lt; <span class="num">8</span>; d++) {
        <span class="kw">int</span> nr = r + dr[d];
        <span class="kw">int</span> nc = c + dc[d];
        <span class="kw">if</span> (nr &lt; 0 || nr &gt;= h || nc &lt; 0 || nc &gt;= w) <span class="kw">continue</span>;
        <span class="kw">if</span> (visited[nr][nc]) <span class="kw">continue</span>;
        <span class="kw">if</span> (board[nr][nc] != <span class="num">'L'</span>) <span class="kw">continue</span>;

        <span class="fn">dfs</span>(nr, nc);   <span class="cm">// 여기서 바로 다음 칸으로 "타고 들어감"</span>
    }
}</pre>"""
html = html.replace(old_bfs, new_dfs)

html = html.replace('bfs(i, j);', 'dfs(i, j);')
html = html.replace('codeBfs', 'codeDfs')

with open('/Users/cheonhyeonjun/com_gui/public/dfs.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated dfs.html")
