export interface Example {
  input: string;
  output: string;
}

export interface Problem {
  id: number;
  title: string;
  type: 'blank' | 'code';
  description: string;
  input_desc: string;
  output_desc: string;
  examples: Example[];
  starter_code: string;
  solution_code?: string;
  test_cases: Example[];
  classLevel?: 2 | 3;
}

export const problems: Problem[] = [
  {
    id: 1,
    classLevel: 3,
    title: "문제 1 - 세 수의 합과 평균 (빈칸 채우기)",
    type: "blank",
    description: "세 수의 합과 평균을 구하려 합니다. 표준 입력으로 수 세 개를 입력받아, 세 수의 합과 평균을 출력하도록 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요. (평균은 소수 셋째자리에서 반올림하여 둘째자리까지 출력하세요)",
    input_desc: "표준 입력으로 숫자 세 개가 주어집니다. 세 수는 1 이상 100 이하인 자연수입니다.",
    output_desc: "세 수의 합과 평균을 출력해주세요.",
    examples: [
      { input: "5 3 6", output: "sum = 14\navg = 4.67" },
      { input: "1 4 2", output: "sum = 7\navg = 2.33" }
    ],
    starter_code: `a, b, c = map(int, input("세 수를 입력하세요 ").split())

hap = a + b + c
ave = hap / 3
print( @@@ );
print( @@@ )
`,
    solution_code: `# [정답 및 해설]
# 1. input().split()으로 세 수를 공백 기준으로 나눕니다.
# 2. map(int, ...)을 이용해 정수로 변환하여 a, b, c에 저장합니다.
# 3. hap(합)과 ave(평균)을 계산합니다. (평균은 3으로 나눕니다.)
# 4. print 함수를 사용하여 sum과 avg를 포맷에 맞춰 출력합니다. (소수 둘째자리 반올림: :.2f)

a, b, c = map(int, input("세 수를 입력하세요 ").split())

hap = a + b + c
ave = hap / 3
print(f"sum = {hap}")
print(f"avg = {ave:.2f}")
`,
    test_cases: [
      { input: "5 3 6", output: "sum = 14\navg = 4.67" },
      { input: "1 4 2", output: "sum = 7\navg = 2.33" },
      { input: "10 20 30", output: "sum = 60\navg = 20.00" }
    ]
  },
  {
    id: 2,
    title: "문제 2 - 두 문자열의 길이 합 (소스코드 작성)",
    type: "code",
    description: "두 문자열을 입력 받아 두 문자열의 길이의 합을 출력하세요. 첫 번째 입력받은 문자열의 길이는 10, 두 번째 문자열의 길이는 16입니다. 길이의 합은 26입니다.",
    input_desc: "표준 입력으로 문자열 두 개가 주어집니다. 두 문자열의 길이는 1 이상 100 이하입니다.",
    output_desc: "두 문자열의 길이의 합을 출력해 주세요.",
    examples: [
      { input: "HelloWorld Programmingisfun", output: "26" }
    ],
    starter_code: `# 두 문자열을 입력받아 길이의 합을 출력하세요.
# 예: input().split() 또는 각각 input() 등으로 처리 가능
`,
    solution_code: `# [정답 및 해설]
# 1. 두 문자열을 input().split()으로 나누어 리스트로 입력받습니다.
# 2. 리스트의 첫 번째 원소와 두 번째 원소의 길이(len)를 구하여 더해줍니다.

s = input().split()
print(len(s[0]) + len(s[1]))
`,
    test_cases: [
      { input: "HelloWorld Programmingisfun", output: "26" },
      { input: "abc defg", output: "7" },
      { input: "Python Rules", output: "11" }
    ]
  },
  {
    id: 3,
    title: "문제 3 - 직각삼각형 출력 (소스코드 작성)",
    type: "code",
    description: "별(\"*\")로 밑변과 높이가 N인 직각삼각형을 출력하려고 합니다. 표준 입력으로 자연수 N을 입력받아 밑변과 높이가 N인 직각삼각형을 출력해주세요.",
    input_desc: "표준 입력으로 자연수 N이 주어집니다. N은 1 이상 100 이하입니다.",
    output_desc: "별로 밑변과 높이가 N인 직각삼각형을 출력해주세요.",
    examples: [
      { input: "5", output: "*\n**\n***\n****\n*****" }
    ],
    starter_code: `n = int(input())
# 여기에 코드를 작성해 직각삼각형을 출력하세요.
`,
    solution_code: `# [정답 및 해설]
# 1. 높이 N을 입력받습니다.
# 2. 1부터 N까지 반복하면서 별('*')을 반복 횟수(i)만큼 곱해 출력합니다.

n = int(input())
for i in range(1, n + 1):
    print("*" * i)
`,
    test_cases: [
      { input: "5", output: "*\n**\n***\n****\n*****" },
      { input: "1", output: "*" },
      { input: "3", output: "*\n**\n***" }
    ]
  },
  {
    id: 4,
    title: "문제 4 - 따옴표 붙이기 (빈칸 채우기)",
    type: "blank",
    description: "문자열 한 개가 주어졌을 때, 주어진 문자열 양 옆에 작은따옴표를 붙이려 합니다. 표준 입력으로 문자열 한 개를 입력받아, 입력받은 문자열 양 옆에 작은따옴표를 붙여 출력하도록 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "표준 입력으로 문자열 한 개가 주어집니다. 문자열은 알파벳 대문자와 소문자로만 이루어집니다. 문자열 길이는 1 이상 100 이하입니다.",
    output_desc: "입력받은 문자열 양 옆에 작은따옴표를 붙여 출력해주세요.",
    examples: [
      { input: "HelloWorld", output: "'HelloWorld'" },
      { input: "Quote", output: "'Quote'" }
    ],
    starter_code: `s = input("")

print( @@@ )
`,
    solution_code: `# [정답 및 해설]
# 1. 입력받은 문자열 양 옆에 f-string을 활용해 작은따옴표를 붙입니다.

s = input("")
print(f"'{s}'")
`,
    test_cases: [
      { input: "HelloWorld", output: "'HelloWorld'" },
      { input: "Quote", output: "'Quote'" },
      { input: "Python", output: "'Python'" }
    ]
  },
  {
    id: 5,
    title: "문제 5 - 홀짝 판별 (소스코드 작성)",
    type: "code",
    description: "수 한 개가 주어졌을 때 그 숫자가 짝수인지 홀수인지 판별하는 프로그램을 작성하세요.",
    input_desc: "표준 입력으로 숫자 한 개가 주어집니다. 입력되는 수는 1이상 1,000 이하인 정수입니다.",
    output_desc: "입력받은 수의 홀수 또는 짝수를 출력해주세요.",
    examples: [
      { input: "13", output: "홀수" },
      { input: "6", output: "짝수" }
    ],
    starter_code: `n = int(input())
# 여기에 코드를 작성하여 홀수 또는 짝수를 출력하세요.
`,
    solution_code: `# [정답 및 해설]
# 1. 정수를 입력받아 2로 나눈 나머지가 0이면 "짝수", 0이 아니면 "홀수"를 출력합니다.

n = int(input())
if n % 2 == 0:
    print("짝수")
else:
    print("홀수")
`,
    test_cases: [
      { input: "13", output: "홀수" },
      { input: "6", output: "짝수" },
      { input: "100", output: "짝수" },
      { input: "1", output: "홀수" }
    ]
  },
  {
    id: 6,
    title: "문제 6 - 두 수의 차 (소스코드 작성)",
    type: "code",
    description: "표준 입력으로 두 수를 입력 받아 큰수에서 작은수의 차를 출력하세요.",
    input_desc: "표준 입력으로 숫자 두 개가 주어집니다. 두 숫자는 1 이상 100 이하인 자연수입니다.",
    output_desc: "두 수 중 큰수에서 작은수의 차를 출력해주세요.",
    examples: [
      { input: "5 7", output: "2" },
      { input: "10 2", output: "8" },
      { input: "5 5", output: "0" }
    ],
    starter_code: `# 표준 입력으로 두 수를 받아 큰 수와 작은 수의 차이를 구하세요.
`,
    solution_code: `# [정답 및 해설]
# 1. 두 수를 입력받습니다.
# 2. 큰 수에서 작은 수를 뺍니다. abs() 내장 함수를 사용하면 순서와 상관없이 차를 구할 수 있습니다.

a, b = map(int, input().split())
print(abs(a - b))
`,
    test_cases: [
      { input: "5 7", output: "2" },
      { input: "10 2", output: "8" },
      { input: "5 5", output: "0" },
      { input: "1 100", output: "99" }
    ]
  },
  {
    id: 7,
    title: "문제 7 - 역순 숫자 출력 (빈칸 채우기)",
    type: "blank",
    description: "n부터 1까지의 숫자를 출력하려고 합니다. 표준 입력으로 자연수 n을 받아 n부터 1까지의 정수를 가로로 출력하는 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "표준 입력으로 자연수 n이 주어집니다. n은 1 이상 1,000 이하입니다.",
    output_desc: "n부터 1까지의 자연수를 가로로 출력해주세요.",
    examples: [
      { input: "5", output: "5 4 3 2 1" }
    ],
    starter_code: `n = int(input(""))

while @@@ :
    print( @@@ )
    @@@
`,
    solution_code: `# [정답 및 해설]
# 1. n이 1 이상인 동안 반복합니다. (while n >= 1)
# 2. n을 가로로 출력하기 위해 print(n, end=" ")을 사용합니다.
# 3. n을 1씩 감소시킵니다. (n -= 1)

n = int(input(""))

while n >= 1 :
    print( n, end=" " )
    n -= 1
`,
    test_cases: [
      { input: "5", output: "5 4 3 2 1" },
      { input: "1", output: "1" },
      { input: "10", output: "10 9 8 7 6 5 4 3 2 1" }
    ]
  },
  {
    id: 8,
    title: "문제 8 - 짝수와 홀수의 개수 (소스코드 작성)",
    type: "code",
    description: "길이가 n인 배열 arr에서 짝수의 개수와 홀수의 개수를 출력하세요. 표준 입력으로 자연수 n과 배열 arr을 입력받아, 짝수의 개수와 홀수의 개수를 출력하는 코드를 작성하려 합니다.",
    input_desc: "표준 입력으로 자연수 n과 배열 arr이 주어집니다. n은 2 이상 50 이하입니다. arr의 원소는 1 이상 100 이하인 정수입니다. (입력은 첫 줄에 n, 둘째 줄에 배열의 원소들이 공백으로 주어집니다.)",
    output_desc: "배열 arr에서 홀수의 개수와 짝수의 개수를 차례대로 출력해주세요.",
    examples: [
      { input: "5\n3 6 2 1 10", output: "2 3" }
    ],
    starter_code: `# n과 배열을 입력받아 홀수 개수와 짝수 개수를 출력하는 코드를 작성하세요.
`,
    solution_code: `# [정답 및 해설]
# 1. 배열의 원소를 반복문으로 돌면서 홀수와 짝수의 개수를 각각 누적합니다.
# 2. 누적된 홀수 개수와 짝수 개수를 공백으로 구분하여 출력합니다.

n = int(input())
arr = list(map(int, input().split()))

odd = 0
even = 0
for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"{odd} {even}")
`,
    test_cases: [
      { input: "5\n3 6 2 1 10", output: "2 3" },
      { input: "2\n2 4", output: "0 2" },
      { input: "3\n1 3 5", output: "3 0" }
    ]
  },
  {
    id: 9,
    title: "문제 9 - 배열의 합과 평균 (빈칸 채우기)",
    type: "blank",
    description: "길이가 n인 배열 arr의 합과 평균을 출력하세요. 표준 입력으로 자연수 n과 배열 arr을 입력받아, arr배열의 총합과 평균을 출력하는 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요. (평균은 소수 첫째자리까지 출력하세요)",
    input_desc: "표준 입력으로 자연수 n과 배열 arr이 주어집니다. n은 2 이상 50 이하입니다. arr의 원소는 1 이상 100 이하인 정수입니다. (입력은 첫 줄에 n, 둘째 줄에 배열의 원소들이 공백으로 주어집니다.)",
    output_desc: "배열 arr의 총합과 평균을 차례대로 출력해주세요.",
    examples: [
      { input: "6\n12 1 9 17 31 7", output: "77\n12.8" }
    ],
    starter_code: `n = int(input(""))
arr= []
arr = input().split()

hap = 0
avg = 0

for i in range(n):
    arr[i] = int(arr[i])

for x in @@@:
    hap += @@@

avg = @@@
print(hap)
print( @@@ )
`,
    solution_code: `# [정답 및 해설]
# 1. arr배열을 반복하면서 총합(hap)에 누적합니다. (for x in arr)
# 2. hap에 x를 누적합니다. (hap += x)
# 3. 평균을 구해 avg 변수에 저장한 뒤, 소수 첫째자리까지 포맷하여 출력합니다.

n = int(input(""))
arr= []
arr = input().split()

hap = 0
avg = 0

for i in range(n):
    arr[i] = int(arr[i])

for x in arr:
    hap += x

avg = hap / n
print(hap)
print(f"{avg:.1f}")
`,
    test_cases: [
      { input: "6\n12 1 9 17 31 7", output: "77\n12.8" },
      { input: "3\n10 20 30", output: "60\n20.0" }
    ]
  },
  {
    id: 10,
    title: "문제 10 - p와 P의 개수 (빈칸 채우기)",
    type: "blank",
    description: "문자열 s에서 'p'와 'P'의 개수를 출력해주세요. 예를 들어 s가 \"happyHappy\"일 때, 'p' and 'P'의 개수 4를 출력합니다.",
    input_desc: "표준 입력으로 문자열 s가 주어집니다. 문자열 s의 길이는 1 이상 1,000 이하입니다. 문자열 s는 영문자로 이루어진 문자열입니다.",
    output_desc: "문자열 s에서 'p'와 'P'의 개수를 출력해주세요.",
    examples: [
      { input: "Happy", output: "2" },
      { input: "Programmingpython", output: "2" }
    ],
    starter_code: `s = input("")

cnt = 0
for x in @@@:
   if @@@:
        cnt += 1

print(cnt)
`,
    solution_code: `# [정답 및 해설]
# 1. 문자열 s의 문자들을 하나씩 검사합니다. (for x in s)
# 2. 문자가 소문자 'p'이거나 대문자 'P'인지 확인합니다. (if x == 'p' or x == 'P')

s = input("")

cnt = 0
for x in s:
   if x == 'p' or x == 'P':
        cnt += 1

print(cnt)
`,
    test_cases: [
      { input: "Happy", output: "2" },
      { input: "Programmingpython", output: "2" },
      { input: "applePie", output: "3" },
      { input: "abc", output: "0" }
    ]
  },
  {
    id: 11,
    title: "문제 11 - 두 수의 합 (빈칸 채우기)",
    type: "blank",
    description: "두 숫자를 더한 값을 구하려 합니다. 표준 입력으로 숫자 두 개를 입력받아, 두 수의 합을 출력하도록 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "표준 입력으로 숫자 두 개가 주어집니다. 두 수는 1 이상 100 이하인 자연수입니다.",
    output_desc: "두 수의 합을 출력해주세요.",
    examples: [
      { input: "5 3", output: "8" },
      { input: "1 4", output: "5" }
    ],
    starter_code: `num1, num2 = input("숫자 두 개를 입력하세요 ").split()
num1 = int(num1)
num2 = int(num2)
print( @@@ )
`,
    solution_code: `# [정답 및 해설]
# 1. 입력받은 두 숫자를 정수(int)로 변환해 더한 값을 print로 출력합니다.

num1, num2 = input("숫자 두 개를 입력하세요 ").split()
num1 = int(num1)
num2 = int(num2)
print( num1 + num2 )
`,
    test_cases: [
      { input: "5 3", output: "8" },
      { input: "1 4", output: "5" },
      { input: "50 50", output: "100" }
    ]
  },
  {
    id: 12,
    title: "문제 12 - 더 긴 문자열 찾기 (소스코드 작성)",
    type: "code",
    description: "두 문자열 중 더 긴 문자열을 찾고자 합니다. 표준 입력으로 문자열 두 개를 입력받아, 두 문자열 중 더 긴 문자열을 출력해주세요.",
    input_desc: "표준 입력으로 문자열 두 개가 주어집니다. 두 문자열의 길이는 1 이상 100 이하입니다. 두 문자열의 길이가 같은 경우는 없습니다.",
    output_desc: "두 문자열 중 더 긴 문자열을 출력해주세요.",
    examples: [
      { input: "HelloWorld Programmingisfun", output: "Programmingisfun" }
    ],
    starter_code: `# 두 문자열 중 더 긴 문자열을 출력하는 코드를 작성하세요.
`,
    solution_code: `# [정답 및 해설]
# 1. 입력받은 두 문자열 중 len()이 더 큰 문자열을 출력합니다.

s1, s2 = input().split()
if len(s1) > len(s2):
    print(s1)
else:
    print(s2)
`,
    test_cases: [
      { input: "HelloWorld Programmingisfun", output: "Programmingisfun" },
      { input: "abc defgh", output: "defgh" }
    ]
  },
  {
    id: 13,
    title: "문제 13 - 거꾸로 직각삼각형 (소스코드 작성)",
    type: "code",
    description: "별(\"*\")로 밑변과 높이가 N인 직각삼각형을 거꾸로 출력하려고 합니다. 표준 입력으로 자연수 N을 입력받아 밑변과 높이가 N인 직각삼각형을 거꾸로 출력해주세요.",
    input_desc: "표준 입력으로 자연수 N이 주어집니다. N은 1 이상 100 이하입니다.",
    output_desc: "별로 밑변과 높이가 N인 직각삼각형을 거꾸로 출력해주세요.",
    examples: [
      { input: "5", output: "*****\n****\n***\n**\n*" }
    ],
    starter_code: `n = int(input())
# 여기에 코드를 작성해 거꾸로 직각삼각형을 출력하세요.
`,
    solution_code: `# [정답 및 해설]
# 1. i를 N부터 1까지 거꾸로 1씩 감소시키며 반복하면서 별('*')을 i개씩 출력합니다.

n = int(input())
for i in range(n, 0, -1):
    print("*" * i)
`,
    test_cases: [
      { input: "5", output: "*****\n****\n***\n**\n*" },
      { input: "1", output: "*" },
      { input: "3", output: "***\n**\n*" }
    ]
  },
  {
    id: 14,
    title: "문제 14 - 큰따옴표 붙이기 (빈칸 채우기)",
    type: "blank",
    description: "문자열 한 개가 주어졌을 때, 주어진 문자열 양 옆에 큰따옴표를 붙이려 합니다. 표준 입력으로 문자열 한 개를 입력받아, 입력받은 문자열 양 옆에 큰따옴표를 붙여 출력하도록 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "표준 입력으로 문자열 한 개가 주어집니다. 문자열은 알파벳 대문자와 소문자로만 이루어집니다. 문자열 길이는 1 이상 100 이하입니다.",
    output_desc: "입력받은 문자열 양 옆에 큰따옴표를 붙여 출력해주세요.",
    examples: [
      { input: "HelloWorld", output: "\"HelloWorld\"" },
      { input: "Quote", output: "\"Quote\"" }
    ],
    starter_code: `str = input("문자열을 입력하세요 ")
print( @@@ )
`,
    solution_code: `# [정답 및 해설]
# 1. f-string 등을 사용하여 문자열 양 옆에 큰따옴표(")를 감싸 출력합니다.

str = input("문자열을 입력하세요 ")
print( f'"{str}"' )
`,
    test_cases: [
      { input: "HelloWorld", output: "\"HelloWorld\"" },
      { input: "Quote", output: "\"Quote\"" },
      { input: "Python", output: "\"Python\"" }
    ]
  },
  {
    id: 15,
    title: "문제 15 - 절댓값 구하기 (소스코드 작성)",
    type: "code",
    description: "숫자 한 개가 주어졌을 때 그 숫자의 절댓값을 구하려 합니다. 표준 입력으로 숫자 한 개를 입력받아, 그 수의 절댓값을 출력해주세요.",
    input_desc: "표준 입력으로 숫자 한 개가 주어집니다. 입력되는 수는 -1,000 이상 1,000 이하인 정수입니다.",
    output_desc: "입력받은 수의 절댓값을 출력해주세요.",
    examples: [
      { input: "-13", output: "13" },
      { input: "7", output: "7" }
    ],
    starter_code: `n = int(input())
# 여기에 코드를 작성하여 절댓값을 출력하세요.
`,
    solution_code: `# [정답 및 해설]
# 1. 입력받은 수가 음수이면 -1을 곱해 양수로 만들어 출력하고, 양수이면 그대로 출력합니다. (내장 함수 abs() 사용도 가능)

n = int(input())
print(abs(n))
`,
    test_cases: [
      { input: "-13", output: "13" },
      { input: "7", output: "7" },
      { input: "0", output: "0" }
    ]
  },
  {
    id: 16,
    title: "문제 16 - 합 또는 차 (소스코드 작성)",
    type: "code",
    description: "두 숫자가 같으면 두 숫자의 합을, 다르면 차를 구하려 합니다. 표준 입력으로 숫자 두 개를 입력받아 두 숫자가 같으면 두 숫자의 합을, 다르면 차를 출력해주세요.",
    input_desc: "표준 입력으로 숫자 두 개가 주어집니다. 두 숫자는 1 이상 100 이하인 자연수입니다. 두 번째 숫자는 첫 번째 숫자와 같거나 큽니다.",
    output_desc: "두 숫자가 같으면 두 숫자의 합을, 다르면 차를 출력해주세요.",
    examples: [
      { input: "5 5", output: "10" },
      { input: "7 10", output: "3" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    solution_code: `# [정답 및 해설]
# 1. 두 수가 같으면 a + b를 출력하고, 다르면 큰 수에서 작은 수를 뺀 값(b - a)을 출력합니다.

a, b = map(int, input().split())
if a == b:
    print(a + b)
else:
    print(b - a)
`,
    test_cases: [
      { input: "5 5", output: "10" },
      { input: "7 10", output: "3" },
      { input: "1 2", output: "1" }
    ]
  },
  {
    id: 17,
    title: "문제 17 - 1부터 n까지 출력 (빈칸 채우기)",
    type: "blank",
    description: "1부터 n까지의 숫자를 출력하려고 합니다. 표준 입력으로 자연수 n을 받아 1부터 n까지의 정수를 출력하는 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "표준 입력으로 자연수 n이 주어집니다. n은 1 이상 1,000 이하입니다.",
    output_desc: "1부터 n까지의 자연수를 출력해주세요.",
    examples: [
      { input: "5", output: "1\n2\n3\n4\n5" }
    ],
    starter_code: `n = int(input("수를 입력하세요 "))

i = 1
while @@@:
    print(i)
    @@@
`,
    solution_code: `# [정답 및 해설]
# 1. i가 n 이하인 동안 반복을 진행합니다. (while i <= n)
# 2. 매 반복마다 i를 1씩 누적 증가시킵니다. (i += 1)

n = int(input("수를 입력하세요 "))

i = 1
while i <= n:
    print(i)
    i += 1
`,
    test_cases: [
      { input: "5", output: "1\n2\n3\n4\n5" },
      { input: "1", output: "1" },
      { input: "3", output: "1\n2\n3" }
    ]
  },
  {
    id: 18,
    title: "문제 18 - 인접 원소 차 출력 (빈칸 채우기)",
    type: "blank",
    description: "길이가 n인 배열 arr에서 인접하는 두 숫자 중 첫 번째 숫자에서 두 번째 숫자를 뺀 값을 모두 출력하려 합니다. 표준 입력으로 자연수 n과 배열 arr을 입력받아, 인접하는 두 숫자 중 첫 번째 숫자에서 두 번째 숫자를 뺀 값을 차례대로 출력하는 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "표준 입력으로 자연수 n과 배열 arr이 주어집니다. n은 2 이상 50 이하입니다. arr의 원소는 -100 이상 100 이하인 정수입니다. (입력은 첫 줄에 n, 둘째 줄에 배열의 원소들이 공백으로 주어집니다.)",
    output_desc: "배열 arr에서 인접하는 두 숫자 중 첫 번째 숫자에서 두 번째 숫자를 뺀 값을 차례대로 출력해주세요.",
    examples: [
      { input: "4\n1 3 6 2", output: "-2\n-3\n4" }
    ],
    starter_code: `n = int(input(""))
arr= []
arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])

for i in range( @@@ ):
    print( @@@ )
`,
    solution_code: `# [정답 및 해설]
# 1. 마지막 원소 바로 전까지(n - 1) 인덱스를 순회합니다. (range(n - 1))
# 2. 인접한 두 원소의 차이인 arr[i] - arr[i+1]을 계산하여 출력합니다.

n = int(input(""))
arr= []
arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])

for i in range( n - 1 ):
    print( arr[i] - arr[i+1] )
`,
    test_cases: [
      { input: "4\n1 3 6 2", output: "-2\n-3\n4" },
      { input: "2\n10 5", output: "5" }
    ]
  },
  {
    id: 19,
    title: "문제 19 - 숫자를 거꾸로 출력 (빈칸 채우기)",
    type: "blank",
    description: "숫자 한 개를 입력받았을 때 숫자를 거꾸로 출력하려고 합니다. 예를 들어, 12345가 입력되면 54321을 출력합니다. 표준 입력으로 자연수 n을 입력받아 숫자 n을 거꾸로 출력하도록 코드를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "표준 입력으로 자연수 n이 주어집니다. n은 1 이상 100,000,000 이하입니다. n은 0으로 끝나지 않습니다.",
    output_desc: "숫자 n을 거꾸로 출력해주세요.",
    examples: [
      { input: "12345", output: "54321" }
    ],
    starter_code: `n = input("")

for i in range( len(n) ):
    print( @@@ )
`,
    solution_code: `# [정답 및 해설]
# 1. 뒤에서부터 역방향 인덱싱을 하기 위해 n[len(n) - 1 - i]를 참조하여 end=""과 함께 출력합니다.

n = input("")

for i in range( len(n) ):
    print( n[len(n) - 1 - i], end="" )
`,
    test_cases: [
      { input: "12345", output: "54321" }
    ]
  },
  {
    id: 20,
    title: "문제 20 - 1의 개수 구하기 (소스코드 작성)",
    type: "code",
    description: "문자열 s에서 '1'의 개수를 구하려 합니다. 예를 들어 s가 \"4156721\"일 때, 2번째와 마지막 번째 문자가 '1'이므로 2를 출력합니다. 표준 입력으로 문자열 s를 입력받아 s에서 '1'의 개수를 출력해주세요.",
    input_desc: "표준 입력으로 문자열 s가 주어집니다. 문자열 s의 길이는 1 이상 1,000 이하입니다. 문자열 s는 '1'~'9'로 이루어진 문자열입니다.",
    output_desc: "문자열 s에서 '1'의 개수를 출력해주세요.",
    examples: [
      { input: "4156721", output: "2" },
      { input: "48273", output: "0" }
    ],
    starter_code: `# 문자열 s에서 '1'의 개수를 출력하는 코드를 작성하세요.
`,
    solution_code: `# [정답 및 해설]
# 1. 문자열 s에서 문자 '1'을 찾아 카운트합니다.

s = input()
print(s.count('1'))
`,
    test_cases: [
      { input: "4156721", output: "2" },
      { input: "48273", output: "0" },
      { input: "1111", output: "4" }
    ]
  },
  {
    id: 21,
    title: "문제 21 - 약수의 개수 (소스코드 작성)",
    type: "code",
    description: "자연수 n을 입력 받아 약수의 개수를 출력하는 프로그램을 작성하세요.",
    input_desc: "첫 줄에 정수 N이 주어집니다.",
    output_desc: "n의 약수의 개수를 출력하세요.",
    examples: [
      { input: "12", output: "6" }
    ],
    starter_code: `# 자연수 n을 입력 받아 약수의 개수를 출력하는 코드를 작성하세요.
`,
    test_cases: [
      { input: "12", output: "6" },
      { input: "1", output: "1" },
      { input: "7", output: "2" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 자연수 n을 입력받습니다.
# 2. 1부터 n까지 순회하며 n을 나누어 떨어지게 하는 수(약수)의 개수를 누적합니다.

n = int(input())
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
print(cnt)
`
  },
  {
    id: 22,
    title: "문제 22 - 숫자 쌍 출력 (빈칸 채우기)",
    type: "blank",
    description: "\`while\`문을 이용하여 출력의 예처럼 숫자를 두 개씩 쌍으로 출력하세요.",
    input_desc: "표준 입력으로 정수 n이 주어집니다. (n은 항상 짝수입니다.)",
    output_desc: "1부터 n까지의 숫자를 한 줄에 두 개씩 공백으로 구분하여 출력하세요.",
    examples: [
      { input: "12", output: "1 2\n3 4\n5 6\n7 8\n9 10\n11 12" }
    ],
    starter_code: `i = 1

n = input("")
n = int(n)

while @@@:
    print(i, i+1)
    @@@
`,
    test_cases: [
      { input: "12", output: "1 2\n3 4\n5 6\n7 8\n9 10\n11 12" },
      { input: "4", output: "1 2\n3 4" }
    ],
    solution_code: `# [정답 및 해설]
# 1. i가 n보다 작을 때까지 반복을 진행합니다. (while i < n)
# 2. i와 i+1을 쌍으로 출력하므로, 한 번 반복할 때마다 i를 2씩 증가시킵니다. (i += 2)

i = 1

n = input("")
n = int(n)

while i < n:
    print(i, i+1)
    i += 2
`
  },
  {
    id: 23,
    title: "문제 23 - 과목 통과 판별 (빈칸 채우기)",
    type: "blank",
    description: "세 과목 점수를 입력 받아 세 과목 모두 60점 이상이면 \"YES\", 아니면 \"NO\"를 출력하는 프로그램을 작성하세요.",
    input_desc: "표준 입력으로 정수 3개가 줄바꿈으로 구분되어 주어집니다. 각 점수는 1 이상 100 이하입니다.",
    output_desc: "세 과목 모두 60점 이상이면 \"YES\", 아니면 \"NO\"를 출력하시오.",
    examples: [
      { input: "75\n95\n85", output: "YES" },
      { input: "75\n95\n55", output: "NO" }
    ],
    starter_code: `a = input("")
b = input("")
c = input("")

a = int(a)
b = int(b)
c = int(c)

if @@@:
    print("YES")
else:
    print("NO")
`,
    test_cases: [
      { input: "75\n95\n85", output: "YES" },
      { input: "75\n95\n55", output: "NO" },
      { input: "60\n60\n60", output: "YES" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 세 점수 a, b, c가 모두 60 이상인지 확인하는 조건식을 빈칸에 작성합니다. (a >= 60 and b >= 60 and c >= 60)

a = input("")
b = input("")
c = input("")

a = int(a)
b = int(b)
c = int(c)

if a >= 60 and b >= 60 and c >= 60:
    print("YES")
else:
    print("NO")
`
  },
  {
    id: 24,
    title: "문제 24 - 배수 출력 (빈칸 채우기)",
    type: "blank",
    description: "1 ~ 100 사이의 숫자 중 3의 배수이거나 7의 배수인 수를 공백으로 구분하여 가로로 출력하는 프로그램을 완성하세요.",
    input_desc: "입력 데이터는 없습니다.",
    output_desc: "3의 배수이거나 7의 배수인 숫자를 한 줄에 출력하세요.",
    examples: [
      { input: "", output: "3 6 7 9 12 14 15 18 21 24 27 28 30 33 35 36 39 42 45 48 49 51 54 56 57 60 63 66 69 70 72 75 77 78 81 84 87 90 91 93 96 98 99" }
    ],
    starter_code: `a = 1

while a < 100:
    if @@@:
        print(a, end=' ')
    a += 1
`,
    test_cases: [
      { input: "", output: "3 6 7 9 12 14 15 18 21 24 27 28 30 33 35 36 39 42 45 48 49 51 54 56 57 60 63 66 69 70 72 75 77 78 81 84 87 90 91 93 96 98 99" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 3의 배수이거나 7의 배수인 조건을 작성합니다. (a % 3 == 0 or a % 7 == 0)

a = 1

while a < 100:
    if a % 3 == 0 or a % 7 == 0:
        print(a, end=' ')
    a += 1
`
  },
  {
    id: 25,
    title: "문제 25 - 합 출력 형식 (소스코드 작성)",
    type: "code",
    description: "1부터 입력받은 수까지의 합을 구하여 형식에 맞춰 출력하는 프로그램을 작성하세요.",
    input_desc: "표준 입력으로 숫자 한 개가 주어집니다. 입력되는 수는 1 이상 1,000 이하인 정수입니다.",
    output_desc: "\`1 ----- [입력값] = [총합]\` 형태로 출력하세요.",
    examples: [
      { input: "5", output: "1 ----- 5 = 15" },
      { input: "10", output: "1 ----- 10 = 55" }
    ],
    starter_code: `n = int(input())
# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "5", output: "1 ----- 5 = 15" },
      { input: "10", output: "1 ----- 10 = 55" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 1부터 n까지의 합을 구합니다.
# 2. 지정된 형식 '1 ----- [입력값] = [총합]'으로 포맷팅하여 출력합니다.

n = int(input())
hap = sum(range(1, n + 1))
print(f"1 ----- {n} = {hap}")
`
  },
  {
    id: 26,
    title: "문제 26 - 문자열 N번 반복 (소스코드 작성)",
    type: "code",
    description: "문자열과 정수 n을 입력받아 입력받은 문자열을 n번 연속해서 출력하세요.",
    input_desc: "표준 입력으로 첫 번째 줄에 문자열, 두 번째 줄에 정수 n이 주어집니다.",
    output_desc: "문자열을 n번 이어 붙여 출력하세요.",
    examples: [
      { input: "Hello\n3", output: "HelloHelloHello" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "Hello\n3", output: "HelloHelloHello" },
      { input: "ABC\n1", output: "ABC" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 첫 번째 줄에서 문자열을 입력받고, 두 번째 줄에서 반복 횟수 n을 정수로 입력받습니다.
# 2. 파이썬에서는 문자열 곱하기 정수를 통해 문자열을 반복해서 이어 붙일 수 있습니다. (s * n)

s = input()
n = int(input())
print(s * n)
`
  },
  {
    id: 27,
    title: "문제 27 - 특정 문자 제거하기 (소스코드 작성)",
    type: "code",
    description: "문자열과 문자 1개를 입력받아 문자열에서 입력받은 문자를 모두 제거하고 출력하세요.",
    input_desc: "표준 입력으로 첫 번째 줄에 대상 문자열, 두 번째 줄에 제거할 문자 1개가 주어집니다.",
    output_desc: "지정된 문자가 제거된 문자열을 출력하세요.",
    examples: [
      { input: "ABCdefabcABC\nA", output: "BCdefabcBC" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "ABCdefabcABC\nA", output: "BCdefabcBC" },
      { input: "apple\np", output: "ale" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 대상 문자열 s와 제거할 문자 char을 각각 입력받습니다.
# 2. replace 내장 함수를 사용해 특정 문자를 빈 문자열("")로 치환하여 제거합니다.

s = input()
char = input()
print(s.replace(char, ""))
`
  },
  {
    id: 28,
    title: "문제 28 - 숫자 빈도수 구하기 (소스코드 작성)",
    type: "code",
    description: "정수 n과 배열 arr을 입력받아 배열 내에 존재하는 0의 개수, 1의 개수 ... 9의 개수를 각각 줄바꿈하여 순서대로 출력하는 프로그램을 작성하세요.",
    input_desc: "표준 입력으로 첫 번째 줄에 자연수 n이 주어지고, 두 번째 줄에 공백으로 구분된 n개의 원소를 가진 배열 arr이 주어집니다. n은 2 이상 50 이하이며, arr의 원소는 0부터 9까지의 정수로 구성됩니다.",
    output_desc: "0부터 9까지 각 숫자의 빈도수를 한 줄에 하나씩 총 10줄로 출력하세요.",
    examples: [
      { input: "11\n0 5 7 2 2 1 9 2 1 6 5", output: "1\n2\n3\n0\n0\n2\n1\n1\n0\n1" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "11\n0 5 7 2 2 1 9 2 1 6 5", output: "1\n2\n3\n0\n0\n2\n1\n1\n0\n1" }
    ],
    solution_code: `# [정답 및 해설]
# 1. n과 배열 arr을 정수형 리스트로 입력받습니다.
# 2. 0부터 9까지 순회하면서 list.count() 함수를 이용해 개수를 구하고 출력합니다.

n = int(input())
arr = list(map(int, input().split()))

for i in range(10):
    print(arr.count(i))
`
  },
  {
    id: 29,
    title: "문제 29 - 5의 배수 통계 (소스코드 작성)",
    type: "code",
    description: "10개의 정수를 입력받아 그중 5의 배수만 첫째 줄에 공백으로 구분하여 출력하고, 둘째 줄에는 5의 배수의 개수, 총합, 평균을 공백으로 구분하여 출력하세요. (평균은 소수 셋째자리에서 반올림하여 둘째자리까지 출력합니다.)",
    input_desc: "표준 입력으로 공백으로 구분된 10개의 정수가 주어집니다.",
    output_desc: "첫째 줄에 5의 배수들만 출력하고, 둘째 줄에 5의 배수의 개수, 합계, 평균을 순서대로 출력하세요.",
    examples: [
      { input: "12 5 10 57 30 6 11 90 47 2", output: "5 10 30 90\n4 135 33.75" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "12 5 10 57 30 6 11 90 47 2", output: "5 10 30 90\n4 135 33.75" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 10개의 정수를 입력받아 정수 리스트로 만듭니다.
# 2. 리스트에서 5의 배수만 필터링합니다.
# 3. 5의 배수들을 출력하고, 개수, 총합, 평균을 계산하여 포맷팅해 출력합니다.

arr = list(map(int, input().split()))
multiples_5 = [x for x in arr if x % 5 == 0]

# 첫 번째 줄 출력
print(*(multiples_5))

# 두 번째 줄 출력
cnt = len(multiples_5)
hap = sum(multiples_5)
avg = hap / cnt
print(f"{cnt} {hap} {avg:.2f}")
`
  },
  {
    id: 30,
    title: "문제 30 - 나머지 연산 (소스코드 작성)",
    type: "code",
    description: "두 정수 n과 m이 주어질 때, n을 m으로 나눈 나머지 값을 구하는 프로그램을 작성하세요.",
    input_desc: "표준 입력으로 정수 n과 m이 공백으로 구분되어 주어집니다.",
    output_desc: "n을 m으로 나눈 나머지 값을 출력하세요.",
    examples: [
      { input: "3 2", output: "1" },
      { input: "10 5", output: "0" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "3 2", output: "1" },
      { input: "10 5", output: "0" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 공백으로 구분된 두 수 n과 m을 정수로 입력받습니다.
# 2. 나머지 연산자 %를 활용해 n % m 값을 구해 출력합니다.

n, m = map(int, input().split())
print(n % m)
`
  },
  {
    id: 31,
    title: "문제 31 - 성적 테이블 출력 (소스코드 작성)",
    type: "code",
    description: "지정된 형식에 맞추어 성적 테이블을 출력하는 프로그램을 작성하세요. 각 항목(name, kor, mat, tot, avg)과 데이터들은 **10칸씩 공간을 확보하여 오른쪽 정렬**하여 출력해야 합니다.",
    input_desc: "입력 데이터는 없습니다.",
    output_desc: "각 열마다 10자리의 너비를 확보하고 우측 정렬하여 성적 데이터를 출력하세요.",
    examples: [
      { input: "", output: "      name       kor       mat       tot       avg\n       aaa        55        95       150        75\n       bbb       100        90       190        95\n       ggg        88       100       188        94" }
    ],
    starter_code: `# 성적 테이블을 10칸씩 우측 정렬하여 출력하세요.
`,
    test_cases: [
      { input: "", output: "      name       kor       mat       tot       avg\n       aaa        55        95       150        75\n       bbb       100        90       190        95\n       ggg        88       100       188        94" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 포맷 스트링의 우측 정렬 너비 10(>10)을 활용하여 성적 테이블을 출력합니다.
# 2. 각 항목명과 데이터를 동일한 방식으로 포맷하여 한 줄씩 출력합니다.

print(f"{'name':>10}{'kor':>10}{'mat':>10}{'tot':>10}{'avg':>10}")
print(f"{'aaa':>10}{55:>10}{95:>10}{150:>10}{75:>10}")
print(f"{'bbb':>10}{100:>10}{90:>10}{190:>10}{95:>10}")
print(f"{'ggg':>10}{88:>10}{100:>10}{188:>10}{94:>10}")
`
  },
  {
    id: 32,
    title: "문제 32 - 문자 집계 (소스코드 작성)",
    type: "code",
    description: "영문자, 숫자, 특수문자로 구성된 문자열을 입력받아 대문자, 소문자, 숫자의 개수를 각각 세어 출력하는 프로그램을 작성하세요. (공백은 포함되지 않습니다.)",
    input_desc: "표준 입력으로 공백이 없는 문자열 한 개가 주어집니다.",
    output_desc: "문자열에 포함된 대문자의 개수, 소문자의 개수, 숫자의 개수를 공백으로 구분하여 차례대로 한 줄에 출력하세요.",
    examples: [
      { input: "Coding-C++/Python", output: "3 10 0" },
      { input: "C++456Programming!!!", output: "2 10 3" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "Coding-C++/Python", output: "3 10 0" },
      { input: "C++456Programming!!!", output: "2 10 3" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 문자열을 입력받습니다.
# 2. 각 문자를 순회하며 대문자(isupper), 소문자(islower), 숫자(isdigit)의 개수를 셉니다.

s = input()
upper_cnt = sum(1 for c in s if c.isupper())
lower_cnt = sum(1 for c in s if c.islower())
digit_cnt = sum(1 for c in s if c.isdigit())
print(f"{upper_cnt} {lower_cnt} {digit_cnt}")
`
  },
  {
    id: 33,
    title: "문제 33 - 우측 정렬 직각삼각형 (소스코드 작성)",
    type: "code",
    description: "별(\"*\")을 사용하여 밑변과 높이가 N인 직각삼각형을 우측 정렬 형태로 출력하려고 합니다. 표준 입력으로 자연수 N을 입력받아 형태에 맞는 삼각형을 출력하세요.",
    input_desc: "표준 입력으로 자연수 N이 주어집니다. (1 <= N <= 100)",
    output_desc: "우측 정렬된 형태의 밑변과 높이가 N인 별 삼각형을 출력하세요.",
    examples: [
      { input: "5", output: "    *\n   **\n  ***\n ****\n*****" }
    ],
    starter_code: `n = int(input())
# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "5", output: "    *\n   **\n  ***\n ****\n*****" },
      { input: "2", output: " *\n**" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 입력받은 자연수 N에 대해 반복을 순회합니다.
# 2. i번째 줄에는 공백 N-i개와 별 i개를 출력하여 우측 정렬 효과를 냅니다.

n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
`
  },
  {
    id: 34,
    title: "문제 34 - 성적 총합과 평균 (빈칸 채우기)",
    type: "blank",
    description: "국어, 영어, 수학, 컴퓨터 점수를 공백으로 구분하여 한 줄로 입력받은 뒤, 총점(sum)과 평균(avg)을 구하는 프로그램을 작성하세요. (평균은 소수점 첫째자리까지 출력합니다.)",
    input_desc: "표준 입력으로 정수 4개가 공백으로 구분되어 주어집니다.",
    output_desc: "총점과 평균을 형식에 맞춰 출력하세요.",
    examples: [
      { input: "70 85 61 99", output: "sum = 315\navg = 78.8" }
    ],
    starter_code: `a, b, c, d = @@@

print( @@@ )
print( @@@ )
`,
    test_cases: [
      { input: "70 85 61 99", output: "sum = 315\navg = 78.8" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 입력되는 4개의 정수를 map(int, input().split())으로 분할하여 저장합니다.
# 2. sum과 avg를 계산해 지정된 형식에 맞추어 출력합니다.

a, b, c, d = map(int, input().split())

print(f"sum = {a + b + c + d}")
print(f"avg = {(a + b + c + d) / 4:.1f}")
`
  },
  {
    id: 35,
    title: "문제 35 - 짝홀 조건 연산 (빈칸 채우기)",
    type: "blank",
    description: "2개의 정수를 입력받아서 두 수가 모두 짝수이면 두 수의 합을 출력하고, 그렇지 않으면 큰 짝수에서 홀수를 뺀 값을 출력하세요. (즉, 한 수가 짝수이고 다른 수가 홀수일 때, 짝수에서 홀수를 뺀 결과를 출력합니다.)",
    input_desc: "표준 입력으로 1 이상 1,000 이하인 정수 두 개가 공백으로 구분되어 주어집니다.",
    output_desc: "문제 조건에 따른 연산 결과를 출력하세요.",
    examples: [
      { input: "10 6", output: "16" },
      { input: "8 7", output: "1" },
      { input: "11 20", output: "9" }
    ],
    starter_code: `a, b = map(int, input("").split())

if @@@ :
    print(a+b)
else:
    if @@@ :
        print(a-b)
    else:
        print(b-a)
`,
    test_cases: [
      { input: "10 6", output: "16" },
      { input: "8 7", output: "1" },
      { input: "11 20", output: "9" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 두 수가 모두 짝수인 조건식: a % 2 == 0 and b % 2 == 0
# 2. 첫 번째 수만 짝수이고 두 번째 수는 홀수인 조건식 (a가 짝수이고 b가 홀수): a % 2 == 0

a, b = map(int, input("").split())

if a % 2 == 0 and b % 2 == 0 :
    print(a+b)
else:
    if a % 2 == 0 :
        print(a-b)
    else:
        print(b-a)
`
  },
  {
    id: 36,
    title: "문제 36 - 배수 가로 출력 (빈칸 채우기)",
    type: "blank",
    description: "\`while\`문을 이용하여 1부터 입력받은 자연수 n 사이에서 3의 배수이거나 7의 배수인 수를 모두 찾아 공백으로 구분하여 가로로 출력하는 프로그램을 완성하세요.",
    input_desc: "표준 입력으로 자연수 n이 주어집니다.",
    output_desc: "1 이상 n 이하의 수 중 3 또는 7의 배수를 공백으로 구분하여 한 줄에 출력하세요.",
    examples: [
      { input: "30", output: "3 6 7 9 12 14 15 18 21 24 27 28 30" }
    ],
    starter_code: `n = int(input(""))

a = 1;

while @@@ :
    if @@@ :
        print(a, end=' ')
    a += 1
`,
    test_cases: [
      { input: "30", output: "3 6 7 9 12 14 15 18 21 24 27 28 30" }
    ],
    solution_code: `# [정답 및 해설]
# 1. a가 n 이하일 때까지 반복합니다: a <= n
# 2. 3의 배수이거나 7의 배수인 조건식: a % 3 == 0 or a % 7 == 0

n = int(input(""))

a = 1;

while a <= n :
    if a % 3 == 0 or a % 7 == 0 :
        print(a, end=' ')
    a += 1
`
  },
  {
    id: 37,
    title: "문제 37 - 구구단 정렬 출력 (빈칸 채우기)",
    type: "blank",
    description: "입력받은 자연수 n에 해당하는 구구단 단수를 출력 서식에 맞춰 출력하는 프로그램을 완성하세요. 결과값의 정렬 방식을 출력 예시를 보고 구현하세요.",
    input_desc: "표준 입력으로 1 이상 9 이하의 자연수 n이 주어집니다.",
    output_desc: "n단의 곱셈 결과를 형식에 맞춰 출력하세요. 결과값(곱한 값)은 3칸의 자리를 오른쪽 정렬 확보해야 합니다.",
    examples: [
      { input: "3", output: "3 x 1 =   3\n3 x 2 =   6\n3 x 3 =   9\n3 x 4 =  12\n3 x 5 =  15\n3 x 6 =  18\n3 x 7 =  21\n3 x 8 =  24\n3 x 9 =  27" }
    ],
    starter_code: `n = int(input(""))

a = 1;

while a<=9:
    print( @@@ )
    a += 1
`,
    test_cases: [
      { input: "3", output: "3 x 1 =   3\n3 x 2 =   6\n3 x 3 =   9\n3 x 4 =  12\n3 x 5 =  15\n3 x 6 =  18\n3 x 7 =  21\n3 x 8 =  24\n3 x 9 =  27" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 출력 결과값은 총 3자리의 우측 정렬을 이용합니다.
# 2. print(f"{n} x {a} = {n * a:>3}") 방식을 이용해 포맷팅합니다.

n = int(input(""))

a = 1;

while a<=9:
    print( f"{n} x {a} = {n*a:>3}" )
    a += 1
`
  },
  {
    id: 38,
    title: "문제 38 - 숫자 격자 사각형 (빈칸 채우기)",
    type: "blank",
    description: "자연수 n과 m을 입력받아 n행 m열 크기의 정수 격자 사각형을 출력하는 프로그램을 완성하세요. 격자의 값은 각 행마다 \`행 번호\`부터 시작하여 1씩 증가하는 숫자로 채워집니다.",
    input_desc: "표준 입력으로 자연수 n과 m이 공백으로 구분되어 주어집니다. (2 <= n, m <= 50)",
    output_desc: "행과 열의 규칙에 맞는 n x m 크기의 숫자 사각형을 출력하세요. 각 원소는 공백으로 구분합니다.",
    examples: [
      { input: "4 6", output: "1 2 3 4 5 6\n2 3 4 5 6 7\n3 4 5 6 7 8\n4 5 6 7 8 9" }
    ],
    starter_code: `n, m = map(int, input("").split())

for i in range( @@@ ):
    for j in range( @@@ ):
        print( @@@ , end=' ')
    print()
`,
    test_cases: [
      { input: "4 6", output: "1 2 3 4 5 6\n2 3 4 5 6 7\n3 4 5 6 7 8\n4 5 6 7 8 9" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 행 개수만큼 반복합니다: range(n)
# 2. 열 개수만큼 반복합니다: range(m)
# 3. 값은 각 행마다 행 번호 i+1부터 1씩 증가하므로 \`i + 1 + j\`를 출력합니다.

n, m = map(int, input("").split())

for i in range( n ):
    for j in range( m ):
        print( i + 1 + j , end=' ')
    print()
`
  },
  {
    id: 39,
    title: "문제 39 - 역순 및 구간 필터링 (소스코드 작성)",
    type: "code",
    description: "표준 입력으로 10개의 정수를 입력받아 배열(리스트)에 저장합니다. 첫 번째 줄에는 입력받은 10개의 정수를 입력된 순서의 **역순**으로 출력하고, 두 번째 줄에는 입력받은 수 중 **30 이상 50 이하**에 속하는 수만 필터링하여 순서대로 출력하세요.",
    input_desc: "표준 입력으로 줄바꿈으로 구분된 10개의 정수가 차례대로 주어집니다.",
    output_desc: "첫 번째 줄에는 역순으로, 두 번째 줄에는 30 이상 50 이하인 정수를 공백으로 구분해 출력하세요.",
    examples: [
      { input: "12\n25\n31\n10\n58\n100\n95\n46\n78\n60", output: "60 78 46 95 100 58 10 31 25 12\n31 46" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "12\n25\n31\n10\n58\n100\n95\n46\n78\n60", output: "60 78 46 95 100 58 10 31 25 12\n31 46" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 10개의 정수를 줄바꿈으로 입력받아 리스트에 담습니다.
# 2. 역순 출력을 위해 arr[::-1]을 사용합니다.
# 3. 30 이상 50 이하인 정수들을 필터링하여 출력합니다.

arr = [int(input()) for _ in range(10)]
print(*(arr[::-1]))
filtered = [x for x in arr if 30 <= x <= 50]
print(*filtered)
`
  },
  {
    id: 40,
    title: "문제 40 - 최댓값과 최솟값 (소스코드 작성)",
    type: "code",
    description: "표준 입력으로 10개의 정수를 입력받아 배열에 저장한 뒤, 10개의 수 중 **최댓값**과 **최솟값**을 찾아 공백으로 구분하여 한 줄에 출력하는 프로그램을 작성하세요.",
    input_desc: "표준 입력으로 공백으로 구분된 10개의 자연수가 차례대로 주어집니다.",
    output_desc: "입력받은 정수 데이터 중 최댓값과 최솟값을 순서대로 출력하세요.",
    examples: [
      { input: "12 25 31 10 58 100 95 46 78 60", output: "100 10" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "12 25 31 10 58 100 95 46 78 60", output: "100 10" }
    ],
    solution_code: `# [정답 및 해설]
# 1. 공백으로 분할된 10개의 정수를 입력받아 리스트로 만듭니다.
# 2. max()와 min() 내장 함수를 활용해 최댓값과 최솟값을 구해 출력합니다.

arr = list(map(int, input().split()))
print(f"{max(arr)} {min(arr)}")
`
  },
  {
    id: 41,
    classLevel: 2,
    title: "[문제 1] 티셔츠 주문 수량 구하기 (소스코드 작성)",
    type: "code",
    description: "A 학교에서는 단체 티셔츠를 주문하기 위해 학생별로 원하는 티셔츠 사이즈를 조사했습니다. 선택할 수 있는 티셔츠 사이즈는 작은 순서대로 \"XS\", \"S\", \"M\", \"L\", \"XL\", \"XXL\" 총 6종류가 있습니다. 학생별로 원하는 티셔츠 사이즈를 조사한 결과가 들어있는 배열 shirt_size가 매개변수로 주어질 때, 사이즈별로 티셔츠가 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.",
    input_desc: "입력값으로 shirt_size를 모사한 문자열이 주어집니다. (예: 공백으로 구분된 티셔츠 사이즈 목록)",
    output_desc: "[\"XS\" 개수, \"S\" 개수, \"M\" 개수, \"L\" 개수, \"XL\" 개수, \"XXL\" 개수] 순서의 리스트를 반환하거나 출력합니다.",
    examples: [
      { input: "XS S L L XL S", output: "[1, 2, 0, 2, 1, 0]" }
    ],
    starter_code: `def solution(shirt_size):
    # 여기에 코드를 작성하세요.
    answer = []
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
shirt_size = input().split()
print(solution(shirt_size))
`,
    solution_code: `# [정답 및 해설]
# 1. XS부터 XXL까지의 티셔츠 사이즈 순서를 리스트로 정의합니다.
# 2. 각 사이즈에 대응하는 카운트값을 세어 결과 리스트에 순서대로 담아 반환합니다.

def solution(shirt_size):
    sizes = ["XS", "S", "M", "L", "XL", "XXL"]
    answer = [0] * 6
    for size in shirt_size:
        if size in sizes:
            idx = sizes.index(size)
            answer[idx] += 1
    return answer

shirt_size = input().split()
print(solution(shirt_size))
`,
    test_cases: [
      { input: "XS S L L XL S", output: "[1, 2, 0, 2, 1, 0]" },
      { input: "XXL XL L M S XS", output: "[1, 1, 1, 1, 1, 1]" },
      { input: "M M M XS", output: "[1, 0, 3, 0, 0, 0]" }
    ]
  },
  {
    id: 42,
    classLevel: 2,
    title: "[문제 2] 회원 등급별 할인율 적용 (소스코드 작성)",
    type: "code",
    description: "A 쇼핑몰에서는 회원 등급에 따라 할인 서비스를 제공합니다. 회원 등급에 따른 할인율은 다음과 같습니다. (\"S\" = 실버, \"G\" = 골드, \"V\" = VIP)\n- \"S\": 5%\n- \"G\": 10%\n- \"V\": 15%\n상품의 가격 price와 구매자의 회원 등급을 나타내는 문자열 grade가 매개변수로 주어질 때, 할인 서비스를 적용한 가격을 return 하도록 solution 함수를 완성해주세요. (단, 할인된 가격은 정수형태로 반환합니다.)",
    input_desc: "입력값으로 상품의 가격 price와 회원 등급 grade가 공백으로 구분되어 주어집니다.",
    output_desc: "할인이 적용된 가격을 정수로 반환하거나 출력합니다.",
    examples: [
      { input: "2500 V", output: "2125" },
      { input: "96900 S", output: "92055" }
    ],
    starter_code: `def solution(price, grade):
    # 여기에 코드를 작성하세요.
    answer = 0
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
inputs = input().split()
price = int(inputs[0])
grade = inputs[1]
print(solution(price, grade))
`,
    solution_code: `# [정답 및 해설]
# 1. 회원 등급("S", "G", "V")에 따른 할인율을 조건문이나 딕셔너리로 관리합니다.
# 2. 할인된 금액을 차감한 뒤, int()를 사용해 소수점을 버리고 정수로 반환합니다.

def solution(price, grade):
    discount = 0
    if grade == "S":
        discount = 0.05
    elif grade == "G":
        discount = 0.10
    elif grade == "V":
        discount = 0.15
    return int(price * (1 - discount))

inputs = input().split()
price = int(inputs[0])
grade = inputs[1]
print(solution(price, grade))
`,
    test_cases: [
      { input: "2500 V", output: "2125" },
      { input: "96900 S", output: "92055" },
      { input: "10000 G", output: "9000" }
    ]
  },
  {
    id: 43,
    classLevel: 2,
    title: "[문제 3] 날짜 간격 구하기 (빈칸 채우기)",
    type: "blank",
    description: "시작 날짜와 끝 날짜가 주어질 때, 두 날짜가 며칠만큼 떨어져 있는지(D-day)를 구하려 합니다. 이를 위해 다음과 같이 3단계로 프로그램 구조를 작성했습니다. (단, 윤년은 고려하지 않습니다.)\n1. 시작 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.\n2. 끝 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.\n3. (2단계에서 구한 날짜) - (1단계에서 구한 날짜)를 구합니다.\n시작 날짜의 월, 일을 나타내는 start_month, start_day, 끝 날짜의 월, 일을 나타내는 end_month, end_day가 매개변수로 주어질 때, 시작 날짜와 끝 날짜가 며칠만큼 떨어져 있는지 return 하도록 solution 함수를 완성해 주세요. 중복되는 계산 부분은 func_a라는 함수로 작성되어 있습니다.",
    input_desc: "공백으로 구분된 시작월, 시작일, 종료월, 종료일이 주어집니다.",
    output_desc: "두 날짜 간의 일수(차이)를 반환하거나 출력합니다.",
    examples: [
      { input: "1 2 2 2", output: "31" }
    ],
    starter_code: `def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0;
    for i in @@@:
        total += @@@
    total += @@@
    return total - 1

def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1], inputs[2], inputs[3]))
`,
    solution_code: `# [정답 및 해설]
# 1. 1월 1일부터 특정 날짜까지의 총 일수를 계산하기 위해 이전 월(month - 1)까지의 일수를 누적합니다.
# 2. range(month - 1) 또는 range(0, month - 1)을 순회하며 month_list[i]를 더해줍니다.
# 3. 마지막으로 현재 달의 일수(day)를 누적 더해줍니다.

def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(month - 1):
        total += month_list[i]
    total += day
    return total - 1

def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1], inputs[2], inputs[3]))
`,
    test_cases: [
      { input: "1 2 2 2", output: "31" },
      { input: "2 10 3 12", output: "30" },
      { input: "1 1 12 31", output: "364" }
    ]
  },
  {
    id: 44,
    classLevel: 2,
    title: "[문제 4] 최빈값과 최저빈도 비율 (빈칸 채우기)",
    type: "blank",
    description: "자연수가 들어있는 배열이 있습니다. 이 배열에서 가장 많이 등장하는 숫자의 개수는 가장 적게 등장하는 숫자 개수의 몇 배인지 구하려 합니다. 이를 위해 다음과 같이 프로그램 구조를 작성했습니다.\n1. 배열에 들어있는 각 자연수의 개수를 셉니다. (func_a)\n2. 가장 많이 등장하는 수의 개수를 구합니다. (func_b)\n3. 가장 적게 등장하는 수의 개수를 구합니다. (func_c)\n4. 가장 많이 등장하는 수가 가장 적게 등장하는 수보다 몇 배 더 많은지 구합니다.\n단, 몇 배 더 많은지 구할 때는 소수 부분은 버리고 정수 부분만 구하면 됩니다. 자연수가 들어있는 배열 arr가 매개변수로 주어질 때, 알맞은 함수와 매개변수를 빈칸에 채워 solution 함수를 완성해주세요.",
    input_desc: "공백으로 구분된 자연수 리스트가 주어집니다.",
    output_desc: "최다 빈도를 최소 빈도로 나눈 몫(정수)을 반환하거나 출력합니다.",
    examples: [
      { input: "1 2 3 3 1 3 3 2 3 2", output: "2" }
    ],
    starter_code: `def func_a(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_@@@(@@@)
    max_cnt = func_@@@(@@@)
    min_cnt = func_@@@(@@@)
    return max_cnt // min_cnt

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
arr = list(map(int, input().split()))
print(solution(arr))
`,
    solution_code: `# [정답 및 해설]
# 1. 각 수의 등장 횟수를 기록한 빈도 카운터 배열을 얻기 위해 func_a(arr)를 호출합니다.
# 2. 카운터 배열에서 최다 빈도를 구하기 위해 func_b(counter)를 호출합니다.
# 3. 카운터 배열에서 최소 빈도를 구하기 위해 func_c(counter)를 호출합니다.

def func_a(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = list(map(int, input().split()))
print(solution(arr))
`,
    test_cases: [
      { input: "1 2 3 3 1 3 3 2 3 2", output: "2" },
      { input: "5 5 5 5 5", output: "1" },
      { input: "1 1 2 2 3 3 3 3", output: "2" }
    ]
  },
  {
    id: 45,
    classLevel: 2,
    title: "[문제 5] 배열 순서 뒤집기 (빈칸 채우기)",
    type: "blank",
    description: "주어진 배열의 순서를 뒤집으려고 합니다. 예를 들어 주어진 배열이 [1, 4, 2, 3]이면, 순서를 뒤집은 배열은 [3, 2, 4, 1]입니다. 정수가 들어있는 배열 arr가 매개변수로 주어졌을 때, 투 포인터(Two Pointer) 형태로 arr를 스왑(swap)하며 뒤집어서 return 하도록 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "공백으로 구분된 정수 리스트가 주어집니다.",
    output_desc: "뒤집힌 배열 리스트를 반환하거나 출력합니다.",
    examples: [
      { input: "1 4 2 3", output: "[3, 2, 4, 1]" }
    ],
    starter_code: `def solution(arr):
    left, right = 0, len(arr)-1
    while @@@:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
arr = list(map(int, input().split()))
print(solution(arr))
`,
    solution_code: `# [정답 및 해설]
# 1. left 포인터가 right 포인터보다 작을 때(left < right) 동안 계속 스왑을 진행합니다.

def solution(arr):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = list(map(int, input().split()))
print(solution(arr))
`,
    test_cases: [
      { input: "1 4 2 3", output: "[3, 2, 4, 1]" },
      { input: "10 20 30", output: "[30, 20, 10]" },
      { input: "5", output: "[5]" }
    ]
  },
  {
    id: 46,
    classLevel: 2,
    title: "[문제 6] 369 게임 박수 횟수 구하기 (빈칸 채우기)",
    type: "blank",
    description: "369 게임은 여러 명이 같이하는 게임입니다. 게임의 규칙은 아래와 같습니다.\n- 1부터 시작합니다.\n- 한 사람씩 차례대로 숫자를 1씩 더해가며 말합니다.\n- 말해야 하는 숫자에 3, 6, 9중 하나라도 포함되어있다면 숫자를 말하는 대신 숫자에 포함된 3, 6, 9의 개수만큼 손뼉을 칩니다.\n어떤 수 number가 매개변수로 주어질 때, 1부터 number까지 369게임을 올바르게 진행했을 경우 박수를 총 몇 번 쳤는지를 return 하도록 solution 함수를 완성해주세요.",
    input_desc: "정수 number가 주어집니다. (10 이상 1,000 이하)",
    output_desc: "1부터 number까지 친 총 박수 횟수를 반환하거나 출력합니다.",
    examples: [
      { input: "40", output: "22" }
    ],
    starter_code: `def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            if @@@:
                count += 1
                print("pair", end = '')
            current = current // 10
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
number = int(input())
solution(number)
`,
    solution_code: `# [정답 및 해설]
# 1. 숫자의 각 자릿수를 확인하여 3, 6, 9인 경우 박수 카운트를 1 증가시킵니다.
# 2. current % 10이 3, 6, 9 중 하나인지 판별해야 하므로, current % 10 in [3, 6, 9] 또는 current % 10 == 3 or current % 10 == 6 or current % 10 == 9 등을 사용합니다.

def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            if current % 10 in [3, 6, 9]:
                count += 1
                print("pair", end = '')
            current = current // 10
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count

number = int(input())
solution(number)
`,
    test_cases: [
      { input: "40", output: "1 2 pair 4 5 pair 7 8 pair 10 11 12 pair 14 15 pair 17 18 pair 20 21 22 pair 24 25 pair 27 28 pair pair pair pair pairpair pair pair pairpair pair pair pairpair 40" },
      { input: "10", output: "1 2 pair 4 5 pair 7 8 pair 10" },
      { input: "15", output: "1 2 pair 4 5 pair 7 8 pair 10 11 12 pair 14 15" }
    ]
  },
  {
    id: 47,
    classLevel: 2,
    title: "[문제 7] 초급 영어 수강 대상 인원수 구하기 (한 줄 수정)",
    type: "code",
    description: "A 대학에서는 수준별 영어 강의를 제공하고 있습니다. 초급 영어 강의는 토익시험에서 650점 이상 800점 미만의 성적을 취득한 학생만을 수강대상으로 하고 있습니다. 초급 영어 강의에 수강신청한 사람이 10명일 때, 이 중에서 몇 명이 수강 대상에 해당하는지 확인하려 합니다. 수강신청자들의 토익 성적이 들어있는 배열 scores가 매개변수로 주어질 때, 수강 대상자들의 인원수를 return 하도록 solution 함수를 작성했습니다. 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.",
    input_desc: "공백으로 구분된 10개의 토익 성적이 주어집니다.",
    output_desc: "조건을 충족하는 초급 영어 수강 대상자 인원수를 반환하거나 출력합니다.",
    examples: [
      { input: "650 722 914 558 714 803 650 679 669 800", output: "6" }
    ],
    starter_code: `def solution(scores):
    count = 0
    for s in scores:
        if 650 <= s or s < 800:
            count += 1
    return count

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
scores = list(map(int, input().split()))
print(solution(scores))
`,
    solution_code: `# [정답 및 해설]
# 1. 기존의 조건인 650 <= s or s < 800는 or 조건이어서 모든 점수가 참이 됩니다.
# 2. '650점 이상 800점 미만'은 두 조건을 모두 충족해야 하므로 and 연산자로 연결해야 합니다. (650 <= s and s < 800)

def solution(scores):
    count = 0
    for s in scores:
        if 650 <= s and s < 800:
            count += 1
    return count

scores = list(map(int, input().split()))
print(solution(scores))
`,
    test_cases: [
      { input: "650 722 914 558 714 803 650 679 669 800", output: "6" },
      { input: "500 550 600 649 800 810 820 900 950 990", output: "0" },
      { input: "650 660 670 680 690 700 710 720 730 740", output: "10" }
    ]
  },
  {
    id: 48,
    classLevel: 2,
    title: "[문제 8] 팰린드롬 판단하기 (한 줄 수정)",
    type: "code",
    description: "앞에서부터 읽을 때와 뒤에서부터 읽을 때 똑같은 단어 또는 문장을 팰린드롬(palindrome)이라고 합니다. 예를 들어서 racecar, noon은 팰린드롬 단어입니다. 소문자 알파벳, 공백(\" \"), 그리고 마침표(\".\")로 이루어진 문장이 팰린드롬 문장인지 점검하려 합니다. 문장 내에서 알파벳만 추출하였을 때 팰린드롬 단어이면 팰린드롬 문장입니다. 주어진 문장 sentence가 주어질 때 팰린드롬이면 True, 아니면 False를 return 하도록 작성된 코드에서 한 줄만 변경하여 올바르게 동작하도록 수정해주세요.",
    input_desc: "팰린드롬 여부를 점검할 문장 sentence가 한 줄로 주어집니다.",
    output_desc: "팰린드롬 문장인지 아닌지 여부(True 또는 False)를 반환하거나 출력합니다.",
    examples: [
      { input: "never odd or even.", output: "True" },
      { input: "palindrome", output: "False" }
    ],
    starter_code: `def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' or c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
sentence = input()
print(solution(sentence))
`,
    solution_code: `# [정답 및 해설]
# 1. 마침표와 공백을 제외한 문자들만 str에 담아야 합니다.
# 2. '마침표가 아니고 공백도 아니다'를 의미하려면 c != '.' and c != ' '를 사용해야 합니다.

def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True

sentence = input()
print(solution(sentence))
`,
    test_cases: [
      { input: "never odd or even.", output: "True" },
      { input: "palindrome", output: "False" },
      { input: "a.", output: "True" }
    ]
  },
  {
    id: 49,
    classLevel: 2,
    title: "[문제 9] 연속하는 중복 문자 제거 (한 줄 수정)",
    type: "code",
    description: "알파벳 문자열이 주어질 때, 연속하는 중복 문자를 삭제하려고 합니다. 예를 들어, \"senteeeencccccceeee\"라는 문자열이 주어진다면, 연속된 중복 문자들이 1개로 압축되어 \"sentence\"라는 결과물이 나옵니다. 영어 소문자 알파벳으로 이루어진 임의의 문자열 characters가 매개변수로 주어질 때, 연속하는 중복 문자들을 삭제한 결과를 return 하도록 작성된 코드에서 한 줄만 변경하여 모든 입력에 대해 올바르게 동작하도록 수정하세요.",
    input_desc: "알파벳 소문자로 구성된 문자열 characters가 한 줄로 주어집니다.",
    output_desc: "연속하는 중복 문자가 삭제된 문자열을 반환하거나 출력합니다.",
    examples: [
      { input: "senteeeencccccceeee", output: "sentence" }
    ],
    starter_code: `def solution(characters):
    result = ""
    result += characters[0]
    for i in range(len(characters)):
        if characters[i - 1] != characters[i]:
            result += characters[i]
    return result

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
characters = input()
print(solution(characters))
`,
    solution_code: `# [정답 및 해설]
# 1. 루프의 인덱스가 0일 때, characters[i - 1]은 파이썬에서 characters[-1](마지막 문자)이 됩니다.
# 2. 따라서 루프는 0번째가 아닌 1번째 인덱스부터 검사해야 연속 중복 문자가 정상적으로 삭제됩니다. range(1, len(characters))로 변경합니다.

def solution(characters):
    result = ""
    result += characters[0]
    for i in range(1, len(characters)):
        if characters[i - 1] != characters[i]:
            result += characters[i]
    return result

characters = input()
print(solution(characters))
`,
    test_cases: [
      { input: "senteeeencccccceeee", output: "sentence" },
      { input: "aabccba", output: "abcba" },
      { input: "wwwwwwwwww", output: "w" }
    ]
  },
  {
    id: 50,
    classLevel: 2,
    title: "[문제 10] 평균 이하인 원소 개수 구하기 (한 줄 수정)",
    type: "code",
    description: "자연수가 들어있는 배열의 평균을 구하고, 평균 이하인 숫자는 몇 개 있는지 구하려 합니다. 예를 들어 주어진 배열이 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]이라면, 평균은 5.5이므로 배열에서 평균 이하인 값(1, 2, 3, 4, 5)은 5개입니다. 자연수가 들어있는 배열 data가 매개변수로 주어질 때, 배열에 평균 이하인 값은 몇 개인지 return 하도록 작성된 코드에서 한 줄만 변경하여 모든 입력에 대해 올바르게 동작하도록 수정하세요.",
    input_desc: "공백으로 구분된 자연수 데이터 리스트가 주어집니다.",
    output_desc: "평균보다 작거나 같은 원소의 개수를 반환하거나 출력합니다.",
    examples: [
      { input: "1 2 3 4 5 6 7 8 9 10", output: "5" },
      { input: "1 1 1 1 1 1 1 1 1 10", output: "9" }
    ],
    starter_code: `def solution(data):
    total = sum(data)
    average = len(data) / total
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
data = list(map(int, input().split()))
print(solution(data))
`,
    solution_code: `# [정답 및 해설]
# 1. 평균(average)은 합계(total) 나누기 개수(len(data))여야 합니다.
# 2. 기존 코드는 average = len(data) / total 로 나눗셈 연산의 피연산자 순서가 뒤집혀 있습니다. average = total / len(data) 로 수정해야 합니다.

def solution(data):
    total = sum(data)
    average = total / len(data)
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt

data = list(map(int, input().split()))
print(solution(data))
`,
    test_cases: [
      { input: "1 2 3 4 5 6 7 8 9 10", output: "5" },
      { input: "1 1 1 1 1 1 1 1 1 10", output: "9" },
      { input: "5 5 5 5 5", output: "5" }
    ]
  },
  {
    id: 51,
    classLevel: 2,
    title: "[2차] [문제 1] 장갑 매칭 최대 쌍 구하기 (빈칸 채우기)",
    type: "blank",
    description: "왼손 장갑의 제품 번호가 들어있는 배열과 오른손 장갑의 제품 번호가 들어있는 배열이 있습니다. 제품 번호는 1부터 10 사이의 자연수입니다. 제품 번호가 같은 왼손 장갑과 오른손 장갑을 합쳐 장갑 한 쌍을 만들 수 있습니다. 이때, 최대한 많은 쌍의 장갑을 만들면 최대 몇 쌍을 만들 수 있는지 구하려 합니다. 이를 위해 다음과 같이 프로그램 구조를 작성했습니다.\n1. 왼손 장갑이 제품 번호별로 몇 개씩 있는지 개수를 셉니다. (func_a)\n2. 오른손 장갑이 제품 번호별로 몇 개씩 있는지 개수를 셉니다. (func_a)\n3. 각 제품 번호별로 최대한 많은 장갑 쌍을 만들면서 개수를 셉니다.\n왼손 장갑의 제품 번호가 들어있는 배열 left_gloves와 오른손 장갑의 제품 번호가 들어있는 배열 right_gloves가 매개변수로 주어질 때, 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "첫 번째 줄에는 왼손 장갑 제품 번호들이 공백으로 구분되어 주어집니다. 두 번째 줄에는 오른손 장갑 제품 번호들이 공백으로 구분되어 주어집니다.",
    output_desc: "제품 번호가 같은 장갑끼리 만들 수 있는 최대 쌍의 개수를 반환하거나 출력합니다.",
    examples: [
      { input: "2 1 2 2 4\n1 2 2 4 4 7", output: "4" }
    ],
    starter_code: `max_product_number = 10

def func_a(gloves):
    counter = [0 for _ in range(max_product_number + 1)]
    for x in gloves:
        @@@
    return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)

    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    return total

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
left_gloves = list(map(int, input().split()))
right_gloves = list(map(int, input().split()))
print(solution(left_gloves, right_gloves))
`,
    solution_code: `# [정답 및 해설]
# 1. 왼손/오른손 장갑의 제품 번호별 개수를 세어야 합니다.
# 2. 리스트(counter)의 해당 제품 번호 인덱스에 매칭되는 값을 1씩 가산해주면 되므로 counter[x] += 1 을 작성합니다.

max_product_number = 10

def func_a(gloves):
    counter = [0 for _ in range(max_product_number + 1)]
    for x in gloves:
        counter[x] += 1
    return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)

    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    return total

left_gloves = list(map(int, input().split()))
right_gloves = list(map(int, input().split()))
print(solution(left_gloves, right_gloves))
`,
    test_cases: [
      { input: "2 1 2 2 4\n1 2 2 4 4 7", output: "4" },
      { input: "1 2 3\n4 5 6", output: "0" },
      { input: "10 10 10\n10 10 10 10", output: "3" }
    ]
  },
  {
    id: 52,
    classLevel: 2,
    title: "[2차] [문제 2] 3의 배수와 5의 배수 개수 비교 (빈칸 채우기)",
    type: "blank",
    description: "자연수가 들어있는 배열에 3의 배수와 5의 배수 중 어떤 수가 더 많은지 알아보려 합니다. 이를 위해 다음과 같이 프로그램 구조를 작성했습니다.\n1. 3의 배수의 개수를 셉니다. (func_c)\n2. 5의 배수의 개수를 셉니다. (func_a)\n3. 3의 배수와 5의 배수의 개수를 비교 후 다음을 수행합니다. (func_b)\n   - 만약 3의 배수가 더 많다면 \"three\"를 return 합니다.\n   - 만약 5의 배수가 더 많다면 \"five\"를 return 합니다.\n   - 만약 두 배수의 개수가 같다면 \"same\"을 return 합니다.\n자연수가 들어있는 배열 arr가 매개변수로 주어질 때, 구조에 맞춰 알맞은 함수와 매개변수를 빈칸에 채워 solution 함수를 완성해주세요.",
    input_desc: "공백으로 구분된 자연수 리스트가 주어집니다.",
    output_desc: "조건에 따라 \"three\", \"five\", \"same\" 중 하나를 출력합니다.",
    examples: [
      { input: "2 3 6 9 12 15 10 20 22 25", output: "three" }
    ],
    starter_code: `def func_a(arr):
    count = 0
    for n in arr:
        if n % 5 == 0:
            count += 1
    return count

def func_b(three, five):
    if three > five:
        return "three"
    elif three < five:
        return "five"
    else:
        return "same"

def func_c(arr):
    count = 0
    for n in arr:
        if n % 3 == 0:
            count += 1
    return count

def solution(arr):
    count_three = func_@@@(@@@)
    count_five = func_@@@(@@@)
    answer = func_@@@(@@@)
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
arr = list(map(int, input().split()))
print(solution(arr))
`,
    solution_code: `# [정답 및 해설]
# 1. 3의 배수를 세어 저장할 count_three 변수에는 func_c(arr)를 호출합니다.
# 2. 5의 배수를 세어 저장할 count_five 변수에는 func_a(arr)를 호출합니다.
# 3. 두 배수들의 개수를 비교하기 위해 func_b(count_three, count_five)를 호출합니다.

def func_a(arr):
    count = 0
    for n in arr:
        if n % 5 == 0:
            count += 1
    return count

def func_b(three, five):
    if three > five:
        return "three"
    elif three < five:
        return "five"
    else:
        return "same"

def func_c(arr):
    count = 0
    for n in arr:
        if n % 3 == 0:
            count += 1
    return count

def solution(arr):
    count_three = func_c(arr)
    count_five = func_a(arr)
    answer = func_b(count_three, count_five)
    return answer

arr = list(map(int, input().split()))
print(solution(arr))
`,
    test_cases: [
      { input: "2 3 6 9 12 15 10 20 22 25", output: "three" },
      { input: "5 10 15 20", output: "five" },
      { input: "15 30", output: "same" }
    ]
  },
  {
    id: 53,
    classLevel: 2,
    title: "[2차] [문제 3] 짝수들의 제곱의 합 (소스코드 작성)",
    type: "code",
    description: "서로 다른 두 자연수 N과 M이 매개변수로 주어질 때, N부터 M까지의 자연수 중에서 짝수들의 제곱의 합을 구하는 함수를 완성해주세요.",
    input_desc: "공백으로 구분된 두 자연수 N과 M이 주어집니다. (N < M)",
    output_desc: "N부터 M까지의 수 중 짝수들의 제곱 합을 반환하거나 출력합니다.",
    examples: [
      { input: "4 7", output: "52" }
    ],
    starter_code: `def solution(N, M):
    # 여기에 코드를 작성해주세요.
    answer = 0
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1]))
`,
    solution_code: `# [정답 및 해설]
# 1. N부터 M까지 루프를 수행하면서 각 수(i)가 짝수(i % 2 == 0)인 경우에만 i의 제곱(i ** 2)을 합산(answer)에 더합니다.

def solution(N, M):
    answer = 0
    for i in range(N, M + 1):
        if i % 2 == 0:
            answer += i ** 2
    return answer

inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1]))
`,
    test_cases: [
      { input: "4 7", output: "52" },
      { input: "1 5", output: "20" },
      { input: "2 2", output: "4" }
    ]
  },
  {
    id: 54,
    classLevel: 2,
    title: "[2차] [문제 4] 5글자 이상 단어 연결하기 (소스코드 작성)",
    type: "code",
    description: "단어들이 들어있는 배열에서 길이가 5 이상인 단어를 배열에 들어있는 순서대로 이어 붙인 문자열을 만들려고 합니다. 만약 이어 붙일 문자열이 아예 없다면(빈 문자열인 경우) \"empty\"를 return 하도록 solution 함수를 완성해주세요.",
    input_desc: "공백으로 구분된 영어 소문자 단어 리스트가 주어집니다.",
    output_desc: "길이가 5 이상인 단어를 이어 붙인 단일 문자열을 출력하며, 해당되는 단어가 전혀 없는 경우 \"empty\"를 출력합니다.",
    examples: [
      { input: "my favorite color is violet", output: "favoritecolorviolet" },
      { input: "yes i am", output: "empty" }
    ],
    starter_code: `def solution(words):
    # 여기에 코드를 작성해주세요.
    answer = ''
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
words = input().split()
print(solution(words))
`,
    solution_code: `# [정답 및 해설]
# 1. 단어 목록(words)을 순회하며 글자 수가 5글자 이상인 단어들(len(word) >= 5)만 answer에 이어 붙입니다.
# 2. 순회가 끝나고 answer가 빈 문자열("")인 경우 "empty"를 반환하고, 그렇지 않으면 누적 문자열을 반환합니다.

def solution(words):
    answer = ''
    for word in words:
        if len(word) >= 5:
            answer += word
    if answer == '':
        return "empty"
    return answer

words = input().split()
print(solution(words))
`,
    test_cases: [
      { input: "my favorite color is violet", output: "favoritecolorviolet" },
      { input: "yes i am", output: "empty" },
      { input: "hello world nice", output: "helloworld" }
    ]
  },
  {
    id: 55,
    classLevel: 2,
    title: "[2차] [문제 5] 몬스터 잡기 공격 횟수 구하기 (빈칸 채우기)",
    type: "blank",
    description: "게임 캐릭터가 몬스터와 1:1 전투를 합니다. 캐릭터는 매 턴마다 항상 일정한 데미지(attack)를 주는 공격 마법만 사용하고, 몬스터는 항상 일정한 수치(recovery)로 체력을 회복하는 힐링 마법만 사용합니다. 항상 캐릭터가 먼저 공격을 시작하며 번갈아 가며 턴이 진행됩니다. 캐릭터가 몬스터를 처치하기 위해(체력을 0 이하로 만들기 위해) 최소 몇 번 공격해야 하는지 구하려고 합니다. 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "공백으로 구분된 공격력(attack), 회복력(recovery), 초기 체력(hp)가 차례대로 주어집니다.",
    output_desc: "몬스터를 처치하기 위해 필요로 하는 최소 공격 횟수를 반환하거나 출력합니다.",
    examples: [
      { input: "30 10 60", output: "3" }
    ],
    starter_code: `def solution(attack, recovery, hp):
    count = 0
    while(True):
        count += @@@
        hp -= @@@
        if hp <= 0:
            @@@
        hp += @@@
    return count

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1], inputs[2]))
`,
    solution_code: `# [정답 및 해설]
# 1. 한 번 공격할 때마다 count를 1씩 누적합니다. (count += 1)
# 2. 몬스터 체력에서 공격력만큼 데미지를 뺍니다. (hp -= attack)
# 3. 몬스터 체력이 0 이하가 된 경우, 루프를 탈출하여 종료합니다. (break)
# 4. 몬스터가 살아있는 경우 몬스터가 회복합니다. (hp += recovery)

def solution(attack, recovery, hp):
    count = 0
    while(True):
        count += 1
        hp -= attack
        if hp <= 0:
            break
        hp += recovery
    return count

inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1], inputs[2]))
`,
    test_cases: [
      { input: "30 10 60", output: "3" },
      { input: "100 10 250", output: "3" },
      { input: "50 49 50", output: "1" }
    ]
  },
  {
    id: 56,
    classLevel: 2,
    title: "[2차] [문제 6] 엘리베이터 총 이동거리 구하기 (빈칸 채우기)",
    type: "blank",
    description: "하루 동안 엘리베이터가 멈춘 층이 순서대로 들어있는 배열이 있습니다. 이때, 엘리베이터의 총 이동거리를 구하려 합니다. 단, 층과 층 사이의 거리는 1입니다. 예를 들어 배열에 [1, 2, 5, 4, 2]가 들어있다면, 엘리베이터가 이동한 거리는 7입니다. 하루 동안 엘리베이터가 멈춰 선 층이 순서대로 들어있는 배열 floors가 매개변수로 주어질 때, 빈칸을 채워 엘리베이터의 총 이동 거리를 return 하는 solution 함수를 완성해주세요.",
    input_desc: "공백으로 구분된 하루 동안 엘리베이터가 멈춘 층들의 리스트가 주어집니다.",
    output_desc: "엘리베이터의 총 이동 거리를 반환하거나 출력합니다.",
    examples: [
      { input: "1 2 5 4 2", output: "7" }
    ],
    starter_code: `def solution(floors):
    dist = 0
    length = len(floors)
    for i in range(@@@):
        if @@@:
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1] - floors[i]
    return dist

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
floors = list(map(int, input().split()))
print(solution(floors))
`,
    solution_code: `# [정답 및 해설]
# 1. 인덱스 1번 원소부터 순회하며 직전 층(floors[i-1])과의 높이 차이를 누적 합산해야 하므로 루프는 range(1, length)로 설정합니다.
# 2. 이동거리는 항상 양수여야 하므로 현재 층이 이전 층보다 높으면(floors[i] > floors[i-1]) floors[i] - floors[i-1]을 더하고, 그렇지 않으면 반대로 더합니다.

def solution(floors):
    dist = 0
    length = len(floors)
    for i in range(1, length):
        if floors[i] > floors[i-1]:
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1] - floors[i]
    return dist

floors = list(map(int, input().split()))
print(solution(floors))
`,
    test_cases: [
      { input: "1 2 5 4 2", output: "7" },
      { input: "10 20", output: "10" },
      { input: "3 2 1 2 3", output: "4" }
    ]
  },
  {
    id: 57,
    classLevel: 2,
    title: "[2차] [문제 7] 온도의 정수 부분 환산하기 (한 줄 수정)",
    type: "code",
    description: "화씨온도(°F)를 섭씨온도(°C)로, 섭씨온도(°C)를 화씨온도(°F)로 바꾸려고 합니다. 두 온도 사이의 환산 공식은 다음과 같습니다.\n- 화씨온도(°F)에서 섭씨온도(°C)로 환산: (화씨온도 - 32) / 1.8 = 섭씨온도\n- 섭씨온도(°C)에서 화씨온도(°F)로 환산: (섭씨온도 * 1.8) + 32 = 화씨온도\n현재 온도 value와 현재 단위 unit이 매개변수로 주어질 때, 환산한 온도의 정수 부분을 return 하도록 작성된 코드입니다. 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.",
    input_desc: "공백으로 구분된 온도 정수 value와 단위 unit(C 또는 F)이 주어집니다.",
    output_desc: "환산한 온도의 정수 부분을 반환하거나 출력합니다.",
    examples: [
      { input: "527 C", output: "980" }
    ],
    starter_code: `def solution(value, unit):
    converted = 0
    if unit == "C":
        value = value * 1.8 + 32
    if unit == "F":
        value = value - 32 / 1.8
    converted = int(value)
    return converted

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
inputs = input().split()
value = int(inputs[0])
unit = inputs[1]
print(solution(value, unit))
`,
    solution_code: `# [정답 및 해설]
# 1. 섭씨에서 화씨는 정상적으로 구현되었으나, 화씨에서 섭씨 환산식 'value = value - 32 / 1.8'은 연산자 우선순위로 인해 32 / 1.8을 먼저 연산하게 됩니다.
# 2. 괄호를 씌워 (value - 32) / 1.8 형식으로 동작하도록 수정해야 합니다: value = (value - 32) / 1.8

def solution(value, unit):
    converted = 0
    if unit == "C":
        value = value * 1.8 + 32
    if unit == "F":
        value = (value - 32) / 1.8
    converted = int(value)
    return converted

inputs = input().split()
value = int(inputs[0])
unit = inputs[1]
print(solution(value, unit))
`,
    test_cases: [
      { input: "527 C", output: "980" },
      { input: "980 F", output: "526" },
      { input: "32 F", output: "0" }
    ]
  },
  {
    id: 58,
    classLevel: 2,
    title: "[2차] [문제 8] 자릿수 소수(2,3,5,7) 개수 세기 (한 줄 수정)",
    type: "code",
    description: "자연수의 각 자릿수 중에서 소수(Prime Number)는 몇 개인지 구하려 합니다. 즉, 자연수를 각 자릿수별로 나누었을 때, 2, 3, 5, 7이 몇 개 있는지 구하려 합니다. 예를 들어, 자연수가 29022531일 때, 소수인 자릿수는 2, 2, 2, 5, 3으로 총 5개입니다. 자연수 number가 매개변수로 주어질 때, 자릿수 중 소수의 개수를 return 하도록 작성된 코드에서 한 줄만 변경해서 올바르게 동작하도록 수정하세요.",
    input_desc: "자연수 number가 한 줄로 주어집니다.",
    output_desc: "각 자릿수 중 2, 3, 5, 7에 해당하는 자릿수들의 개수를 출력합니다.",
    examples: [
      { input: "29022531", output: "5" }
    ],
    starter_code: `def solution(number):
    count = 0
    while number >= 0:
        n = number % 10
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        number //= 10
    return count

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
number = int(input())
print(solution(number))
`,
    solution_code: `# [정답 및 해설]
# 1. 0보다 크거나 같을 때(number >= 0) 루프를 돌게 되면, 몫이 0이 된 이후에도 무한 루프가 발생하여 에러가 나거나 끝나지 않습니다.
# 2. 따라서 number > 0 일 때로 탈출 조건을 변경하여, 자연수를 모두 나눈 시점에 안전하게 탈출하도록 해야 합니다.

def solution(number):
    count = 0
    while number > 0:
        n = number % 10
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        number //= 10
    return count

number = int(input())
print(solution(number))
`,
    test_cases: [
      { input: "29022531", output: "5" },
      { input: "1234567890", output: "4" },
      { input: "4", output: "0" }
    ]
  },
  {
    id: 59,
    classLevel: 2,
    title: "[2차] [문제 9] 정확히 K 표를 받은 후보 세기 (한 줄 수정)",
    type: "code",
    description: "N명의 후보에 대해 투표한 결과가 들어있는 배열이 있습니다. 이때, 정확히 K 표를 받은 후보는 총 몇 명인지 구하려 합니다. 투표 결과가 들어있는 배열 votes, 후보의 수 N, 표의 개수 K가 매개변수로 주어질 때, K 표를 받은 후보가 몇 명인지 return 하도록 작성된 코드입니다. 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.",
    input_desc: "첫 번째 줄에 공백으로 구분된 후보 투표 리스트가 주어집니다. 두 번째 줄에 후보 수 N과 득표수 K가 공백으로 구분되어 주어집니다.",
    output_desc: "정확히 K 표를 얻은 후보의 인원수를 출력합니다.",
    examples: [
      { input: "2 5 3 4 1 5 1 5 5 3\n5 2", output: "2" }
    ],
    starter_code: `def solution(votes, N, K):
    counter = [0 for _ in range(N + 1)]
    for x in votes:
        counter[x] += 1
    answer = -1
    for c in counter:
        if c == K:
            answer += 1
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
votes = list(map(int, input().split()))
inputs = list(map(int, input().split()))
N, K = inputs[0], inputs[1]
print(solution(votes, N, K))
`,
    solution_code: `# [정답 및 해설]
# 1. 득표수의 카운트를 세는 answer 변수의 초깃값이 -1 로 잘못 설정되어 있습니다.
# 2. 맞게 카운트하기 위해 answer의 초깃값을 0으로 변경해 주어야 합니다.

def solution(votes, N, K):
    counter = [0 for _ in range(N + 1)]
    for x in votes:
        counter[x] += 1
    answer = 0
    for c in counter:
        if c == K:
            answer += 1
    return answer

votes = list(map(int, input().split()))
inputs = list(map(int, input().split()))
N, K = inputs[0], inputs[1]
print(solution(votes, N, K))
`,
    test_cases: [
      { input: "2 5 3 4 1 5 1 5 5 3\n5 2", output: "2" },
      { input: "1 1 1 2 2 3\n3 3", output: "1" },
      { input: "1 1 1\n1 0", output: "1" }
    ]
  },
  {
    id: 60,
    classLevel: 2,
    title: "[2차] [문제 10] 고객 상품권 총 지급액 구하기 (한 줄 수정)",
    type: "code",
    description: "A 백화점에서는 고객의 구매금액에 따라 다음과 같이 상품권을 지급합니다. 상품권은 지급 가능한 가장 큰 금액으로 한 장만 지급합니다.\n- 100만 원 이상 구매: 5만 원 상품권\n- 60만 원 이상 구매: 3만 원 상품권\n- 40만 원 이상 구매: 2만 원 상품권\n- 20만 원 이상 구매: 1만 원 상품권\n고객들의 구매 금액이 들어있는 배열 purchase가 주어질 때, 고객들에게 지급해야 하는 상품권 총액을 return 하도록 작성된 코드입니다. 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.",
    input_desc: "공백으로 구분된 고객들의 구매 금액 리스트가 한 줄로 주어집니다.",
    output_desc: "백화점에서 지급해야 할 총 상품권 지급액을 출력합니다.",
    examples: [
      { input: "150000 210000 399990 990000 1000000", output: "100000" }
    ],
    starter_code: `def solution(purchase):
    total = 0
    for p in purchase:
        if p >= 1000000:
            total += 50000
        elif p >= 600000:
            total += 30000
        elif p >= 400000:
            total += 20000
        else:
            total += 10000
    return total

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
purchase = list(map(int, input().split()))
print(solution(purchase))
`,
    solution_code: `# [정답 및 해설]
# 1. 20만 원 이상 40만 원 미만일 때의 엘리프 분기(p >= 200000) 및 상품권 지급 처리 조건이 누락되었습니다.
# 2. 누락된 분기를 보완하여 20만 원 이상일 때 1만 원 상품권을 지급하고(elif p >= 200000: total += 10000), 20만 원 미만일 때(else) 지급하지 않도록(아무것도 가산하지 않음) 수정해야 합니다.
# 3. 추가로 return total은 모든 구매 목록의 순회가 종료된 후 한 번만 이루어져야 하므로 들여쓰기 위치를 for문 밖으로 내어줍니다.

def solution(purchase):
    total = 0
    for p in purchase:
        if p >= 1000000:
            total += 50000
        elif p >= 600000:
            total += 30000
        elif p >= 400000:
            total += 20000
        elif p >= 200000:
            total += 10000
    return total

purchase = list(map(int, input().split()))
print(solution(purchase))
`,
    test_cases: [
      { input: "150000 210000 399990 990000 1000000", output: "100000" },
      { input: "100000 190000 50000", output: "0" },
      { input: "200000 400000 600000 1000000", output: "110000" }
    ]
  },
  {
    id: 61,
    classLevel: 2,
    title: "[3차] [문제 1] 학생 시험 석차 구하기 (빈칸 채우기)",
    type: "blank",
    description: "학생들의 시험 점수가 주어졌을 때, n번 학생이 몇 등인지 구하려 합니다. 학번은 0번부터 시작하며, 시험 점수는 학번순으로 주어집니다. 동점자는 없다고 가정합니다. 이를 위해 다음과 같이 프로그램 구조를 작성했습니다.\n1. n번 학생의 점수를 변수에 저장합니다. (func_c)\n2. 점수를 내림차순으로 정렬합니다. (func_b)\n3. 배열의 첫 번째 원소부터 마지막 원소까지 순회하며 n번 학생의 점수를 찾아 등수를 return 합니다. (func_a)\n학생들의 시험 점수가 번호순으로 들은 배열 scores와 학번 n이 주어질 때, 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "첫 번째 줄에 공백으로 구분된 시험 점수 리스트 scores가 주어집니다. 두 번째 줄에 등수를 구하고 싶은 학번 n이 주어집니다.",
    output_desc: "학번 n인 학생의 석차(등수)를 출력합니다.",
    examples: [
      { input: "20 60 98 59\n3", output: "3" }
    ],
    starter_code: `def func_a(scores, score):
    rank = 1
    for s in scores:
        if s == score:
            return rank
        rank += 1
    return 0

def func_b(arr):
    arr.sort(reverse=True)

def func_c(arr, n):
    return arr[n]

def solution(scores, n):
    score = func_@@@(@@@)
    func_@@@(@@@)
    answer = func_@@@(@@@)
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
scores = list(map(int, input().split()))
n = int(input())
print(solution(scores, n))
`,
    solution_code: `# [정답 및 해설]
# 1. n번 학생의 원본 점수를 구하기 위해 func_c(scores, n)을 호출해 score 변수에 저장합니다.
# 2. 등수 확인을 위해 점수를 내림차순으로 정렬하는 func_b(scores)를 수행합니다.
# 3. 내림차순 정렬된 점수 리스트(scores)와 n번 학생의 점수(score)를 func_a(scores, score)에 전달하여 등수를 구합니다.

def func_a(scores, score):
    rank = 1
    for s in scores:
        if s == score:
            return rank
        rank += 1
    return 0

def func_b(arr):
    arr.sort(reverse=True)

def func_c(arr, n):
    return arr[n]

def solution(scores, n):
    score = func_c(scores, n)
    func_b(scores)
    answer = func_a(scores, score)
    return answer

scores = list(map(int, input().split()))
n = int(input())
print(solution(scores, n))
`,
    test_cases: [
      { input: "20 60 98 59\n3", output: "3" },
      { input: "90 80 70 60\n0", output: "1" },
      { input: "50 70 60 80 90\n2", output: "4" }
    ]
  },
  {
    id: 62,
    classLevel: 2,
    title: "[3차] [문제 2] 장학생 선발 인원 세기 (빈칸 채우기)",
    type: "blank",
    description: "장학생 선발 기준에 부합하는 학생 수를 구하려고 합니다. 장학금을 주는 조건은 다음과 같으며, 중복 수혜는 불가합니다.\n1. 이번 학기 성적이 80점 이상이면서 석차가 상위 10% 이내인 학생\n2. 이번 학기 성적이 80점 이상이면서 1등인 학생\n3. 직전 학기 대비 성적이 가장 많이 오른 학생 (여러 명인 경우 전부 포함, 성적이 오른 경우만 해당)\n이를 위해 다음과 같이 프로그램 구조를 작성했습니다.\n- 1단계: 이번 학기 성적을 기준으로 학생별 석차를 구합니다. (func_b)\n- 2단계: 각 학생의 (이번 학기 성적 - 직전 학기 성적) 중 최댓값을 구합니다. (func_c)\n- 3단계: 조건을 만족하는 학생들을 선발하여 인원을 셉니다. (func_a)\n학생들의 이번 학기 성적 배열 current_grade와 직전 학기 성적 배열 last_grade가 주어질 때, 알맞은 함수와 매개변수를 빈칸에 채워 solution 함수를 완성해주세요.",
    input_desc: "첫 번째 줄에는 이번 학기 성적들이 공백으로 구분되어 주어집니다. 두 번째 줄에는 직전 학기 성적들이 공백으로 구분되어 주어집니다.",
    output_desc: "선발된 총 장학생 수를 출력합니다.",
    examples: [
      { input: "70 100 70 80 50 95\n35 65 80 50 20 60", output: "3" }
    ],
    starter_code: `def func_a(current_grade, last_grade, rank, max_diff_grade):
    arr_length = len(current_grade)
    count = 0
    for i in range(arr_length):
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10:
            count += 1
        elif current_grade[i] >= 80 and rank[i] == 1:
            count += 1
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:
            count += 1
    return count

def func_b(current_grade):
    arr_length = len(current_grade)
    rank = [1] * arr_length
    for i in range(arr_length):
        for j in range(arr_length):
            if current_grade[i] < current_grade[j]:
                rank[i] += 1
    return rank

def func_c(current_grade, last_grade):
    max_diff_grade = 1
    for i in range(len(current_grade)):
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])
    return max_diff_grade

def solution(current_grade, last_grade):
    rank = func_@@@(@@@)
    max_diff_grade = func_@@@(@@@)
    answer = func_@@@(@@@)
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
current_grade = list(map(int, input().split()))
last_grade = list(map(int, input().split()))
print(solution(current_grade, last_grade))
`,
    solution_code: `# [정답 및 해설]
# 1. 1단계 석차 계산을 위해 rank = func_b(current_grade)를 호출합니다.
# 2. 2단계 최대 성적 격차 계산을 위해 max_diff_grade = func_c(current_grade, last_grade)를 호출합니다.
# 3. 3단계 최종 선발 인원을 세기 위해 answer = func_a(current_grade, last_grade, rank, max_diff_grade)를 호출합니다.

def func_a(current_grade, last_grade, rank, max_diff_grade):
    arr_length = len(current_grade)
    count = 0
    for i in range(arr_length):
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10:
            count += 1
        elif current_grade[i] >= 80 and rank[i] == 1:
            count += 1
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:
            count += 1
    return count

def func_b(current_grade):
    arr_length = len(current_grade)
    rank = [1] * arr_length
    for i in range(arr_length):
        for j in range(arr_length):
            if current_grade[i] < current_grade[j]:
                rank[i] += 1
    return rank

def func_c(current_grade, last_grade):
    max_diff_grade = 1
    for i in range(len(current_grade)):
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])
    return max_diff_grade

def solution(current_grade, last_grade):
    rank = func_b(current_grade)
    max_diff_grade = func_c(current_grade, last_grade)
    answer = func_a(current_grade, last_grade, rank, max_diff_grade)
    return answer

current_grade = list(map(int, input().split()))
last_grade = list(map(int, input().split()))
print(solution(current_grade, last_grade))
`,
    test_cases: [
      { input: "70 100 70 80 50 95\n35 65 80 50 20 60", output: "3" },
      { input: "90 90 90\n80 80 80", output: "3" },
      { input: "50 60 70\n50 50 50", output: "1" }
    ]
  },
  {
    id: 63,
    classLevel: 2,
    title: "[3차] [문제 3] 체조 점수 계산 (소스코드 작성)",
    type: "code",
    description: "체조선수의 최종 점수를 계산하려 합니다. 최종 점수는 심사위원의 점수 중 가장 높은 점수 하나와 가장 낮은 점수 하나를 제외한 나머지 점수들의 평균으로 구합니다. 단, 평균 계산 시 소수점 이하의 수는 버립니다(정수 나눗셈 결과 요구). 각 심사위원의 점수가 담긴 배열 scores가 매개변수로 주어질 때, 선수가 받은 최종 점수를 return 하도록 solution 함수를 완성해주세요.",
    input_desc: "공백으로 구분된 심사위원들의 점수 리스트가 주어집니다.",
    output_desc: "최고점과 최저점을 제외한 점수 평균의 정수(몫)를 출력합니다.",
    examples: [
      { input: "35 28 98 34 20 50 85 74 71 7", output: "49" },
      { input: "1 1 1 1 1", output: "1" }
    ],
    starter_code: `def solution(scores):
    # 여기에 코드를 작성해주세요.
    answer = 0
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
scores = list(map(int, input().split()))
print(solution(scores))
`,
    solution_code: `# [정답 및 해설]
# 1. scores 리스트의 전체 합 sum(scores)에서 최댓값 max(scores)와 최솟값 min(scores)을 빼줍니다.
# 2. 제외한 데이터 개수인 len(scores) - 2 로 나눈 몫(//)을 계산하여 소수점 아래는 버린 정수 형태로 반환합니다.

def solution(scores):
    total = sum(scores) - max(scores) - min(scores)
    answer = total // (len(scores) - 2)
    return answer

scores = list(map(int, input().split()))
print(solution(scores))
`,
    test_cases: [
      { input: "35 28 98 34 20 50 85 74 71 7", output: "49" },
      { input: "1 1 1 1 1", output: "1" },
      { input: "10 20 30", output: "20" }
    ]
  },
  {
    id: 64,
    classLevel: 2,
    title: "[3차] [문제 4] 영어 타이핑 오타 수 구하기 (소스코드 작성)",
    type: "code",
    description: "영어 타이핑 오타를 점검하려 합니다. 원래 치려고 했던 표준 단어 문자열 word와, 타이핑한 결과 단어들이 담긴 배열 words가 주어집니다. 각각의 단어들을 원래 단어와 자릿수별로 비교하여, 원래 단어와 일치하지 않는 문자의 총 개수(틀린 자릿수의 누적합)를 계산하여 return 하는 solution 함수를 완성해주세요.",
    input_desc: "첫 번째 줄에는 공백으로 구분된 타이핑한 단어들의 배열 words가 주어집니다. 두 번째 줄에는 원래 치려했던 표준 단어 word가 주어집니다.",
    output_desc: "원래 단어와 달라 고쳐야 하는 문자의 누적 총 개수를 출력합니다.",
    examples: [
      { input: "CODE COED CDEO\nCODE", output: "5" }
    ],
    starter_code: `def solution(words, word):
    # 여기에 코드를 작성해주세요.
    count = 0
    return count

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
words = input().split()
word = input()
print(solution(words, word))
`,
    solution_code: `# [정답 및 해설]
# 1. 입력된 words 리스트 내의 각 문자열(w)을 타겟 단어(word)와 인덱스별로 순회하며 대조합니다.
# 2. w[i] != word[i]가 성립하는 경우 오타로 취급하여 count를 1씩 가산하고 최종 합을 반환합니다.

def solution(words, word):
    count = 0
    for w in words:
        for i in range(len(word)):
            if w[i] != word[i]:
                count += 1
    return count

words = input().split()
word = input()
print(solution(words, word))
`,
    test_cases: [
      { input: "CODE COED CDEO\nCODE", output: "5" },
      { input: "TEST TAST TERT\nTEST", output: "2" },
      { input: "ABC\nABC", output: "0" }
    ]
  },
  {
    id: 65,
    classLevel: 2,
    title: "[3차] [문제 5] 몬스터 처치 최소 턴수 (빈칸 채우기)",
    type: "blank",
    description: "게임 캐릭터가 몬스터와 1:1 전투를 진행합니다. 캐릭터는 매 턴마다 일정한 데미지(attack)를 입히는 공격 마법만 사용하고, 몬스터는 매 턴마다 일정한 수치(recovery)로 체력을 회복하는 힐링 마법만 사용합니다. 항상 캐릭터가 먼저 공격을 시작하고 번갈아 가며 진행됩니다. 몬스터의 초기 체력 hp가 주어질 때, 몬스터의 체력을 0 이하로 만들기 위해 최소 몇 번 공격해야 하는지 구하려고 합니다. 빈칸을 채워 전체 코드를 완성해주세요.",
    input_desc: "공백으로 구분된 공격력(attack), 회복력(recovery), 초기체력(hp)가 차례대로 주어집니다.",
    output_desc: "몬스터를 처치하기 위해 요구되는 최소 공격 횟수를 반환하거나 출력합니다.",
    examples: [
      { input: "30 10 60", output: "3" }
    ],
    starter_code: `def solution(attack, recovery, hp):
    count = 0
    while(True):
        count += @@@
        hp -= @@@
        if hp <= 0:
            @@@
        hp += @@@
    return count

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1], inputs[2]))
`,
    solution_code: `# [정답 및 해설]
# 1. 턴이 한번 돌 때마다 공격 횟수 count를 1씩 가산합니다. (count += 1)
# 2. 몬스터 체력을 공격력만큼 감소시킵니다. (hp -= attack)
# 3. 몬스터 체력이 0 이하가 된 경우, 루프를 종료하고 즉시 빠져나갑니다. (break)
# 4. 몬스터 체력이 남아있다면 회복량만큼 증가시킵니다. (hp += recovery)

def solution(attack, recovery, hp):
    count = 0
    while(True):
        count += 1
        hp -= attack
        if hp <= 0:
            break
        hp += recovery
    return count

inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1], inputs[2]))
`,
    test_cases: [
      { input: "30 10 60", output: "3" },
      { input: "100 10 250", output: "3" },
      { input: "50 49 50", output: "1" }
    ]
  },
  {
    id: 66,
    classLevel: 2,
    title: "[3차] [문제 6] 타일 색칠 순서 구하기 (빈칸 채우기)",
    type: "blank",
    description: "타일을 'R', 'G', 'B' 색으로 칠하려 합니다. R 색으로는 3칸을 한 번에, G 색으로는 2칸을 한 번에 칠할 수 있으며, B 색으로는 1칸을 칠할 수 있습니다. 색은 R, G, B 순서로 한 번씩 번갈아 가면서 사용해야 하며, 타일의 길이를 넘겨서 칠할 수는 없습니다. 타일 길이가 매개변수 tile_length로 주어질 때, 타일을 색칠한 순서를 문자열로 return하는 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요. 순서에 맞게 타일을 칠할 수 없다면 -1을 문자열 '-1'로 return 해주세요.",
    input_desc: "타일 길이 tile_length가 1,000 이하의 자연수로 주어집니다.",
    output_desc: "타일을 칠한 패턴 문자열을 출력하거나, 올바르게 칠하지 못하면 '-1'을 출력합니다.",
    examples: [
      { input: "11", output: "RRRGGBRRRGG" },
      { input: "16", output: "-1" }
    ],
    starter_code: `def solution(tile_length):
    answer = ''
    com = 'RRRGGB'
    if tile_length % 6 == 1 or tile_length % 6 == 2 or @@@:
        answer = '-1'
    else:
        for i in range(tile_length):
            answer += com[i % 6]
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
tile_length = int(input())
print(solution(tile_length))
`,
    solution_code: `# [정답 및 해설]
# 1. 하나의 완성 주기는 'RRRGGB'로 총 6칸입니다.
# 2. R을 칠하려다 실패하는 케이스(길이가 6으로 나눈 나머지가 1 또는 2인 경우)와, G를 칠하려다 실패하는 케이스(나머지가 4인 경우)가 예외 상황입니다. 
# 3. 나머지가 3, 5, 0인 경우에는 타일 길이를 초과하지 않고 딱 나누어 떨어지거나 단위를 맞출 수 있습니다. 따라서 조건식에 tile_length % 6 == 4 를 작성해 줍니다.

def solution(tile_length):
    answer = ''
    com = 'RRRGGB'
    if tile_length % 6 == 1 or tile_length % 6 == 2 or tile_length % 6 == 4:
        answer = '-1'
    else:
        for i in range(tile_length):
            answer += com[i % 6]
    return answer

tile_length = int(input())
print(solution(tile_length))
`,
    test_cases: [
      { input: "11", output: "RRRGGBRRRGG" },
      { input: "16", output: "-1" },
      { input: "6", output: "RRRGGB" }
    ]
  },
  {
    id: 67,
    classLevel: 2,
    title: "[3차] [문제 7] 주스 제조 최대 잔수 구하기 (한 줄 수정)",
    type: "code",
    description: "주스 1잔을 만들려면 사과 3개와 당근 1개가 필요합니다. 그런데 키우는 토끼에게 먹이를 주기 위해 사과와 당근 종류에 상관없이 k개를 빼놓으려고 합니다. 주스는 최대한 많이 만들수록 좋습니다. 사과 개수 num_apple과 당근 개수 num_carrot, 토끼에게 줄 먹이 개수 k가 주어질 때 주스를 최대 몇 잔 만들 수 있는지 return 하도록 solution 함수를 작성했습니다. 코드 일부분을 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.",
    input_desc: "사과 수 num_apple, 당근 수 num_carrot, 토끼 먹이 수 k가 공백으로 구분되어 주어집니다.",
    output_desc: "만들 수 있는 최대 주스 잔수를 출력합니다.",
    examples: [
      { input: "5 1 2", output: "1" },
      { input: "10 5 4", output: "2" }
    ],
    starter_code: `def solution(num_apple, num_carrot, k):
    answer = 0

    if num_apple < num_carrot * 3:
        answer = num_apple // 3
    else:
        answer = num_carrot    

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0
    while k - (num_apple + num_carrot + i) > 0:
        if i % 4 == 0:
            answer += 1
        i = i + 1

    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1], inputs[2]))
`,
    solution_code: `# [정답 및 해설]
# 1. 1차적으로 주스를 다 만든 후, 남은 재료(num_apple + num_carrot)로 먹이 k개를 우선 차감합니다. 
# 2. 만약 재료가 모자라면 주스를 허물어야(answer -= 1) 하며, 주스 1잔을 허물 때마다 과일 4개(사과 3개, 당근 1개)가 추가로 확보됩니다.
# 3. while 조건식 'while k - (num_apple + num_carrot + i) > 0:' 에 따라, 1잔을 줄여서 사과 3개와 당근 1개를 복원하므로 answer가 1 감소해야 합니다. 기존 코드는 answer += 1로 잘못 증가시켰으므로 answer -= 1로 수정합니다.

def solution(num_apple, num_carrot, k):
    answer = 0

    if num_apple < num_carrot * 3:
        answer = num_apple // 3
    else:
        answer = num_carrot    

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0
    while k - (num_apple + num_carrot + i) > 0:
        if i % 4 == 0:
            answer -= 1
        i = i + 1

    return answer

inputs = list(map(int, input().split()))
print(solution(inputs[0], inputs[1], inputs[2]))
`,
    test_cases: [
      { input: "5 1 2", output: "1" },
      { input: "10 5 4", output: "2" },
      { input: "3 1 1", output: "0" }
    ]
  },
  {
    id: 68,
    classLevel: 2,
    title: "[3차] [문제 8] TV 2대 이상 시청 시간 구하기 (한 줄 수정)",
    type: "code",
    description: "A씨가 하루에 TV를 두 대 이상 틀는 시간을 알아내려 합니다. A씨는 매일 세 프로그램을 시청합니다. 프로그램 방송 시간이 겹칠 때는 TV를 여러 대 켜서 모든 프로그램을 봅니다. 세 프로그램 방영 시작 시각과 끝 시각이 담긴 2차원 배열 programs가 매개변수로 주어질 때, 하루에 TV를 2대 이상 틀는 총 시간을 return 하도록 solution 함수를 작성했습니다. 한 줄만 변경해서 올바르게 동작하도록 수정하세요.",
    input_desc: "3개 프로그램의 시작 및 끝 시각이 순서대로 공백 구분으로 주어집니다. (예: 1 6 3 5 2 8)",
    output_desc: "TV를 2대 이상 시청하는 시간(시간 단위)을 정수로 출력합니다.",
    examples: [
      { input: "1 6 3 5 2 8", output: "4" }
    ],
    starter_code: `def solution(programs):
    answer = 0
    used_tv = [0] * 25

    for program in programs:
        for i in range(program[0], program[1]):
            used_tv[i] = used_tv[i] + 1

    for i in used_tv:
        if i >= 1:
            answer = answer + 1
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
inputs = list(map(int, input().split()))
programs = [[inputs[0], inputs[1]], [inputs[2], inputs[3]], [inputs[4], inputs[5]]]
print(solution(programs))
`,
    solution_code: `# [정답 및 해설]
# 1. used_tv 리스트에 시각별 켜져 있는 TV 개수를 저장했습니다.
# 2. 문제 조건에 맞춰 'TV를 2대 이상 틀어놓는 시간'을 합산해야 하므로, 조건식 if i >= 1: 을 if i >= 2: 로 한 줄 변경해야 합니다.

def solution(programs):
    answer = 0
    used_tv = [0] * 25

    for program in programs:
        for i in range(program[0], program[1]):
            used_tv[i] = used_tv[i] + 1

    for i in used_tv:
        if i >= 2:
            answer = answer + 1
    return answer

inputs = list(map(int, input().split()))
programs = [[inputs[0], inputs[1]], [inputs[2], inputs[3]], [inputs[4], inputs[5]]]
print(solution(programs))
`,
    test_cases: [
      { input: "1 6 3 5 2 8", output: "4" },
      { input: "1 2 2 3 3 4", output: "0" },
      { input: "1 5 1 5 1 5", output: "4" }
    ]
  },
  {
    id: 69,
    classLevel: 2,
    title: "[3차] [문제 9] 차량 2부제 통과 차량수 구하기 (한 줄 수정)",
    type: "code",
    description: "관공서 주차장에서는 차량 2부제를 실시합니다. 차량 2부제는 차량 번호 끝자리가 홀수인 차량은 홀수 일에만, 짝수인 차량은 짝수 일에만 주차장에 들어올 수 있도록 하는 제도입니다. 며칠인지를 나타내는 day와 그날 주차장에 들어오려고 하는 차들의 번호를 담고 있는 배열 numbers가 매개변수로 주어질 때, 주차장에 들어올 수 있는 차량의 수를 return 하도록 solution 함수를 작성했습니다. 코드에서 한 줄만 변경해서 올바르게 동작하도록 수정해주세요.",
    input_desc: "첫 번째 줄에 날짜 day가 주어집니다. 두 번째 줄에 주차장에 입차를 시도하는 차들의 번호 numbers가 공백으로 구분되어 주어집니다.",
    output_desc: "2부제를 위반하지 않고 입차 가능한 차량 대수를 출력합니다.",
    examples: [
      { input: "17\n3285 1724 4438 2988 3131 2998", output: "2" }
    ],
    starter_code: `def solution(day, numbers):
    count = 0
    for number in numbers:
        if number % 2 != day % 2:
            count += 1
    return count

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
day = int(input())
numbers = list(map(int, input().split()))
print(solution(day, numbers))
`,
    solution_code: `# [정답 및 해설]
# 1. 2부제에 따라 날짜의 홀짝 여부(day % 2)와 차량 번호 마지막 자리의 홀짝 여부(number % 2)가 '동일해야' 진입이 허용됩니다.
# 2. 기존 코드는 'number % 2 != day % 2'로 서로 일치하지 않는 경우 카운트하고 있습니다. 이를 일치하는 조건 'number % 2 == day % 2'로 수정해 줍니다.

def solution(day, numbers):
    count = 0
    for number in numbers:
        if number % 2 == day % 2:
            count += 1
    return count

day = int(input())
numbers = list(map(int, input().split()))
print(solution(day, numbers))
`,
    test_cases: [
      { input: "17\n3285 1724 4438 2988 3131 2998", output: "2" },
      { input: "20\n1000 2001 3002", output: "2" },
      { input: "1\n1111 2222 3333 4444", output: "2" }
    ]
  },
  {
    id: 70,
    classLevel: 2,
    title: "[3차] [문제 10] 절반값이 배열에 있는 원소 개수 세기 (한 줄 수정)",
    type: "code",
    description: "배열 원소 중에서 '자신을 2로 나눈 값'이 해당 배열에 똑같이 존재하는 수의 개수를 구하려고 합니다. 예를 들어, 배열이 [4, 8, 3, 6, 7]인 경우, 6 / 2 = 3이고 3이 배열에 존재하며, 8 / 2 = 4이고 4가 배열에 존재하므로 조건에 맞는 수는 총 2개입니다. 숫자가 담긴 배열 arr가 주어졌을 때, 조건에 만족하는 수의 개수를 return 하도록 작성된 코드입니다. 문법적 오류 혹은 논리적 오류가 있는 한 줄만 변경해서 올바르게 동작하도록 수정해주세요.",
    input_desc: "공백으로 구분된 양의 정수 배열 arr가 주어집니다.",
    output_desc: "자신을 2로 나눈 값이 배열 내에 들어있는 수의 총 개수를 출력합니다.",
    examples: [
      { input: "4 8 3 6 7", output: "2" }
    ],
    starter_code: `def solution(arr):
    answer = 0
    for i in arr:
        for i/2 in arr:
            answer += 1
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
arr = list(map(int, input().split()))
print(solution(arr))
`,
    solution_code: `# [정답 및 해설]
# 1. 안쪽 for 루프의 'for i/2 in arr:'는 파이썬에서 문법 오류(SyntaxError)를 발생시킵니다.
# 2. 루프 내에서 조건문을 이용해 i / 2가 배열 arr에 포함되어 있는지(if i / 2 in arr:) 검사하도록 한 줄을 수정해 줍니다.

def solution(arr):
    answer = 0
    for i in arr:
        if i / 2 in arr:
            answer += 1
    return answer

arr = list(map(int, input().split()))
print(solution(arr))
`,
    test_cases: [
      { input: "4 8 3 6 7", output: "2" },
      { input: "10 20 5", output: "2" },
      { input: "1 3 5", output: "0" }
    ]
  },
  {
    id: 71,
    classLevel: 2,
    title: "[4차] [문제 1] 상담실 방문 학생 중 미상담자 구하기 (빈칸 채우기)",
    type: "blank",
    description: "학생 10명이 상담을 받기 위해 매일 한 명씩, 순서대로 상담실을 찾아갑니다. 상담은 상담 선생님이 계실 때에만 받을 수 있습니다. 또한 한번 상담실을 방문한 학생은 다시 상담실에 찾아가지 않습니다. 선생님의 일정표가 주어질 때, 누가 상담을 받지 못했는지 알아내는 프로그램을 작성하려 합니다. 일정표에는 선생님이 있는 날엔 \"O\"가, 없는 날엔 \"X\"가 표시됩니다. 선생님의 일정을 담은 배열 schedule이 매개변수로 주어질 때, 상담을 받지 못한 학생의 번호(1부터 시작)를 오름차순으로 정렬하여 return 하도록 빈칸을 채워 solution 함수를 완성해주세요.",
    input_desc: "선생님의 일정 10개가 공백으로 구분되어 주어집니다. (예: O X X O O O X O X X)",
    output_desc: "상담을 받지 못한 학생들의 번호를 오름차순 정렬한 리스트를 출력하거나 반환합니다.",
    examples: [
      { input: "O X X O O O X O X X", output: "[2, 3, 7, 9, 10]" }
    ],
    starter_code: `def solution(schedule):
    answer = []
    for idx, i in enumerate(schedule):
        if i == @@@:
            answer.append(@@@)
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
schedule = input().split()
print(solution(schedule))
`,
    solution_code: `# [정답 및 해설]
# 1. schedule의 각 날짜(i)를 순회하며 선생님이 계시지 않은 날("X")을 찾습니다: if i == "X":
# 2. 학생의 번호는 1번부터 시작하므로, 인덱스 idx에 1을 더해 추가합니다: answer.append(idx + 1)

def solution(schedule):
    answer = []
    for idx, i in enumerate(schedule):
        if i == "X":
            answer.append(idx + 1)
    return answer

schedule = input().split()
print(solution(schedule))
`,
    test_cases: [
      { input: "O X X O O O X O X X", output: "[2, 3, 7, 9, 10]" },
      { input: "O O O O O O O O O O", output: "[]" },
      { input: "X X X X X X X X X X", output: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" }
    ]
  },
  {
    id: 72,
    classLevel: 2,
    title: "[4차] [문제 2] 체력시험 합격 인원 구하기 (빈칸 채우기)",
    type: "blank",
    description: "체력시험 합격 인원을 알아보려고 합니다. 체력시험 종목으로는 윗몸일으키기, 팔굽혀펴기, 달리기가 있으며 종목별 합격 기준은 다음과 같습니다.\n- 윗몸일으키기: 80점 이상\n- 팔굽혀펴기: 88점 이상\n- 달리기: 70점 이상\n단, 통과한 종목이 1개 이하이거나, 단 한 종목이라도 통과 기준 점수의 반(50%)을 넘기지 못한 종목(과락)이 있다면 불합격입니다. 그 외에는 모두 합격입니다. 이를 위해 다음과 같이 프로그램 구조를 작성했습니다.\n\n1. 통과한 종목이 몇 개인지 셉니다. (func_c)\n2. 통과 점수의 반을 넘기지 못한 종목이 몇 개인지 셉니다. (func_b)\n3. 통과한 종목이 1개보다 많고(2개 이상) 통과 점수의 반을 넘기지 못한 종목이 없으면(0개) 합격 인원으로 셉니다. (func_a)\n\n각 응시자의 종목 기록을 담고 있는 2차원 배열 scores가 매개변수로 주어질 때, 빈칸에 알맞은 함수와 매개변수를 채워 solution 함수를 완성해주세요.",
    input_desc: "첫 번째 줄에 응시자 수가 주어지고, 두 번째 줄부터 각 줄마다 한 응시자의 [윗몸일으키기, 팔굽혀펴기, 달리기] 점수가 공백으로 구분되어 주어집니다.",
    output_desc: "시험에 합격한 총 인원수를 출력하거나 반환합니다.",
    examples: [
      { input: "2\n30 40 100\n97 88 95", output: "1" },
      { input: "6\n90 88 70\n85 90 90\n100 100 70\n30 90 80\n40 10 20\n83 88 80", output: "4" }
    ],
    starter_code: `def func_a(passed, non_passed):
    return ( passed > 1 and non_passed == 0 )

def func_b(scores):
    answer = 0
    if scores[0] < 40:
        answer += 1
    if scores[1] < 44:
        answer += 1
    if scores[2] < 35:
        answer += 1
    return answer

def func_c(scores):
    answer = 0
    if scores[0] >= 80:
        answer += 1
    if scores[1] >= 88:
        answer += 1
    if scores[2] >= 70:
        answer += 1
    return answer

def solution(scores):
    answer = 0
    for my_score in scores:
        passed = func_@@@(@@@)
        non_passed = func_@@@(@@@)
        answer += func_@@@(@@@, @@@)
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
n = int(input())
scores = []
for _ in range(n):
    scores.append(list(map(int, input().split())))
print(solution(scores))
`,
    solution_code: `# [정답 및 해설]
# 1. 통과한 과목 개수를 구하기 위해 func_c(my_score)를 호출합니다.
# 2. 과락 기준(통과 기준 점수의 50% 미만) 과목 개수를 구하기 위해 func_b(my_score)를 호출합니다.
# 3. 최종 합격 여부를 판별하기 위해 func_a(passed, non_passed)를 호출하여 참(True)이면 answer를 1 증가시킵니다.

def func_a(passed, non_passed):
    return ( passed > 1 and non_passed == 0 )

def func_b(scores):
    answer = 0
    if scores[0] < 40:
        answer += 1
    if scores[1] < 44:
        answer += 1
    if scores[2] < 35:
        answer += 1
    return answer

def func_c(scores):
    answer = 0
    if scores[0] >= 80:
        answer += 1
    if scores[1] >= 88:
        answer += 1
    if scores[2] >= 70:
        answer += 1
    return answer

def solution(scores):
    answer = 0
    for my_score in scores:
        passed = func_c(my_score)
        non_passed = func_b(my_score)
        if func_a(passed, non_passed):
            answer += 1
    return answer

n = int(input())
scores = []
for _ in range(n):
    scores.append(list(map(int, input().split())))
print(solution(scores))
`,
    test_cases: [
      { input: "2\n30 40 100\n97 88 95", output: "1" },
      { input: "6\n90 88 70\n85 90 90\n100 100 70\n30 90 80\n40 10 20\n83 88 80", output: "4" }
    ]
  },
  {
    id: 73,
    classLevel: 2,
    title: "[4차] [문제 3] 카드 게임 점수 계산 (빈칸 채우기)",
    type: "blank",
    description: "A와 B가 카드 게임을 할 때, 누가 더 많은 점수를 획득했는지, 또 승리자의 점수는 몇 점인지 알아보려 합니다. 게임 규칙은 다음과 같습니다.\n- 알파벳 'a', 'b', 'c', 'd', 'e'가 적힌 카드뭉치(bundle)가 있습니다.\n- A와 B가 서로 번갈아 가면서 n장씩 카드를 순서대로 뽑습니다. (A가 항상 먼저 뽑습니다.)\n- 알파벳 카드 한 장당 점수는 a = 1점, b = 2점, c = 3점, d = 4점, e = 5점으로 계산하여 합산합니다.\n- 점수가 높은 사람이 승리합니다.\n\n이를 위해 다음과 같이 프로그램 구조를 작성했습니다.\n1. A와 B가 번갈아가며 가져간 카드를 각각 문자열 배열로 분리합니다. (func_a)\n2. A와 B가 각각 획득한 총점수를 구합니다. (func_c)\n3. 승리한 사람의 번호(A는 1, B는 2, 무승부는 0)와 획득한 점수를 순서대로 배열에 담아 return 합니다. (func_b)\n\n뽑아야 하는 카드 개수 n과 카드 뭉치 문자열 bundle이 매개변수로 주어질 때, 빈칸을 알맞게 채워 solution 함수를 완성해주세요.",
    input_desc: "첫 번째 줄에 뽑아야 하는 카드 개수 n이 주어집니다. 두 번째 줄에 카드 뭉치 문자열 bundle이 주어집니다.",
    output_desc: "[이긴 사람의 번호, 승리자의 점수]를 출력하거나 반환합니다.",
    examples: [
      { input: "4\ncacdbdedccbb", output: "[0, 13]" }
    ],
    starter_code: `def func_a(bundle, start):
    return bundle[start::2]

def func_b(score1, score2):
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]

def func_c(bundle):
    answer = 0
    score_per_cards = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5
    }
    for card in bundle:
        answer += score_per_cards[card]
    return answer

def solution(n, bundle):
    a_cards = func_a(@@@, @@@)[:n]
    b_cards = func_a(@@@, @@@)[:n]
    a_score = func_c(@@@)
    b_score = func_c(@@@)
    return func_b(@@@, @@@)

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
n = int(input())
bundle = input()
print(solution(n, bundle))
`,
    solution_code: `# [정답 및 해설]
# 1. A는 첫 번째(인덱스 0)부터 시작해서 번갈아 카드를 가져가므로 func_a(bundle, 0)을 통해 카드 슬라이싱을 진행합니다.
# 2. B는 두 번째(인덱스 1)부터 시작하므로 func_a(bundle, 1)을 호출합니다.
# 3. A와 B 각각의 점수를 합산하기 위해 func_c(a_cards), func_c(b_cards)를 호출합니다.
# 4. 최종적으로 두 선수의 점수를 대조하기 위해 func_b(a_score, b_score)의 판정 값을 반환합니다.

def func_a(bundle, start):
    return bundle[start::2]

def func_b(score1, score2):
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]

def func_c(bundle):
    answer = 0
    score_per_cards = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5
    }
    for card in bundle:
        answer += score_per_cards[card]
    return answer

def solution(n, bundle):
    a_cards = func_a(bundle, 0)[:n]
    b_cards = func_a(bundle, 1)[:n]
    a_score = func_c(a_cards)
    b_score = func_c(b_cards)
    return func_b(a_score, b_score)

n = int(input())
bundle = input()
print(solution(n, bundle))
`,
    test_cases: [
      { input: "4\ncacdbdedccbb", output: "[0, 13]" },
      { input: "3\nabcde", output: "[1, 4]" }
    ]
  },
  {
    id: 74,
    classLevel: 2,
    title: "[4차] [문제 4] 필요한 총 조교 수 구하기 (빈칸 채우기)",
    type: "blank",
    description: "프로그래밍 수업 n개를 동시에 진행할 때, 필요한 총 조교 수를 알아보려고 합니다. 조교 1명이 최대 m명의 학생을 담당할 수 있으며, 각 교실별로 필요한 조교 수를 구한 뒤 모두 더해야 합니다. (예를 들어 한 반에 학생이 33명이고 m=30이면 조교는 2명이 필요합니다.) 교실별 학생 수가 담긴 배열 classes와 조교 1명이 담당하는 학생 수 m이 주어질 때, 빈칸 연산자를 알맞게 채워 총 조교 수를 return 하는 solution 함수를 완성해주세요.",
    input_desc: "첫 번째 줄에 교실별 학생 수가 공백으로 구분되어 주어집니다. 두 번째 줄에 조교 1명이 담당할 수 있는 학생 수 m이 주어집니다.",
    output_desc: "필요한 총 조교 수를 출력하거나 반환합니다.",
    examples: [
      { input: "80 45 33 20\n30", output: "8" }
    ],
    starter_code: `def solution(classes, m):
    answer = 0
    for students in classes:
        answer += students @@@ m
        if students @@@ m != 0:
            answer += 1
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
classes = list(map(int, input().split()))
m = int(input())
print(solution(classes, m))
`,
    solution_code: `# [정답 및 해설]
# 1. 학생 수(students)를 m으로 나눈 몫(//)만큼의 조교 수가 기본적으로 필요하므로: answer += students // m
# 2. m명으로 똑떨어지지 않는 나머지 학생이 존재할 경우(나머지 % 연산자 결과가 0이 아닐 때) 조교 1명을 더 배치합니다: if students % m != 0:

def solution(classes, m):
    answer = 0
    for students in classes:
        answer += students // m
        if students % m != 0:
            answer += 1
    return answer

classes = list(map(int, input().split()))
m = int(input())
print(solution(classes, m))
`,
    test_cases: [
      { input: "80 45 33 20\n30", output: "8" },
      { input: "30 60 90\n30", output: "6" }
    ]
  },
  {
    id: 75,
    classLevel: 2,
    title: "[4차] [문제 5] 다이어트 소모 열량 계산 (한 줄 수정)",
    type: "code",
    description: "다이어트를 하는 A 씨는 오늘 먹은 식단의 열량이 그동안(오늘 전까지) 먹은 식단의 열량 중 최솟값보다 큰 경우, 운동을 하여 그 차이만큼의 열량을 소모합니다. 식단의 열량이 날짜순으로 담긴 배열 calorie가 매개변수로 주어질 때, 운동으로 소모하는 총열량을 구하도록 작성된 소스코드입니다. 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.",
    input_desc: "식단의 일자별 열량이 공백으로 구분되어 한 줄로 주어집니다.",
    output_desc: "운동으로 소모하는 총 열량을 출력하거나 반환합니다.",
    examples: [
      { input: "713 665 873 500 751", output: "459" }
    ],
    starter_code: `def solution(calorie):
    min_cal = 0
    answer = 0
    for cal in calorie:
        if cal > min_cal:
            answer += cal - min_cal
        min_cal = min(min_cal, cal)
    return answer

# 아래 코드는 실행을 돕기 위한 입출력 코드입니다. 수정하지 마세요.
calorie = list(map(int, input().split()))
print(solution(calorie))
`,
    solution_code: `# [정답 및 해설]
# 1. 최솟값을 0으로 설정하면, 입력 식단 열량이 항상 0보다 크므로 첫 번째 날부터 잘못된 운동 칼로리 누적이 일어납니다.
# 2. 따라서, 이전 최솟값의 기준을 무한대(float('inf')) 혹은 매우 큰 값, 또는 첫날 열량 값 등으로 초기화해주어야 올바르게 소모량을 연산할 수 있습니다.
# 3. min_cal = float('inf') 로 초기 설정 한 줄을 수정해 줍니다.

def solution(calorie):
    min_cal = float('inf')
    answer = 0
    for cal in calorie:
        if cal > min_cal:
            answer += cal - min_cal
        min_cal = min(min_cal, cal)
    return answer

calorie = list(map(int, input().split()))
print(solution(calorie))
`,
    test_cases: [
      { input: "713 665 873 500 751", output: "459" },
      { input: "100 200 300", output: "300" }
    ]
  }
];




