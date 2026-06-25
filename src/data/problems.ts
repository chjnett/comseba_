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
}

export const problems: Problem[] = [
  {
    id: 1,
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

print(hap)
print( @@@ )
`,
    solution_code: `# [정답 및 해설]
# 1. arr배열을 반복하면서 총합(hap)에 누적합니다. (for x in arr)
# 2. hap에 x를 누적합니다. (hap += x)
# 3. 평균을 소수 첫째자리까지 출력하기 위해 f-string 포맷인 :.1f를 사용합니다. (f"{hap/n:.1f}")

n = int(input(""))
arr= []
arr = input().split()

hap = 0
avg = 0

for i in range(n):
    arr[i] = int(arr[i])

for x in arr:
    hap += x

print(hap)
print(f"{hap/n:.1f}")
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
  }
];
