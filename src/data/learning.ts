// Mock Database Data
export const mockDb = {
  students: [
    { id: 1, name: "김철수", grade: 3, math_score: 85, eng_score: 90 },
    { id: 2, name: "이영희", grade: 2, math_score: 92, eng_score: 88 },
    { id: 3, name: "박민수", grade: 3, math_score: 78, eng_score: 85 },
    { id: 4, name: "최지우", grade: 1, math_score: 88, eng_score: 92 },
    { id: 5, name: "정다은", grade: 2, math_score: 95, eng_score: 89 }
  ],
  employees: [
    { emp_id: 101, name: "홍길동", dept_id: 10, salary: 3500000 },
    { emp_id: 102, name: "이순신", dept_id: 20, salary: 4500000 },
    { emp_id: 103, name: "강감찬", dept_id: 10, salary: 3800000 },
    { emp_id: 104, name: "장보고", dept_id: 30, salary: 5000000 },
    { emp_id: 105, name: "유관순", dept_id: 20, salary: 4200000 }
  ],
  departments: [
    { dept_id: 10, dept_name: "개발팀" },
    { dept_id: 20, dept_name: "인사팀" },
    { dept_id: 30, dept_name: "영업팀" }
  ]
};

export interface SqlResult {
  columns: string[];
  rows: any[][];
  error?: string;
}

