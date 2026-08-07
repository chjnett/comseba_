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
  /* ---------------- animations & misc ---------------- */
.shake{animation: shake .4s;}
@keyframes shake{ 0%,100%{transform:translateX(0);} 25%{transform:translateX(-5px);} 75%{transform:translateX(5px);} }
@keyframes pop-in{ 0%{opacity:0; transform:scale(0.95);} 100%{opacity:1; transform:scale(1);} }

.typing-view{display:none;}
.typing-view.show{display:block; animation: pop-in .25s ease;}
.typing-stage-btn{
  display:block; width:100%; text-align:left;
  padding:15px; margin-bottom:10px;
  background:var(--bg-panel-2); border:2px solid var(--border-soft);
  border-radius:12px; color:var(--text-light); font-size:16px;
  cursor:pointer; transition:all .2s; font-weight:bold;
}
.typing-stage-btn:hover{ border-color:var(--accent-mint); transform:translateY(-2px); }
.typing-stage-btn.completed{ border-color:var(--accent-gold); }

.typing-display{
  font-family: 'D2Coding', 'Fira Code', 'Consolas', monospace;
  font-size:24px; padding:20px; background:var(--bg-dark);
  border-radius:12px; margin-bottom:15px; line-height:1.5;
  white-space:pre-wrap; word-break:break-all;
  border:2px solid var(--border-soft);
}
.typing-display span.correct{ color: #4ade80; } /* green */
.typing-display span.wrong{ color: #f87171; background: rgba(248,113,113,0.2); border-radius:3px; }
.typing-display span.current{ border-bottom: 2px solid #60a5fa; background: rgba(96,165,250,0.2); }
.typing-input{
  opacity:0; position:absolute; z-index:-1;
}
.typing-stats{
  display:flex; justify-content:space-between; margin-bottom:15px; font-size:18px; font-weight:bold;
}
.typing-result{
  display:none; text-align:center; margin-top:20px; padding:20px;
  background:var(--bg-panel-2); border-radius:12px; border:2px solid var(--accent-gold);
}
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
  .problem-body .explain-box.wrong-tone{
    background:rgba(255,107,107,.08); border-color:rgba(255,107,107,.3); color:#FFC2C2;
  }
  .problem-body .explain-box.correct-tone{
    background:rgba(67,229,180,.08); border-color:rgba(67,229,180,.3); color:#B9FBE3;
  }
  .target-output{
    margin-top:2px; margin-bottom:12px; font-size:13px; color:var(--text-muted);
  }
  .target-output b{color:var(--accent-gold); font-family:'JetBrains Mono',monospace; font-weight:400;}
  .code-input{
    width:100%; min-height:96px; resize:vertical;
    background:#0D1428; border:1px solid var(--border-soft); border-radius:12px;
    color:var(--text-light); font-family:'JetBrains Mono',monospace; font-size:13.5px;
    padding:14px 16px; line-height:1.7; outline:none;
  }
  .code-input:focus{border-color:var(--accent-blue);}
  .write-actions{display:flex; gap:10px; margin-top:10px; flex-wrap:wrap;}
  .check-btn{
    background:var(--accent-blue); color:#fff; border:none; padding:9px 18px;
    border-radius:10px; font-family:'Jua',sans-serif; font-size:13px; cursor:pointer;
  }
  .check-btn:hover{filter:brightness(1.1);}
  .reveal-btn{
    background:none; border:1px solid var(--border-soft); color:var(--text-muted);
    padding:9px 16px; border-radius:10px; font-family:'Gowun Dodum',sans-serif; font-size:12.5px;
    cursor:pointer;
  }
  .reveal-btn:hover{border-color:var(--accent-gold); color:var(--accent-gold);}
  .sample-box{
    display:none; margin-top:10px; background:#0D1428; border:1px dashed var(--border-soft);
    border-radius:12px; padding:12px 16px; font-family:'JetBrains Mono',monospace;
    font-size:13px; color:#9FC1FF; white-space:pre-line;
  }
  .sample-box .tag2{display:block; font-family:'Gowun Dodum',sans-serif; color:var(--text-muted); font-size:11.5px; margin-bottom:6px;}


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
    .tab-btn{font-size:12.5px; padding:8px 4px 10px;}
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


  <nav class="tab-bar">
    <button class="tab-btn active" id="tabExplore" data-tab="explore">🚀 행성 탐험</button>
    <button class="tab-btn" id="tabProblems" data-tab="problems">🧠 생각하는 응용문제</button>
    <button class="tab-btn" id="tabConcept" data-tab="concept">💡 개념 쏙쏙 점검</button>
    <button class="tab-btn" id="tabTest" data-tab="test">💯 실전 모의고사</button>
    <button class="tab-btn" id="tabTyping" data-tab="typing">⌨️ 타자 연습 (복습)</button>
  </nav>

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



  <!-- CONCEPT CHECK TAB VIEW -->
  <div class="test-view" id="conceptView">
    <div class="problem-card">
      <div class="lesson-head">
        <div class="emoji">💡</div>
        <h2>개념 쏙쏙 점검 (O/X 퀴즈)</h2>
      </div>
      <div class="speech">🐍 모의고사를 풀기 전에 파이썬의 핵심 개념을 O/X 퀴즈로 가볍게 점검해봐요!</div>
      <div id="conceptList" style="margin-top:20px;"></div>
      <div class="test-submit-area" style="text-align:center; margin-top:30px;">
        <button class="next-btn ready" id="submitConceptBtn" style="font-size:18px; padding:15px 30px;">결과 확인하기</button>
      </div>
      <div id="conceptResultArea" style="display:none; text-align:center; margin-top:20px; padding:20px; background:var(--bg-panel-2); border-radius:12px; border:2px solid var(--accent-mint);">
        <h2 style="color:var(--accent-mint); font-size:32px; margin-bottom:10px;" id="conceptScoreDisplay"></h2>
        <div class="speech" id="conceptFeedbackMsg" style="font-size:18px;"></div>
      </div>
    </div>
  </div>

  <!-- MOCK EXAMS TAB VIEW -->
  <div class="test-view" id="testView">
    <!-- LOBBY -->
    <div id="mockLobby">
      <div class="problem-card">
        <div class="lesson-head">
          <div class="emoji">💯</div>
          <h2>실전 모의고사 (총 10회)</h2>
        </div>
        <div class="speech">🐍 회차를 거듭할수록 조금씩 새로워집니다! 100점에 도전하세요.</div>
        <div id="mockLobbyList" style="display:flex; flex-direction:column; gap:10px; margin-top:20px;"></div>
      </div>
    </div>

    <!-- EXAM ROOM -->
    <div id="mockExamRoom" style="display:none;">
      <div class="problem-card">
        <div class="lesson-head">
          <div class="emoji">📝</div>
          <h2 id="mockExamTitle">제X회 모의고사</h2>
        </div>
        <button class="back-btn" id="mockBackBtn" style="margin-bottom:15px; font-size:14px;">← 목록으로 돌아가기</button>
        <div class="speech">🐍 10문제를 모두 풀고 <b>'답안 제출하기'</b> 버튼을 누르면 채점됩니다!</div>
        <div id="testList" style="margin-top:20px;"></div>
        <div class="test-submit-area" style="text-align:center; margin-top:30px;">
          <button class="next-btn ready" id="submitTestBtn" style="font-size:18px; padding:15px 30px;">답안 제출하기</button>
        </div>
        <div id="testResultArea" style="display:none; text-align:center; margin-top:20px; padding:20px; background:var(--bg-panel-2); border-radius:12px; border:2px solid var(--accent-gold);">
          <h2 style="color:var(--accent-gold); font-size:32px; margin-bottom:10px;" id="testScoreDisplay"></h2>
          <div class="speech" id="testFeedbackMsg" style="font-size:18px;"></div>
          <button class="next-btn ready" id="mockRetryBtn" style="margin-top:15px; font-size:16px;">다시 풀기</button>
        </div>
      </div>
    </div>
  </div>

  <!-- TYPING PRACTICE TAB VIEW -->
  <div class="typing-view" id="typingView">
    <!-- LOBBY -->
    <div id="typingLobby">
      <div class="problem-card">
        <div class="lesson-head">
          <div class="emoji">⌨️</div>
          <h2>파이썬 타자 연습 (종합 복습)</h2>
        </div>
        <div class="speech">🐍 코드를 빠르고 정확하게 타이핑하며 파이썬 문법을 복습해보세요! 원하는 단계를 선택하세요.</div>
        <div id="typingLobbyList" style="margin-top:20px;"></div>
      </div>
    </div>

    <!-- TYPING ROOM -->
    <div id="typingRoom" style="display:none;">
      <div class="problem-card">
        <div class="lesson-head">
          <div class="emoji">⏱️</div>
          <h2 id="typingStageTitle">1단계: 출력문</h2>
        </div>
        <button class="back-btn" id="typingBackBtn" style="margin-bottom:15px; font-size:14px;">← 목록으로 돌아가기</button>
        <div class="speech">🐍 타자를 시작하면 시간이 측정됩니다. 대소문자와 띄어쓰기에 주의하세요!</div>
        <div class="typing-stats">
          <div>정확도: <span id="typingAccuracy" style="color:var(--accent-mint);">100</span>%</div>
          <div>경과 시간: <span id="typingTimer" style="color:var(--accent-gold);">0.0</span>초</div>
        </div>
        <div class="typing-display" id="typingDisplay"></div>
        <input type="text" id="typingHiddenInput" class="typing-input" autocomplete="off" spellcheck="false" autocorrect="off">
        
        <div id="typingResultArea" class="typing-result">
          <h2 style="color:var(--accent-gold); font-size:32px; margin-bottom:10px;" id="typingFinalTime">기록: 0.0초</h2>
          <div class="speech" id="typingFeedbackMsg" style="font-size:18px;">완벽해요! 정말 빠르네요!</div>
          <button class="next-btn ready" id="typingRetryBtn" style="margin-top:15px; font-size:16px;">다시 도전하기</button>
        </div>
      </div>
    </div>
  </div>
  <!-- TROPHY VIEW -->
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
},
  {
    id:7, emoji:'🧰', name:'함수 행성', desc:'def로 나만의 명령어 만들기',
    explain:`<b>함수</b>는 자주 쓰는 명령들을 이름 붙여서 저장해두는 상자예요.<br>
    <code>def</code>로 만들고, <code>함수이름()</code>으로 언제든지 다시 불러 쓸 수 있어요.`,
    code:[
      {t:'kw',v:'def'},{t:'p',v:' '},{t:'fn',v:'greet'},{t:'p',v:'():'},{t:'nl'},
      {t:'p',v:'    '},{t:'kw',v:'print'},{t:'p',v:'('},{t:'str',v:'"안녕! 반가워!"'},{t:'p',v:')'},{t:'nl'},{t:'nl'},
      {t:'fn',v:'greet'},{t:'p',v:'()'},{t:'nl'},
      {t:'fn',v:'greet'},{t:'p',v:'()'}
    ],
    output:'안녕! 반가워!\n안녕! 반가워!',
    mission:{
      goal:'실행하면 "잘가!"를 출력하는 올바른 함수 코드는?',
      choices:[
        {code:'def bye():\n    print("잘가!")\n\nbye()', correct:true, out:'잘가!'},
        {code:'def bye():\nprint("잘가!")\n\nbye()', correct:false, hint:'함수 안의 코드도 들여쓰기(공백 4칸)가 필요해요!'},
        {code:'def bye()\n    print("잘가!")\n\nbye()', correct:false, hint:'def 뒤에도 콜론(:)이 꼭 필요해요!'}
      ]
    },
    quiz:[
      {q:'함수를 만들 때 사용하는 키워드는?', choices:['def','for','if','list'], answer:0},
      {q:'만들어 둔 함수를 실행(호출)하려면 어떻게 해야 할까요?', choices:['함수이름() 을 쓴다','def를 또 쓴다','print만 쓰면 된다','아무것도 안 해도 자동 실행된다'], answer:0}
    ]
  },
  {
    id:8, emoji:'♾️', name:'무한도전 행성', desc:'while 반복문',
    explain:`<code>while</code>은 "조건이 참인 동안 계속 반복해라"는 뜻이에요.<br>
    <code>for</code>와 달리 반복 횟수가 정해져 있지 않고, 조건이 <b>거짓</b>이 될 때까지 계속돼요. 무한반복 되지 않게 조심!`,
    code:[
      {t:'fn',v:'count'},{t:'p',v:' = '},{t:'num',v:'0'},{t:'nl'},
      {t:'kw',v:'while'},{t:'p',v:' count < '},{t:'num',v:'3'},{t:'p',v:':'},{t:'nl'},
      {t:'p',v:'    '},{t:'kw',v:'print'},{t:'p',v:'('},{t:'str',v:'"점프!"'},{t:'p',v:')'},{t:'nl'},
      {t:'p',v:'    '},{t:'fn',v:'count'},{t:'p',v:' = count + '},{t:'num',v:'1'}
    ],
    output:'점프!\n점프!\n점프!',
    mission:{
      goal:'"안녕"을 정확히 2번만 출력하는 올바른 코드는?',
      choices:[
        {code:'i = 0\nwhile i < 2:\n    print("안녕")\n    i = i + 1', correct:true, out:'안녕\n안녕'},
        {code:'i = 0\nwhile i < 2:\n    print("안녕")', correct:false, hint:'i 값을 늘려주지 않으면 무한 반복돼요! i = i + 1을 꼭 넣어주세요.'},
        {code:'i = 0\nwhile i > 2:\n    print("안녕")\n    i = i + 1', correct:false, hint:'조건이 i > 2 이면 처음부터 거짓이라 한 번도 실행되지 않아요!'}
      ]
    },
    quiz:[
      {q:'while 반복문은 언제까지 반복할까요?', choices:['조건이 거짓이 될 때까지','딱 3번만','1번만','무조건 10번'], answer:0},
      {q:'while문에서 무한 반복에 빠지지 않으려면 무엇이 중요할까요?', choices:['조건이 언젠가 거짓이 되도록 값을 바꿔줘야 한다','아무것도 안 해도 된다','print를 여러 번 써야 한다','else를 꼭 써야 한다'], answer:0}
    ]
  },
  {
    id:9, emoji:'🧩', name:'종합응용 행성', desc:'if + for + 리스트 합체!',
    explain:`지금까지 배운 것들을 <b>합쳐서</b> 진짜 프로그램처럼 만들어볼까요?<br>
    리스트를 반복하면서 조건에 맞는 것만 골라내는 것, 이게 진짜 코딩의 재미예요! <code>%</code>는 나눈 <b>나머지</b>를 구하는 기호예요.`,
    code:[
      {t:'fn',v:'numbers'},{t:'p',v:' = '},{t:'p',v:'['},{t:'num',v:'1'},{t:'p',v:', '},{t:'num',v:'2'},{t:'p',v:', '},{t:'num',v:'3'},{t:'p',v:', '},{t:'num',v:'4'},{t:'p',v:', '},{t:'num',v:'5'},{t:'p',v:', '},{t:'num',v:'6'},{t:'p',v:']'},{t:'nl'},
      {t:'kw',v:'for'},{t:'p',v:' n in '},{t:'fn',v:'numbers'},{t:'p',v:':'},{t:'nl'},
      {t:'p',v:'    '},{t:'kw',v:'if'},{t:'p',v:' n % '},{t:'num',v:'2'},{t:'p',v:' == '},{t:'num',v:'0'},{t:'p',v:':'},{t:'nl'},
      {t:'p',v:'        '},{t:'kw',v:'print'},{t:'p',v:'(n)'}
    ],
    output:'2\n4\n6',
    mission:{
      goal:'리스트 [1,3,5,2,8] 에서 3보다 큰 수만 출력하는 올바른 코드는?',
      choices:[
        {code:'for n in [1,3,5,2,8]:\n    if n > 3:\n        print(n)', correct:true, out:'5\n8'},
        {code:'for n in [1,3,5,2,8]:\n    if n > 3\n        print(n)', correct:false, hint:'if 조건 뒤에도 콜론(:)이 필요해요!'},
        {code:'for n in [1,3,5,2,8]:\nif n > 3:\n    print(n)', correct:false, hint:'if문도 for문 안쪽에 있으려면 들여쓰기가 필요해요!'}
      ]
    },
    quiz:[
      {q:'<b>n % 2 == 0</b> 은 무슨 뜻일까요?', choices:['n이 짝수다','n이 홀수다','n이 0이다','n이 음수다'], answer:0},
      {q:'for문과 if문을 함께 쓰면 무엇을 할 수 있나요?', choices:['리스트에서 원하는 조건의 값만 골라낼 수 있다','아무 의미 없다','변수를 지울 수 있다','화면을 지울 수 있다'], answer:0}
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
      <button class="planet-node ${cls}" data-id="${i}">
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
    <button class="planet-node ${bCls}" data-boss="1">
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
      if(btn.classList.contains('locked')) {
        const pwd = prompt("잠겨있는 행성입니다. 비밀번호를 입력하세요:");
        if (pwd === "1000") {
          openLesson(parseInt(btn.dataset.id));
        } else if (pwd !== null) {
          alert("비밀번호가 틀렸습니다!");
        }
        return;
      }
      openLesson(parseInt(btn.dataset.id));
    });
  });
  const bossBtn = wrap.querySelector('.planet-node[data-boss]');
  if(bossBtn){
    bossBtn.addEventListener('click', ()=>{
      if(bossBtn.classList.contains('locked')) {
        const pwd = prompt("잠겨있는 행성입니다. 비밀번호를 입력하세요:");
        if (pwd === "1000") {
          openBoss();
        } else if (pwd !== null) {
          alert("비밀번호가 틀렸습니다!");
        }
        return;
      }
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
  document.getElementById('problemsView').classList.toggle('show', name==='problems');
  document.getElementById('testView').classList.toggle('show', name==='test');
  document.getElementById('conceptView').classList.toggle('show', name==='concept');
  document.getElementById('typingView').classList.toggle('show', name==='typing');
  window.scrollTo({top:0, behavior:'smooth'});
}

/* ---------------- tab switching ---------------- */
function switchTab(tab){
  document.getElementById('tabExplore').classList.toggle('active', tab==='explore');
  document.getElementById('tabProblems').classList.toggle('active', tab==='problems');
  document.getElementById('tabConcept').classList.toggle('active', tab==='concept');
  document.getElementById('tabTest').classList.toggle('active', tab==='test');
  document.getElementById('tabTyping').classList.toggle('active', tab==='typing');
  if(tab==='explore'){
    showView('map');
  } else if(tab==='problems') {
    showView('problems');
  } else if(tab==='concept') {
    showView('concept');
  } else if(tab==='test') {
    showView('test');
  } else if(tab==='typing') {
    showView('typing');
  }
}
document.getElementById('tabExplore').addEventListener('click', ()=>switchTab('explore'));
document.getElementById('tabProblems').addEventListener('click', ()=>switchTab('problems'));
document.getElementById('tabConcept').addEventListener('click', ()=>switchTab('concept'));
document.getElementById('tabTest').addEventListener('click', ()=>switchTab('test'));
document.getElementById('tabTyping').addEventListener('click', ()=>switchTab('typing'));

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
    q.shuffledChoices.forEach((choiceObj, ci)=>{
      const b = document.createElement('button');
      b.className = 'choice-btn';
      b.style.fontFamily = "'Gowun Dodum',sans-serif";
      b.textContent = `${['①','②','③','④'][ci]} ${choiceObj.text}`;
      b.addEventListener('click', ()=>{
        if(choiceObj.isCorrect){
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
    q.shuffledChoices.forEach((choiceObj,ci)=>{
      const b = document.createElement('button');
      b.className='choice-btn';
      b.style.fontFamily = "'Gowun Dodum',sans-serif";
      b.textContent = `${['①','②','③','④'][ci]} ${choiceObj.text}`;
      b.addEventListener('click', ()=>{
        if(choiceObj.isCorrect){
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

/* ---------------- APPLIED THINKING PROBLEMS ---------------- */
const PROBLEMS = [
  {
    type:'quiz', emoji:'📝', title:`가장 기본 명령어`, tag:`퀴즈 · 출력 · 쉬움`,
    scenario:`화면에 글자나 숫자를 보여주고 싶을 때 사용하는 파이썬의 주문(명령어)은 무엇인가요?`,
    code:``,
    choices:[ {text:`print()`, correct:true, feedback:`✅ 맞아요! 화면에 무언가를 출력할 때는 print()를 사용해요.`}, {text:`show()`, correct:false, feedback:`🤔 show()라는 명령어는 기본 파이썬에는 없어요.`}, {text:`say()`, correct:false, feedback:`🤔 말하는 느낌은 비슷하지만 정답은 아니에요.`}, {text:`out()`, correct:false, feedback:`🤔 out()은 파이썬 명령어가 아니에요.`} ]
  },
  {
    type:'quiz', emoji:'🔤', title:`글자 감싸기`, tag:`퀴즈 · 문자열 · 쉬움`,
    scenario:`파이썬에서 '안녕'이라는 글자를 컴퓨터에게 알려주려면 어떻게 감싸야 할까요?`,
    code:`print( ___안녕___ )`,
    choices:[ {text:`따옴표 (" ")`, correct:true, feedback:`✅ 맞아요! 글자(문자열)는 항상 따옴표로 감싸야 해요.`}, {text:`괄호 ( )`, correct:false, feedback:`🤔 괄호는 함수를 실행할 때 써요. 글자 자체를 감싸진 않아요.`}, {text:`대괄호 [ ]`, correct:false, feedback:`🤔 대괄호는 리스트(상자 모음)를 만들 때 써요.`}, {text:`별표 * *`, correct:false, feedback:`🤔 별표는 보통 곱하기를 할 때 쓴답니다.`} ]
  },
  {
    type:'quiz', emoji:'➕', title:`간단한 덧셈`, tag:`퀴즈 · 연산 · 쉬움`,
    scenario:`다음 코드를 실행하면 화면에 어떤 숫자가 나올까요?`,
    code:`print(10 + 5)`,
    choices:[ {text:`15`, correct:true, feedback:`✅ 맞아요! 컴퓨터가 10 + 5를 계산해서 15를 출력해요.`}, {text:`105`, correct:false, feedback:`🤔 숫자끼리 더하면 진짜 수학처럼 계산돼요. 글자일 때만 이어 붙어요.`}, {text:`10 + 5`, correct:false, feedback:`🤔 따옴표가 없기 때문에 그대로 출력되지 않고 계산된답니다.`}, {text:`오류 발생`, correct:false, feedback:`🤔 완벽히 정상적인 파이썬 코드예요!`} ]
  },
  {
    type:'quiz', emoji:'✖️', title:`곱하기 기호`, tag:`퀴즈 · 연산 · 쉬움`,
    scenario:`파이썬에서 곱하기를 할 때 사용하는 기호는 무엇일까요?`,
    code:``,
    choices:[ {text:`* (별표)`, correct:true, feedback:`✅ 맞아요! 파이썬에서 곱하기는 * 를 사용해요.`}, {text:`x (알파벳 x)`, correct:false, feedback:`🤔 수학에서는 x를 쓰지만 컴퓨터는 헷갈려 한답니다.`}, {text:`^ (눈웃음)`, correct:false, feedback:`🤔 ^ 기호는 곱하기가 아니에요.`}, {text:`# (우물정자)`, correct:false, feedback:`🤔 #은 파이썬에서 메모(주석)를 남길 때 써요.`} ]
  },
  {
    type:'quiz', emoji:'📦', title:`변수 만들기`, tag:`퀴즈 · 변수 · 쉬움`,
    scenario:`이름이 \`age\`인 상자에 12라는 숫자를 넣으려고 해요. 알맞은 기호는?`,
    code:`age ___ 12`,
    choices:[ {text:`=`, correct:true, feedback:`✅ 맞아요! 파이썬에서 = 기호는 '오른쪽 값을 왼쪽 상자에 넣어라!' 라는 뜻이에요.`}, {text:`==`, correct:false, feedback:`🤔 == 는 '양쪽이 똑같은가요?' 하고 물어보는 기호예요.`}, {text:`+`, correct:false, feedback:`🤔 + 는 더하기 기호랍니다.`}, {text:`<-`, correct:false, feedback:`🤔 화살표 모양은 파이썬에서 쓰지 않아요.`} ]
  },
  {
    type:'quiz', emoji:'📋', title:`리스트의 생김새`, tag:`퀴즈 · 리스트 · 쉬움`,
    scenario:`여러 개의 물건을 한 줄로 담을 수 있는 '리스트'를 만들 때 사용하는 괄호는?`,
    code:`friends = ___ '짱구', '철수', '훈이' ___`,
    choices:[ {text:`[ ] 대괄호`, correct:true, feedback:`✅ 맞아요! 리스트는 항상 [ ] 로 감싸서 만들어요.`}, {text:`( ) 소괄호`, correct:false, feedback:`🤔 소괄호는 다른 용도로 쓰인답니다.`}, {text:`{ } 중괄호`, correct:false, feedback:`🤔 중괄호는 딕셔너리(사전)를 만들 때 써요.`}, {text:`< > 꺾쇠`, correct:false, feedback:`🤔 꺾쇠는 파이썬에서 보통 크기를 비교할 때 써요.`} ]
  },
  {
    type:'quiz', emoji:'🔀', title:`만약에 ~라면`, tag:`퀴즈 · 조건문 · 쉬움`,
    scenario:`'만약 날씨가 맑다면 놀러 가자!' 할 때 사용하는 파이썬 키워드는?`,
    code:`___ weather == '맑음':\n    print('놀러 가자!')`,
    choices:[ {text:`if`, correct:true, feedback:`✅ 맞아요! if는 영어로 '만약~' 이라는 뜻이죠.`}, {text:`for`, correct:false, feedback:`🤔 for는 여러 번 반복할 때 써요.`}, {text:`def`, correct:false, feedback:`🤔 def는 나만의 새로운 명령어를 만들 때 써요.`}, {text:`else`, correct:false, feedback:`🤔 else는 '그렇지 않다면' 이라는 뜻으로 if 뒤에 따라와요.`} ]
  },
  {
    type:'quiz', emoji:'🔗', title:`글자 이어붙이기`, tag:`퀴즈 · 문자열 · 보통`,
    scenario:`다음 코드를 실행하면 화면에 어떻게 출력될까요?`,
    code:`print('사과' + '주스')`,
    choices:[ {text:`사과주스`, correct:true, feedback:`✅ 맞아요! 글자끼리 + 를 쓰면 딱 붙어서 출력돼요.`}, {text:`사과 주스`, correct:false, feedback:`🤔 띄어쓰기를 따로 넣어주지 않았기 때문에 딱 붙어서 나와요.`}, {text:`사과+주스`, correct:false, feedback:`🤔 + 기호 자체는 계산되느라 화면에 나오지 않아요.`}, {text:`오류 발생`, correct:false, feedback:`🤔 글자끼리 더하는 것은 가능하답니다!`} ]
  },
  {
    type:'quiz', emoji:'🧐', title:`두 숫자의 비교`, tag:`퀴즈 · 비교 연산 · 보통`,
    scenario:`파이썬에서 '왼쪽과 오른쪽이 똑같니?' 라고 물어볼 때 쓰는 기호는?`,
    code:`if 10 ___ 10:\n    print('똑같아!')`,
    choices:[ {text:`==`, correct:true, feedback:`✅ 맞아요! 등호 두 개(==)를 써야 '같다'는 뜻이 돼요.`}, {text:`=`, correct:false, feedback:`🤔 등호 한 개(=)는 값을 상자에 넣을 때만 써요.`}, {text:`!=`, correct:false, feedback:`🤔 != 는 '다르다'는 뜻이에요.`}, {text:`=>`, correct:false, feedback:`🤔 파이썬에 이런 모양의 비교 기호는 없어요 (>= 가 맞아요).`} ]
  },
  {
    type:'quiz', emoji:'📏', title:`리스트 길이 재기`, tag:`퀴즈 · 리스트 · 보통`,
    scenario:`\`len()\`은 상자 안에 물건이 몇 개 들어있는지 세어줘요. 다음 코드의 결과는?`,
    code:`bag = ['지우개', '연필', '공책']\nprint(len(bag))`,
    choices:[ {text:`3`, correct:true, feedback:`✅ 맞아요! 지우개, 연필, 공책 총 3개가 들어있죠!`}, {text:`0`, correct:false, feedback:`🤔 리스트 안에 분명 물건이 들어있어요.`}, {text:`지우개`, correct:false, feedback:`🤔 len()은 개수(숫자)를 알려주는 함수예요.`}, {text:`2`, correct:false, feedback:`🤔 번호를 매길 때는 0부터 세지만, '개수'는 진짜 3개예요!`} ]
  },
  {
    type:'quiz', emoji:'☝️', title:`첫 번째 물건 꺼내기`, tag:`퀴즈 · 리스트 · 보통`,
    scenario:`리스트에서 가장 첫 번째에 있는 물건을 꺼내려고 해요. 숫자로 뭘 적어야 할까요?`,
    code:`bag = ['지우개', '연필']\nprint(bag[___])`,
    choices:[ {text:`0`, correct:true, feedback:`✅ 맞아요! 파이썬은 항상 0부터 순서를 세기 시작해요.`}, {text:`1`, correct:false, feedback:`🤔 1을 적으면 두 번째 물건인 '연필'이 나와요.`}, {text:`first`, correct:false, feedback:`🤔 순서는 무조건 숫자로 적어줘야 해요.`}, {text:`-1`, correct:false, feedback:`🤔 -1을 적으면 맨 마지막 물건을 꺼낸답니다.`} ]
  },
  {
    type:'quiz', emoji:'🤷‍♂️', title:`if else의 마법`, tag:`퀴즈 · 조건문 · 보통`,
    scenario:`다음 코드가 실행되면 화면에 어떤 글자가 나올까요?`,
    code:`score = 80\nif score >= 90:\n    print('합격')\nelse:\n    print('불합격')`,
    choices:[ {text:`불합격`, correct:true, feedback:`✅ 맞아요! 80은 90보다 크거나 같지 않아서 else 부분이 실행돼요.`}, {text:`합격`, correct:false, feedback:`🤔 score가 80이니까 90을 넘지 못했어요.`}, {text:`아무것도 안 나옴`, correct:false, feedback:`🤔 else가 있기 때문에 반드시 불합격이 나와요.`}, {text:`오류 발생`, correct:false, feedback:`🤔 정상적인 코드랍니다.`} ]
  },
  {
    type:'quiz', emoji:'🔁', title:`정해진 만큼 반복하기`, tag:`퀴즈 · 반복문 · 보통`,
    scenario:`\`for\`문을 써서 5번 반복하려고 해요. 알맞은 코드는?`,
    code:`for i in range(___):\n    print('야호!')`,
    choices:[ {text:`5`, correct:true, feedback:`✅ 맞아요! range(5)라고 적으면 0부터 4까지 딱 5번 반복돼요.`}, {text:`1, 5`, correct:false, feedback:`🤔 range(1, 5)는 1, 2, 3, 4로 4번만 반복돼요.`}, {text:`6`, correct:false, feedback:`🤔 range(6)은 6번 반복돼요.`}, {text:`무한대`, correct:false, feedback:`🤔 for문은 정해진 숫자만큼만 반복해요.`} ]
  },
  {
    type:'quiz', emoji:'🎒', title:`리스트에 물건 추가하기`, tag:`퀴즈 · 리스트 · 보통`,
    scenario:`리스트 맨 뒤에 새로운 물건을 추가하고 싶을 때 쓰는 명령어는?`,
    code:`bag = ['지우개']\nbag.____('연필')`,
    choices:[ {text:`append`, correct:true, feedback:`✅ 맞아요! append는 '덧붙이다'라는 뜻으로 맨 뒤에 추가해줘요.`}, {text:`add`, correct:false, feedback:`🤔 add라는 단어도 맞을 것 같지만 파이썬 리스트에서는 append를 써요.`}, {text:`insert`, correct:false, feedback:`🤔 insert는 중간에 끼워넣을 때 쓰고, 위치도 알려줘야 해요.`}, {text:`push`, correct:false, feedback:`🤔 push는 다른 프로그래밍 언어에서 자주 써요.`} ]
  },
  {
    type:'quiz', emoji:'🧮', title:`나머지 구하기`, tag:`퀴즈 · 연산 · 어려움`,
    scenario:`숫자를 나누었을 때 몫이 아니라 '나머지'를 구해주는 연산 기호는?`,
    code:`print(10 ___ 3) # 1이 출력돼야 함`,
    choices:[ {text:`% (퍼센트)`, correct:true, feedback:`✅ 맞아요! %는 나머지를 구해줘서 짝수/홀수 판별할 때 아주 유용해요.`}, {text:`/ (슬래시)`, correct:false, feedback:`🤔 / 는 진짜 나누기를 해서 3.333... 이 나와요.`}, {text:`// (슬래시 두개)`, correct:false, feedback:`🤔 // 는 나누었을 때 '몫'만 구해줘요.`}, {text:`mod`, correct:false, feedback:`🤔 파이썬에서는 글자 대신 % 기호를 써요.`} ]
  },
  {
    type:'quiz', emoji:'🤝', title:`두 조건 모두 만족?`, tag:`퀴즈 · 논리 연산 · 어려움`,
    scenario:`두 가지 조건이 **모두 참(True)**일 때만 실행하게 만들고 싶어요.`,
    code:`if age > 10 ___ height > 140:\n    print('놀이기구 탑승 가능!')`,
    choices:[ {text:`and`, correct:true, feedback:`✅ 맞아요! and는 '그리고' 라는 뜻으로 양쪽 다 참이어야 해요.`}, {text:`or`, correct:false, feedback:`🤔 or는 둘 중 하나만 참이어도 통과시켜 줘요.`}, {text:`with`, correct:false, feedback:`🤔 with는 완전히 다른 곳에서 쓰이는 파이썬 키워드예요.`}, {text:`&&`, correct:false, feedback:`🤔 &&는 파이썬이 아닌 다른 언어에서 쓰는 기호예요.`} ]
  },
  {
    type:'quiz', emoji:'🏃‍♂️', title:`끝나지 않는 질주`, tag:`퀴즈 · 반복문 · 어려움`,
    scenario:`다음 코드는 치명적인 문제가 하나 있어요. 무엇일까요?`,
    code:`n = 0\nwhile n < 5:\n    print('달려!')`,
    choices:[ {text:`n을 더해주지 않아서 영원히 반복된다`, correct:true, feedback:`✅ 빙고! n이 계속 0이라서 영원히 화면에 '달려!'가 찍힐 거예요.`}, {text:`문법 오류가 발생한다`, correct:false, feedback:`🤔 코드는 정상이라 컴퓨터는 그대로 실행해버려요.`}, {text:`한 번도 실행되지 않는다`, correct:false, feedback:`🤔 처음엔 n이 0이라 5보다 작아서 실행은 돼요.`}, {text:`딱 5번만 실행된다`, correct:false, feedback:`🤔 n 값을 바꿔주는 코드가 없어서 5번에서 멈추지 않아요.`} ]
  },
  {
    type:'quiz', emoji:'📦', title:`상자 안의 상자`, tag:`퀴즈 · 리스트 · 어려움`,
    scenario:`리스트 안에 또 리스트가 들어있어요! \`print(box[1][0])\`을 하면 무엇이 나올까요?`,
    code:`box = [ ['사과', '배'], ['강아지', '고양이'] ]`,
    choices:[ {text:`강아지`, correct:true, feedback:`✅ 완벽해요! box[1]은 두 번째 리스트고, 그 안에서 [0]이니까 강아지예요!`}, {text:`사과`, correct:false, feedback:`🤔 사과는 box[0][0] 이랍니다.`}, {text:`고양이`, correct:false, feedback:`🤔 고양이는 box[1][1] 이에요.`}, {text:`오류`, correct:false, feedback:`🤔 리스트 안에 리스트를 넣는 건 아주 흔한 일이랍니다.`} ]
  },
  {
    type:'quiz', emoji:'🧰', title:`함수 호출 횟수`, tag:`퀴즈 · 함수 · 어려움`,
    scenario:`다음 코드를 실행하면 화면에 '야호'가 몇 번 출력될까요?`,
    code:`def shout():\n    print('야호')\n    print('야호')\n\nshout()\nshout()`,
    choices:[ {text:`4번`, correct:true, feedback:`✅ 맞아요! 함수 한 번에 2번 출력되는데, 함수를 2번 불렀으니 총 4번!`}, {text:`2번`, correct:false, feedback:`🤔 shout()를 한 번 부를 때마다 2번씩 출력돼요.`}, {text:`0번`, correct:false, feedback:`🤔 shout()를 두 번 호출했으니 출력이 발생해요.`}, {text:`8번`, correct:false, feedback:`🤔 2 곱하기 2는 4번이에요.`} ]
  },
  {
    type:'quiz', emoji:'🕵️', title:`참인지 거짓인지`, tag:`퀴즈 · 데이터 타입 · 어려움`,
    scenario:`파이썬에서 '맞다(참)' 와 '틀리다(거짓)'를 나타내는 특별한 단어는?`,
    code:`is_raining = ____`,
    choices:[ {text:`True / False`, correct:true, feedback:`✅ 맞아요! 파이썬에서는 무조건 앞글자를 대문자로 써야 해요.`}, {text:`true / false`, correct:false, feedback:`🤔 파이썬은 대문자 소문자를 가려요. 앞글자가 대문자여야 해요.`}, {text:`Yes / No`, correct:false, feedback:`🤔 컴퓨터는 Yes/No 대신 True/False를 써요.`}, {text:`O / X`, correct:false, feedback:`🤔 O, X는 사람이 보기 편한 기호일 뿐이에요.`} ]
  },
  {
    type:'write', emoji:'✍️', title:`화면에 글자 띄우기`, tag:`직접 작성 · 쉬움`,
    scenario:`화면에 **나는 코딩 왕!** 이라고 출력되도록 코드를 한 줄로 작성해보세요.`,
    targetLabel:`나는 코딩 왕!`,
    placeholder:`print(?)`,
    hint:`💡 print() 괄호 안에 따옴표를 잊지 마세요!`,
    sampleAnswer:`print('나는 코딩 왕!')`,
    validate:(code)=>{ const norm = code.replace(/[’‘]/g,"'^").trim(); return /^print\(\s*["']나는 코딩 왕!["']\s*\)$/.test(norm); }
  },
  {
    type:'write', emoji:'✍️', title:`변수에 숫자 넣기`, tag:`직접 작성 · 쉬움`,
    scenario:`\`my_money\`라는 변수를 만들고 숫자 **5000**을 넣은 다음 출력해보세요. (두 줄로 작성)`,
    targetLabel:`5000`,
    placeholder:`my_money = ?\nprint(?)`,
    hint:`💡 첫째 줄에 변수를 만들고 값을 넣어요. 둘째 줄에서 print()로 꺼내요.`,
    sampleAnswer:`my_money = 5000\nprint(my_money)`,
    validate:(code)=>{ const lines = code.split('\n').map(l=>l.trim()).filter(Boolean); return lines.length>=2 && /^my_money\s*=\s*5000$/.test(lines[0]) && /^print\(\s*my_money\s*\)$/.test(lines[1]); }
  },
  {
    type:'write', emoji:'✍️', title:`간단한 뺄셈 계산기`, tag:`직접 작성 · 쉬움`,
    scenario:`파이썬이 대신 계산하게 해볼까요? 100 빼기 35의 결과를 출력하는 코드를 한 줄로 작성하세요.`,
    targetLabel:`65`,
    placeholder:``,
    hint:`💡 print() 안에 100 - 35 를 따옴표 없이 그대로 적어보세요.`,
    sampleAnswer:`print(100 - 35)`,
    validate:(code)=>{ const norm = code.replace(/[’‘]/g,"'^").trim(); return /^print\(\s*100\s*-\s*35\s*\)$/.test(norm); }
  },
  {
    type:'write', emoji:'✍️', title:`글자 이어 붙이기`, tag:`직접 작성 · 쉬움`,
    scenario:`'바나나'와 '우유'라는 글자를 \`+\` 기호로 이어 붙여서 출력해보세요.`,
    targetLabel:`바나나우유`,
    placeholder:``,
    hint:`💡 print('바나나' + '우유') 처럼 작성하면 돼요.`,
    sampleAnswer:`print('바나나' + '우유')`,
    validate:(code)=>{ const norm = code.replace(/[’‘]/g,"'^").trim(); return /^print\(\s*["']바나나["']\s*\+\s*["']우유["']\s*\)$/.test(norm); }
  },
  {
    type:'write', emoji:'✍️', title:`반가워 리스트`, tag:`직접 작성 · 쉬움`,
    scenario:`\`animals\` 라는 이름의 리스트를 만들고, 그 안에 '사자'와 '호랑이'를 담아보세요. (출력은 안 해도 됨)`,
    targetLabel:`(출력 없음)`,
    placeholder:`animals = [?, ?]`,
    hint:`💡 리스트는 대괄호 [ ] 를 쓰고 쉼표 , 로 구분해요.`,
    sampleAnswer:`animals = ['사자', '호랑이']`,
    validate:(code)=>{ const norm = code.replace(/[’‘]/g,"'^").trim(); return /^animals\s*=\s*\[\s*["']사자["']\s*,\s*["']호랑이["']\s*\]$/.test(norm); }
  },
  {
    type:'write', emoji:'✍️', title:`만약에 진짜라면!`, tag:`직접 작성 · 쉬움`,
    scenario:`변수 \`x\`가 5와 같다면 '정답'이라고 출력하는 코드를 완성하세요.`,
    targetLabel:`정답`,
    placeholder:`x = 5\nif x == 5:\n    print(?)`,
    hint:`💡 if문 아래 코드는 스페이스바 4칸 들여쓰기가 되어 있어야 해요.`,
    sampleAnswer:`x = 5\nif x == 5:\n    print('정답')`,
    validate:(code)=>{ return /x\s*=\s*5/.test(code) && /if\s*x\s*==\s*5\s*:/.test(code) && /print\(\s*["']정답["']\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`똑같은 말 3번 반복`, tag:`직접 작성 · 쉬움`,
    scenario:`\`for\`문을 사용해서 '파이썬 최고'라는 글자를 화면에 3번 출력해보세요.`,
    targetLabel:`파이썬 최고\n파이썬 최고\n파이썬 최고`,
    placeholder:`for i in range(?):\n    print(?)`,
    hint:`💡 range(3)을 쓰면 3번 반복된답니다.`,
    sampleAnswer:`for i in range(3):\n    print('파이썬 최고')`,
    validate:(code)=>{ return /for\s+\w+\s+in\s+range\(\s*3\s*\)\s*:/.test(code) && /print\(\s*["']파이썬 최고["']\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`동물 친구 추가하기`, tag:`직접 작성 · 보통`,
    scenario:`\`animals = ['강아지']\` 가 있습니다. 여기에 \`append\`를 써서 '고양이'를 추가하고 리스트 전체를 출력해보세요.`,
    targetLabel:`['강아지', '고양이']`,
    placeholder:`animals = ['강아지']\n# 여기에 고양이 추가\nprint(animals)`,
    hint:`💡 animals.append('고양이') 를 중간에 넣어보세요.`,
    sampleAnswer:`animals = ['강아지']\nanimals.append('고양이')\nprint(animals)`,
    validate:(code)=>{ const lines = code.split('\n').map(l=>l.trim()).filter(Boolean); return lines.length>=3 && /animals\.append\(\s*["']고양이["']\s*\)/.test(code) && /print\(\s*animals\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`비밀번호 검사기`, tag:`직접 작성 · 보통`,
    scenario:`변수 \`pw\`에 1234가 들어있습니다. \`pw == 1234\`면 '환영합니다', 아니면 '누구세요'를 출력하는 코드를 짜보세요.`,
    targetLabel:`환영합니다`,
    placeholder:`pw = 1234\nif pw == 1234:\n    print(?)\nelse:\n    print(?)`,
    hint:`💡 if와 else 안에 각각 맞는 print를 적어주세요.`,
    sampleAnswer:`pw = 1234\nif pw == 1234:\n    print('환영합니다')\nelse:\n    print('누구세요')`,
    validate:(code)=>{ return /if\s*pw\s*==\s*1234\s*:/.test(code) && /print\(\s*["']환영합니다["']\s*\)/.test(code) && /else\s*:/.test(code) && /print\(\s*["']누구세요["']\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`리스트 크기 확인`, tag:`직접 작성 · 보통`,
    scenario:`과자가 4개 든 리스트 \`snacks = ['홈런볼', '감자깡', '새우깡', '양파링']\` 이 있어요. 이 리스트의 길이를 출력하세요.`,
    targetLabel:`4`,
    placeholder:`snacks = ['홈런볼', '감자깡', '새우깡', '양파링']\n# 길이를 재서 출력하세요`,
    hint:`💡 print(len(snacks)) 를 쓰면 리스트의 크기를 출력할 수 있어요.`,
    sampleAnswer:`snacks = ['홈런볼', '감자깡', '새우깡', '양파링']\nprint(len(snacks))`,
    validate:(code)=>{ return /print\(\s*len\(\s*snacks\s*\)\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`짝수/홀수 판독기`, tag:`직접 작성 · 보통`,
    scenario:`변수 \`num = 7\`이 홀수인지 짝수인지 판별하는 코드를 \`if else\` 와 \`%\` 연산자를 써서 작성하세요.`,
    targetLabel:`홀수`,
    placeholder:`num = 7\nif num % 2 == 0:\n    print('짝수')\nelse:\n    print('홀수')`,
    hint:`💡 2로 나눈 나머지가 0이면 짝수, 아니면 홀수예요. 코드를 끝까지 완성해보세요.`,
    sampleAnswer:`num = 7\nif num % 2 == 0:\n    print('짝수')\nelse:\n    print('홀수')`,
    validate:(code)=>{ return /if\s+num\s*%\s*2\s*==\s*0\s*:/.test(code) && /else\s*:/.test(code) && /print\(\s*["']홀수["']\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`리스트 항목 하나씩 꺼내기`, tag:`직접 작성 · 보통`,
    scenario:`\`colors = ['빨강', '파랑', '초록']\` 리스트가 있어요. \`for\`문을 써서 항목들을 한 줄에 하나씩 출력하세요.`,
    targetLabel:`빨강\n파랑\n초록`,
    placeholder:`colors = ['빨강', '파랑', '초록']\nfor c in colors:\n    print(?)`,
    hint:`💡 for c in colors: 라고 썼으니, 변수 c를 그냥 출력하면 돼요.`,
    sampleAnswer:`colors = ['빨강', '파랑', '초록']\nfor c in colors:\n    print(c)`,
    validate:(code)=>{ return /for\s+\w+\s+in\s+colors\s*:/.test(code) && /print\(\s*\w+\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`문자열 곱하기`, tag:`직접 작성 · 보통`,
    scenario:`파이썬에서는 글자에 숫자를 곱하면 그만큼 반복돼요! '안녕'을 5번 곱해서 출력하는 코드를 짜보세요.`,
    targetLabel:`안녕안녕안녕안녕안녕`,
    placeholder:``,
    hint:`💡 print('안녕' * 5) 라고 쓰면 간단하게 해결!`,
    sampleAnswer:`print('안녕' * 5)`,
    validate:(code)=>{ const norm = code.replace(/[’‘]/g,"'^").trim(); return /^print\(\s*["']안녕["']\s*\*\s*5\s*\)$/.test(norm); }
  },
  {
    type:'write', emoji:'✍️', title:`나이 제한 확인`, tag:`직접 작성 · 보통`,
    scenario:`\`age = 15\` 이고 \`height = 150\` 입니다. 나이가 12 이상 **그리고** 키가 140 이상이면 '탑승'을 출력하세요.`,
    targetLabel:`탑승`,
    placeholder:`age = 15\nheight = 150\nif age >= 12 and height >= 140:\n    print(?)`,
    hint:`💡 조건문 안에 and 를 써서 두 조건이 모두 맞을 때 print('탑승')을 하세요.`,
    sampleAnswer:`age = 15\nheight = 150\nif age >= 12 and height >= 140:\n    print('탑승')`,
    validate:(code)=>{ return /if\s+age\s*>=\s*12\s+and\s+height\s*>=\s*140\s*:/.test(code) && /print\(\s*["']탑승["']\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`while 카운트다운`, tag:`직접 작성 · 어려움`,
    scenario:`\`while\` 반복문을 사용해 변수 \`n\`을 3부터 1까지 거꾸로 출력하고, 마지막에 '발사!'를 출력하세요.`,
    targetLabel:`3\n2\n1\n발사!`,
    placeholder:`n = 3\nwhile n > 0:\n    print(n)\n    n = n - 1\n# while문이 끝난 뒤\nprint('발사!')`,
    hint:`💡 while문 안에서 n을 1씩 줄여주어야 무한 반복을 피할 수 있어요. '발사!'는 들여쓰기를 하지 않아야 반복이 끝난 후 나옵니다.`,
    sampleAnswer:`n = 3\nwhile n > 0:\n    print(n)\n    n = n - 1\nprint('발사!')`,
    validate:(code)=>{ return /while\s+n\s*>\s*0\s*:/.test(code) && /n\s*=\s*n\s*-\s*1/.test(code) && /print\(\s*["']발사!["']\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`큰 수만 골라내기`, tag:`직접 작성 · 어려움`,
    scenario:`\`nums = [2, 7, 4, 9, 1]\` 리스트가 있습니다. \`for\`문과 \`if\`문을 섞어서 5보다 큰 숫자만 골라 출력하세요.`,
    targetLabel:`7\n9`,
    placeholder:`nums = [2, 7, 4, 9, 1]\nfor n in nums:\n    if n > 5:\n        print(n)`,
    hint:`💡 for문 안쪽에 if문이 들어가야 하므로, if 안쪽의 print는 총 8칸 띄어쓰기(들여쓰기 두 번)를 해야 해요.`,
    sampleAnswer:`nums = [2, 7, 4, 9, 1]\nfor n in nums:\n    if n > 5:\n        print(n)`,
    validate:(code)=>{ return /for\s+\w+\s+in\s+nums\s*:/.test(code) && /if\s+\w+\s*>\s*5\s*:/.test(code) && /print\(\s*\w+\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`리스트 총합 구하기`, tag:`직접 작성 · 어려움`,
    scenario:`\`scores = [10, 20, 30]\` 리스트의 모든 숫자를 더한 결과를 출력하고 싶어요. 변수 \`total = 0\`을 만들고 for문으로 더해보세요.`,
    targetLabel:`60`,
    placeholder:`scores = [10, 20, 30]\ntotal = 0\nfor s in scores:\n    total = total + s\nprint(total)`,
    hint:`💡 for문 안에서 하나씩 꺼낸 값을 total에 계속 누적해서 더해주면 돼요.`,
    sampleAnswer:`scores = [10, 20, 30]\ntotal = 0\nfor s in scores:\n    total = total + s\nprint(total)`,
    validate:(code)=>{ return /total\s*=\s*total\s*\+\s*\w+/.test(code) && /print\(\s*total\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`나만의 함수 만들기`, tag:`직접 작성 · 어려움`,
    scenario:`\`hello()\` 라는 함수를 만들어서, 그 함수를 부르면 '안녕하세요'가 2번 나오게 작성한 후 맨 마지막에 호출하세요.`,
    targetLabel:`안녕하세요\n안녕하세요`,
    placeholder:`def hello():\n    print('안녕하세요')\n    print('안녕하세요')\n\nhello()`,
    hint:`💡 def 함수이름(): 로 시작하고, 들여쓰기를 한 뒤 코드를 적어요. 마지막엔 꼭 함수이름() 으로 불러줘야 실행돼요.`,
    sampleAnswer:`def hello():\n    print('안녕하세요')\n    print('안녕하세요')\nhello()`,
    validate:(code)=>{ return /def\s+hello\(\)\s*:/.test(code) && /hello\(\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`매개변수 함수 만들기`, tag:`직접 작성 · 어려움`,
    scenario:`두 숫자를 받아서 더한 값을 출력하는 함수 \`add(a, b)\`를 만들고, \`add(3, 4)\`를 호출해 7이 나오게 해보세요.`,
    targetLabel:`7`,
    placeholder:`def add(a, b):\n    print(a + b)\n\nadd(3, 4)`,
    hint:`💡 괄호 안에 a, b 를 넣어서 바깥에서 숫자를 던져줄 수 있는 문(매개변수)을 만들 수 있어요.`,
    sampleAnswer:`def add(a, b):\n    print(a + b)\nadd(3, 4)`,
    validate:(code)=>{ return /def\s+add\(a\s*,\s*b\)\s*:/.test(code) && /print\(\s*a\s*\+\s*b\s*\)/.test(code) && /add\(\s*3\s*,\s*4\s*\)/.test(code); }
  },
  {
    type:'write', emoji:'✍️', title:`1부터 10까지 짝수만`, tag:`직접 작성 · 어려움`,
    scenario:`\`for i in range(1, 11):\` 을 쓰면 1부터 10까지 반복돼요. 그 안에서 \`if\`문을 써서 짝수만 출력되게 하세요.`,
    targetLabel:`2\n4\n6\n8\n10`,
    placeholder:`for i in range(1, 11):\n    if i % 2 == 0:\n        print(i)`,
    hint:`💡 반복문 안의 조건문 구조를 완벽하게 작성해야 해요. 들여쓰기 4칸, 8칸을 꼭 지키세요!`,
    sampleAnswer:`for i in range(1, 11):\n    if i % 2 == 0:\n        print(i)`,
    validate:(code)=>{ return /for\s+i\s+in\s+range\(\s*1\s*,\s*11\s*\)\s*:/.test(code) && /if\s+i\s*%\s*2\s*==\s*0\s*:/.test(code) && /print\(\s*i\s*\)/.test(code); }
  }
];
const problemState = PROBLEMS.map(()=>false);

const CONCEPT_PROBLEMS = [{"q": "파이썬에서 문자를 출력할 때는 반드시 따옴표('', \"\")로 감싸야 한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "파이썬은 대문자와 소문자를 구별하지 않는다. (A와 a는 같다)", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1}, {"q": "변수는 숫자나 문자를 담아두는 '상자'와 같다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "a = 5 라고 쓰면, 'a와 5가 똑같다'는 뜻이다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1}, {"q": "파이썬에서 '같다'를 비교할 때는 == 기호를 사용한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "여러 개의 데이터를 하나의 상자에 담는 것을 리스트(List)라고 한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "리스트의 첫 번째 물건을 꺼낼 때는 인덱스 번호 1을 사용한다. (예: list[1])", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1}, {"q": "if문 아래에 있는 코드는 반드시 '들여쓰기(스페이스 4칸)'를 해야 실행된다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "if문의 조건이 틀렸을 때(거짓일 때) 실행되는 부분은 else 이다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "for문은 정해진 횟수만큼 코드를 반복할 때 사용한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "while문은 특정 조건이 참(True)인 동안 무한히 반복한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "파이썬에서 곱하기를 할 때는 x 알파벳을 사용한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1}, {"q": "10을 3으로 나눈 '나머지'를 구하고 싶을 때는 10 % 3 이라고 쓴다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "def는 나만의 새로운 함수(명령어)를 만들 때 사용하는 키워드이다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0}, {"q": "파이썬에서 컴퓨터에게 명령을 내릴 때 소문자 true나 false를 써도 된다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1}];
const TYPING_SNIPPETS = [
  {"title": "출력하기 (기초)", "code": "print('Hello, World!')\nprint('안녕, 파이썬!')"},
  {"title": "변수 만들기", "code": "name = '파이'\nage = 12\nprint(name, age)"},
  {"title": "사칙연산", "code": "a = 10\nb = 3\nprint(a + b)\nprint(a * b)"},
  {"title": "리스트 (목록)", "code": "fruits = ['사과', '바나나']\nfruits.append('포도')\nprint(fruits[0])"},
  {"title": "조건문 (if)", "code": "score = 85\nif score >= 80:\n    print('합격')\nelse:\n    print('불합격')"},
  {"title": "반복문 (for)", "code": "for i in range(3):\n    print('파이썬 최고!')\n\nfor f in fruits:\n    print(f)"},
  {"title": "반복문 (while)", "code": "count = 3\nwhile count > 0:\n    print(count)\n    count = count - 1"},
  {"title": "함수 만들기", "code": "def add(x, y):\n    return x + y\n\nresult = add(5, 7)\nprint(result)"},
  {"title": "모듈 사용하기", "code": "import random\nnum = random.randint(1, 10)\nprint(num)"},
  {"title": "종합 복습 마스터", "code": "def check_even(n):\n    if n % 2 == 0:\n        return True\n    return False\n\nprint(check_even(4))"}
];

const MOCK_EXAMS = [[{"q": "화면에 '안녕'을 출력하려고 합니다. 알맞은 코드는?", "choices": ["print('안녕')", "show('안녕')", "write('안녕')", "say('안녕')"], "answer": 0}, {"q": "변수 `age`에 숫자 12를 넣으려면?", "choices": ["age = 12", "age == 12", "12 = age", "age <- 12"], "answer": 0}, {"q": "변수의 이름으로 사용할 수 없는 것은?", "choices": ["1number (숫자로 시작)", "my_score", "name", "age2"], "answer": 0}, {"q": "print(10 + 5) 의 결과는?", "choices": ["15", "105", "10+5", "오류"], "answer": 0}, {"q": "print('파이썬' + '최고') 의 결과는?", "choices": ["파이썬최고", "파이썬 최고", "오류", "아무것도 안나옴"], "answer": 0}, {"q": "파이썬에서 주석(메모)을 달 때 사용하는 기호는?", "choices": ["#", "//", "<!--", "--"], "answer": 0}, {"q": "x = 5\\ny = 3\\nprint(x * y) 의 결과는?", "choices": ["15", "8", "53", "오류"], "answer": 0}, {"q": "문자열을 나타낼 때 쓸 수 있는 기호는?", "choices": ["따옴표('', \"\")", "괄호(())", "대괄호([])", "중괄호({})"], "answer": 0}, {"q": "파이썬에서 변수를 만드는 올바른 방법은?", "choices": ["이름 = 값", "값 = 이름", "변수 이름", "만들기 변수"], "answer": 0}, {"q": "다음 중 성격이 다른 하나는?", "choices": ["100 (숫자)", "'100' (문자열)", "'안녕'", "'사과'"], "answer": 0}], [{"q": "파이썬에서 10을 3으로 나눈 '몫'만 구하는 기호는?", "choices": ["//", "/", "%", "mod"], "answer": 0}, {"q": "파이썬에서 10을 3으로 나눈 '나머지'를 구하는 기호는?", "choices": ["%", "/", "//", "mod"], "answer": 0}, {"q": "print('하하' * 3) 의 결과는?", "choices": ["하하하하하하", "하하3", "하하 하하 하하", "오류"], "answer": 0}, {"q": "변수 a에 담긴 값이 숫자인지 문자인지 헷갈립니다. 확인하는 함수는?", "choices": ["type(a)", "check(a)", "find(a)", "what(a)"], "answer": 0}, {"q": "문자열 '123'을 진짜 숫자 123으로 바꾸는 함수는?", "choices": ["int()", "str()", "num()", "math()"], "answer": 0}, {"q": "숫자 456을 문자열 '456'으로 바꾸는 함수는?", "choices": ["str()", "string()", "word()", "int()"], "answer": 0}, {"q": "a = 2\\nb = 3\\nprint(a ** b) 의 결과는? (2의 3제곱)", "choices": ["8", "6", "5", "9"], "answer": 0}, {"q": "파이썬에서 '같지 않다'를 뜻하는 비교 기호는?", "choices": ["!=", "==", "<>", "not="], "answer": 0}, {"q": "10 >= 5 의 결과는 참(True)인가요 거짓(False)인가요?", "choices": ["True", "False", "10", "5"], "answer": 0}, {"q": "True 와 False의 첫 글자는 반드시 어떻게 써야 하나요?", "choices": ["대문자", "소문자", "상관없음", "기호로 쓴다"], "answer": 0}], [{"q": "리스트를 만들 때 사용하는 괄호는?", "choices": ["[ ]", "( )", "{ }", "< >"], "answer": 0}, {"q": "리스트 a = ['사과', '바나나', '포도'] 가 있습니다. '사과'를 꺼내는 코드는?", "choices": ["a[0]", "a[1]", "a[사과]", "a.first()"], "answer": 0}, {"q": "a = [10, 20, 30] 일 때, a[2] 의 값은?", "choices": ["30", "20", "10", "오류"], "answer": 0}, {"q": "리스트의 맨 끝에 새로운 항목을 추가하는 명령어는?", "choices": ["append()", "add()", "insert()", "push()"], "answer": 0}, {"q": "리스트의 길이를 알아내는 함수는?", "choices": ["len()", "size()", "count()", "length()"], "answer": 0}, {"q": "a = [1, 2, 3] 이고 b = [4, 5] 일 때, a + b 의 결과는?", "choices": ["[1, 2, 3, 4, 5]", "15", "오류", "[[1, 2, 3], [4, 5]]"], "answer": 0}, {"q": "a = ['월', '화', '수'] 일 때 맨 마지막 항목을 뜻하는 인덱스는?", "choices": ["-1", "3", "last", "end"], "answer": 0}, {"q": "리스트에서 특정 위치의 항목을 삭제하는 키워드는?", "choices": ["del", "remove()", "pop()", "셋 다 가능함"], "answer": 3}, {"q": "리스트 안에 리스트가 들어갈 수 있나요? (예: a = [[1,2], [3,4]])", "choices": ["가능하다", "불가능하다", "숫자만 가능하다", "에러가 난다"], "answer": 0}, {"q": "파이썬 인덱스 번호는 항상 몇 번부터 시작하나요?", "choices": ["0번", "1번", "상관없음", "-1번"], "answer": 0}], [{"q": "if문을 작성할 때 조건 끝에 반드시 찍어야 하는 기호는?", "choices": [": (콜론)", "; (세미콜론)", ". (마침표)", "아무것도 안 찍음"], "answer": 0}, {"q": "if문 안쪽에 속한 코드를 쓰려면 어떻게 해야 하나요?", "choices": ["들여쓰기(스페이스 4칸)", "대괄호로 감싸기", "한 줄 띄우기", "따옴표 치기"], "answer": 0}, {"q": "if 조건이 거짓(False)일 때 실행할 내용을 적는 곳은?", "choices": ["else:", "if not:", "false:", "other:"], "answer": 0}, {"q": "score = 80 일 때, if score >= 90: 은 어떻게 될까요?", "choices": ["실행되지 않는다", "실행된다", "에러가 난다", "90으로 바뀐다"], "answer": 0}, {"q": "조건이 3개 이상일 때 사용하는 키워드는? (if -> ? -> else)", "choices": ["elif", "else if", "if else", "elseif"], "answer": 0}, {"q": "x = 10 이 홀수인지 짝수인지 확인하려면 어떤 기호를 쓸까요?", "choices": ["x % 2 == 0", "x / 2 == 0", "x // 2 == 0", "x * 2 == 0"], "answer": 0}, {"q": "if a == b: 의 뜻은 무엇인가요?", "choices": ["a와 b가 같다면", "a에 b를 넣어라", "a와 b가 다르다면", "a가 b보다 크다면"], "answer": 0}, {"q": "파이썬에서 '들여쓰기'가 잘못되면 어떻게 되나요?", "choices": ["IndentationError(오류)가 난다", "그냥 무시하고 실행된다", "컴퓨터가 알아서 고친다", "실행 속도가 느려진다"], "answer": 0}, {"q": "if True: 아래의 코드는 어떻게 될까요?", "choices": ["무조건 실행된다", "절대 실행되지 않는다", "에러가 난다", "한 번만 무시된다"], "answer": 0}, {"q": "비밀번호 검사 코드로 적절한 것은?", "choices": ["if pw == '1234':", "if pw = '1234':", "if pw === '1234':", "if pw => '1234':"], "answer": 0}], [{"q": "두 조건이 '모두' 참이어야 통과시키는 키워드는?", "choices": ["and", "or", "not", "both"], "answer": 0}, {"q": "두 조건 중 '하나만' 참이어도 통과시키는 키워드는?", "choices": ["or", "and", "not", "any"], "answer": 0}, {"q": "조건을 반대로(참을 거짓으로, 거짓을 참으로) 뒤집는 키워드는?", "choices": ["not", "reverse", "flip", "!"], "answer": 0}, {"q": "age = 15, height = 150 입니다. (age >= 12 and height >= 140) 의 결과는?", "choices": ["True", "False", "에러", "숫자 150"], "answer": 0}, {"q": "score = 80 입니다. (score > 90 or score == 80) 의 결과는?", "choices": ["True", "False", "에러", "숫자 80"], "answer": 0}, {"q": "not (5 > 10) 의 결과는?", "choices": ["True", "False", "에러", "숫자 5"], "answer": 0}, {"q": "'사과' in ['사과', '바나나'] 의 결과는? (in 연산자)", "choices": ["True", "False", "에러", "'사과'"], "answer": 0}, {"q": "'포도' not in ['사과', '바나나'] 의 결과는?", "choices": ["True", "False", "에러", "'포도'"], "answer": 0}, {"q": "놀이기구 탑승: 나이 10살 이상, 키 120 이상. 적절한 코드는?", "choices": ["age >= 10 and height >= 120", "age >= 10 or height >= 120", "age > 10 and height > 120", "age > 10 or height > 120"], "answer": 0}, {"q": "if문 조건에 and와 or를 같이 쓸 수 있나요?", "choices": ["네, 여러 개 연결해서 쓸 수 있어요.", "아니요, 하나만 써야 해요.", "에러가 납니다.", "파이썬에서는 불가능합니다."], "answer": 0}], [{"q": "정해진 횟수만큼 반복할 때 사용하는 키워드는?", "choices": ["for", "while", "if", "def"], "answer": 0}, {"q": "for i in range(5): 는 몇 번 반복될까요?", "choices": ["5번 (0,1,2,3,4)", "6번 (0~5)", "4번 (1~4)", "5번 (1~5)"], "answer": 0}, {"q": "range(1, 4) 가 만들어내는 숫자는?", "choices": ["1, 2, 3", "1, 2, 3, 4", "0, 1, 2, 3", "0, 1, 2, 3, 4"], "answer": 0}, {"q": "range(0, 10, 2) 의 2는 무슨 뜻인가요?", "choices": ["2씩 건너뛰며(짝수)", "2번만 반복", "2부터 시작", "2로 나누기"], "answer": 0}, {"q": "for i in range(3): 안에서 print('안녕') 을 쓰면 안녕은 몇 번 나올까요?", "choices": ["3번", "4번", "2번", "1번"], "answer": 0}, {"q": "for문도 끝에 콜론(:)을 찍어야 하나요?", "choices": ["네, 반드시 찍어야 합니다.", "아니요, 안 찍어도 됩니다.", "if문만 찍습니다.", "세미콜론(;)을 찍습니다."], "answer": 0}, {"q": "for문 안쪽에 있는 코드는 어떻게 구별하나요?", "choices": ["들여쓰기(스페이스 4칸)", "대괄호 묶기", "번호 매기기", "색깔 칠하기"], "answer": 0}, {"q": "for i in 'Hello': 처럼 글자를 넣으면 어떻게 되나요?", "choices": ["H, e, l, l, o 한 글자씩 반복됩니다.", "에러가 납니다.", "Hello 전체가 1번 반복됩니다.", "무한 반복됩니다."], "answer": 0}, {"q": "반복을 돌다가 중간에 아예 멈추고(탈출하고) 싶을 때 쓰는 키워드는?", "choices": ["break", "stop", "exit", "quit"], "answer": 0}, {"q": "반복을 돌다가 이번 순서만 건너뛰고 다음으로 넘어가고 싶을 때는?", "choices": ["continue", "pass", "skip", "next"], "answer": 0}], [{"q": "fruits = ['사과', '바나나', '포도'] 일 때, 모든 과일을 하나씩 출력하려면?", "choices": ["for f in fruits: print(f)", "for fruits: print(f)", "print(fruits)", "for f in range(fruits):"], "answer": 0}, {"q": "nums = [1, 2, 3]\\nfor n in nums:\\n    print(n * 10)\\n결과는?", "choices": ["10, 20, 30", "1, 2, 3", "102030", "에러"], "answer": 0}, {"q": "리스트의 총합(다 더한 값)을 구할 때, 처음에 total 변수를 얼마로 만들어야 할까요?", "choices": ["0", "1", "10", "빈 리스트"], "answer": 0}, {"q": "scores = [80, 90, 100]\\nfor s in scores:\\n    if s >= 90:\\n        print('합격')\\n합격은 몇 번 출력될까요?", "choices": ["2번", "3번", "1번", "0번"], "answer": 0}, {"q": "for i in range(len(a)): 에서 len(a)는 무슨 역할인가요?", "choices": ["리스트 a의 길이만큼 반복하기 위해", "a를 지우기 위해", "a를 숫자 0으로 바꾸기 위해", "아무 의미 없음"], "answer": 0}, {"q": "리스트를 반복하면서 번호(인덱스)와 값을 같이 꺼내주는 마법의 함수는?", "choices": ["enumerate()", "number()", "zip()", "list()"], "answer": 0}, {"q": "짝수만 골라서 새 리스트에 넣고 싶을 때 사용하는 방법은?", "choices": ["for문과 if문을 섞어 쓴다.", "for문만 쓰면 된다.", "if문만 쓰면 된다.", "리스트는 원래 짝수만 담긴다."], "answer": 0}, {"q": "반복문 안에서 append() 를 쓰면 어떻게 되나요?", "choices": ["리스트에 여러 개의 값이 계속 추가된다.", "에러가 난다.", "리스트가 초기화된다.", "맨 앞의 값이 지워진다."], "answer": 0}, {"q": "a = []\\nfor i in range(3):\\n    a.append(i)\\nprint(a) 의 결과는?", "choices": ["[0, 1, 2]", "[1, 2, 3]", "[3, 3, 3]", "오류"], "answer": 0}, {"q": "문자열 'Python'도 리스트처럼 for문에 넣을 수 있나요?", "choices": ["네, 한 글자씩 출력됩니다.", "아니요, 문자열은 안 됩니다.", "에러가 납니다.", "숫자만 가능합니다."], "answer": 0}], [{"q": "while문의 뜻은 무엇인가요?", "choices": ["~하는 동안 계속해라", "만약 ~라면", "모든 요소에 대해", "정해진 횟수만큼"], "answer": 0}, {"q": "while True: 는 무슨 뜻일까요?", "choices": ["조건이 항상 참이므로 무한히 반복해라", "한 번만 실행해라", "에러가 난다", "조건이 틀렸다"], "answer": 0}, {"q": "n = 0\\nwhile n < 3:\\n    print(n)\\n    n = n + 1\\n결과는?", "choices": ["0, 1, 2", "1, 2, 3", "0, 1, 2, 3", "무한 반복"], "answer": 0}, {"q": "위 문제에서 n = n + 1 이 없다면 어떻게 되나요?", "choices": ["0이 무한히 출력된다 (무한 루프)", "아무것도 안 나온다", "에러가 난다", "한 번만 출력된다"], "answer": 0}, {"q": "사용자가 '종료'를 입력할 때까지 계속 물어보려면 어떤 반복문을 쓸까요?", "choices": ["while문", "for문", "if문", "def문"], "answer": 0}, {"q": "while문을 즉시 멈추고 빠져나오는(부수고 나오는) 명령어는?", "choices": ["break", "stop", "exit", "quit"], "answer": 0}, {"q": "while문에서 continue를 만나면 어떻게 되나요?", "choices": ["아래 코드를 무시하고 조건 검사(맨 위)로 돌아간다", "반복문이 아예 끝난다", "프로그램이 종료된다", "에러가 난다"], "answer": 0}, {"q": "while n > 0: 은 n이 어떨 때 반복하나요?", "choices": ["0보다 클 때 (양수일 때)", "0일 때", "0보다 작을 때", "0과 같거나 클 때"], "answer": 0}, {"q": "카운트다운을 만들려면 n = n - 1 을 넣어야 할까요?", "choices": ["네, 값을 줄여나가야 합니다.", "아니요, 값을 더해야 합니다.", "변하지 않게 둡니다.", "0으로 만듭니다."], "answer": 0}, {"q": "파이썬 게임(Pygame)에서 게임이 계속 켜져있게 하는 심장 역할은?", "choices": ["while True:", "for i in range(100):", "if True:", "def game():"], "answer": 0}], [{"q": "파이썬에서 나만의 함수를 만들 때 시작하는 단어는?", "choices": ["def", "function", "make", "fun"], "answer": 0}, {"q": "함수의 이름을 지을 때 지켜야 할 것은?", "choices": ["띄어쓰기를 하지 않는다 (대신 밑줄_ 사용)", "무조건 한글로 짓는다", "숫자로 시작해야 한다", "기호를 맘껏 쓴다"], "answer": 0}, {"q": "def hello():\\n    print('안녕')\\n을 만들었습니다. 어떻게 실행(호출)하나요?", "choices": ["hello()", "hello", "run(hello)", "def hello"], "answer": 0}, {"q": "함수 안으로 던져주는 값(예: add(3, 4)의 3과 4)을 담는 상자를 무엇이라 하나요?", "choices": ["매개변수 (파라미터)", "리스트", "조건문", "반환값"], "answer": 0}, {"q": "함수가 계산을 다 하고 결과를 밖으로 던져줄(뱉어줄) 때 쓰는 키워드는?", "choices": ["return", "give", "send", "throw"], "answer": 0}, {"q": "def add(a, b):\\n    return a + b\\nprint(add(2, 3)) 의 결과는?", "choices": ["5", "23", "a+b", "오류"], "answer": 0}, {"q": "함수를 쓰는 가장 큰 이유는 무엇일까요?", "choices": ["똑같은 코드를 여러 번 쓰지 않고 재사용하려고", "프로그램 속도를 늦추려고", "코드를 어렵게 보이려고", "에러를 만들려고"], "answer": 0}, {"q": "return을 만나면 함수는 어떻게 되나요?", "choices": ["값을 던져주고 함수는 즉시 끝난다", "계속 아래 코드를 실행한다", "무한 반복된다", "에러가 난다"], "answer": 0}, {"q": "파이썬에 원래 들어있는 내장 함수가 아닌 것은?", "choices": ["make_pizza()", "print()", "len()", "type()"], "answer": 0}, {"q": "함수 안에서 만들어진 변수는 함수 밖에서도 쓸 수 있나요?", "choices": ["아니요, 함수가 끝나면 사라집니다 (지역변수).", "네, 언제든 쓸 수 있습니다.", "비밀번호를 입력해야 합니다.", "모릅니다."], "answer": 0}], [{"q": "다음 중 성격이 완전 다른 자료형은?", "choices": ["[1, 2, 3] (리스트)", "'123' (문자열)", "123 (정수)", "True (불리언)"], "answer": 0}, {"q": "a = 5\\na += 2\\nprint(a) 의 결과는?", "choices": ["7", "2", "52", "오류"], "answer": 0}, {"q": "빈 리스트를 만드는 올바른 코드는?", "choices": ["a = []", "a = 0", "a = ''", "a = None"], "answer": 0}, {"q": "파이썬에서 '주석'이 하는 역할은?", "choices": ["메모를 남긴다 (컴퓨터는 무시함)", "화면에 출력한다", "에러를 고친다", "반복한다"], "answer": 0}, {"q": "문자열 '사과'의 길이는 len('사과')로 구하면 얼마인가요?", "choices": ["2", "1", "4", "0"], "answer": 0}, {"q": "print(10 == 10 and 5 > 1) 의 결과는?", "choices": ["True", "False", "에러", "10"], "answer": 0}, {"q": "x가 10보다 크거나 5보다 작을 때를 나타내는 조건식은?", "choices": ["x > 10 or x < 5", "x > 10 and x < 5", "x >= 10 and x <= 5", "10 < x < 5"], "answer": 0}, {"q": "while문을 멈추게 하는 코드는?", "choices": ["break", "stop", "continue", "return"], "answer": 0}, {"q": "리스트 요소들을 거꾸로 뒤집는 함수나 방법은?", "choices": ["reverse()", "flip()", "back()", "turn()"], "answer": 0}, {"q": "파이썬 코딩 마스터가 되기 위해 가장 중요한 것은?", "choices": ["포기하지 않고 계속 만들어보기!", "눈으로만 읽기", "복사해서 붙여넣기만 하기", "컴퓨터 끄기"], "answer": 0}]];

const conceptState = { answers: new Array(CONCEPT_PROBLEMS.length).fill(-1), submitted: false };

function renderConcept(){
  const list = document.getElementById('conceptList');
  list.innerHTML = '';
  CONCEPT_PROBLEMS.forEach((q, qi)=>{
    const qDiv = document.createElement('div');
    qDiv.className = 'test-q-card';
    qDiv.innerHTML = `<div class="test-q-text">Q${qi+1}. ${q.q}</div><div class="test-choices" id="concept-choices-${qi}"></div>`;
    const cWrap = qDiv.querySelector('.test-choices');
    q.shuffledChoices.forEach((choiceObj, ci)=>{
      const btn = document.createElement('button');
      btn.className = 'test-choice-btn';
      btn.textContent = choiceObj.text;
      btn.addEventListener('click', ()=>{
        if(conceptState.submitted) return;
        conceptState.answers[qi] = ci;
        cWrap.querySelectorAll('.test-choice-btn').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
      });
      cWrap.appendChild(btn);
    });
    list.appendChild(qDiv);
  });
}

document.getElementById('submitConceptBtn').addEventListener('click', ()=>{
  if(conceptState.submitted) return;
  if(conceptState.answers.includes(-1)){
    alert("아직 풀지 않은 문제가 있습니다!");
    return;
  }
  conceptState.submitted = true;
  document.getElementById('submitConceptBtn').style.display = 'none';
  
  let correctCount = 0;
  CONCEPT_PROBLEMS.forEach((q, qi)=>{
    const selectedIdx = conceptState.answers[qi];
    const cWrap = document.getElementById(`concept-choices-${qi}`);
    const btns = cWrap.querySelectorAll('.test-choice-btn');
    if(q.shuffledChoices[selectedIdx].isCorrect) correctCount++;
    q.shuffledChoices.forEach((choiceObj, ci)=>{
      if(choiceObj.isCorrect) btns[ci].classList.add('correct-ans');
      else if (ci === selectedIdx && !choiceObj.isCorrect) btns[ci].classList.add('wrong-ans');
    });
  });
  
  document.getElementById('conceptResultArea').style.display = 'block';
  document.getElementById('conceptScoreDisplay').textContent = `🎉 내 점수: ${Math.round(correctCount/CONCEPT_PROBLEMS.length*100)}점 (${correctCount}/${CONCEPT_PROBLEMS.length})`;
  document.getElementById('conceptFeedbackMsg').textContent = (correctCount === CONCEPT_PROBLEMS.length) ? '완벽해요! 개념을 확실히 잡으셨네요!' : '틀린 문제를 다시 한번 확인해보세요!';
  window.scrollTo({top: document.getElementById('conceptResultArea').offsetTop - 50, behavior: 'smooth'});
});

/* --- Mock Exams Logic --- */
const mockState = { currentExam: -1, answers: [], submitted: false, scores: new Array(MOCK_EXAMS.length).fill(null) };

function renderMockLobby(){
  const lobby = document.getElementById('mockLobbyList');
  lobby.innerHTML = '';
  MOCK_EXAMS.forEach((exam, i) => {
    const btn = document.createElement('button');
    btn.className = 'test-choice-btn';
    btn.style.fontSize = '16px';
    btn.style.fontWeight = 'bold';
    btn.style.textAlign = 'center';
    const scoreText = mockState.scores[i] !== null ? `(최고: ${mockState.scores[i]}점)` : '';
    btn.textContent = `제${i+1}회 모의고사 ${scoreText}`;
    if(mockState.scores[i] !== null) btn.style.borderColor = 'var(--accent-gold)';
    
    btn.addEventListener('click', () => openMockExam(i));
    lobby.appendChild(btn);
  });
  document.getElementById('mockLobby').style.display = 'block';
  document.getElementById('mockExamRoom').style.display = 'none';
}

function openMockExam(idx){
  mockState.currentExam = idx;
  mockState.answers = new Array(MOCK_EXAMS[idx].length).fill(-1);
  mockState.submitted = false;
  
  document.getElementById('mockLobby').style.display = 'none';
  document.getElementById('mockExamRoom').style.display = 'block';
  document.getElementById('mockExamTitle').textContent = `제${idx+1}회 모의고사`;
  document.getElementById('submitTestBtn').style.display = 'inline-block';
  document.getElementById('testResultArea').style.display = 'none';
  
  const list = document.getElementById('testList');
  list.innerHTML = '';
  MOCK_EXAMS[idx].forEach((q, qi)=>{
    const qDiv = document.createElement('div');
    qDiv.className = 'test-q-card';
    qDiv.innerHTML = `<div class="test-q-text">Q${qi+1}. ${q.q}</div><div class="test-choices" id="test-choices-${qi}"></div>`;
    const cWrap = qDiv.querySelector('.test-choices');
    q.shuffledChoices.forEach((choiceObj, ci)=>{
      const btn = document.createElement('button');
      btn.className = 'test-choice-btn';
      btn.textContent = `${['①','②','③','④'][ci]} ${choiceObj.text}`;
      btn.addEventListener('click', ()=>{
        if(mockState.submitted) return;
        mockState.answers[qi] = ci;
        cWrap.querySelectorAll('.test-choice-btn').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
      });
      cWrap.appendChild(btn);
    });
    list.appendChild(qDiv);
  });
  window.scrollTo({top:0, behavior:'smooth'});
}

document.getElementById('mockBackBtn').addEventListener('click', renderMockLobby);
document.getElementById('mockRetryBtn').addEventListener('click', () => openMockExam(mockState.currentExam));

document.getElementById('submitTestBtn').addEventListener('click', ()=>{
  if(mockState.submitted) return;
  if(mockState.answers.includes(-1)){
    alert("아직 풀지 않은 문제가 있습니다!");
    return;
  }
  mockState.submitted = true;
  document.getElementById('submitTestBtn').style.display = 'none';
  
  let correctCount = 0;
  const currentExamData = MOCK_EXAMS[mockState.currentExam];
  
  currentExamData.forEach((q, qi)=>{
    const selectedIdx = mockState.answers[qi];
    const cWrap = document.getElementById(`test-choices-${qi}`);
    const btns = cWrap.querySelectorAll('.test-choice-btn');
    if(q.shuffledChoices[selectedIdx].isCorrect) correctCount++;
    q.shuffledChoices.forEach((choiceObj, ci)=>{
      if(choiceObj.isCorrect) btns[ci].classList.add('correct-ans');
      else if (ci === selectedIdx && !choiceObj.isCorrect) btns[ci].classList.add('wrong-ans');
    });
  });
  
  const score = correctCount * 10;
  if(mockState.scores[mockState.currentExam] === null || score > mockState.scores[mockState.currentExam]){
    mockState.scores[mockState.currentExam] = score;
  }
  
  document.getElementById('testResultArea').style.display = 'block';
  document.getElementById('testScoreDisplay').textContent = `🎉 내 점수: ${score}점 (${correctCount}/10)`;
  document.getElementById('testFeedbackMsg').textContent = score >= 80 ? '참 잘했어요! 대단합니다!' : '틀린 문제를 다시 복습해봐요!';
  window.scrollTo({top: document.getElementById('testResultArea').offsetTop - 50, behavior: 'smooth'});
});

/* --- Typing Practice Logic --- */
const typingState = { currentStage: -1, text: '', input: '', startTime: null, timerInterval: null, finished: false };

function renderTypingLobby(){
  const lobby = document.getElementById('typingLobbyList');
  lobby.innerHTML = '';
  TYPING_SNIPPETS.forEach((snip, i) => {
    const btn = document.createElement('button');
    btn.className = 'typing-stage-btn';
    btn.textContent = `${i+1}단계: ${snip.title}`;
    btn.addEventListener('click', () => openTypingStage(i));
    lobby.appendChild(btn);
  });
  document.getElementById('typingLobby').style.display = 'block';
  document.getElementById('typingRoom').style.display = 'none';
}

function openTypingStage(idx){
  typingState.currentStage = idx;
  typingState.text = TYPING_SNIPPETS[idx].code;
  typingState.input = '';
  typingState.startTime = null;
  typingState.finished = false;
  clearInterval(typingState.timerInterval);
  
  document.getElementById('typingLobby').style.display = 'none';
  document.getElementById('typingRoom').style.display = 'block';
  document.getElementById('typingStageTitle').textContent = `${idx+1}단계: ${TYPING_SNIPPETS[idx].title}`;
  document.getElementById('typingTimer').textContent = '0.0';
  document.getElementById('typingAccuracy').textContent = '100';
  document.getElementById('typingResultArea').style.display = 'none';
  
  const inputEl = document.getElementById('typingHiddenInput');
  inputEl.value = '';
  inputEl.disabled = false;
  
  updateTypingDisplay();
  
  setTimeout(() => inputEl.focus(), 100);
}

function updateTypingDisplay(){
  const display = document.getElementById('typingDisplay');
  const target = typingState.text;
  const input = typingState.input;
  
  let html = '';
  let correctCount = 0;
  for(let i=0; i<target.length; i++){
    const tChar = target[i];
    const iChar = input[i];
    
    if(iChar === undefined){
      if(i === input.length && !typingState.finished) {
        html += `<span class="current">${tChar}</span>`;
      } else {
        html += `<span>${tChar}</span>`;
      }
    } else {
      if(tChar === iChar){
        html += `<span class="correct">${tChar}</span>`;
        correctCount++;
      } else {
        html += `<span class="wrong">${tChar === '\\n' ? '↵\\n' : tChar}</span>`;
      }
    }
  }
  display.innerHTML = html;
  
  if(input.length > 0){
    const acc = Math.floor((correctCount / input.length) * 100);
    document.getElementById('typingAccuracy').textContent = acc;
  }
  
  if(input.length >= target.length && !typingState.finished){
    finishTypingStage();
  }
}

document.getElementById('typingHiddenInput').addEventListener('input', (e)=>{
  if(typingState.finished) return;
  if(typingState.startTime === null){
    typingState.startTime = Date.now();
    typingState.timerInterval = setInterval(()=>{
      const elapsed = (Date.now() - typingState.startTime) / 1000;
      document.getElementById('typingTimer').textContent = elapsed.toFixed(1);
    }, 100);
  }
  
  let val = e.target.value;
  typingState.input = val;
  updateTypingDisplay();
});

document.getElementById('typingHiddenInput').addEventListener('keydown', (e)=>{
  if(e.key === 'Enter'){
    e.preventDefault();
    if(typingState.finished) return;
    const inputEl = document.getElementById('typingHiddenInput');
    inputEl.value += '\\n';
    typingState.input = inputEl.value;
    updateTypingDisplay();
  }
});

document.getElementById('typingDisplay').addEventListener('click', ()=>{
  if(!typingState.finished) document.getElementById('typingHiddenInput').focus();
});

function finishTypingStage(){
  typingState.finished = true;
  clearInterval(typingState.timerInterval);
  document.getElementById('typingHiddenInput').disabled = true;
  
  const elapsed = (Date.now() - typingState.startTime) / 1000;
  
  const target = typingState.text;
  const input = typingState.input;
  let correctCount = 0;
  for(let i=0; i<target.length; i++){
    if(target[i] === input[i]) correctCount++;
  }
  const acc = Math.floor((correctCount / target.length) * 100);
  
  document.getElementById('typingResultArea').style.display = 'block';
  document.getElementById('typingFinalTime').textContent = `최종 기록: ${elapsed.toFixed(1)}초 (정확도: ${acc}%)`;
  
  const fb = document.getElementById('typingFeedbackMsg');
  if(acc === 100){
    fb.textContent = '완벽해요! 빠르고 정확합니다! 🎉';
    burstConfetti(window.innerWidth/2, window.innerHeight/2);
    
    // Add completed mark to lobby button
    const lobbyBtns = document.querySelectorAll('.typing-stage-btn');
    if(lobbyBtns[typingState.currentStage]){
      lobbyBtns[typingState.currentStage].classList.add('completed');
    }
  } else if (acc >= 90){
    fb.textContent = '아주 좋아요! 오타만 조금 줄여볼까요? 👍';
  } else {
    fb.textContent = '오타가 많아요. 조금 더 천천히 정확하게 쳐보세요! 💪';
  }
  
  window.scrollTo({top: document.getElementById('typingResultArea').offsetTop - 50, behavior: 'smooth'});
}

document.getElementById('typingBackBtn').addEventListener('click', renderTypingLobby);
document.getElementById('typingRetryBtn').addEventListener('click', () => openTypingStage(typingState.currentStage));


function updateProblemsProgress(){
  const solved = problemState.filter(Boolean).length;
  document.getElementById('probSolvedCount').textContent = solved;
  document.getElementById('probTotalCount').textContent = PROBLEMS.length;
}

function markProblemSolved(idx, card, anchorEl){
  if(!problemState[idx]){
    problemState[idx] = true;
    card.classList.add('solved');
    const rect = anchorEl.getBoundingClientRect();
    burstConfetti(rect.left, rect.top);
    updateProblemsProgress();
  }
}

function renderProblems(){
  const list = document.getElementById('problemsList');
  list.innerHTML = '';
  PROBLEMS.forEach((p, idx)=>{
    const card = document.createElement('div');
    card.className = 'problem-card';

    if(p.type === 'write'){
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
          <div class="target-output">🎯 목표 출력: <b>${escapeHtml(p.targetLabel)}</b></div>
          <textarea class="code-input" placeholder="${escapeHtml(p.placeholder)}" spellcheck="false"></textarea>
          <div class="write-actions">
            <button class="check-btn">▶ 실행 확인하기</button>
            <button class="reveal-btn">모범답안 보기</button>
          </div>
          <div class="explain-box"></div>
          <div class="sample-box"><span class="tag2">모범답안 예시</span>${escapeHtml(p.sampleAnswer)}</div>
        </div>
      `;
      const head = card.querySelector('.problem-head');
      head.addEventListener('click', ()=>{ card.classList.toggle('open'); });

      const textarea = card.querySelector('.code-input');
      const explainBox = card.querySelector('.explain-box');
      const sampleBox = card.querySelector('.sample-box');

      card.querySelector('.check-btn').addEventListener('click', (e)=>{
        e.stopPropagation();
        const code = textarea.value;
        explainBox.style.display = 'block';
        if(!code.trim()){
          explainBox.className = 'explain-box wrong-tone';
          explainBox.textContent = '🤔 코드를 입력한 다음 확인해보세요!';
          return;
        }
        if(p.validate(code)){
          explainBox.className = 'explain-box correct-tone';
          explainBox.textContent = '✅ 정답이에요! 코드를 정확하게 작성했어요.';
          markProblemSolved(idx, card, e.currentTarget);
        } else {
          explainBox.className = 'explain-box wrong-tone';
          explainBox.textContent = '🤔 아직이에요. ' + p.hint;
        }
      });
      card.querySelector('.reveal-btn').addEventListener('click', (e)=>{
        e.stopPropagation();
        sampleBox.style.display = sampleBox.style.display==='block' ? 'none' : 'block';
      });

      list.appendChild(card);
      return; // quiz 렌더링 로직을 건너뜀
    }

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
          explainBox.className = 'explain-box correct-tone';
          choicesWrap.querySelectorAll('.choice-btn').forEach(x=>x.disabled=true);
          markProblemSolved(idx, card, btn);
        } else {
          btn.classList.add('wrong');
          explainBox.className = 'explain-box wrong-tone';
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
function shuffleArray(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
}

LESSONS.forEach(l => {
  if (l.mission && l.mission.choices) shuffleArray(l.mission.choices);
  if (l.quiz) {
    l.quiz.forEach(q => {
      let objs = q.choices.map((text, i) => ({ text, isCorrect: i === q.answer }));
      shuffleArray(objs);
      q.shuffledChoices = objs;
    });
  }
});
if (BOSS && BOSS.quiz) {
  BOSS.quiz.forEach(q => {
    let objs = q.choices.map((text, i) => ({ text, isCorrect: i === q.answer }));
    shuffleArray(objs);
    q.shuffledChoices = objs;
  });
}


if (typeof CONCEPT_PROBLEMS !== 'undefined') {
  CONCEPT_PROBLEMS.forEach(q => {
    let objs = q.choices.map((text, i) => ({ text, isCorrect: i === q.answer }));
    shuffleArray(objs);
    q.shuffledChoices = objs;
  });
}
if (typeof MOCK_EXAMS !== 'undefined') {
  MOCK_EXAMS.forEach(exam => {
    exam.forEach(q => {
      let objs = q.choices.map((text, i) => ({ text, isCorrect: i === q.answer }));
      shuffleArray(objs);
      q.shuffledChoices = objs;
    });
  });
}

if (typeof PROBLEMS !== 'undefined') {
  PROBLEMS.forEach(p => {
    if (p.choices) shuffleArray(p.choices);
  });
}

renderMap();
renderProblems();
renderConcept();
renderMockLobby();
renderTypingLobby();
</script>
</body>
</html>
"""

with open('/Users/cheonhyeonjun/com_gui/public/python_basic_reference.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated python_basic_reference.html")
