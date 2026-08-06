import json

problems = []

# --- QUIZ: EASY (7) ---
problems.append({
    "type": "quiz", "emoji": "📝", "title": "가장 기본 명령어", "tag": "퀴즈 · 출력 · 쉬움",
    "scenario": "화면에 글자나 숫자를 보여주고 싶을 때 사용하는 파이썬의 주문(명령어)은 무엇인가요?",
    "code": "",
    "choices": [
        {"text": "print()", "correct": True, "feedback": "✅ 맞아요! 화면에 무언가를 출력할 때는 print()를 사용해요."},
        {"text": "show()", "correct": False, "feedback": "🤔 show()라는 명령어는 기본 파이썬에는 없어요."},
        {"text": "say()", "correct": False, "feedback": "🤔 말하는 느낌은 비슷하지만 정답은 아니에요."},
        {"text": "out()", "correct": False, "feedback": "🤔 out()은 파이썬 명령어가 아니에요."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🔤", "title": "글자 감싸기", "tag": "퀴즈 · 문자열 · 쉬움",
    "scenario": "파이썬에서 '안녕'이라는 글자를 컴퓨터에게 알려주려면 어떻게 감싸야 할까요?",
    "code": "print( ___안녕___ )",
    "choices": [
        {"text": "따옴표 (\" \")", "correct": True, "feedback": "✅ 맞아요! 글자(문자열)는 항상 따옴표로 감싸야 해요."},
        {"text": "괄호 ( )", "correct": False, "feedback": "🤔 괄호는 함수를 실행할 때 써요. 글자 자체를 감싸진 않아요."},
        {"text": "대괄호 [ ]", "correct": False, "feedback": "🤔 대괄호는 리스트(상자 모음)를 만들 때 써요."},
        {"text": "별표 * *", "correct": False, "feedback": "🤔 별표는 보통 곱하기를 할 때 쓴답니다."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "➕", "title": "간단한 덧셈", "tag": "퀴즈 · 연산 · 쉬움",
    "scenario": "다음 코드를 실행하면 화면에 어떤 숫자가 나올까요?",
    "code": "print(10 + 5)",
    "choices": [
        {"text": "15", "correct": True, "feedback": "✅ 맞아요! 컴퓨터가 10 + 5를 계산해서 15를 출력해요."},
        {"text": "105", "correct": False, "feedback": "🤔 숫자끼리 더하면 진짜 수학처럼 계산돼요. 글자일 때만 이어 붙어요."},
        {"text": "10 + 5", "correct": False, "feedback": "🤔 따옴표가 없기 때문에 그대로 출력되지 않고 계산된답니다."},
        {"text": "오류 발생", "correct": False, "feedback": "🤔 완벽히 정상적인 파이썬 코드예요!"}
    ]
})
problems.append({
    "type": "quiz", "emoji": "✖️", "title": "곱하기 기호", "tag": "퀴즈 · 연산 · 쉬움",
    "scenario": "파이썬에서 곱하기를 할 때 사용하는 기호는 무엇일까요?",
    "code": "",
    "choices": [
        {"text": "* (별표)", "correct": True, "feedback": "✅ 맞아요! 파이썬에서 곱하기는 * 를 사용해요."},
        {"text": "x (알파벳 x)", "correct": False, "feedback": "🤔 수학에서는 x를 쓰지만 컴퓨터는 헷갈려 한답니다."},
        {"text": "^ (눈웃음)", "correct": False, "feedback": "🤔 ^ 기호는 곱하기가 아니에요."},
        {"text": "# (우물정자)", "correct": False, "feedback": "🤔 #은 파이썬에서 메모(주석)를 남길 때 써요."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "📦", "title": "변수 만들기", "tag": "퀴즈 · 변수 · 쉬움",
    "scenario": "이름이 `age`인 상자에 12라는 숫자를 넣으려고 해요. 알맞은 기호는?",
    "code": "age ___ 12",
    "choices": [
        {"text": "=", "correct": True, "feedback": "✅ 맞아요! 파이썬에서 = 기호는 '오른쪽 값을 왼쪽 상자에 넣어라!' 라는 뜻이에요."},
        {"text": "==", "correct": False, "feedback": "🤔 == 는 '양쪽이 똑같은가요?' 하고 물어보는 기호예요."},
        {"text": "+", "correct": False, "feedback": "🤔 + 는 더하기 기호랍니다."},
        {"text": "<-", "correct": False, "feedback": "🤔 화살표 모양은 파이썬에서 쓰지 않아요."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "📋", "title": "리스트의 생김새", "tag": "퀴즈 · 리스트 · 쉬움",
    "scenario": "여러 개의 물건을 한 줄로 담을 수 있는 '리스트'를 만들 때 사용하는 괄호는?",
    "code": "friends = ___ '짱구', '철수', '훈이' ___",
    "choices": [
        {"text": "[ ] 대괄호", "correct": True, "feedback": "✅ 맞아요! 리스트는 항상 [ ] 로 감싸서 만들어요."},
        {"text": "( ) 소괄호", "correct": False, "feedback": "🤔 소괄호는 다른 용도로 쓰인답니다."},
        {"text": "{ } 중괄호", "correct": False, "feedback": "🤔 중괄호는 딕셔너리(사전)를 만들 때 써요."},
        {"text": "< > 꺾쇠", "correct": False, "feedback": "🤔 꺾쇠는 파이썬에서 보통 크기를 비교할 때 써요."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🔀", "title": "만약에 ~라면", "tag": "퀴즈 · 조건문 · 쉬움",
    "scenario": "'만약 날씨가 맑다면 놀러 가자!' 할 때 사용하는 파이썬 키워드는?",
    "code": "___ weather == '맑음':\n    print('놀러 가자!')",
    "choices": [
        {"text": "if", "correct": True, "feedback": "✅ 맞아요! if는 영어로 '만약~' 이라는 뜻이죠."},
        {"text": "for", "correct": False, "feedback": "🤔 for는 여러 번 반복할 때 써요."},
        {"text": "def", "correct": False, "feedback": "🤔 def는 나만의 새로운 명령어를 만들 때 써요."},
        {"text": "else", "correct": False, "feedback": "🤔 else는 '그렇지 않다면' 이라는 뜻으로 if 뒤에 따라와요."}
    ]
})

# --- QUIZ: MEDIUM (7) ---
problems.append({
    "type": "quiz", "emoji": "🔗", "title": "글자 이어붙이기", "tag": "퀴즈 · 문자열 · 보통",
    "scenario": "다음 코드를 실행하면 화면에 어떻게 출력될까요?",
    "code": "print('사과' + '주스')",
    "choices": [
        {"text": "사과주스", "correct": True, "feedback": "✅ 맞아요! 글자끼리 + 를 쓰면 딱 붙어서 출력돼요."},
        {"text": "사과 주스", "correct": False, "feedback": "🤔 띄어쓰기를 따로 넣어주지 않았기 때문에 딱 붙어서 나와요."},
        {"text": "사과+주스", "correct": False, "feedback": "🤔 + 기호 자체는 계산되느라 화면에 나오지 않아요."},
        {"text": "오류 발생", "correct": False, "feedback": "🤔 글자끼리 더하는 것은 가능하답니다!"}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🧐", "title": "두 숫자의 비교", "tag": "퀴즈 · 비교 연산 · 보통",
    "scenario": "파이썬에서 '왼쪽과 오른쪽이 똑같니?' 라고 물어볼 때 쓰는 기호는?",
    "code": "if 10 ___ 10:\n    print('똑같아!')",
    "choices": [
        {"text": "==", "correct": True, "feedback": "✅ 맞아요! 등호 두 개(==)를 써야 '같다'는 뜻이 돼요."},
        {"text": "=", "correct": False, "feedback": "🤔 등호 한 개(=)는 값을 상자에 넣을 때만 써요."},
        {"text": "!=", "correct": False, "feedback": "🤔 != 는 '다르다'는 뜻이에요."},
        {"text": "=>", "correct": False, "feedback": "🤔 파이썬에 이런 모양의 비교 기호는 없어요 (>= 가 맞아요)."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "📏", "title": "리스트 길이 재기", "tag": "퀴즈 · 리스트 · 보통",
    "scenario": "`len()`은 상자 안에 물건이 몇 개 들어있는지 세어줘요. 다음 코드의 결과는?",
    "code": "bag = ['지우개', '연필', '공책']\nprint(len(bag))",
    "choices": [
        {"text": "3", "correct": True, "feedback": "✅ 맞아요! 지우개, 연필, 공책 총 3개가 들어있죠!"},
        {"text": "0", "correct": False, "feedback": "🤔 리스트 안에 분명 물건이 들어있어요."},
        {"text": "지우개", "correct": False, "feedback": "🤔 len()은 개수(숫자)를 알려주는 함수예요."},
        {"text": "2", "correct": False, "feedback": "🤔 번호를 매길 때는 0부터 세지만, '개수'는 진짜 3개예요!"}
    ]
})
problems.append({
    "type": "quiz", "emoji": "☝️", "title": "첫 번째 물건 꺼내기", "tag": "퀴즈 · 리스트 · 보통",
    "scenario": "리스트에서 가장 첫 번째에 있는 물건을 꺼내려고 해요. 숫자로 뭘 적어야 할까요?",
    "code": "bag = ['지우개', '연필']\nprint(bag[___])",
    "choices": [
        {"text": "0", "correct": True, "feedback": "✅ 맞아요! 파이썬은 항상 0부터 순서를 세기 시작해요."},
        {"text": "1", "correct": False, "feedback": "🤔 1을 적으면 두 번째 물건인 '연필'이 나와요."},
        {"text": "first", "correct": False, "feedback": "🤔 순서는 무조건 숫자로 적어줘야 해요."},
        {"text": "-1", "correct": False, "feedback": "🤔 -1을 적으면 맨 마지막 물건을 꺼낸답니다."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🤷‍♂️", "title": "if else의 마법", "tag": "퀴즈 · 조건문 · 보통",
    "scenario": "다음 코드가 실행되면 화면에 어떤 글자가 나올까요?",
    "code": "score = 80\nif score >= 90:\n    print('합격')\nelse:\n    print('불합격')",
    "choices": [
        {"text": "불합격", "correct": True, "feedback": "✅ 맞아요! 80은 90보다 크거나 같지 않아서 else 부분이 실행돼요."},
        {"text": "합격", "correct": False, "feedback": "🤔 score가 80이니까 90을 넘지 못했어요."},
        {"text": "아무것도 안 나옴", "correct": False, "feedback": "🤔 else가 있기 때문에 반드시 불합격이 나와요."},
        {"text": "오류 발생", "correct": False, "feedback": "🤔 정상적인 코드랍니다."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🔁", "title": "정해진 만큼 반복하기", "tag": "퀴즈 · 반복문 · 보통",
    "scenario": "`for`문을 써서 5번 반복하려고 해요. 알맞은 코드는?",
    "code": "for i in range(___):\n    print('야호!')",
    "choices": [
        {"text": "5", "correct": True, "feedback": "✅ 맞아요! range(5)라고 적으면 0부터 4까지 딱 5번 반복돼요."},
        {"text": "1, 5", "correct": False, "feedback": "🤔 range(1, 5)는 1, 2, 3, 4로 4번만 반복돼요."},
        {"text": "6", "correct": False, "feedback": "🤔 range(6)은 6번 반복돼요."},
        {"text": "무한대", "correct": False, "feedback": "🤔 for문은 정해진 숫자만큼만 반복해요."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🎒", "title": "리스트에 물건 추가하기", "tag": "퀴즈 · 리스트 · 보통",
    "scenario": "리스트 맨 뒤에 새로운 물건을 추가하고 싶을 때 쓰는 명령어는?",
    "code": "bag = ['지우개']\nbag.____('연필')",
    "choices": [
        {"text": "append", "correct": True, "feedback": "✅ 맞아요! append는 '덧붙이다'라는 뜻으로 맨 뒤에 추가해줘요."},
        {"text": "add", "correct": False, "feedback": "🤔 add라는 단어도 맞을 것 같지만 파이썬 리스트에서는 append를 써요."},
        {"text": "insert", "correct": False, "feedback": "🤔 insert는 중간에 끼워넣을 때 쓰고, 위치도 알려줘야 해요."},
        {"text": "push", "correct": False, "feedback": "🤔 push는 다른 프로그래밍 언어에서 자주 써요."}
    ]
})

# --- QUIZ: HARD (6) ---
problems.append({
    "type": "quiz", "emoji": "🧮", "title": "나머지 구하기", "tag": "퀴즈 · 연산 · 어려움",
    "scenario": "숫자를 나누었을 때 몫이 아니라 '나머지'를 구해주는 연산 기호는?",
    "code": "print(10 ___ 3) # 1이 출력돼야 함",
    "choices": [
        {"text": "% (퍼센트)", "correct": True, "feedback": "✅ 맞아요! %는 나머지를 구해줘서 짝수/홀수 판별할 때 아주 유용해요."},
        {"text": "/ (슬래시)", "correct": False, "feedback": "🤔 / 는 진짜 나누기를 해서 3.333... 이 나와요."},
        {"text": "// (슬래시 두개)", "correct": False, "feedback": "🤔 // 는 나누었을 때 '몫'만 구해줘요."},
        {"text": "mod", "correct": False, "feedback": "🤔 파이썬에서는 글자 대신 % 기호를 써요."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🤝", "title": "두 조건 모두 만족?", "tag": "퀴즈 · 논리 연산 · 어려움",
    "scenario": "두 가지 조건이 **모두 참(True)**일 때만 실행하게 만들고 싶어요.",
    "code": "if age > 10 ___ height > 140:\n    print('놀이기구 탑승 가능!')",
    "choices": [
        {"text": "and", "correct": True, "feedback": "✅ 맞아요! and는 '그리고' 라는 뜻으로 양쪽 다 참이어야 해요."},
        {"text": "or", "correct": False, "feedback": "🤔 or는 둘 중 하나만 참이어도 통과시켜 줘요."},
        {"text": "with", "correct": False, "feedback": "🤔 with는 완전히 다른 곳에서 쓰이는 파이썬 키워드예요."},
        {"text": "&&", "correct": False, "feedback": "🤔 &&는 파이썬이 아닌 다른 언어에서 쓰는 기호예요."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🏃‍♂️", "title": "끝나지 않는 질주", "tag": "퀴즈 · 반복문 · 어려움",
    "scenario": "다음 코드는 치명적인 문제가 하나 있어요. 무엇일까요?",
    "code": "n = 0\nwhile n < 5:\n    print('달려!')",
    "choices": [
        {"text": "n을 더해주지 않아서 영원히 반복된다", "correct": True, "feedback": "✅ 빙고! n이 계속 0이라서 영원히 화면에 '달려!'가 찍힐 거예요."},
        {"text": "문법 오류가 발생한다", "correct": False, "feedback": "🤔 코드는 정상이라 컴퓨터는 그대로 실행해버려요."},
        {"text": "한 번도 실행되지 않는다", "correct": False, "feedback": "🤔 처음엔 n이 0이라 5보다 작아서 실행은 돼요."},
        {"text": "딱 5번만 실행된다", "correct": False, "feedback": "🤔 n 값을 바꿔주는 코드가 없어서 5번에서 멈추지 않아요."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "📦", "title": "상자 안의 상자", "tag": "퀴즈 · 리스트 · 어려움",
    "scenario": "리스트 안에 또 리스트가 들어있어요! `print(box[1][0])`을 하면 무엇이 나올까요?",
    "code": "box = [ ['사과', '배'], ['강아지', '고양이'] ]",
    "choices": [
        {"text": "강아지", "correct": True, "feedback": "✅ 완벽해요! box[1]은 두 번째 리스트고, 그 안에서 [0]이니까 강아지예요!"},
        {"text": "사과", "correct": False, "feedback": "🤔 사과는 box[0][0] 이랍니다."},
        {"text": "고양이", "correct": False, "feedback": "🤔 고양이는 box[1][1] 이에요."},
        {"text": "오류", "correct": False, "feedback": "🤔 리스트 안에 리스트를 넣는 건 아주 흔한 일이랍니다."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🧰", "title": "함수 호출 횟수", "tag": "퀴즈 · 함수 · 어려움",
    "scenario": "다음 코드를 실행하면 화면에 '야호'가 몇 번 출력될까요?",
    "code": "def shout():\n    print('야호')\n    print('야호')\n\nshout()\nshout()",
    "choices": [
        {"text": "4번", "correct": True, "feedback": "✅ 맞아요! 함수 한 번에 2번 출력되는데, 함수를 2번 불렀으니 총 4번!"},
        {"text": "2번", "correct": False, "feedback": "🤔 shout()를 한 번 부를 때마다 2번씩 출력돼요."},
        {"text": "0번", "correct": False, "feedback": "🤔 shout()를 두 번 호출했으니 출력이 발생해요."},
        {"text": "8번", "correct": False, "feedback": "🤔 2 곱하기 2는 4번이에요."}
    ]
})
problems.append({
    "type": "quiz", "emoji": "🕵️", "title": "참인지 거짓인지", "tag": "퀴즈 · 데이터 타입 · 어려움",
    "scenario": "파이썬에서 '맞다(참)' 와 '틀리다(거짓)'를 나타내는 특별한 단어는?",
    "code": "is_raining = ____",
    "choices": [
        {"text": "True / False", "correct": True, "feedback": "✅ 맞아요! 파이썬에서는 무조건 앞글자를 대문자로 써야 해요."},
        {"text": "true / false", "correct": False, "feedback": "🤔 파이썬은 대문자 소문자를 가려요. 앞글자가 대문자여야 해요."},
        {"text": "Yes / No", "correct": False, "feedback": "🤔 컴퓨터는 Yes/No 대신 True/False를 써요."},
        {"text": "O / X", "correct": False, "feedback": "🤔 O, X는 사람이 보기 편한 기호일 뿐이에요."}
    ]
})

# --- WRITE: EASY (7) ---
problems.append({
    "type": "write", "emoji": "✍️", "title": "화면에 글자 띄우기", "tag": "직접 작성 · 쉬움",
    "scenario": "화면에 **나는 코딩 왕!** 이라고 출력되도록 코드를 한 줄로 작성해보세요.",
    "targetLabel": "나는 코딩 왕!",
    "placeholder": "print(?)",
    "hint": "💡 print() 괄호 안에 따옴표를 잊지 마세요!",
    "sampleAnswer": "print('나는 코딩 왕!')",
    "validate_regex_pattern": "^print\(\s*[\"']나는 코딩 왕![\"']\s*\)$"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "변수에 숫자 넣기", "tag": "직접 작성 · 쉬움",
    "scenario": "`my_money`라는 변수를 만들고 숫자 **5000**을 넣은 다음 출력해보세요. (두 줄로 작성)",
    "targetLabel": "5000",
    "placeholder": "my_money = ?\nprint(?)",
    "hint": "💡 첫째 줄에 변수를 만들고 값을 넣어요. 둘째 줄에서 print()로 꺼내요.",
    "sampleAnswer": "my_money = 5000\nprint(my_money)",
    "validate_func": "const lines = code.split('\\n').map(l=>l.trim()).filter(Boolean); return lines.length>=2 && /^my_money\s*=\s*5000$/.test(lines[0]) && /^print\(\s*my_money\s*\)$/.test(lines[1]);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "간단한 뺄셈 계산기", "tag": "직접 작성 · 쉬움",
    "scenario": "파이썬이 대신 계산하게 해볼까요? 100 빼기 35의 결과를 출력하는 코드를 한 줄로 작성하세요.",
    "targetLabel": "65",
    "placeholder": "",
    "hint": "💡 print() 안에 100 - 35 를 따옴표 없이 그대로 적어보세요.",
    "sampleAnswer": "print(100 - 35)",
    "validate_regex_pattern": "^print\(\s*100\s*-\s*35\s*\)$"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "글자 이어 붙이기", "tag": "직접 작성 · 쉬움",
    "scenario": "'바나나'와 '우유'라는 글자를 `+` 기호로 이어 붙여서 출력해보세요.",
    "targetLabel": "바나나우유",
    "placeholder": "",
    "hint": "💡 print('바나나' + '우유') 처럼 작성하면 돼요.",
    "sampleAnswer": "print('바나나' + '우유')",
    "validate_regex_pattern": "^print\(\s*[\"']바나나[\"']\s*\+\s*[\"']우유[\"']\s*\)$"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "반가워 리스트", "tag": "직접 작성 · 쉬움",
    "scenario": "`animals` 라는 이름의 리스트를 만들고, 그 안에 '사자'와 '호랑이'를 담아보세요. (출력은 안 해도 됨)",
    "targetLabel": "(출력 없음)",
    "placeholder": "animals = [?, ?]",
    "hint": "💡 리스트는 대괄호 [ ] 를 쓰고 쉼표 , 로 구분해요.",
    "sampleAnswer": "animals = ['사자', '호랑이']",
    "validate_regex_pattern": "^animals\s*=\s*\[\s*[\"']사자[\"']\s*,\s*[\"']호랑이[\"']\s*\]$"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "만약에 진짜라면!", "tag": "직접 작성 · 쉬움",
    "scenario": "변수 `x`가 5와 같다면 '정답'이라고 출력하는 코드를 완성하세요.",
    "targetLabel": "정답",
    "placeholder": "x = 5\nif x == 5:\n    print(?)",
    "hint": "💡 if문 아래 코드는 스페이스바 4칸 들여쓰기가 되어 있어야 해요.",
    "sampleAnswer": "x = 5\nif x == 5:\n    print('정답')",
    "validate_func": "return /x\s*=\s*5/.test(code) && /if\s*x\s*==\s*5\s*:/.test(code) && /print\(\s*[\"']정답[\"']\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "똑같은 말 3번 반복", "tag": "직접 작성 · 쉬움",
    "scenario": "`for`문을 사용해서 '파이썬 최고'라는 글자를 화면에 3번 출력해보세요.",
    "targetLabel": "파이썬 최고\n파이썬 최고\n파이썬 최고",
    "placeholder": "for i in range(?):\n    print(?)",
    "hint": "💡 range(3)을 쓰면 3번 반복된답니다.",
    "sampleAnswer": "for i in range(3):\n    print('파이썬 최고')",
    "validate_func": "return /for\s+\w+\s+in\s+range\(\s*3\s*\)\s*:/.test(code) && /print\(\s*[\"']파이썬 최고[\"']\s*\)/.test(code);"
})

# --- WRITE: MEDIUM (7) ---
problems.append({
    "type": "write", "emoji": "✍️", "title": "동물 친구 추가하기", "tag": "직접 작성 · 보통",
    "scenario": "`animals = ['강아지']` 가 있습니다. 여기에 `append`를 써서 '고양이'를 추가하고 리스트 전체를 출력해보세요.",
    "targetLabel": "['강아지', '고양이']",
    "placeholder": "animals = ['강아지']\n# 여기에 고양이 추가\nprint(animals)",
    "hint": "💡 animals.append('고양이') 를 중간에 넣어보세요.",
    "sampleAnswer": "animals = ['강아지']\nanimals.append('고양이')\nprint(animals)",
    "validate_func": "const lines = code.split('\\n').map(l=>l.trim()).filter(Boolean); return lines.length>=3 && /animals\.append\(\s*[\"']고양이[\"']\s*\)/.test(code) && /print\(\s*animals\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "비밀번호 검사기", "tag": "직접 작성 · 보통",
    "scenario": "변수 `pw`에 1234가 들어있습니다. `pw == 1234`면 '환영합니다', 아니면 '누구세요'를 출력하는 코드를 짜보세요.",
    "targetLabel": "환영합니다",
    "placeholder": "pw = 1234\nif pw == 1234:\n    print(?)\nelse:\n    print(?)",
    "hint": "💡 if와 else 안에 각각 맞는 print를 적어주세요.",
    "sampleAnswer": "pw = 1234\nif pw == 1234:\n    print('환영합니다')\nelse:\n    print('누구세요')",
    "validate_func": "return /if\s*pw\s*==\s*1234\s*:/.test(code) && /print\(\s*[\"']환영합니다[\"']\s*\)/.test(code) && /else\s*:/.test(code) && /print\(\s*[\"']누구세요[\"']\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "리스트 크기 확인", "tag": "직접 작성 · 보통",
    "scenario": "과자가 4개 든 리스트 `snacks = ['홈런볼', '감자깡', '새우깡', '양파링']` 이 있어요. 이 리스트의 길이를 출력하세요.",
    "targetLabel": "4",
    "placeholder": "snacks = ['홈런볼', '감자깡', '새우깡', '양파링']\n# 길이를 재서 출력하세요",
    "hint": "💡 print(len(snacks)) 를 쓰면 리스트의 크기를 출력할 수 있어요.",
    "sampleAnswer": "snacks = ['홈런볼', '감자깡', '새우깡', '양파링']\nprint(len(snacks))",
    "validate_func": "return /print\(\s*len\(\s*snacks\s*\)\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "짝수/홀수 판독기", "tag": "직접 작성 · 보통",
    "scenario": "변수 `num = 7`이 홀수인지 짝수인지 판별하는 코드를 `if else` 와 `%` 연산자를 써서 작성하세요.",
    "targetLabel": "홀수",
    "placeholder": "num = 7\nif num % 2 == 0:\n    print('짝수')\nelse:\n    print('홀수')",
    "hint": "💡 2로 나눈 나머지가 0이면 짝수, 아니면 홀수예요. 코드를 끝까지 완성해보세요.",
    "sampleAnswer": "num = 7\nif num % 2 == 0:\n    print('짝수')\nelse:\n    print('홀수')",
    "validate_func": "return /if\s+num\s*%\s*2\s*==\s*0\s*:/.test(code) && /else\s*:/.test(code) && /print\(\s*[\"']홀수[\"']\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "리스트 항목 하나씩 꺼내기", "tag": "직접 작성 · 보통",
    "scenario": "`colors = ['빨강', '파랑', '초록']` 리스트가 있어요. `for`문을 써서 항목들을 한 줄에 하나씩 출력하세요.",
    "targetLabel": "빨강\n파랑\n초록",
    "placeholder": "colors = ['빨강', '파랑', '초록']\nfor c in colors:\n    print(?)",
    "hint": "💡 for c in colors: 라고 썼으니, 변수 c를 그냥 출력하면 돼요.",
    "sampleAnswer": "colors = ['빨강', '파랑', '초록']\nfor c in colors:\n    print(c)",
    "validate_func": "return /for\s+\w+\s+in\s+colors\s*:/.test(code) && /print\(\s*\w+\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "문자열 곱하기", "tag": "직접 작성 · 보통",
    "scenario": "파이썬에서는 글자에 숫자를 곱하면 그만큼 반복돼요! '안녕'을 5번 곱해서 출력하는 코드를 짜보세요.",
    "targetLabel": "안녕안녕안녕안녕안녕",
    "placeholder": "",
    "hint": "💡 print('안녕' * 5) 라고 쓰면 간단하게 해결!",
    "sampleAnswer": "print('안녕' * 5)",
    "validate_regex_pattern": "^print\(\s*[\"']안녕[\"']\s*\*\s*5\s*\)$"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "나이 제한 확인", "tag": "직접 작성 · 보통",
    "scenario": "`age = 15` 이고 `height = 150` 입니다. 나이가 12 이상 **그리고** 키가 140 이상이면 '탑승'을 출력하세요.",
    "targetLabel": "탑승",
    "placeholder": "age = 15\nheight = 150\nif age >= 12 and height >= 140:\n    print(?)",
    "hint": "💡 조건문 안에 and 를 써서 두 조건이 모두 맞을 때 print('탑승')을 하세요.",
    "sampleAnswer": "age = 15\nheight = 150\nif age >= 12 and height >= 140:\n    print('탑승')",
    "validate_func": "return /if\s+age\s*>=\s*12\s+and\s+height\s*>=\s*140\s*:/.test(code) && /print\(\s*[\"']탑승[\"']\s*\)/.test(code);"
})

# --- WRITE: HARD (6) ---
problems.append({
    "type": "write", "emoji": "✍️", "title": "while 카운트다운", "tag": "직접 작성 · 어려움",
    "scenario": "`while` 반복문을 사용해 변수 `n`을 3부터 1까지 거꾸로 출력하고, 마지막에 '발사!'를 출력하세요.",
    "targetLabel": "3\n2\n1\n발사!",
    "placeholder": "n = 3\nwhile n > 0:\n    print(n)\n    n = n - 1\n# while문이 끝난 뒤\nprint('발사!')",
    "hint": "💡 while문 안에서 n을 1씩 줄여주어야 무한 반복을 피할 수 있어요. '발사!'는 들여쓰기를 하지 않아야 반복이 끝난 후 나옵니다.",
    "sampleAnswer": "n = 3\nwhile n > 0:\n    print(n)\n    n = n - 1\nprint('발사!')",
    "validate_func": "return /while\s+n\s*>\s*0\s*:/.test(code) && /n\s*=\s*n\s*-\s*1/.test(code) && /print\(\s*[\"']발사![\"']\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "큰 수만 골라내기", "tag": "직접 작성 · 어려움",
    "scenario": "`nums = [2, 7, 4, 9, 1]` 리스트가 있습니다. `for`문과 `if`문을 섞어서 5보다 큰 숫자만 골라 출력하세요.",
    "targetLabel": "7\n9",
    "placeholder": "nums = [2, 7, 4, 9, 1]\nfor n in nums:\n    if n > 5:\n        print(n)",
    "hint": "💡 for문 안쪽에 if문이 들어가야 하므로, if 안쪽의 print는 총 8칸 띄어쓰기(들여쓰기 두 번)를 해야 해요.",
    "sampleAnswer": "nums = [2, 7, 4, 9, 1]\nfor n in nums:\n    if n > 5:\n        print(n)",
    "validate_func": "return /for\s+\w+\s+in\s+nums\s*:/.test(code) && /if\s+\w+\s*>\s*5\s*:/.test(code) && /print\(\s*\w+\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "리스트 총합 구하기", "tag": "직접 작성 · 어려움",
    "scenario": "`scores = [10, 20, 30]` 리스트의 모든 숫자를 더한 결과를 출력하고 싶어요. 변수 `total = 0`을 만들고 for문으로 더해보세요.",
    "targetLabel": "60",
    "placeholder": "scores = [10, 20, 30]\ntotal = 0\nfor s in scores:\n    total = total + s\nprint(total)",
    "hint": "💡 for문 안에서 하나씩 꺼낸 값을 total에 계속 누적해서 더해주면 돼요.",
    "sampleAnswer": "scores = [10, 20, 30]\ntotal = 0\nfor s in scores:\n    total = total + s\nprint(total)",
    "validate_func": "return /total\s*=\s*total\s*\+\s*\w+/.test(code) && /print\(\s*total\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "나만의 함수 만들기", "tag": "직접 작성 · 어려움",
    "scenario": "`hello()` 라는 함수를 만들어서, 그 함수를 부르면 '안녕하세요'가 2번 나오게 작성한 후 맨 마지막에 호출하세요.",
    "targetLabel": "안녕하세요\n안녕하세요",
    "placeholder": "def hello():\n    print('안녕하세요')\n    print('안녕하세요')\n\nhello()",
    "hint": "💡 def 함수이름(): 로 시작하고, 들여쓰기를 한 뒤 코드를 적어요. 마지막엔 꼭 함수이름() 으로 불러줘야 실행돼요.",
    "sampleAnswer": "def hello():\n    print('안녕하세요')\n    print('안녕하세요')\nhello()",
    "validate_func": "return /def\s+hello\(\)\s*:/.test(code) && /hello\(\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "매개변수 함수 만들기", "tag": "직접 작성 · 어려움",
    "scenario": "두 숫자를 받아서 더한 값을 출력하는 함수 `add(a, b)`를 만들고, `add(3, 4)`를 호출해 7이 나오게 해보세요.",
    "targetLabel": "7",
    "placeholder": "def add(a, b):\n    print(a + b)\n\nadd(3, 4)",
    "hint": "💡 괄호 안에 a, b 를 넣어서 바깥에서 숫자를 던져줄 수 있는 문(매개변수)을 만들 수 있어요.",
    "sampleAnswer": "def add(a, b):\n    print(a + b)\nadd(3, 4)",
    "validate_func": "return /def\s+add\(a\s*,\s*b\)\s*:/.test(code) && /print\(\s*a\s*\+\s*b\s*\)/.test(code) && /add\(\s*3\s*,\s*4\s*\)/.test(code);"
})
problems.append({
    "type": "write", "emoji": "✍️", "title": "1부터 10까지 짝수만", "tag": "직접 작성 · 어려움",
    "scenario": "`for i in range(1, 11):` 을 쓰면 1부터 10까지 반복돼요. 그 안에서 `if`문을 써서 짝수만 출력되게 하세요.",
    "targetLabel": "2\n4\n6\n8\n10",
    "placeholder": "for i in range(1, 11):\n    if i % 2 == 0:\n        print(i)",
    "hint": "💡 반복문 안의 조건문 구조를 완벽하게 작성해야 해요. 들여쓰기 4칸, 8칸을 꼭 지키세요!",
    "sampleAnswer": "for i in range(1, 11):\n    if i % 2 == 0:\n        print(i)",
    "validate_func": "return /for\s+i\s+in\s+range\(\s*1\s*,\s*11\s*\)\s*:/.test(code) && /if\s+i\s*%\s*2\s*==\s*0\s*:/.test(code) && /print\(\s*i\s*\)/.test(code);"
})

# That is 20 + 20 = 40 problems exactly. (Wait, let's recount.
# Easy Quiz: 7, Med Quiz: 7, Hard Quiz: 6 = 20 Quizzes
# Easy Write: 7, Med Write: 7, Hard Write: 6 = 20 Writes.
# Total = 40.
# Excellent. Let's serialize these problems into a JS string format.

def escape_js(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$').replace('\n', '\\n')

js_lines = []
for p in problems:
    if p['type'] == 'quiz':
        choices_str = ", ".join([f"{{text:`{escape_js(c['text'])}`, correct:{str(c['correct']).lower()}, feedback:`{escape_js(c['feedback'])}`}}" for c in p['choices']])
        js_lines.append(f"""  {{
    type:'quiz', emoji:'{p['emoji']}', title:`{escape_js(p['title'])}`, tag:`{escape_js(p['tag'])}`,
    scenario:`{escape_js(p['scenario'])}`,
    code:`{escape_js(p['code'])}`,
    choices:[ {choices_str} ]
  }}""")
    else:
        if 'validate_regex_pattern' in p:
            val = f"const norm = code.replace(/[’‘]/g,\"'^\").trim(); return /{p['validate_regex_pattern']}/.test(norm);"
        else:
            val = p['validate_func']
            
        js_lines.append(f"""  {{
    type:'write', emoji:'{p['emoji']}', title:`{escape_js(p['title'])}`, tag:`{escape_js(p['tag'])}`,
    scenario:`{escape_js(p['scenario'])}`,
    targetLabel:`{escape_js(p['targetLabel'])}`,
    placeholder:`{escape_js(p['placeholder'])}`,
    hint:`{escape_js(p['hint'])}`,
    sampleAnswer:`{escape_js(p['sampleAnswer'])}`,
    validate:(code)=>{{ {val} }}
  }}""")

js_array_str = "const PROBLEMS = [\n" + ",\n".join(js_lines) + "\n];"

# Read gen_python_basics.py, find PROBLEMS array, and replace it.
with open('gen_python_basics.py', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# We need to replace from `const PROBLEMS = [` down to `];` right before `const problemState =`
# Using regex to find the start and end safely.
start_idx = content.find("const PROBLEMS = [")
end_idx = content.find("];\nconst problemState =")
if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + js_array_str + content[end_idx+2:]
    with open('gen_python_basics.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced PROBLEMS with 40 new items.")
else:
    print("Could not find PROBLEMS array bounds.")
