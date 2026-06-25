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
      { input: "11\n0 5 7 2 2 1 9 2 1 6 5", output: "1\n2\n3\n0\n0\n1\n1\n1\n0\n1" }
    ],
    starter_code: `# 여기에 코드를 작성하세요.
`,
    test_cases: [
      { input: "11\n0 5 7 2 2 1 9 2 1 6 5", output: "1\n2\n3\n0\n0\n1\n1\n1\n0\n1" }
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
      { input: "40", output: "22" },
      { input: "10", output: "3" },
      { input: "15", output: "5" }
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
  }
];