// A simple client-side SQL parser and engine
export function runMockSQL(query: string): SqlResult {
  try {
    const normalized = query.trim().replace(/\s+/g, " ");
    const selectMatch = normalized.match(/SELECT\s+(.+?)\s+FROM\s+(\w+)(?:\s+(?:AS\s+)?\w+)?(?:\s+JOIN\s+(\w+)(?:\s+(?:AS\s+)?\w+)?\s+ON\s+([\w.]+)\s*=\s*([\w.]+))?(?:\s+WHERE\s+(.+?))?(?:\s+GROUP\s+BY\s+(.+?))?(?:\s+ORDER\s+BY\s+(.+?))?(?:\s+LIMIT\s+(\d+))?$/i);

    if (!selectMatch) {
      // Let's try parsing simpler query or throw custom error
      if (!normalized.toUpperCase().startsWith("SELECT")) {
        return { columns: [], rows: [], error: "SELECT 문만 지원합니다." };
      }
      return { columns: [], rows: [], error: "SQL 구문 분석 실패. 지원하지 않는 문법이 포함되어 있거나 괄호/키워드 형태를 확인하세요." };
    }

    const selectColsStr = selectMatch[1].trim();
    const primaryTable = selectMatch[2].trim().toLowerCase();
    const joinTable = selectMatch[3] ? selectMatch[3].trim().toLowerCase() : null;
    const joinCol1 = selectMatch[4] ? selectMatch[4].trim() : null;
    const joinCol2 = selectMatch[5] ? selectMatch[5].trim() : null;
    const whereStr = selectMatch[6] ? selectMatch[6].trim() : null;
    const groupByStr = selectMatch[7] ? selectMatch[7].trim() : null;
    const orderByStr = selectMatch[8] ? selectMatch[8].trim() : null;
    const limitStr = selectMatch[9] ? selectMatch[9].trim() : null;

    if (!(primaryTable in mockDb)) {
      return { columns: [], rows: [], error: `테이블 '${primaryTable}'을(를) 찾을 수 없습니다.` };
    }

    let dataset: any[] = JSON.parse(JSON.stringify((mockDb as any)[primaryTable]));

    // Perform JOIN
    if (joinTable) {
      if (!(joinTable in mockDb)) {
        return { columns: [], rows: [], error: `조인 대상 테이블 '${joinTable}'을(를) 찾을 수 없습니다.` };
      }
      const joinDataset = (mockDb as any)[joinTable];
      const joined: any[] = [];

      dataset.forEach(row => {
        joinDataset.forEach((joinRow: any) => {
          // Check join condition (e.g. e.dept_id = d.dept_id or dept_id = dept_id)
          const getVal = (r1: any, r2: any, col: string) => {
            const cleanCol = col.split(".").pop() || "";
            if (col.startsWith("e.") || col.startsWith("employees.")) return r1[cleanCol] !== undefined ? r1[cleanCol] : r2[cleanCol];
            if (col.startsWith("d.") || col.startsWith("departments.")) return r2[cleanCol] !== undefined ? r2[cleanCol] : r1[cleanCol];
            return r1[cleanCol] !== undefined ? r1[cleanCol] : r2[cleanCol];
          };

          const val1 = getVal(row, joinRow, joinCol1 || "");
          const val2 = getVal(row, joinRow, joinCol2 || "");

          if (val1 !== undefined && val2 !== undefined && val1 === val2) {
            joined.push({ ...row, ...joinRow });
          }
        });
      });
      dataset = joined;
    }

    // Apply WHERE clause
    if (whereStr) {
      dataset = dataset.filter(row => {
        // Simple expression parser
        // Supports: grade = 3, math_score >= 80, salary >= 4000000, etc.
        const matches = whereStr.match(/([\w.+()-]+)\s*(=|>=|<=|>|<|!=)\s*(.+)/i);
        if (!matches) return true;

        let col = matches[1].trim();
        const op = matches[2].trim();
        let valStr = matches[3].trim().replace(/['"]/g, "");

        // Remove aliases from column name (e.g., e.dept_id -> dept_id)
        if (col.includes(".")) {
          col = col.split(".").pop() || col;
        }

        let rowVal = row[col];
        if (rowVal === undefined) {
          // Check if expression like math_score + eng_score
          if (col.includes("+")) {
            const parts = col.split("+").map(p => p.trim());
            rowVal = (row[parts[0]] || 0) + (row[parts[1]] || 0);
          } else {
            return true;
          }
        }

        const compVal = isNaN(Number(valStr)) ? valStr : Number(valStr);

        switch (op) {
          case "=": return rowVal == compVal;
          case ">=": return rowVal >= compVal;
          case "<=": return rowVal <= compVal;
          case ">": return rowVal > compVal;
          case "<": return rowVal < compVal;
          case "!=": return rowVal != compVal;
          default: return true;
        }
      });
    }

    // Apply GROUP BY & aggregation
    let finalColumns: string[] = [];
    let finalRows: any[][] = [];

    // Helper to evaluate columns in a row
    const evalColumns = (row: any, colStr: string): { name: string, value: any }[] => {
      const parsedCols = colStr.split(",").map(c => c.trim());
      return parsedCols.map(c => {
        let name = c;
        let value = null;
        let cleanCol = c;
        if (c.toUpperCase().includes(" AS ")) {
          const parts = c.split(/ AS /i);
          cleanCol = parts[0].trim();
          name = parts[1].trim().replace(/['"]/g, "");
        }

        if (cleanCol.includes(".")) {
          cleanCol = cleanCol.split(".").pop() || cleanCol;
        }

        if (cleanCol === "*") {
          return { name: "*", value: row }; // special case handled below
        }

        if (row[cleanCol] !== undefined) {
          value = row[cleanCol];
        } else if (cleanCol.includes("+")) {
          const parts = cleanCol.split("+").map(p => p.trim());
          value = (row[parts[0]] || 0) + (row[parts[1]] || 0);
        }
        return { name, value };
      });
    };

    if (groupByStr) {
      let groupCol = groupByStr.trim();
      if (groupCol.includes(".")) {
        groupCol = groupCol.split(".").pop() || groupCol;
      }

      // Group records
      const groups: Record<any, any[]> = {};
      dataset.forEach(row => {
        const key = row[groupCol];
        if (!groups[key]) groups[key] = [];
        groups[key].push(row);
      });

      // For each group, construct one row
      const selectParts = selectColsStr.split(",").map(c => c.trim());
      finalColumns = selectParts.map(c => {
        if (c.toUpperCase().includes(" AS ")) {
          return c.split(/ AS /i)[1].trim().replace(/['"]/g, "");
        }
        return c;
      });

      Object.keys(groups).forEach(key => {
        const rowsInGroup = groups[key];
        const newRow = selectParts.map(colExpr => {
          let expr = colExpr;
          if (expr.toUpperCase().includes(" AS ")) {
            expr = expr.split(/ AS /i)[0].trim();
          }
          if (expr.includes(".")) {
            expr = expr.split(".").pop() || expr;
          }

          if (expr === groupCol) {
            return rowsInGroup[0][groupCol];
          }

          // Aggregate functions
          const aggMatch = expr.match(/(COUNT|AVG|SUM|MAX|MIN)\((.+?)\)/i);
          if (aggMatch) {
            const func = aggMatch[1].toUpperCase();
            let aggCol = aggMatch[2].trim();
            if (aggCol.includes(".")) {
              aggCol = aggCol.split(".").pop() || aggCol;
            }

            if (func === "COUNT") {
              return rowsInGroup.length;
            }

            const vals = rowsInGroup.map(r => Number(r[aggCol])).filter(v => !isNaN(v));
            if (vals.length === 0) return null;

            if (func === "SUM") return vals.reduce((a, b) => a + b, 0);
            if (func === "AVG") return Math.round((vals.reduce((a, b) => a + b, 0) / vals.length) * 10) / 10;
            if (func === "MAX") return Math.max(...vals);
            if (func === "MIN") return Math.min(...vals);
          }
          return rowsInGroup[0][expr];
        });
        finalRows.push(newRow);
      });

    } else {
      // Check if global aggregates are used (e.g. SELECT COUNT(*), AVG(salary))
      const hasAggregate = selectColsStr.match(/(COUNT|AVG|SUM|MAX|MIN)\(/i);

      if (hasAggregate) {
        const selectParts = selectColsStr.split(",").map(c => c.trim());
        finalColumns = selectParts.map(c => {
          if (c.toUpperCase().includes(" AS ")) {
            return c.split(/ AS /i)[1].trim().replace(/['"]/g, "");
          }
          return c;
        });

        const newRow = selectParts.map(colExpr => {
          let expr = colExpr;
          if (expr.toUpperCase().includes(" AS ")) {
            expr = expr.split(/ AS /i)[0].trim();
          }
          if (expr.includes(".")) {
            expr = expr.split(".").pop() || expr;
          }

          const aggMatch = expr.match(/(COUNT|AVG|SUM|MAX|MIN)\((.+?)\)/i);
          if (aggMatch) {
            const func = aggMatch[1].toUpperCase();
            let aggCol = aggMatch[2].trim();
            if (aggCol.includes(".")) {
              aggCol = aggCol.split(".").pop() || aggCol;
            }

            if (func === "COUNT") {
              return dataset.length;
            }

            const vals = dataset.map(r => Number(r[aggCol])).filter(v => !isNaN(v));
            if (vals.length === 0) return null;

            if (func === "SUM") return vals.reduce((a, b) => a + b, 0);
            if (func === "AVG") return Math.round((vals.reduce((a, b) => a + b, 0) / vals.length) * 10) / 10;
            if (func === "MAX") return Math.max(...vals);
            if (func === "MIN") return Math.min(...vals);
          }
          return null;
        });
        finalRows.push(newRow);
      } else {
        // Plain SELECT without GROUP BY
        dataset.forEach(row => {
          if (selectColsStr === "*") {
            if (finalColumns.length === 0) {
              finalColumns = Object.keys(row);
            }
            finalRows.push(Object.values(row));
          } else {
            const evaluated = evalColumns(row, selectColsStr);
            if (finalColumns.length === 0) {
              finalColumns = evaluated.map(e => e.name);
            }
            finalRows.push(evaluated.map(e => e.value));
          }
        });
      }
    }

    // Apply ORDER BY
    if (orderByStr) {
      const parts = orderByStr.trim().split(/\s+/);
      let orderCol = parts[0];
      if (orderCol.includes(".")) {
        orderCol = orderCol.split(".").pop() || orderCol;
      }
      const dir = parts[1] ? parts[1].toUpperCase() : "ASC";
      
      const colIdx = finalColumns.findIndex(c => c.toLowerCase() === orderCol.toLowerCase() || c.toLowerCase().includes(orderCol.toLowerCase()));
      if (colIdx !== -1) {
        finalRows.sort((a, b) => {
          const valA = a[colIdx];
          const valB = b[colIdx];
          if (valA === valB) return 0;
          if (valA === null) return 1;
          if (valB === null) return -1;
          if (typeof valA === "number" && typeof valB === "number") {
            return dir === "DESC" ? valB - valA : valA - valB;
          }
          return dir === "DESC" 
            ? String(valB).localeCompare(String(valA)) 
            : String(valA).localeCompare(String(valB));
        });
      }
    }

    // Apply LIMIT
    if (limitStr) {
      const limit = parseInt(limitStr, 10);
      if (!isNaN(limit)) {
        finalRows = finalRows.slice(0, limit);
      }
    }

    return { columns: finalColumns, rows: finalRows };
  } catch (err: any) {
    return { columns: [], rows: [], error: err.message || "SQL 실행 도중 예기치 못한 에러가 발생했습니다." };
  }
}

// Concepts Data for Python
export const pythonConcepts = [
  {
    id: 1,
    title: "1. 변수와 연산자 (Variables & Operators)",
    desc: "변수 선언법과 산술, 비교, 논리 연산자",
    content: `파이썬에서 변수는 값을 저장하는 공간입니다. 별도의 타입 선언 없이 값을 대입하는 순간 변수가 생성되고 타입이 결정됩니다.

### 산술 연산자
* \`+\` : 더하기
* \`-\` : 빼기
* \`*\` : 곱하기
* \`/\` : 나누기 (소수점 포함 결과 반환)
* \`//\` : 몫 (소수점 버림)
* \`%\` : 나머지 (나눈 나머지 값 반환)
* \`**\` : 거듭제곱

### 예제 코드
\`\`\`python
a = 10
b = 3

print(a + b)  # 13
print(a // b) # 3 (몫)
print(a % b)  # 1 (나머지)
print(a ** b) # 1000 (10의 3승)
\`\`\``
  },
  {
    id: 2,
    title: "2. 조건문 (Conditionals)",
    desc: "if, elif, else를 사용한 흐름 제어",
    content: `조건문은 프로그램의 흐름을 분기할 때 사용합니다. 파이썬은 들여쓰기(Indentation)를 사용하여 코드 블록을 구분하므로 들여쓰기 규칙을 반드시 준수해야 합니다.

### 문법 구조
\`\`\`python
if 조건식1:
    # 조건식1이 참일 때 실행
elif 조건식2:
    # 조건식1이 거짓이고 조건식2가 참일 때 실행
else:
    # 위 조건이 모두 거짓일 때 실행
\`\`\`

### 예제 코드
\`\`\`python
score = 85

if score >= 90:
    print("A 학점")
elif score >= 80:
    print("B 학점")
else:
    print("C 학점")
# 결과: B 학점
\`\`\``
  },
  {
    id: 3,
    title: "3. 반복문 (Loops)",
    desc: "for, while 루프와 range() 함수 활용",
    content: `반복문은 동일하거나 유사한 작업을 반복 수행할 때 사용합니다.

### for 문과 range()
\`range(start, stop, step)\` 함수는 특정 범위의 숫자 시퀀스를 생성합니다.
* \`range(5)\` : 0부터 4까지 (5개)
* \`range(1, 6)\` : 1부터 5까지
* \`range(1, 10, 2)\` : 1부터 9까지 2씩 증가

### 예제 코드 (for 문)
\`\`\`python
# 1부터 5까지의 합 구하기
total = 0
for i in range(1, 6):
    total += i
print("합계:", total) # 합계: 15
\`\`\`

### 예제 코드 (while 문)
\`\`\`python
count = 0
while count < 3:
    print("hello")
    count += 1
\`\`\``
  },
  {
    id: 4,
    title: "4. 리스트 (Lists)",
    desc: "인덱싱, 슬라이싱, 주요 리스트 메서드",
    content: `리스트는 여러 값을 순서대로 저장하는 자료구조입니다. 다른 타입의 데이터를 섞어서 저장할 수도 있습니다.

### 주요 기능
* **인덱싱**: \`lst[0]\` (첫 번째 요소)
* **슬라이싱**: \`lst[1:4]\` (인덱스 1부터 3까지 추출)
* **요소 추가**: \`lst.append(value)\`
* **요소 제거**: \`lst.remove(value)\` 또는 \`del lst[index]\`
* **정렬**: \`lst.sort()\` (오름차순)

### 예제 코드
\`\`\`python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits) # ['apple', 'banana', 'cherry']

numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers) # [1, 1, 3, 4, 5]
\`\`\``
  },
  {
    id: 5,
    title: "5. 사용자 정의 함수 (Functions)",
    desc: "def 예약어를 통한 함수 정의와 반환값 처리",
    content: `함수는 코드의 재사용성을 높이기 위해 특정 코드를 블록으로 묶어 이름을 붙인 것입니다.

### 문법 구조
\`\`\`python
def 함수이름(매개변수1, 매개변수2):
    # 수행할 문장
    return 결과값
\`\`\`

### 예제 코드
\`\`\`python
def add_and_mul(a, b):
    sum_val = a + b
    mul_val = a * b
    return sum_val, mul_val # 튜플 형태로 복수 반환 가능

s, m = add_and_mul(3, 5)
print("합:", s, "곱:", m) # 합: 8 곱: 15
\`\`\``
  },
  {
    id: 6,
    title: "6. 문자열 처리 (Strings)",
    desc: "문자열 인덱싱, 슬라이싱 및 주요 메서드",
    content: `파이썬에서 문자열은 변경 불가능(Immutable)한 시퀀스 자료형입니다.

### 주요 메서드
* \`len(str)\`: 문자열 길이 반환
* \`str.upper()\` / \`str.lower()\`: 대/소문자 변환
* \`str.split(separator)\`: 구분자를 기준으로 리스트로 분할
* \`str.replace(old, new)\`: 문자열 치환
* \`str.count(sub)\`: 특정 문자나 문자열의 개수 카운트

### 예제 코드
\`\`\`python
text = "Python Programming"
print(len(text))          # 18
print(text[0:6])          # Python
print(text.lower())       # python programming
print("apple,banana".split(",")) # ['apple', 'banana']
\`\`\``
  },
  {
    id: 7,
    title: "7. 내장 함수와 모듈 (Builtins & Modules)",
    desc: "자주 쓰이는 내장 함수와 모듈 활용법",
    content: `파이썬은 수많은 유용한 내장 함수와 표준 라이브러리(모듈)를 기본 제공합니다.

### 주요 내장 함수
* \`sum(iterable)\`: 합계 계산
* \`min()\` / \`max()\`: 최솟값 / 최댓값 반환
* \`abs(x)\`: 절대값 반환
* \`sorted(iterable)\`: 정렬된 새 리스트 반환

### 표준 모듈 가져오기 (math)
\`\`\`python
import math

print(math.ceil(3.14))  # 4 (올림)
print(math.floor(3.14)) # 3 (내림)
print(math.sqrt(16))    # 4.0 (제곱근)
\`\`\``
  }
];

// SQL Basic Lessons/Missions
export const sqlBasicLessons = [
  {
    id: 1,
    title: "기초 1: 모든 학생 데이터 조회",
    desc: "students 테이블의 모든 컬럼과 모든 행을 조회해보세요.",
    table: "students",
    hint: "SELECT * FROM 테이블명",
    starterQuery: "SELECT * FROM students;",
    correctQuery: "SELECT * FROM students;"
  },
  {
    id: 2,
    title: "기초 2: 특정 학년 학생 조회",
    desc: "3학년(grade = 3)에 재학 중인 학생들의 이름(name)과 수학 점수(math_score)를 조회해보세요.",
    table: "students",
    hint: "SELECT name, math_score FROM students WHERE grade = 3;",
    starterQuery: "SELECT name, math_score FROM students WHERE grade = 3;",
    correctQuery: "SELECT name, math_score FROM students WHERE grade = 3;"
  },
  {
    id: 3,
    title: "기초 3: 정렬을 이용한 학생 정렬",
    desc: "수학 점수가 80점 이상인 학생들을 조회하되, 영어 점수(eng_score)가 높은 순서(내림차순, DESC)로 정렬하여 조회해보세요.",
    table: "students",
    hint: "ORDER BY 컬럼명 DESC",
    starterQuery: "SELECT * FROM students WHERE math_score >= 80 ORDER BY eng_score DESC;",
    correctQuery: "SELECT * FROM students WHERE math_score >= 80 ORDER BY eng_score DESC;"
  },
  {
    id: 4,
    title: "기초 4: 수학 성적 우수자 제한 조회",
    desc: "수학 점수가 높은 순으로 정렬하여 상위 2명의 학생 레코드 전체를 조회해보세요.",
    table: "students",
    hint: "ORDER BY math_score DESC LIMIT 2",
    starterQuery: "SELECT * FROM students ORDER BY math_score DESC LIMIT 2;",
    correctQuery: "SELECT * FROM students ORDER BY math_score DESC LIMIT 2;"
  },
  {
    id: 5,
    title: "기초 5: 수학과 영어 성적 합산",
    desc: "수학 점수와 영어 점수의 합이 180점 이상인 학생들의 이름(name)과 총점(math_score + eng_score)을 'total_score'라는 별칭(AS)으로 조회해보세요.",
    table: "students",
    hint: "SELECT name, (math_score + eng_score) AS total_score FROM students WHERE (math_score + eng_score) >= 180",
    starterQuery: "SELECT name, (math_score + eng_score) AS total_score FROM students WHERE math_score + eng_score >= 180;",
    correctQuery: "SELECT name, (math_score + eng_score) AS total_score FROM students WHERE math_score + eng_score >= 180;"
  }
];

// SQL Advanced Lessons/Missions
export const sqlAdvancedLessons = [
  {
    id: 1,
    title: "심화 1: 부서별 평균 급여 계산",
    desc: "employees 테이블에서 부서 번호(dept_id)별 평균 급여(salary)를 구해보세요. 평균 급여 컬럼은 'avg_salary'로 이름 지어주세요.",
    table: "employees",
    hint: "SELECT dept_id, AVG(salary) AS avg_salary FROM employees GROUP BY dept_id",
    starterQuery: "SELECT dept_id, AVG(salary) AS avg_salary FROM employees GROUP BY dept_id;",
    correctQuery: "SELECT dept_id, AVG(salary) AS avg_salary FROM employees GROUP BY dept_id;"
  },
  {
    id: 2,
    title: "심화 2: 직원과 부서 조인(JOIN)",
    desc: "급여가 400만원(4000000) 이상인 사원들의 사원 이름(name)과 그 사원이 소속된 부서 이름(dept_name)을 조회해 보세요. (employees e JOIN departments d ON e.dept_id = d.dept_id)",
    table: "employees",
    hint: "SELECT e.name, d.dept_name FROM employees e JOIN departments d ON e.dept_id = d.dept_id WHERE e.salary >= 4000000",
    starterQuery: "SELECT e.name, d.dept_name FROM employees e JOIN departments d ON e.dept_id = d.dept_id WHERE e.salary >= 4000000;",
    correctQuery: "SELECT e.name, d.dept_name FROM employees e JOIN departments d ON e.dept_id = d.dept_id WHERE e.salary >= 4000000;"
  },
  {
    id: 3,
    title: "심화 3: 전체 사원 집계",
    desc: "employees 테이블에서 전체 사원 수(COUNT(*))를 'emp_count'로, 평균 급여(AVG(salary))를 'avg_salary'로 각각 구하는 쿼리를 작성하세요.",
    table: "employees",
    hint: "SELECT COUNT(*) AS emp_count, AVG(salary) AS avg_salary FROM employees",
    starterQuery: "SELECT COUNT(*) AS emp_count, AVG(salary) AS avg_salary FROM employees;",
    correctQuery: "SELECT COUNT(*) AS emp_count, AVG(salary) AS avg_salary FROM employees;"
  },
  {
    id: 4,
    title: "심화 4: 소속 인원이 많은 부서 조회",
    desc: "부서 번호(dept_id)별 사원 수를 구하되, 소속된 사원이 2명 이상인 부서만 조회해보세요. 사원 수는 'emp_count'로 표시하세요.",
    table: "employees",
    hint: "SELECT dept_id, COUNT(*) AS emp_count FROM employees GROUP BY dept_id HAVING emp_count >= 2 (또는 해석 엔진에서 부서별 개수 조회)",
    starterQuery: "SELECT dept_id, COUNT(*) AS emp_count FROM employees GROUP BY dept_id HAVING COUNT(*) >= 2;",
    correctQuery: "SELECT dept_id, COUNT(*) AS emp_count FROM employees GROUP BY dept_id HAVING COUNT(*) >= 2;"
  }
];
