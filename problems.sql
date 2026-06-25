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
);

-- Enable Row Level Security (RLS) but allow public reads/writes for guest access
ALTER TABLE problems ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow public read access" ON problems
  FOR SELECT USING (true);

CREATE POLICY "Allow public insert access" ON problems
  FOR INSERT WITH CHECK (true);
