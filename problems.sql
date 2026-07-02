-- Create problems table
CREATE TABLE IF NOT EXISTS problems (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  type TEXT NOT NULL, -- 'code' or 'blank'
  description TEXT NOT NULL,
  input_desc TEXT,
  output_desc TEXT,
  examples JSONB, -- Array of {input, output}
  starter_code TEXT,
  test_cases JSONB, -- Array of {input, output}
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Clean existing data
TRUNCATE TABLE problems RESTART IDENTITY;

-- Seed the 10 questions
INSERT INTO problems (id, title, type, description, input_desc, output_desc, examples, starter_code, test_cases) VALUES
(
  1,
  '문제 1 - 세 수의 합과 평균 (빈칸 채우기)',
  'blank',
  '세 수의 합과 평균을 구하려 합니다. 표준 입력으로 수 세 개를 입력받아, 세 수의 합과 평균을 출력하도록 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요. (평균은 소수 셋째자리에서 반올림하여 둘째자리까지 출력하세요)',
  '표준 입력으로 숫자 세 개가 주어집니다. 세 수는 1 이상 100 이하인 자연수입니다.',
  '세 수의 합과 평균을 출력해주세요.',
  '[{"input": "5 3 6", "output": "sum = 14\navg = 4.67"}, {"input": "1 4 2", "output": "sum = 7\navg = 2.33"}]'::jsonb,
  'a, b, c = map(int, input("세 수를 입력하세요 ").split())

hap = a + b + c
ave = hap / 3
print( @@@ );
print( @@@ )
',
  '[{"input": "5 3 6", "output": "sum = 14\navg = 4.67"}, {"input": "1 4 2", "output": "sum = 7\navg = 2.33"}, {"input": "10 20 30", "output": "sum = 60\navg = 20.00"}]'::jsonb
),
(
  2,
  '문제 2 - 두 문자열의 길이 합 (소스코드 작성)',
  'code',
  '두 문자열을 입력 받아 두 문자열의 길이의 합을 출력하세요. 첫 번째 입력받은 문자열의 길이는 10, 두 번째 문자열의 길이는 16입니다. 길이의 합은 26입니다.',
  '표준 입력으로 문자열 두 개가 주어집니다. 두 문자열의 길이는 1 이상 100 이하입니다. (공백 또는 줄바꿈으로 구분되어 주어질 수 있습니다.)',
  '두 문자열의 길이의 합을 출력해 주세요.',
  '[{"input": "HelloWorld Programmingisfun", "output": "26"}]'::jsonb,
  '# 두 문자열을 입력받아 길이의 합을 출력하세요.
# 예: input().split() 또는 각각 input() 등으로 처리 가능
',
  '[{"input": "HelloWorld Programmingisfun", "output": "26"}, {"input": "abc defg", "output": "7"}, {"input": "Python Rules", "output": "11"}]'::jsonb
),
(
  3,
  '문제 3 - 직각삼각형 출력 (소스코드 작성)',
  'code',
  '별("*")로 밑변과 높이가 N인 직각삼각형을 출력하려고 합니다. 표준 입력으로 자연수 N을 입력받아 밑변과 높이가 N인 직각삼각형을 출력해주세요.',
  '표준 입력으로 자연수 N이 주어집니다. N은 1 이상 100 이하입니다.',
  '별로 밑변과 높이가 N인 직각삼각형을 출력해주세요.',
  '[{"input": "5", "output": "*\n**\n***\n****\n*****"}]'::jsonb,
  'n = int(input())
# 여기에 코드를 작성해 직각삼각형을 출력하세요.
',
  '[{"input": "5", "output": "*\n**\n***\n****\n*****"}, {"input": "1", "output": "*"}, {"input": "3", "output": "*\n**\n***"}]'::jsonb
),
(
  4,
  '문제 4 - 따옴표 붙이기 (빈칸 채우기)',
  'blank',
  '문자열 한 개가 주어졌을 때, 주어진 문자열 양 옆에 작은따옴표를 붙이려 합니다. 표준 입력으로 문자열 한 개를 입력받아, 입력받은 문자열 양 옆에 작은따옴표를 붙여 출력하도록 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.',
  '표준 입력으로 문자열 한 개가 주어집니다. 문자열은 알파벳 대문자와 소문자로만 이루어집니다. 문자열 길이는 1 이상 100 이하입니다.',
  '입력받은 문자열 양 옆에 작은따옴표를 붙여 출력해주세요.',
  '[{"input": "HelloWorld", "output": "\u0027HelloWorld\u0027"}, {"input": "Quote", "output": "\u0027Quote\u0027"}]'::jsonb,
  's = input("")

print( @@@ )
',
  '[{"input": "HelloWorld", "output": "\u0027HelloWorld\u0027"}, {"input": "Quote", "output": "\u0027Quote\u0027"}, {"input": "Python", "output": "\u0027Python\u0027"}]'::jsonb
),
(
  5,
  '문제 5 - 홀짝 판별 (소스코드 작성)',
  'code',
  '수 한 개가 주어졌을 때 그 숫자가 짝수인지 홀수인지 판별하는 프로그램을 작성하세요.',
  '표준 입력으로 숫자 한 개가 주어집니다. 입력되는 수는 1이상 1,000 이하인 정수입니다.',
  '입력받은 수의 홀수 또는 짝수를 출력해주세요.',
  '[{"input": "13", "output": "홀수"}, {"input": "6", "output": "짝수"}]'::jsonb,
  'n = int(input())
# 여기에 코드를 작성하여 홀수 또는 짝수를 출력하세요.
',
  '[{"input": "13", "output": "홀수"}, {"input": "6", "output": "짝수"}, {"input": "100", "output": "짝수"}, {"input": "1", "output": "홀수"}]'::jsonb
),
(
  6,
  '문제 6 - 두 수의 차 (소스코드 작성)',
  'code',
  '표준 입력으로 두 수를 입력 받아 큰수에서 작은수의 차를 출력하세요.',
  '표준 입력으로 숫자 두 개가 주어집니다. 두 숫자는 1 이상 100 이하인 자연수입니다.',
  '두 수 중 큰수에서 작은수의 차를 출력해주세요.',
  '[{"input": "5 7", "output": "2"}, {"input": "10 2", "output": "8"}, {"input": "5 5", "output": "0"}]'::jsonb,
  '# 표준 입력으로 두 수를 받아 큰 수와 작은 수의 차이를 구하세요.
',
  '[{"input": "5 7", "output": "2"}, {"input": "10 2", "output": "8"}, {"input": "5 5", "output": "0"}, {"input": "1 100", "output": "99"}]'::jsonb
),
(
  7,
  '문제 7 - 역순 숫자 출력 (빈칸 채우기)',
  'blank',
  'n부터 1까지의 숫자를 출력하려고 합니다. 표준 입력으로 자연수 n을 받아 n부터 1까지의 정수를 가로로 출력하는 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.',
  '표준 입력으로 자연수 n이 주어집니다. n은 1 이상 1,000 이하입니다.',
  'n부터 1까지의 자연수를 가로로 출력해주세요.',
  '[{"input": "5", "output": "5 4 3 2 1"}]'::jsonb,
  'n = int(input(""))

while @@@ :
    print( @@@ )
    @@@
',
  '[{"input": "5", "output": "5 4 3 2 1"}, {"input": "1", "output": "1"}, {"input": "10", "output": "10 9 8 7 6 5 4 3 2 1"}]'::jsonb
),
(
  8,
  '문제 8 - 짝수와 홀수의 개수 (소스코드 작성)',
  'code',
  '길이가 n인 배열 arr에서 짝수의 개수와 홀수의 개수를 출력하세요. 표준 입력으로 자연수 n과 배열 arr을 입력받아, 짝수의 개수와 홀수의 개수를 출력하는 코드를 작성하려 합니다.',
  '표준 입력으로 자연수 n과 배열 arr이 주어집니다. n은 2 이상 50 이하입니다. arr의 원소는 1 이상 100 이하인 정수입니다. (입력은 첫 줄에 n, 둘째 줄에 배열의 원소들이 공백으로 주어집니다.)',
  '배열 arr에서 홀수의 개수와 짝수의 개수를 차례대로 출력해주세요.',
  '[{"input": "5\n3 6 2 1 10", "output": "2 3"}]'::jsonb,
  '# n과 배열을 입력받아 홀수 개수와 짝수 개수를 출력하는 코드를 작성하세요.
',
  '[{"input": "5\n3 6 2 1 10", "output": "2 3"}, {"input": "2\n2 4", "output": "0 2"}, {"input": "3\n1 3 5", "output": "3 0"}]'::jsonb
),
(
  9,
  '문제 9 - 배열의 합과 평균 (빈칸 채우기)',
  'blank',
  '길이가 n인 배열 arr의 합과 평균을 출력하세요. 표준 입력으로 자연수 n과 배열 arr을 입력받아, arr배열의 총합과 평균을 출력하는 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요. (평균은 소수 첫째자리까지 출력하세요)',
  '표준 입력으로 자연수 n과 배열 arr이 주어집니다. n은 2 이상 50 이하입니다. arr의 원소는 1 이상 100 이하인 정수입니다. (입력은 첫 줄에 n, 둘째 줄에 배열의 원소들이 공백으로 주어집니다.)',
  '배열 arr의 총합과 평균을 차례대로 출력해주세요.',
  '[{"input": "6\n12 1 9 17 31 7", "output": "77\n12.8"}]'::jsonb,
  'n = int(input(""))
arr= []
arr = input().split()

hap = 0
avg = 0

for i in range(n):
    arr[i] = int(arr[i])

for x in @@@:
    hap += @@@

print(hap)
print( @@@ )
',
  '[{"input": "6\n12 1 9 17 31 7", "output": "77\n12.8"}, {"input": "3\n10 20 30", "output": "60\n20.0"}]'::jsonb
),
(
  10,
  '문제 10 - p와 P의 개수 (빈칸 채우기)',
  'blank',
  '문자열 s에서 \u0027p\u0027와 \u0027P\u0027의 개수를 출력해주세요. 예를 들어 s가 "happyHappy"일 때, \u0027p\u0027와 \u0027P\u0027의 개수 4를 출력합니다.',
  '표준 입력으로 문자열 s가 주어집니다. 문자열 s의 길이는 1 이상 1,000 이하입니다. 문자열 s는 영문자로 이루어진 문자열입니다.',
  '문자열 s에서 \u0027p\u0027와 \u0027P\u0027의 개수를 출력해주세요.',
  '[{"input": "Happy", "output": "2"}, {"input": "Programmingpython", "output": "2"}]'::jsonb,
  's = input("")

cnt = 0
for x in @@@:
   if @@@:
        cnt += 1

print(cnt)
',
  '[{"input": "Happy", "output": "2"}, {"input": "Programmingpython", "output": "2"}, {"input": "applePie", "output": "3"}, {"input": "abc", "output": "0"}]'::jsonb
),
(
  76,
  '[5차] [문제 1] 이름과 나이 출력 (소스코드 작성)',
  'code',
  '이름과 나이를 입력 받아 다음과 같이 출력되는 프로그램을 작성하세요.',
  '첫 줄에 이름(영문자)이 주어지고, 두 번째 줄에 나이가 입력된다.',
  '출력의 예처럼 출력하세요.',
  '[{"input": "Hong Gil Dong\n16", "output": "Your name is Hong Gil Dong.\nI''m 16 years old."}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "Hong Gil Dong\n16", "output": "Your name is Hong Gil Dong.\nI''m 16 years old."}, {"input": "Alice\n20", "output": "Your name is Alice.\nI''m 20 years old."}, {"input": "Kim Chul Soo\n17", "output": "Your name is Kim Chul Soo.\nI''m 17 years old."}]'::jsonb
),
(
  77,
  '[5차] [문제 2] 사칙연산과 나머지 연산 (소스코드 작성)',
  'code',
  '2개의 수를 입력 받아 출력의 예처럼 출력하세요.',
  '표준 입력으로 정수 2개가 주어집니다.',
  '출력의 예처럼 사칙연산과 나머지 연산 결과를 출력하세요.',
  '[{"input": "10\n4", "output": "10 + 4 = 14\n10 - 4  =  6\n10 x 4  =  40\n10 / 4   =  2\n10 % 4 =  2"}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "10\n4", "output": "10 + 4 = 14\n10 - 4  =  6\n10 x 4  =  40\n10 / 4   =  2\n10 % 4 =  2"}, {"input": "12\n5", "output": "12 + 5 = 17\n12 - 5  =  7\n12 x 5  =  60\n12 / 5   =  2\n12 % 5 =  2"}]'::jsonb
),
(
  78,
  '[5차] [문제 3] 역정수 삼각형 출력 (소스코드 작성)',
  'code',
  '정수 N인 정수 삼각형을 출력하려고 합니다. 예를 들어, N이 5일 때 출력 예시와 같이 줄어드는 형태로 출력합니다.',
  '표준 입력으로 자연수 N이 주어집니다. (1 <= N <= 100)',
  '크기가 N인 정수 삼각형을 출력해주세요.',
  '[{"input": "5", "output": "1 2 3 4 5\n1 2 3 4\n1 2 3\n1 2\n1"}]'::jsonb,
  'n = int(input())
# 여기에 코드를 작성해 역삼각형을 출력하세요.
',
  '[{"input": "5", "output": "1 2 3 4 5\n1 2 3 4\n1 2 3\n1 2\n1"}, {"input": "3", "output": "1 2 3\n1 2\n1"}, {"input": "1", "output": "1"}]'::jsonb
),
(
  79,
  '[5차] [문제 4] 세 수 중 최댓값과 최솟값 (소스코드 작성)',
  'code',
  '정수 3개를 입력 받아 가장 큰 수와 가장 작은 수를 출력하는 프로그램을 작성하세요.',
  '정수 3개가 차례대로 주어집니다.',
  '가장 큰 수와 가장 작은 수를 공백으로 구분하여 출력하시오.',
  '[{"input": "5 9 12", "output": "12 5"}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "5 9 12", "output": "12 5"}, {"input": "100 100 50", "output": "100 50"}, {"input": "-3 0 5", "output": "5 -3"}]'::jsonb
),
(
  80,
  '[5차] [문제 5] 약수 구하기 (빈칸 채우기)',
  'blank',
  '1개의 정수를 입력 받아 약수를 출력하는 프로그램을 빈칸을 채워 완성하세요.',
  '표준 입력으로 수 한 개가 주어집니다. (1 <= 정수 <= 1000)',
  '약수를 차례대로 출력하세요.',
  '[{"input": "16", "output": "1 2 4 8 16"}]'::jsonb,
  'n = int(input(""))

for i in range(1, @@@):
    if @@@:
        print(i, end=" ")
',
  '[{"input": "16", "output": "1 2 4 8 16 "}, {"input": "10", "output": "1 2 5 10 "}, {"input": "1", "output": "1 "}]'::jsonb
),
(
  81,
  '[5차] [문제 6] 규칙적인 영문자 출력 (빈칸 채우기)',
  'blank',
  '정수 N을 입력 받아 N개의 영문자를 대/소문자 및 순방향/역방향 규칙에 맞게 출력하는 프로그램의 빈칸(@@@)을 채워 전체 코드를 완성해주세요.',
  '표준 입력으로 자연수 n이 주어집니다.',
  '영문자 N개를 규칙에 따라 출력합니다.',
  '[{"input": "5", "output": "ABCDE\nVWXYZ\nabcde\nvwxyz"}]'::jsonb,
  'n = int(input(""))

for i in range(n):
    print(@@@, end="")

print()
for i in range(n-1,-1,-1):
    print(@@@, end="")

print()
for i in range(n):
    print(@@@, end="")

print()
for i in range(n-1,-1,-1):
    print(@@@, end="")
',
  '[{"input": "5", "output": "ABCDE\nVWXYZ\nabcde\nvwxyz"}, {"input": "3", "output": "ABC\nXYZ\nabc\nxyz"}]'::jsonb
),
(
  82,
  '[5차] [문제 7] 짝수의 합과 평균 (소스코드 작성)',
  'code',
  '10개의 수를 입력 받아 첫 줄에는 짝수를, 둘째 줄에는 짝수의 합을, 셋째 줄에는 짝수의 평균을 출력하는 프로그램을 작성하세요. (평균은 소수 셋째 자리에서 반올림하여 둘째 자리까지 출력)',
  '표준 입력으로 자연수 10개가 차례대로 한 줄씩 주어집니다.',
  '출력의 예와 같이 첫 줄에 짝수 목록, 둘째 줄에 합, 셋째 줄에 평균을 출력하세요.',
  '[{"input": "2\n8\n10\n3\n2\n7\n4\n51\n12\n6", "output": "2 8 10 2 4 12 6 \n44\n6.29"}]'::jsonb,
  '# 입력받기
arr = []

for i in range(10):
    b = input("")
    arr.append(b)

for i in range(10):
    print(arr[i], end = '' '')
',
  '[{"input": "2\n8\n10\n3\n2\n7\n4\n51\n12\n6", "output": "2 8 10 2 4 12 6 \n44\n6.29"}, {"input": "1\n3\n5\n7\n9\n11\n13\n15\n17\n18", "output": "18 \n18\n18.00"}]'::jsonb
),
(
  83,
  '[5차] [문제 8] 10 이상 30 이하의 수 출력 (소스코드 작성)',
  'code',
  '정수 n과 배열 arr을 입력 받아 10 이상 30 이하의 수만 출력하는 프로그램을 작성하세요.',
  '표준 입력으로 자연수 n이 주어지고, 이어서 n개의 배열 요소가 주어집니다. (2 <= n <= 50)',
  '10 이상 30 이하의 수만 공백으로 구분하여 출력하세요.',
  '[{"input": "6\n3\n15\n74\n51\n23\n21", "output": "15 23 21"}]'::jsonb,
  '# 입력 받기
n = int(input(""))

arr = []

for i in range(n):
    b = input("")
    arr.append(b)

for i in range(n):
    print(arr[i], end = '' '')
',
  '[{"input": "6\n3\n15\n74\n51\n23\n21", "output": "15 23 21"}, {"input": "3\n5\n10\n30", "output": "10 30"}]'::jsonb
),
(
  84,
  '[5차] [문제 9] 홀수 번째 문자 출력 (소스코드 작성)',
  'code',
  '문자열을 입력 받아 홀수 번째 문자만 출력하는 프로그램을 작성하세요.',
  '문자열이 주어집니다.',
  '홀수 번째(1번째, 3번째, 5번째 ...) 입력 받은 문자만 차례대로 출력하세요.',
  '[{"input": "ABCDEFGHIJK", "output": "ACEGIK"}]'::jsonb,
  's = input("")
# 여기에 코드를 작성하세요.
',
  '[{"input": "ABCDEFGHIJK", "output": "ACEGIK"}, {"input": "Hello", "output": "Hlo"}]'::jsonb
),
(
  85,
  '[5차] [문제 10] 짝수이면서 5의 배수인 수 (소스코드 작성)',
  'code',
  '자연수 n과 점수 배열 arr을 입력받아, 입력받은 수 중 짝수이면서 5의 배수인 수를 출력하고, 둘째 줄에는 해당 조건에 맞는 수 중 최댓값과 최솟값을 출력하세요.',
  '표준 입력으로 자연수 n이 주어지고 다음 줄에 공백으로 구분된 배열 arr이 주어집니다.',
  '첫 줄에 짝수이면서 5의 배수인 수를 출력하고, 둘째 줄에는 그 중 최댓값과 최솟값을 출력하세요.',
  '[{"input": "8\n5 10 100 7 20 8 4 16", "output": "10 100 20\n100 10"}]'::jsonb,
  'n = int(input(""))

arr = []
arr = input("").split()

for i in range(n):
    arr[i] = int(arr[i])

for i in range(n):
    print(arr[i], end = '' '')
',
  '[{"input": "8\n5 10 100 7 20 8 4 16", "output": "10 100 20\n100 10"}, {"input": "5\n10 15 20 25 30", "output": "10 20 30\n30 10"}]'::jsonb
),
(
  86,
  '[6차] [문제 1] 약수의 개수 구하기 (소스코드 작성)',
  'code',
  '자연수 n을 입력 받아 약수의 개수를 출력하는 프로그램을 작성하세요.',
  '첫 줄에 정수 N이 주어집니다.',
  '출력의 예처럼 n의 약수의 개수를 출력하세요.',
  '[{"input": "12", "output": "6"}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "12", "output": "6"}, {"input": "1", "output": "1"}, {"input": "17", "output": "2"}]'::jsonb
),
(
  87,
  '[6차] [문제 2] 짝지어 출력하기 (빈칸 채우기)',
  'blank',
  'while문을 이용하여 출력의 예처럼 출력하세요.',
  '표준 입력으로 정수 n이 주어집니다. (n은 항상 짝수입니다.)',
  '출력의 예처럼 두 개씩 짝을 지어 출력하세요.',
  '[{"input": "12", "output": "1 2\n3 4\n5 6\n7 8\n9 10\n11 12"}]'::jsonb,
  'i = 1

n = input("")
n = int(n)

while @@@:
    print(i, i+1)
    @@@
',
  '[{"input": "12", "output": "1 2\n3 4\n5 6\n7 8\n9 10\n11 12"}, {"input": "4", "output": "1 2\n3 4"}]'::jsonb
),
(
  88,
  '[6차] [문제 3] 합격 여부 판단 (빈칸 채우기)',
  'blank',
  '세 과목 점수를 입력 받아 세 과목 모두 60점 이상이면 "YES", 아니면 "NO"를 출력하는 프로그램을 작성하세요.',
  '표준 입력으로 정수 3개가 차례대로 주어집니다. (1 <= 점수 <= 100)',
  '세 과목 모두 60점 이상이면 "YES", 하나라도 미달하면 "NO"를 출력하시오.',
  '[{"input": "75\n95\n85", "output": "YES"}]'::jsonb,
  'a = input("")
b = input("")
c = input("")

a = int(a)
b = int(b)
c = int(c)

if @@@:
    print("YES")
else:
    print("NO")
',
  '[{"input": "75\n95\n85", "output": "YES"}, {"input": "75\n95\n55", "output": "NO"}, {"input": "60\n60\n60", "output": "YES"}]'::jsonb
),
(
  89,
  '[6차] [문제 4] 3 또는 7의 배수 출력 (빈칸 채우기)',
  'blank',
  '1 ~ 100 사이의 수 중 3의 배수이거나 7의 배수인 수를 출력하는 프로그램의 빈칸을 채워 소스 코드를 완성하세요.',
  '입력 데이터는 없습니다.',
  '3의 배수이거나 7의 배수를 공백으로 구분하여 출력하세요.',
  '[{"input": "", "output": "3 6 7 9 12 14 15 18 21 24 27 28 30 33 35 "}]'::jsonb,
  'a = 1

while a < 100:
    if @@@:
        print(a, end='' '')
    a += 1
',
  '[{"input": "", "output": "3 6 7 9 12 14 15 18 21 24 27 28 30 33 35 36 39 42 45 48 49 51 54 56 57 60 63 66 69 70 72 75 77 78 81 84 87 90 91 93 96 98 99 "}]'::jsonb
),
(
  90,
  '[6차] [문제 5] 구간 합 포맷 출력 (소스코드 작성)',
  'code',
  '1부터 입력 받은 수까지의 합을 출력의 예처럼 출력하는 프로그램을 작성하세요.',
  '표준 입력으로 수 한 개가 주어집니다. (1 <= 정수 <= 1,000)',
  '출력의 예시 포맷에 맞추어 결과를 출력하세요.',
  '[{"input": "5", "output": "1 ----- 5 = 15"}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "5", "output": "1 ----- 5 = 15"}, {"input": "10", "output": "1 ----- 10 = 55"}, {"input": "100", "output": "1 ----- 100 = 5050"}]'::jsonb
),
(
  91,
  '[6차] [문제 6] 문자열 N번 반복 출력 (소스코드 작성)',
  'code',
  '문자열과 정수 n을 입력 받아, 입력 받은 문자열을 n번 연속해서 출력하세요.',
  '표준 입력으로 문자열과 정수 n이 차례대로 주어집니다.',
  '출력의 예처럼 공백이나 줄바꿈 없이 연속으로 출력하세요.',
  '[{"input": "Hello\n3", "output": "HelloHelloHello"}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "Hello\n3", "output": "HelloHelloHello"}, {"input": "Python\n2", "output": "PythonPython"}]'::jsonb
),
(
  92,
  '[6차] [문제 7] 특정 문자 제거하기 (소스코드 작성)',
  'code',
  '문자열과 문자 1개를 입력 받아, 문자열에서 입력 받은 해당 문자를 모두 제거하고 출력하세요.',
  '표준 입력으로 문자열과 문자가 차례대로 주어집니다.',
  '특정 문자가 제거된 문자열을 출력하세요.',
  '[{"input": "ABCdefabcABC\nA", "output": "BCdefabcBC"}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "ABCdefabcABC\nA", "output": "BCdefabcBC"}, {"input": "hello world\nl", "output": "heo word"}]'::jsonb
),
(
  93,
  '[6차] [문제 8] 수들의 빈도수 구하기 (소스코드 작성)',
  'code',
  '정수 n과 배열 arr을 입력 받아 수들의 빈도수(0의 개수, 1의 개수 ... 9의 개수)를 출력하는 프로그램을 작성하세요.',
  '표준 입력으로 자연수 n이 주어지고, 다음 줄에 n개의 정수 배열 arr이 주어집니다. 원소는 0부터 9까지의 수만 주어집니다.',
  '0부터 9까지 각각의 개수를 한 줄에 하나씩 차례대로 출력하세요.',
  '[{"input": "10\n0 5 7 2 2 1 9 2 1 6 5", "output": "1\n2\n3\n0\n0\n1\n1\n1\n0\n1"}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "10\n0 5 7 2 2 1 9 2 1 6 5", "output": "1\n2\n3\n0\n0\n1\n1\n1\n0\n1"}, {"input": "5\n1 1 2 2 3", "output": "0\n2\n2\n1\n0\n0\n0\n0\n0\n0"}]'::jsonb
),
(
  94,
  '[6차] [문제 9] 5의 배수의 집계 (소스코드 작성)',
  'code',
  '10개의 수를 입력 받아 5의 배수만 출력하고, 두 번째 줄에는 5의 배수의 개수, 합계, 평균을 출력하세요. (평균은 소수 셋째 자리에서 반올림하여 둘째 자리까지 출력)',
  '정수 10개가 공백으로 구분되어 주어집니다.',
  '첫 줄에 5의 배수만 출력합니다. 둘째 줄에 5의 배수의 개수, 합계, 평균을 공백으로 구분하여 출력합니다.',
  '[{"input": "12 5 10 57 30 6 11 90 47 2", "output": "5 10 30 90\n4 135 33.8"}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "12 5 10 57 30 6 11 90 47 2", "output": "5 10 30 90\n4 135 33.8"}, {"input": "5 15 25 35 45 55 65 75 85 95", "output": "5 15 25 35 45 55 65 75 85 95\n10 500 50.0"}]'::jsonb
),
(
  95,
  '[6차] [문제 10] 나머지 구하기 (소스코드 작성)',
  'code',
  '정수 n과 m이 주어질 때, n을 m으로 나눈 나머지를 구하는 프로그램을 작성하세요.',
  '표준 입력으로 정수 n과 m이 주어집니다.',
  '나머지 값을 출력하세요.',
  '[{"input": "3 2", "output": "1"}]'::jsonb,
  '# 여기에 코드를 작성하세요.
',
  '[{"input": "3 2", "output": "1"}, {"input": "10 5", "output": "0"}]'::jsonb
);

-- Enable Row Level Security (RLS) but allow public reads/writes for guest access
ALTER TABLE problems ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow public read access" ON problems
  FOR SELECT USING (true);

CREATE POLICY "Allow public insert access" ON problems
  FOR INSERT WITH CHECK (true);
