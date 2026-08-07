import json

# 15 Concept Check Questions
concept_questions = [
    {"q": "파이썬에서 문자를 출력할 때는 반드시 따옴표('', \"\")로 감싸야 한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "파이썬은 대문자와 소문자를 구별하지 않는다. (A와 a는 같다)", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1},
    {"q": "변수는 숫자나 문자를 담아두는 '상자'와 같다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "a = 5 라고 쓰면, 'a와 5가 똑같다'는 뜻이다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1},
    {"q": "파이썬에서 '같다'를 비교할 때는 == 기호를 사용한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "여러 개의 데이터를 하나의 상자에 담는 것을 리스트(List)라고 한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "리스트의 첫 번째 물건을 꺼낼 때는 인덱스 번호 1을 사용한다. (예: list[1])", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1},
    {"q": "if문 아래에 있는 코드는 반드시 '들여쓰기(스페이스 4칸)'를 해야 실행된다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "if문의 조건이 틀렸을 때(거짓일 때) 실행되는 부분은 else 이다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "for문은 정해진 횟수만큼 코드를 반복할 때 사용한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "while문은 특정 조건이 참(True)인 동안 무한히 반복한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "파이썬에서 곱하기를 할 때는 x 알파벳을 사용한다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1},
    {"q": "10을 3으로 나눈 '나머지'를 구하고 싶을 때는 10 % 3 이라고 쓴다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "def는 나만의 새로운 함수(명령어)를 만들 때 사용하는 키워드이다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 0},
    {"q": "파이썬에서 컴퓨터에게 명령을 내릴 때 소문자 true나 false를 써도 된다.", "choices": ["O (맞다)", "X (틀리다)"], "answer": 1},
]

# 10 Tests * 10 Questions = 100 Questions
mock_exams = [
    # 1회: 입출력과 변수 기본
    [
        {"q": "화면에 '안녕'을 출력하려고 합니다. 알맞은 코드는?", "choices": ["print('안녕')", "show('안녕')", "write('안녕')", "say('안녕')"], "answer": 0},
        {"q": "변수 `age`에 숫자 12를 넣으려면?", "choices": ["age = 12", "age == 12", "12 = age", "age <- 12"], "answer": 0},
        {"q": "변수의 이름으로 사용할 수 없는 것은?", "choices": ["1number (숫자로 시작)", "my_score", "name", "age2"], "answer": 0},
        {"q": "print(10 + 5) 의 결과는?", "choices": ["15", "105", "10+5", "오류"], "answer": 0},
        {"q": "print('파이썬' + '최고') 의 결과는?", "choices": ["파이썬최고", "파이썬 최고", "오류", "아무것도 안나옴"], "answer": 0},
        {"q": "파이썬에서 주석(메모)을 달 때 사용하는 기호는?", "choices": ["#", "//", "<!--", "--"], "answer": 0},
        {"q": "x = 5\\ny = 3\\nprint(x * y) 의 결과는?", "choices": ["15", "8", "53", "오류"], "answer": 0},
        {"q": "문자열을 나타낼 때 쓸 수 있는 기호는?", "choices": ["따옴표('', \"\")", "괄호(())", "대괄호([])", "중괄호({})"], "answer": 0},
        {"q": "파이썬에서 변수를 만드는 올바른 방법은?", "choices": ["이름 = 값", "값 = 이름", "변수 이름", "만들기 변수"], "answer": 0},
        {"q": "다음 중 성격이 다른 하나는?", "choices": ["100 (숫자)", "'100' (문자열)", "'안녕'", "'사과'"], "answer": 0},
    ],
    # 2회: 연산자와 자료형
    [
        {"q": "파이썬에서 10을 3으로 나눈 '몫'만 구하는 기호는?", "choices": ["//", "/", "%", "mod"], "answer": 0},
        {"q": "파이썬에서 10을 3으로 나눈 '나머지'를 구하는 기호는?", "choices": ["%", "/", "//", "mod"], "answer": 0},
        {"q": "print('하하' * 3) 의 결과는?", "choices": ["하하하하하하", "하하3", "하하 하하 하하", "오류"], "answer": 0},
        {"q": "변수 a에 담긴 값이 숫자인지 문자인지 헷갈립니다. 확인하는 함수는?", "choices": ["type(a)", "check(a)", "find(a)", "what(a)"], "answer": 0},
        {"q": "문자열 '123'을 진짜 숫자 123으로 바꾸는 함수는?", "choices": ["int()", "str()", "num()", "math()"], "answer": 0},
        {"q": "숫자 456을 문자열 '456'으로 바꾸는 함수는?", "choices": ["str()", "string()", "word()", "int()"], "answer": 0},
        {"q": "a = 2\\nb = 3\\nprint(a ** b) 의 결과는? (2의 3제곱)", "choices": ["8", "6", "5", "9"], "answer": 0},
        {"q": "파이썬에서 '같지 않다'를 뜻하는 비교 기호는?", "choices": ["!=", "==", "<>", "not="], "answer": 0},
        {"q": "10 >= 5 의 결과는 참(True)인가요 거짓(False)인가요?", "choices": ["True", "False", "10", "5"], "answer": 0},
        {"q": "True 와 False의 첫 글자는 반드시 어떻게 써야 하나요?", "choices": ["대문자", "소문자", "상관없음", "기호로 쓴다"], "answer": 0},
    ],
    # 3회: 리스트
    [
        {"q": "리스트를 만들 때 사용하는 괄호는?", "choices": ["[ ]", "( )", "{ }", "< >"], "answer": 0},
        {"q": "리스트 a = ['사과', '바나나', '포도'] 가 있습니다. '사과'를 꺼내는 코드는?", "choices": ["a[0]", "a[1]", "a[사과]", "a.first()"], "answer": 0},
        {"q": "a = [10, 20, 30] 일 때, a[2] 의 값은?", "choices": ["30", "20", "10", "오류"], "answer": 0},
        {"q": "리스트의 맨 끝에 새로운 항목을 추가하는 명령어는?", "choices": ["append()", "add()", "insert()", "push()"], "answer": 0},
        {"q": "리스트의 길이를 알아내는 함수는?", "choices": ["len()", "size()", "count()", "length()"], "answer": 0},
        {"q": "a = [1, 2, 3] 이고 b = [4, 5] 일 때, a + b 의 결과는?", "choices": ["[1, 2, 3, 4, 5]", "15", "오류", "[[1, 2, 3], [4, 5]]"], "answer": 0},
        {"q": "a = ['월', '화', '수'] 일 때 맨 마지막 항목을 뜻하는 인덱스는?", "choices": ["-1", "3", "last", "end"], "answer": 0},
        {"q": "리스트에서 특정 위치의 항목을 삭제하는 키워드는?", "choices": ["del", "remove()", "pop()", "셋 다 가능함"], "answer": 3},
        {"q": "리스트 안에 리스트가 들어갈 수 있나요? (예: a = [[1,2], [3,4]])", "choices": ["가능하다", "불가능하다", "숫자만 가능하다", "에러가 난다"], "answer": 0},
        {"q": "파이썬 인덱스 번호는 항상 몇 번부터 시작하나요?", "choices": ["0번", "1번", "상관없음", "-1번"], "answer": 0},
    ],
    # 4회: 조건문 기초
    [
        {"q": "if문을 작성할 때 조건 끝에 반드시 찍어야 하는 기호는?", "choices": [": (콜론)", "; (세미콜론)", ". (마침표)", "아무것도 안 찍음"], "answer": 0},
        {"q": "if문 안쪽에 속한 코드를 쓰려면 어떻게 해야 하나요?", "choices": ["들여쓰기(스페이스 4칸)", "대괄호로 감싸기", "한 줄 띄우기", "따옴표 치기"], "answer": 0},
        {"q": "if 조건이 거짓(False)일 때 실행할 내용을 적는 곳은?", "choices": ["else:", "if not:", "false:", "other:"], "answer": 0},
        {"q": "score = 80 일 때, if score >= 90: 은 어떻게 될까요?", "choices": ["실행되지 않는다", "실행된다", "에러가 난다", "90으로 바뀐다"], "answer": 0},
        {"q": "조건이 3개 이상일 때 사용하는 키워드는? (if -> ? -> else)", "choices": ["elif", "else if", "if else", "elseif"], "answer": 0},
        {"q": "x = 10 이 홀수인지 짝수인지 확인하려면 어떤 기호를 쓸까요?", "choices": ["x % 2 == 0", "x / 2 == 0", "x // 2 == 0", "x * 2 == 0"], "answer": 0},
        {"q": "if a == b: 의 뜻은 무엇인가요?", "choices": ["a와 b가 같다면", "a에 b를 넣어라", "a와 b가 다르다면", "a가 b보다 크다면"], "answer": 0},
        {"q": "파이썬에서 '들여쓰기'가 잘못되면 어떻게 되나요?", "choices": ["IndentationError(오류)가 난다", "그냥 무시하고 실행된다", "컴퓨터가 알아서 고친다", "실행 속도가 느려진다"], "answer": 0},
        {"q": "if True: 아래의 코드는 어떻게 될까요?", "choices": ["무조건 실행된다", "절대 실행되지 않는다", "에러가 난다", "한 번만 무시된다"], "answer": 0},
        {"q": "비밀번호 검사 코드로 적절한 것은?", "choices": ["if pw == '1234':", "if pw = '1234':", "if pw === '1234':", "if pw => '1234':"], "answer": 0},
    ],
    # 5회: 논리 연산과 복합 조건
    [
        {"q": "두 조건이 '모두' 참이어야 통과시키는 키워드는?", "choices": ["and", "or", "not", "both"], "answer": 0},
        {"q": "두 조건 중 '하나만' 참이어도 통과시키는 키워드는?", "choices": ["or", "and", "not", "any"], "answer": 0},
        {"q": "조건을 반대로(참을 거짓으로, 거짓을 참으로) 뒤집는 키워드는?", "choices": ["not", "reverse", "flip", "!"], "answer": 0},
        {"q": "age = 15, height = 150 입니다. (age >= 12 and height >= 140) 의 결과는?", "choices": ["True", "False", "에러", "숫자 150"], "answer": 0},
        {"q": "score = 80 입니다. (score > 90 or score == 80) 의 결과는?", "choices": ["True", "False", "에러", "숫자 80"], "answer": 0},
        {"q": "not (5 > 10) 의 결과는?", "choices": ["True", "False", "에러", "숫자 5"], "answer": 0},
        {"q": "'사과' in ['사과', '바나나'] 의 결과는? (in 연산자)", "choices": ["True", "False", "에러", "'사과'"], "answer": 0},
        {"q": "'포도' not in ['사과', '바나나'] 의 결과는?", "choices": ["True", "False", "에러", "'포도'"], "answer": 0},
        {"q": "놀이기구 탑승: 나이 10살 이상, 키 120 이상. 적절한 코드는?", "choices": ["age >= 10 and height >= 120", "age >= 10 or height >= 120", "age > 10 and height > 120", "age > 10 or height > 120"], "answer": 0},
        {"q": "if문 조건에 and와 or를 같이 쓸 수 있나요?", "choices": ["네, 여러 개 연결해서 쓸 수 있어요.", "아니요, 하나만 써야 해요.", "에러가 납니다.", "파이썬에서는 불가능합니다."], "answer": 0},
    ],
    # 6회: 반복문 기초 (for)
    [
        {"q": "정해진 횟수만큼 반복할 때 사용하는 키워드는?", "choices": ["for", "while", "if", "def"], "answer": 0},
        {"q": "for i in range(5): 는 몇 번 반복될까요?", "choices": ["5번 (0,1,2,3,4)", "6번 (0~5)", "4번 (1~4)", "5번 (1~5)"], "answer": 0},
        {"q": "range(1, 4) 가 만들어내는 숫자는?", "choices": ["1, 2, 3", "1, 2, 3, 4", "0, 1, 2, 3", "0, 1, 2, 3, 4"], "answer": 0},
        {"q": "range(0, 10, 2) 의 2는 무슨 뜻인가요?", "choices": ["2씩 건너뛰며(짝수)", "2번만 반복", "2부터 시작", "2로 나누기"], "answer": 0},
        {"q": "for i in range(3): 안에서 print('안녕') 을 쓰면 안녕은 몇 번 나올까요?", "choices": ["3번", "4번", "2번", "1번"], "answer": 0},
        {"q": "for문도 끝에 콜론(:)을 찍어야 하나요?", "choices": ["네, 반드시 찍어야 합니다.", "아니요, 안 찍어도 됩니다.", "if문만 찍습니다.", "세미콜론(;)을 찍습니다."], "answer": 0},
        {"q": "for문 안쪽에 있는 코드는 어떻게 구별하나요?", "choices": ["들여쓰기(스페이스 4칸)", "대괄호 묶기", "번호 매기기", "색깔 칠하기"], "answer": 0},
        {"q": "for i in 'Hello': 처럼 글자를 넣으면 어떻게 되나요?", "choices": ["H, e, l, l, o 한 글자씩 반복됩니다.", "에러가 납니다.", "Hello 전체가 1번 반복됩니다.", "무한 반복됩니다."], "answer": 0},
        {"q": "반복을 돌다가 중간에 아예 멈추고(탈출하고) 싶을 때 쓰는 키워드는?", "choices": ["break", "stop", "exit", "quit"], "answer": 0},
        {"q": "반복을 돌다가 이번 순서만 건너뛰고 다음으로 넘어가고 싶을 때는?", "choices": ["continue", "pass", "skip", "next"], "answer": 0},
    ],
    # 7회: 리스트와 반복문
    [
        {"q": "fruits = ['사과', '바나나', '포도'] 일 때, 모든 과일을 하나씩 출력하려면?", "choices": ["for f in fruits: print(f)", "for fruits: print(f)", "print(fruits)", "for f in range(fruits):"], "answer": 0},
        {"q": "nums = [1, 2, 3]\\nfor n in nums:\\n    print(n * 10)\\n결과는?", "choices": ["10, 20, 30", "1, 2, 3", "102030", "에러"], "answer": 0},
        {"q": "리스트의 총합(다 더한 값)을 구할 때, 처음에 total 변수를 얼마로 만들어야 할까요?", "choices": ["0", "1", "10", "빈 리스트"], "answer": 0},
        {"q": "scores = [80, 90, 100]\\nfor s in scores:\\n    if s >= 90:\\n        print('합격')\\n합격은 몇 번 출력될까요?", "choices": ["2번", "3번", "1번", "0번"], "answer": 0},
        {"q": "for i in range(len(a)): 에서 len(a)는 무슨 역할인가요?", "choices": ["리스트 a의 길이만큼 반복하기 위해", "a를 지우기 위해", "a를 숫자 0으로 바꾸기 위해", "아무 의미 없음"], "answer": 0},
        {"q": "리스트를 반복하면서 번호(인덱스)와 값을 같이 꺼내주는 마법의 함수는?", "choices": ["enumerate()", "number()", "zip()", "list()"], "answer": 0},
        {"q": "짝수만 골라서 새 리스트에 넣고 싶을 때 사용하는 방법은?", "choices": ["for문과 if문을 섞어 쓴다.", "for문만 쓰면 된다.", "if문만 쓰면 된다.", "리스트는 원래 짝수만 담긴다."], "answer": 0},
        {"q": "반복문 안에서 append() 를 쓰면 어떻게 되나요?", "choices": ["리스트에 여러 개의 값이 계속 추가된다.", "에러가 난다.", "리스트가 초기화된다.", "맨 앞의 값이 지워진다."], "answer": 0},
        {"q": "a = []\\nfor i in range(3):\\n    a.append(i)\\nprint(a) 의 결과는?", "choices": ["[0, 1, 2]", "[1, 2, 3]", "[3, 3, 3]", "오류"], "answer": 0},
        {"q": "문자열 'Python'도 리스트처럼 for문에 넣을 수 있나요?", "choices": ["네, 한 글자씩 출력됩니다.", "아니요, 문자열은 안 됩니다.", "에러가 납니다.", "숫자만 가능합니다."], "answer": 0},
    ],
    # 8회: while 반복문
    [
        {"q": "while문의 뜻은 무엇인가요?", "choices": ["~하는 동안 계속해라", "만약 ~라면", "모든 요소에 대해", "정해진 횟수만큼"], "answer": 0},
        {"q": "while True: 는 무슨 뜻일까요?", "choices": ["조건이 항상 참이므로 무한히 반복해라", "한 번만 실행해라", "에러가 난다", "조건이 틀렸다"], "answer": 0},
        {"q": "n = 0\\nwhile n < 3:\\n    print(n)\\n    n = n + 1\\n결과는?", "choices": ["0, 1, 2", "1, 2, 3", "0, 1, 2, 3", "무한 반복"], "answer": 0},
        {"q": "위 문제에서 n = n + 1 이 없다면 어떻게 되나요?", "choices": ["0이 무한히 출력된다 (무한 루프)", "아무것도 안 나온다", "에러가 난다", "한 번만 출력된다"], "answer": 0},
        {"q": "사용자가 '종료'를 입력할 때까지 계속 물어보려면 어떤 반복문을 쓸까요?", "choices": ["while문", "for문", "if문", "def문"], "answer": 0},
        {"q": "while문을 즉시 멈추고 빠져나오는(부수고 나오는) 명령어는?", "choices": ["break", "stop", "exit", "quit"], "answer": 0},
        {"q": "while문에서 continue를 만나면 어떻게 되나요?", "choices": ["아래 코드를 무시하고 조건 검사(맨 위)로 돌아간다", "반복문이 아예 끝난다", "프로그램이 종료된다", "에러가 난다"], "answer": 0},
        {"q": "while n > 0: 은 n이 어떨 때 반복하나요?", "choices": ["0보다 클 때 (양수일 때)", "0일 때", "0보다 작을 때", "0과 같거나 클 때"], "answer": 0},
        {"q": "카운트다운을 만들려면 n = n - 1 을 넣어야 할까요?", "choices": ["네, 값을 줄여나가야 합니다.", "아니요, 값을 더해야 합니다.", "변하지 않게 둡니다.", "0으로 만듭니다."], "answer": 0},
        {"q": "파이썬 게임(Pygame)에서 게임이 계속 켜져있게 하는 심장 역할은?", "choices": ["while True:", "for i in range(100):", "if True:", "def game():"], "answer": 0},
    ],
    # 9회: 함수 (def)
    [
        {"q": "파이썬에서 나만의 함수를 만들 때 시작하는 단어는?", "choices": ["def", "function", "make", "fun"], "answer": 0},
        {"q": "함수의 이름을 지을 때 지켜야 할 것은?", "choices": ["띄어쓰기를 하지 않는다 (대신 밑줄_ 사용)", "무조건 한글로 짓는다", "숫자로 시작해야 한다", "기호를 맘껏 쓴다"], "answer": 0},
        {"q": "def hello():\\n    print('안녕')\\n을 만들었습니다. 어떻게 실행(호출)하나요?", "choices": ["hello()", "hello", "run(hello)", "def hello"], "answer": 0},
        {"q": "함수 안으로 던져주는 값(예: add(3, 4)의 3과 4)을 담는 상자를 무엇이라 하나요?", "choices": ["매개변수 (파라미터)", "리스트", "조건문", "반환값"], "answer": 0},
        {"q": "함수가 계산을 다 하고 결과를 밖으로 던져줄(뱉어줄) 때 쓰는 키워드는?", "choices": ["return", "give", "send", "throw"], "answer": 0},
        {"q": "def add(a, b):\\n    return a + b\\nprint(add(2, 3)) 의 결과는?", "choices": ["5", "23", "a+b", "오류"], "answer": 0},
        {"q": "함수를 쓰는 가장 큰 이유는 무엇일까요?", "choices": ["똑같은 코드를 여러 번 쓰지 않고 재사용하려고", "프로그램 속도를 늦추려고", "코드를 어렵게 보이려고", "에러를 만들려고"], "answer": 0},
        {"q": "return을 만나면 함수는 어떻게 되나요?", "choices": ["값을 던져주고 함수는 즉시 끝난다", "계속 아래 코드를 실행한다", "무한 반복된다", "에러가 난다"], "answer": 0},
        {"q": "파이썬에 원래 들어있는 내장 함수가 아닌 것은?", "choices": ["make_pizza()", "print()", "len()", "type()"], "answer": 0},
        {"q": "함수 안에서 만들어진 변수는 함수 밖에서도 쓸 수 있나요?", "choices": ["아니요, 함수가 끝나면 사라집니다 (지역변수).", "네, 언제든 쓸 수 있습니다.", "비밀번호를 입력해야 합니다.", "모릅니다."], "answer": 0},
    ],
    # 10회: 종합 퀴즈 마스터
    [
        {"q": "다음 중 성격이 완전 다른 자료형은?", "choices": ["[1, 2, 3] (리스트)", "'123' (문자열)", "123 (정수)", "True (불리언)"], "answer": 0},
        {"q": "a = 5\\na += 2\\nprint(a) 의 결과는?", "choices": ["7", "2", "52", "오류"], "answer": 0},
        {"q": "빈 리스트를 만드는 올바른 코드는?", "choices": ["a = []", "a = 0", "a = ''", "a = None"], "answer": 0},
        {"q": "파이썬에서 '주석'이 하는 역할은?", "choices": ["메모를 남긴다 (컴퓨터는 무시함)", "화면에 출력한다", "에러를 고친다", "반복한다"], "answer": 0},
        {"q": "문자열 '사과'의 길이는 len('사과')로 구하면 얼마인가요?", "choices": ["2", "1", "4", "0"], "answer": 0},
        {"q": "print(10 == 10 and 5 > 1) 의 결과는?", "choices": ["True", "False", "에러", "10"], "answer": 0},
        {"q": "x가 10보다 크거나 5보다 작을 때를 나타내는 조건식은?", "choices": ["x > 10 or x < 5", "x > 10 and x < 5", "x >= 10 and x <= 5", "10 < x < 5"], "answer": 0},
        {"q": "while문을 멈추게 하는 코드는?", "choices": ["break", "stop", "continue", "return"], "answer": 0},
        {"q": "리스트 요소들을 거꾸로 뒤집는 함수나 방법은?", "choices": ["reverse()", "flip()", "back()", "turn()"], "answer": 0},
        {"q": "파이썬 코딩 마스터가 되기 위해 가장 중요한 것은?", "choices": ["포기하지 않고 계속 만들어보기!", "눈으로만 읽기", "복사해서 붙여넣기만 하기", "컴퓨터 끄기"], "answer": 0},
    ]
]


with open('gen_python_basics.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Tab Bar
old_tab_bar = """  <nav class="tab-bar">
    <button class="tab-btn active" id="tabExplore" data-tab="explore">🚀 행성 탐험</button>
    <button class="tab-btn" id="tabProblems" data-tab="problems">🧠 생각하는 응용문제</button>
    <button class="tab-btn" id="tabTest" data-tab="test">💯 실력 평가</button>
  </nav>"""
new_tab_bar = """  <nav class="tab-bar">
    <button class="tab-btn active" id="tabExplore" data-tab="explore">🚀 행성 탐험</button>
    <button class="tab-btn" id="tabProblems" data-tab="problems">🧠 생각하는 응용문제</button>
    <button class="tab-btn" id="tabConcept" data-tab="concept">💡 개념 쏙쏙 점검</button>
    <button class="tab-btn" id="tabTest" data-tab="test">💯 실전 모의고사</button>
  </nav>"""
content = content.replace(old_tab_bar, new_tab_bar)

# 2. Add CONCEPT CHECK and MOCK EXAM Views
# Replace the old testView with the new views
import re
# Find the old SCORE TEST TAB VIEW block and replace it
# We will use string slicing
start_str = "  <!-- SCORE TEST TAB VIEW -->"
end_str = "  <!-- TROPHY VIEW -->"
start_idx = content.find(start_str)
end_idx = content.find(end_str)

new_views_html = """
  <!-- CONCEPT CHECK TAB VIEW -->
  <div class="test-view" id="conceptView" style="display:none;">
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
  <div class="test-view" id="testView" style="display:none;">
    <!-- LOBBY -->
    <div id="mockLobby">
      <div class="lesson-head">
        <div class="emoji">💯</div>
        <h2>실전 모의고사 (총 10회)</h2>
      </div>
      <div class="speech">🐍 회차를 거듭할수록 조금씩 새로워집니다! 100점에 도전하세요.</div>
      <div id="mockLobbyList" style="display:flex; flex-direction:column; gap:10px; margin-top:20px;"></div>
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
"""
content = content[:start_idx] + new_views_html + content[end_idx:]

# 3. Update switchTab and showView logic
content = content.replace("document.getElementById('testView').classList.toggle('show', name==='test');",
                          "document.getElementById('testView').classList.toggle('show', name==='test');\n  document.getElementById('conceptView').classList.toggle('show', name==='concept');")

content = content.replace("document.getElementById('tabTest').classList.toggle('active', tab==='test');",
                          "document.getElementById('tabConcept').classList.toggle('active', tab==='concept');\n  document.getElementById('tabTest').classList.toggle('active', tab==='test');")

content = content.replace("} else if(tab==='test') {", "} else if(tab==='concept') {\n    showView('concept');\n  } else if(tab==='test') {")
content = content.replace("document.getElementById('tabTest').addEventListener('click', ()=>switchTab('test'));",
                          "document.getElementById('tabConcept').addEventListener('click', ()=>switchTab('concept'));\ndocument.getElementById('tabTest').addEventListener('click', ()=>switchTab('test'));")


# 4. Inject Data and JS Logic
# Remove old TEST_PROBLEMS array and old test logic
start_idx_js = content.find("const TEST_PROBLEMS = [")
end_idx_js = content.find("function updateProblemsProgress(){")

js_data = "const CONCEPT_PROBLEMS = " + json.dumps(concept_questions, ensure_ascii=False) + ";\n"
js_data += "const MOCK_EXAMS = " + json.dumps(mock_exams, ensure_ascii=False) + ";\n"

js_logic = """
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
"""

content = content[:start_idx_js] + js_data + js_logic + "\n" + content[end_idx_js:]

# 5. Fix Shuffle Logic in init
shuffle_concept_mock = """
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
"""
# Replace old TEST_PROBLEMS shuffle logic
content = re.sub(r"if \(typeof TEST_PROBLEMS !== 'undefined'\) \{[\s\S]*?\}\n", shuffle_concept_mock, content)

# 6. Initial Renders
content = content.replace("renderTest();", "renderConcept();\nrenderMockLobby();")

with open('gen_python_basics.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Mock Exams and Concept Check generated successfully.")
