"use client";

import React, { useState, useEffect, useRef } from "react";
import Script from "next/script";
import Editor, { loader } from "@monaco-editor/react";

// Pre-configure Monaco editor path to fetch reliably from official CDN and avoid loader errors
if (typeof window !== "undefined") {
  loader.config({
    paths: {
      vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.43.0/min/vs"
    }
  });
}
import { 
  Play, 
  Send, 
  RotateCcw, 
  Plus, 
  CheckCircle2, 
  AlertTriangle, 
  HelpCircle, 
  Terminal, 
  Code,
  Check,
  Copy,
  ChevronRight,
  BookOpen,
  X,
  FileCode2,
  Search,
  PanelLeftClose,
  PanelLeftOpen,
  ArrowLeft,
  Database,
  Sparkles,
  Sun,
  Moon
} from "lucide-react";
import { problems as initialProblems, Problem, Example } from "@/data/problems";
import { 
  mockDb, 
  runMockSQL, 
  pythonConcepts, 
  sqlBasicLessons, 
  sqlAdvancedLessons 
} from "@/data/learning";

// Helper to sanitize python inputs for builtin.input mock
function preparePythonRunner(code: string, inputLines: string[]): string {
  const jsonInputs = JSON.stringify(inputLines);
  const escapedCode = JSON.stringify(code);
  return `
import builtins
import json
import sys
import io

_inputs = json.loads('''${jsonInputs}''')
_input_idx = 0

def _mock_input(prompt=''):
    global _input_idx
    if _input_idx < len(_inputs):
        _val = _inputs[_input_idx]
        _input_idx += 1
        return _val
    raise EOFError("EOF when reading a line")

builtins.input = _mock_input

_orig_stdout = sys.stdout
sys.stdout = io.StringIO()

try:
    exec(${escapedCode}, globals())
finally:
    _captured_stdout = sys.stdout.getvalue()
    sys.stdout = _orig_stdout
`;
}

function getConceptSummaryForProblem(prob: Problem): { title: string; points: string[]; code: string } {
  const id = prob.id;

  if (id === 1 || id === 11 || id === 25) {
    return {
      title: "변수 및 연산자 (몫과 나머지)",
      points: [
        "변수는 값을 저장하는 상자입니다. 파이썬은 변수 선언 시 타입을 명시하지 않습니다.",
        "// 연산자는 나눗셈의 '몫'을 구하고, % 연산자는 나눗셈의 '나머지'를 구합니다.",
        "수 계산식이나 조건 판단(예: 짝수/홀수 판별, 배수 확인)에서 매우 빈번하게 사용됩니다."
      ],
      code: "a = 10\nb = 3\nprint(a // b) # 3 (몫)\nprint(a % b)  # 1 (나머지)"
    };
  }
  
  if (id === 5 || id === 6 || id === 15 || id === 16 || id === 23 || id === 35 || id === 42) {
    return {
      title: "조건문 (if-elif-else)",
      points: [
        "특정 조건이 참(True)인지 거짓(False)인지에 따라 실행 흐름을 제어합니다.",
        "elif와 else를 조합하여 다중 분기를 만들 수 있습니다.",
        "들여쓰기(Indentation) 규칙에 매우 민감하므로 공백 4칸 또는 탭을 일관되게 적용해야 합니다."
      ],
      code: "score = 85\nif score >= 90:\n    print('A')\nelif score >= 80:\n    print('B')\nelse:\n    print('C')"
    };
  }

  if (id === 3 || id === 13 || id === 17 || id === 21 || id === 24 || id === 33 || id === 36 || id === 37 || id === 38 || id === 46) {
    return {
      title: "반복문 (for & range)",
      points: [
        "range(start, stop, step) 함수를 사용하여 원하는 횟수만큼 루프를 돌릴 수 있습니다.",
        "stop 값은 범위에 포함되지 않으므로 주의해야 합니다. (예: range(1, 5)는 1부터 4까지)",
        "별 출력, 특정 구간 숫자 합산, 구구단 출력 등 반복 처리가 필요한 모든 곳에 쓰입니다."
      ],
      code: "total = 0\nfor i in range(1, 6): # 1부터 5까지\n    total += i\nprint(total) # 15"
    };
  }

  if (id === 2 || id === 4 || id === 10 || id === 12 || id === 14 || id === 26 || id === 27 || id === 48 || id === 49) {
    return {
      title: "문자열 다루기 & 슬라이싱",
      points: [
        "문자열은 변경 불가능(immutable)하므로 특정 위치를 직접 바꿀 수 없습니다 (예: s[0] = 'X' 에러).",
        "s[::-1] 처럼 슬라이싱을 이용해 문자열을 쉽게 뒤집을 수 있어 팰린드롬 판별 등에 유용합니다.",
        "join(), count(), upper(), lower(), replace() 등의 문자열 내장 함수를 활용하세요."
      ],
      code: "s = 'hello'\nprint(s[::-1])     # 'olleh'\nprint(s.count('l')) # 2\n# 수정 시 리스트 변환 필수:\nlst = list(s)\nlst[0] = 'H'\ns = ''.join(lst) # 'Hello'"
    };
  }

  if (id === 8 || id === 9 || id === 18 || id === 19 || id === 20 || id === 29 || id === 34 || id === 39 || id === 40 || id === 41 || id === 45 || id === 50) {
    return {
      title: "리스트 다루기 & 투 포인터",
      points: [
        "리스트는 순서가 있고 가변적(mutable)인 파이썬의 핵심 자료 구조입니다.",
        "append(), insert(), pop(), remove() 함수로 리스트를 수정합니다.",
        "투 포인터(Two Pointer)는 left, right 인덱스를 좁혀가며 스왑하거나 탐색할 때 사용됩니다."
      ],
      code: "arr = [1, 2, 3]\narr.append(4)  # [1, 2, 3, 4]\narr.reverse()  # [4, 3, 2, 1]\n\n# 투 포인터 뒤집기 예시\nleft, right = 0, len(arr) - 1\nwhile left < right:\n    arr[left], arr[right] = arr[right], arr[left]\n    left += 1\n    right -= 1"
    };
  }

  if (id === 28 || id === 32 || id === 44) {
    return {
      title: "딕셔너리 & 빈도수 세기",
      points: [
        "딕셔너리는 키-값(key-value) 쌍으로 이루어져 검색이 매우 빠릅니다(O(1)).",
        "get(key, default) 메서드를 사용하면 키가 없는 경우에도 에러 없이 기본값을 지정해 개수를 셀 수 있습니다.",
        "collections 라이브러리의 Counter를 활용하면 한 줄로 빈도수를 수집할 수 있습니다."
      ],
      code: "cnt = {}\nfor ch in 'banana':\n    cnt[ch] = cnt.get(ch, 0) + 1\n# cnt = {'b': 1, 'a': 3, 'n': 2}\n\n# Counter 사용:\nfrom collections import Counter\nc = Counter('banana')"
    };
  }

  return {
    title: "코스프로 기본 알고리즘 & 구현",
    points: [
      "문제의 요구 사항과 제약 조건을 꼼꼼히 확인하고 한 단계씩 구현하세요.",
      "변수명과 함수 반환값(return)을 정확하게 다루는지 점검합니다.",
      "입출력 형식(공백 구분 데이터 읽기, 출력 정밀도 등)이 맞는지 주의해야 합니다."
    ],
    code: "def solution(data):\n    # 문제를 한 단계씩 논리적으로 해결해 보세요\n    answer = sum(data) / len(data)\n    return answer"
  };
}

export default function Home() {
  const [isMounted, setIsMounted] = useState(false);
  const [theme, setTheme] = useState<'light' | 'dark'>('light');
  const [isAdmin, setIsAdmin] = useState(false);
  const [selectedClass, setSelectedClass] = useState<2 | 3>(3);
  const [problems, setProblems] = useState<Problem[]>(initialProblems);
  const [currentProblem, setCurrentProblem] = useState<Problem>(initialProblems[0]);
  const [code, setCode] = useState<string>(initialProblems[0].starter_code);
  
  // Progress states
  const [submissions, setSubmissions] = useState<Record<string, string>>({});
  const [status, setStatus] = useState<Record<string, 'Solved' | 'Attempted' | 'Unsolved'>>({});
  
  // Pyodide runner states
  const [pyodide, setPyodide] = useState<any>(null);
  const [pyodideLoaded, setPyodideLoaded] = useState<boolean>(false);
  const [pyodideLoading, setPyodideLoading] = useState<boolean>(false);
  
  // Running outputs
  const [consoleLogs, setConsoleLogs] = useState<{ text: string; type: 'info' | 'success' | 'error' | 'muted' }[]>([]);
  const [running, setRunning] = useState<boolean>(false);
  
  // Custom dialog state
  const [isAddModalOpen, setIsAddModalOpen] = useState<boolean>(false);
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [showConceptModal, setShowConceptModal] = useState<boolean>(false);
  const [pendingProblem, setPendingProblem] = useState<Problem | null>(null);

  // New Problem Form States
  const [newTitle, setNewTitle] = useState("");
  const [newType, setNewType] = useState<"code" | "blank">("code");
  const [newClassLevel, setNewClassLevel] = useState<2 | 3>(3);
  const [newDesc, setNewDesc] = useState("");
  const [newInDesc, setNewInDesc] = useState("");
  const [newOutDesc, setNewOutDesc] = useState("");
  const [newStarter, setNewStarter] = useState("");
  const [newTestCases, setNewTestCases] = useState("[\n  {\n    \"input\": \"입력값\",\n    \"output\": \"출력값\"\n  }\n]");
  
  // Category & Learning states
  const [currentCategory, setCurrentCategory] = useState<'home' | 'oj' | 'concept' | 'python_basic' | 'sql_basic' | 'sql_advanced' | 'algorithm'>('home');
  const [activeConceptIndex, setActiveConceptIndex] = useState<number>(0);
  const [activeSqlLessonIndex, setActiveSqlLessonIndex] = useState<number>(0);
  const [sqlQuery, setSqlQuery] = useState<string>("");
  const [sqlResult, setSqlResult] = useState<any>(null);
  const [sqlSuccess, setSqlSuccess] = useState<boolean | null>(null);
  const [showSqlHint, setShowSqlHint] = useState<boolean>(false);
  
  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [algoType, setAlgoType] = useState<'bfs' | 'dfs' | 'minesweeper'>('bfs');
  const [pythonViewType, setPythonViewType] = useState<'basic' | 'playground' | 'turtle' | 'turtle_adv' | 'pygame'>('basic');

  // Resizable panel states
  const [consoleHeight, setConsoleHeight] = useState<number>(256); // default 256px
  const [leftWidth, setLeftWidth] = useState<number>(45); // default 45% of width
  
  const isResizingConsole = useRef(false);
  const isResizingWidth = useRef(false);

  const startResizingConsole = (e: React.MouseEvent) => {
    e.preventDefault();
    isResizingConsole.current = true;
    document.addEventListener("mousemove", handleMouseMoveConsole);
    document.addEventListener("mouseup", stopResizingConsole);
  };

  const handleMouseMoveConsole = (e: MouseEvent) => {
    if (!isResizingConsole.current) return;
    const newHeight = window.innerHeight - e.clientY;
    if (newHeight > 100 && newHeight < window.innerHeight - 200) {
      setConsoleHeight(newHeight);
    }
  };

  const stopResizingConsole = () => {
    isResizingConsole.current = false;
    document.removeEventListener("mousemove", handleMouseMoveConsole);
    document.removeEventListener("mouseup", stopResizingConsole);
  };

  const startResizingWidth = (e: React.MouseEvent) => {
    e.preventDefault();
    isResizingWidth.current = true;
    document.addEventListener("mousemove", handleMouseMoveWidth);
    document.addEventListener("mouseup", stopResizingWidth);
  };

  const handleMouseMoveWidth = (e: MouseEvent) => {
    if (!isResizingWidth.current) return;
    const pct = (e.clientX / window.innerWidth) * 100;
    if (pct > 20 && pct < 80) {
      setLeftWidth(pct);
    }
  };

  const stopResizingWidth = () => {
    isResizingWidth.current = false;
    document.removeEventListener("mousemove", handleMouseMoveWidth);
    document.removeEventListener("mouseup", stopResizingWidth);
  };

  // Load progress and custom problems on mount
  useEffect(() => {
    // Load theme
    const savedTheme = localStorage.getItem("oj_theme") as 'light' | 'dark';
    if (savedTheme) {
      setTheme(savedTheme);
      if (savedTheme === 'dark') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    } else {
      document.documentElement.classList.remove('dark');
    }

    // Load custom problems if any
    const savedProblems = localStorage.getItem("oj_problems");
    let loadedProblems = initialProblems;
    if (savedProblems) {
      try {
        loadedProblems = JSON.parse(savedProblems);
        setProblems(loadedProblems);
      } catch (e) {
        console.error(e);
      }
    }

    // Load progress
    const savedSubmissions = localStorage.getItem("oj_submissions");
    const savedStatus = localStorage.getItem("oj_status");
    
    if (savedSubmissions) {
      try {
        const parsed = JSON.parse(savedSubmissions);
        setSubmissions(parsed);
        // Find default problem for the default selected class (3)
        const class3Probs = loadedProblems.filter(p => (p.classLevel || 3) === 3);
        if (class3Probs.length > 0) {
          const defaultProb = class3Probs[0];
          setCurrentProblem(defaultProb);
          const pid = defaultProb.id.toString();
          if (parsed[pid]) {
            setCode(parsed[pid]);
          } else {
            setCode(defaultProb.starter_code);
          }
        }
      } catch (e) {
        console.error(e);
      }
    } else {
      // Set to first class 3 problem
      const class3Probs = loadedProblems.filter(p => (p.classLevel || 3) === 3);
      if (class3Probs.length > 0) {
        setCurrentProblem(class3Probs[0]);
        setCode(class3Probs[0].starter_code);
      }
    }
    
    if (savedStatus) {
      try {
        setStatus(JSON.parse(savedStatus));
      } catch (e) {
        console.error(e);
      }
    }
    
    // Load admin state
    const savedAdmin = localStorage.getItem("oj_isAdmin");
    if (savedAdmin === "true") {
      setIsAdmin(true);
    }
    
    setIsMounted(true);
  }, []);

  // Listen for navigation messages from concept iframe
  useEffect(() => {
    const handleMessage = (e: MessageEvent) => {
      if (e.data && e.data.type === "NAVIGATE_TO_PROBLEM") {
        const problemId = parseInt(e.data.problemId, 10);
        const found = problems.find(p => p.id === problemId);
        if (found) {
          setPendingProblem(found);
          setShowConceptModal(true);
          setCurrentCategory('oj');
        }
      }
    };
    window.addEventListener("message", handleMessage);
    return () => window.removeEventListener("message", handleMessage);
  }, [problems]);

  // Update editor code when current problem changes
  const handleSelectProblem = (prob: Problem) => {
    setPendingProblem(prob);
    setShowConceptModal(true);
  };

  const handleSelectProblemDirect = (prob: Problem) => {
    setCurrentProblem(prob);
    const pid = prob.id.toString();
    const savedCode = submissions[pid] || prob.starter_code;
    setCode(savedCode);
    setConsoleLogs([]);
  };

  // Sync edits to localStorage
  const handleCodeChange = (newVal: string | undefined) => {
    const val = newVal || "";
    setCode(val);
    
    const pid = currentProblem.id.toString();
    const updatedSubmissions = { ...submissions, [pid]: val };
    setSubmissions(updatedSubmissions);
    localStorage.setItem("oj_submissions", JSON.stringify(updatedSubmissions));

    if (status[pid] !== "Solved") {
      const updatedStatus = { ...status, [pid]: "Attempted" as const };
      setStatus(updatedStatus);
      localStorage.setItem("oj_status", JSON.stringify(updatedStatus));
    }
  };

  // Reset starter code
  const handleReset = () => {
    if (window.confirm("작성 중인 코드를 초기화하고 기본 코드로 되돌리시겠습니까?")) {
      const pid = currentProblem.id.toString();
      handleCodeChange(currentProblem.starter_code);
      
      const updatedStatus = { ...status, [pid]: "Unsolved" as const };
      setStatus(updatedStatus);
      localStorage.setItem("oj_status", JSON.stringify(updatedStatus));
    }
  };

  // Load Pyodide from CDN
  const initPyodide = async () => {
    if (pyodideLoaded || pyodideLoading) return;
    setPyodideLoading(true);
    setConsoleLogs([{ text: String.fromCodePoint(0x2699) + " Pyodide (Python WebAssembly) 로딩 중...", type: "info" }]);
    
    try {
      // @ts-ignore
      const py = await window.loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.1/full/"
      });
      setPyodide(py);
      setPyodideLoaded(true);
      setPyodideLoading(false);
      setConsoleLogs([{ text: String.fromCodePoint(0x2714) + " 파이썬 실행 엔진 준비 완료!", type: "success" }]);
    } catch (err: any) {
      setPyodideLoading(false);
      setConsoleLogs([
        { text: String.fromCodePoint(0x274C) + " 파이썬 엔진 로드 실패. 네트워크 연결을 확인하세요.", type: "error" },
        { text: err.message || "", type: "error" }
      ]);
    }
  };

  // Execute single run
  const runSingle = async (py: any, pythonCode: string, inputStr: string): Promise<{ stdout: string; stderr: string }> => {
    const inputLines = inputStr.split("\n");
    const prepCode = preparePythonRunner(pythonCode, inputLines);

    try {
      await py.runPythonAsync(prepCode);
      const stdout = String(py.globals.get("_captured_stdout") || "");
      return { stdout, stderr: "" };
    } catch (err: any) {
      const stdout = String(py.globals.get("_captured_stdout") || "");
      return { stdout, stderr: err.message };
    }
  };

  // Compare actual vs expected
  const checkMatch = (actual: string, expected: string): boolean => {
    // Normalize function to strip all trailing/leading spaces, replace any sequence of whitespaces (including newlines) with a single space
    const normalize = (text: string) => {
      return text.trim()
        .replace(/[\r\n]+/g, " ")  // Replace line breaks with single space to treat line breaks as normal spaces
        .replace(/\s+/g, " ")      // Replace any consecutive whitespaces with a single space
        .trim();
    };

    const actualNormalized = normalize(actual);
    const expectedNormalized = normalize(expected);
    
    // 1. Check if the normalized expected string exists inside or matches the tail of the normalized actual string.
    if (actualNormalized.endsWith(expectedNormalized) || actualNormalized.includes(expectedNormalized)) {
      return true;
    }

    // 2. Check the last N lines of the actual output (ignores intermediate debug prints)
    const expectedLines = expected.trim().split(/\r?\n/).map(l => l.trim()).filter(Boolean);
    const actualLines = actual.trim().split(/\r?\n/).map(l => l.trim()).filter(Boolean);
    
    if (actualLines.length >= expectedLines.length) {
      const lastActualLines = actualLines.slice(-expectedLines.length);
      const collapsedActual = normalize(lastActualLines.join(" "));
      const collapsedExpected = normalize(expectedLines.join(" "));
      if (collapsedActual === collapsedExpected) {
        return true;
      }
    }

    // 3. Fallback: strip all whitespace entirely for a fully lenient check (e.g. ignoring random spaces/newlines)
    const stripAllSpace = (text: string) => text.replace(/\s+/g, "").trim();
    const actualNoSpace = stripAllSpace(actual);
    const expectedNoSpace = stripAllSpace(expected);

    return actualNoSpace.endsWith(expectedNoSpace) || actualNoSpace.includes(expectedNoSpace);
  };

  // Run Test cases
  const handleRunTests = async () => {
    if (running) return;
    
    // Auto-init pyodide if not loaded
    let activePy = pyodide;
    if (!pyodideLoaded) {
      setRunning(true);
      setConsoleLogs([{ text: String.fromCodePoint(0x2699) + " Pyodide 로딩 중...", type: "info" }]);
      try {
        // @ts-ignore
        activePy = await window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.1/full/"
        });
        setPyodide(activePy);
        setPyodideLoaded(true);
        setPyodideLoading(false);
      } catch (err: any) {
        setRunning(false);
        setConsoleLogs([{ text: String.fromCodePoint(0x274C) + " 엔진 로드 실패: " + err.message, type: "error" }]);
        return;
      }
    }

    setRunning(true);
    setConsoleLogs([{ text: String.fromCodePoint(0x1F680) + " 예제 테스트 케이스 검사 시작...", type: "info" }]);

    let passedCount = 0;
    const examples = currentProblem.examples;

    for (let i = 0; i < examples.length; i++) {
      const ex = examples[i];
      setConsoleLogs(prev => [...prev, { text: "\n테스트 케이스 " + (i + 1) + ":", type: "info" }]);
      setConsoleLogs(prev => [...prev, { text: "  - 입력: " + ex.input.replace(/\n/g, " | "), type: "muted" }]);

      const { stdout, stderr } = await runSingle(activePy, code, ex.input);

      if (stderr) {
        setConsoleLogs(prev => [
          ...prev, 
          { text: "  - 결과: [실행 에러]", type: "error" },
          { text: stderr, type: "error" }
        ]);
      } else {
        const passed = checkMatch(stdout, ex.output);
        if (passed) {
          passedCount++;
          setConsoleLogs(prev => [...prev, { text: "  - 결과: [성공]", type: "success" }]);
        } else {
          setConsoleLogs(prev => [
            ...prev, 
            { text: "  - 결과: [실패]", type: "error" },
            { text: "    * 기대 출력:\n" + ex.output, type: "muted" },
            { text: "    * 실제 출력:\n" + stdout.trim(), type: "muted" }
          ]);
        }
      }
    }

    setConsoleLogs(prev => [
      ...prev, 
      { text: "\n" + String.fromCodePoint(0x1F3C1) + " 요약: " + passedCount + "/" + examples.length + " 통과", type: passedCount === examples.length ? "success" : "info" }
    ]);
    setRunning(false);
  };

  // Submit and grade all test cases
  const handleSubmit = async () => {
    if (running) return;

    // Auto-init pyodide if not loaded
    let activePy = pyodide;
    if (!pyodideLoaded) {
      setRunning(true);
      setConsoleLogs([{ text: "\u2699 Pyodide 로딩 중...", type: "info" }]);
      try {
        // @ts-ignore
        activePy = await window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.1/full/"
        });
        setPyodide(activePy);
        setPyodideLoaded(true);
        setPyodideLoading(false);
      } catch (err: any) {
        setRunning(false);
        setConsoleLogs([{ text: "\u274c 엔진 로드 실패: " + err.message, type: "error" }]);
        return;
      }
    }

    setRunning(true);
    setConsoleLogs([{ text: "\u2699 채점 엔진 가동 중...", type: "info" }]);

    let passedCount = 0;
    const testCases = currentProblem.test_cases;

    for (let i = 0; i < testCases.length; i++) {
      const tc = testCases[i];
      const { stdout, stderr } = await runSingle(activePy, code, tc.input);

      if (!stderr && checkMatch(stdout, tc.output)) {
        passedCount++;
        setConsoleLogs(prev => [...prev, { text: "테스트 케이스 " + (i + 1) + ": 성공", type: "success" }]);
      } else {
        setConsoleLogs(prev => [...prev, { text: "테스트 케이스 " + (i + 1) + ": 실패", type: "error" }]);
        if (stderr) {
          setConsoleLogs(prev => [...prev, { text: "    * 에러 메시지:\n" + stderr, type: "error" }]);
        } else {
          setConsoleLogs(prev => [
            ...prev,
            { text: "    * 입력값: " + (tc.input ? tc.input.replace(/\n/g, " | ") : "없음"), type: "muted" },
            { text: "    * 기대 출력:\n" + tc.output, type: "muted" },
            { text: "    * 실제 출력:\n" + (stdout ? stdout.trim() : "(출력 없음)"), type: "muted" }
          ]);
        }
      }
    }

    const pid = currentProblem.id.toString();
    const isSuccess = passedCount === testCases.length;
    
    const updatedStatus = { ...status, [pid]: (isSuccess ? "Solved" : "Attempted") as any };
    setStatus(updatedStatus);
    localStorage.setItem("oj_status", JSON.stringify(updatedStatus));

    if (isSuccess) {
      setConsoleLogs(prev => [
        ...prev, 
        { text: "\n" + String.fromCodePoint(0x2714) + " 정답입니다! (" + passedCount + "/" + testCases.length + " 통과)", type: "success" }
      ]);
    } else {
      setConsoleLogs(prev => [
        ...prev, 
        { text: "\n" + String.fromCodePoint(0x274C) + " 오답 또는 실행 에러가 있습니다. (" + passedCount + "/" + testCases.length + " 통과)", type: "error" }
      ]);
    }

    setRunning(false);
  };

  // Add problem functionality
  const handleAddProblem = (e: React.FormEvent) => {
    e.preventDefault();

    if (!newTitle || !newDesc) {
      alert("제목과 문제 설명은 필수입니다.");
      return;
    }

    let parsedTestCases: Example[] = [];
    try {
      parsedTestCases = JSON.parse(newTestCases);
      if (!Array.isArray(parsedTestCases) || parsedTestCases.length === 0) {
        throw new Error("테스트 케이스는 1개 이상의 객체 배열이어야 합니다.");
      }
    } catch (err: any) {
      alert("테스트 케이스 형식이 잘못되었습니다: " + err.message);
      return;
    }

    const newId = Math.max(...problems.map(p => p.id), 0) + 1;
    const newProb: Problem = {
      id: newId,
      classLevel: newClassLevel,
      title: newTitle,
      type: newType,
      description: newDesc,
      input_desc: newInDesc,
      output_desc: newOutDesc,
      examples: parsedTestCases.slice(0, 2), // First 2 as examples
      starter_code: newStarter,
      test_cases: parsedTestCases
    };

    const updatedProblems = [...problems, newProb];
    setProblems(updatedProblems);
    localStorage.setItem("oj_problems", JSON.stringify(updatedProblems));

    // Reset fields
    setNewTitle("");
    setNewDesc("");
    setNewInDesc("");
    setNewOutDesc("");
    setNewStarter("");
    setNewTestCases("[\n  {\n    \"input\": \"입력값\",\n    \"output\": \"출력값\"\n  }\n]");

    setIsAddModalOpen(false);
    alert("새 문제가 추가되었습니다!");
  };

  const handleAdminToggle = () => {
    if (isAdmin) {
      if (window.confirm("관리자 모드에서 로그아웃 하시겠습니까?")) {
        setIsAdmin(false);
        localStorage.removeItem("oj_isAdmin");
      }
    } else {
      const password = window.prompt("관리자 비밀번호를 입력하세요:");
      if (password === "1000") {
        setIsAdmin(true);
        localStorage.setItem("oj_isAdmin", "true");
        alert("관리자 모드로 로그인되었습니다.");
      } else if (password !== null) {
        alert("비밀번호가 틀렸습니다.");
      }
    }
  };

  const copyToClipboard = (text: string, id: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const toggleTheme = () => {
    const nextTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(nextTheme);
    localStorage.setItem("oj_theme", nextTheme);
    if (nextTheme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }

    // Notify iframe documents of the theme update
    const iframes = document.querySelectorAll('iframe');
    iframes.forEach(iframe => {
      iframe.contentWindow?.postMessage({ type: 'theme-change', theme: nextTheme }, '*');
    });
  };

  const handleRunSQL = (correctQuery: string) => {
    if (!sqlQuery.trim()) return;
    const result = runMockSQL(sqlQuery);
    setSqlResult(result);
    
    if (result.error) {
      setSqlSuccess(false);
      return;
    }

    const expectedResult = runMockSQL(correctQuery);
    const colsMatch = JSON.stringify(result.columns.map(c => c.toLowerCase())) === JSON.stringify(expectedResult.columns.map(c => c.toLowerCase()));
    const rowsMatch = JSON.stringify(result.rows) === JSON.stringify(expectedResult.rows);
    
    if (colsMatch && rowsMatch) {
      setSqlSuccess(true);
    } else {
      setSqlSuccess(false);
    }
  };

  return (
    <main className="h-screen w-screen bg-[var(--bg)] text-[var(--text)] font-sans flex flex-col overflow-hidden">
      <Script 
        src="https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js" 
        strategy="afterInteractive"
        onLoad={initPyodide}
      />

      {/* ========================================================================= */}
      {/* 1. HOME SCREEN CATEGORY SELECTION */}
      {/* ========================================================================= */}
      {currentCategory === 'home' && (
        <div className="flex-1 flex flex-col overflow-y-auto bg-gradient-to-br from-[var(--panel-2)] to-[var(--bg)] p-8 md:p-12 justify-center items-center relative">
          {/* Theme Toggle Button */}
          <button
            onClick={toggleTheme}
            className="absolute top-6 right-6 p-3 rounded-full bg-[var(--panel)] border border-[var(--line)] text-[var(--text)] hover:bg-[var(--panel-2)] transition-colors shadow-md cursor-pointer flex items-center justify-center"
            title="테마 변경"
          >
            {theme === 'light' ? <Moon size={20} /> : <Sun size={20} />}
          </button>

          <div className="max-w-5xl w-full text-center mb-12">
            <h1 className="text-4xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-[var(--accent-3)] via-[#b4befe] to-[var(--accent-2)] tracking-tight mb-4">
              COS Pro & SQL 학습 플랫폼
            </h1>
            <p className="text-lg text-[var(--muted)] max-w-2xl mx-auto">
              자격증 취득부터 실무 데이터 분석까지, 파이썬 알고리즘과 SQL 쿼리를 웹 브라우저에서 실시간으로 학습하고 채점해보세요.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl w-full">
            {/* Card 1: COS Pro OJ */}
            <div 
              onClick={() => setCurrentCategory('oj')}
              className="bg-[var(--panel)] border border-[var(--line)] hover:border-[var(--accent-3)]/50 p-6 rounded-2xl cursor-pointer transition-all duration-300 transform hover:-translate-y-1 hover:shadow-2xl flex flex-col justify-between group"
            >
              <div>
                <div className="bg-[var(--accent-3)]/10 text-[var(--accent-3)] p-4 rounded-xl w-14 h-14 flex items-center justify-center mb-5 group-hover:scale-110 transition-transform duration-300">
                  <FileCode2 size={28} />
                </div>
                <h3 className="text-xl font-bold text-[var(--accent-3)] mb-2">코스프로 문제 풀기</h3>
                <p className="text-sm text-[var(--muted)] leading-relaxed mb-4">
                  COS Pro 2급 & 3급 Python 모의고사를 직접 풀어보고 실시간으로 자동 채점을 받아보세요.
                </p>
              </div>
              <div className="flex items-center justify-between mt-4">
                <span className="text-xs font-bold text-[var(--accent-3)] bg-[var(--accent-3)]/10 px-3 py-1 rounded-full">실시간 채점 샌드박스</span>
                <ChevronRight size={18} className="text-[var(--accent-3)] group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Card 2: Concept Learning */}
            <div 
              onClick={() => {
                setCurrentCategory('concept');
                setActiveConceptIndex(0);
              }}
              className="bg-[var(--panel)] border border-[var(--line)] hover:border-[var(--accent-2)]/50 p-6 rounded-2xl cursor-pointer transition-all duration-300 transform hover:-translate-y-1 hover:shadow-2xl flex flex-col justify-between group"
            >
              <div>
                <div className="bg-[var(--accent-2)]/10 text-[var(--accent-2)] p-4 rounded-xl w-14 h-14 flex items-center justify-center mb-5 group-hover:scale-110 transition-transform duration-300">
                  <BookOpen size={28} />
                </div>
                <h3 className="text-xl font-bold text-[var(--accent-2)] mb-2">코스프로 개념 학습</h3>
                <p className="text-sm text-[var(--muted)] leading-relaxed mb-4">
                  변수, 입출력, 반복문, 리스트, 내장 함수 등 COS Pro 파이썬 시험에 꼭 출제되는 핵심 이론과 예제 코드를 배웁니다.
                </p>
              </div>
              <div className="flex items-center justify-between mt-4">
                <span className="text-xs font-bold text-[var(--accent-2)] bg-[var(--accent-2)]/10 px-3 py-1 rounded-full">파이썬 핵심 문법 수록</span>
                <ChevronRight size={18} className="text-[var(--accent-2)] group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Card 3: Python Basic */}
            <div 
              onClick={() => {
                setCurrentCategory('python_basic');
              }}
              className="bg-[var(--panel)] border border-[var(--line)] hover:border-[var(--accent-3)]/50 p-6 rounded-2xl cursor-pointer transition-all duration-300 transform hover:-translate-y-1 hover:shadow-2xl flex flex-col justify-between group"
            >
              <div>
                <div className="bg-[var(--accent-3)]/10 text-[var(--accent-3)] p-4 rounded-xl w-14 h-14 flex items-center justify-center mb-5 group-hover:scale-110 transition-transform duration-300">
                  <Code size={28} />
                </div>
                <h3 className="text-xl font-bold text-[var(--accent-3)] mb-2">파이썬 기초 문법</h3>
                <p className="text-sm text-[var(--muted)] leading-relaxed mb-4">
                  변수, 연산자, 조건문, 반복문, 리스트, 함수 등 프로그래밍 입문자를 위한 파이썬의 가장 기초적인 문법을 학습합니다.
                </p>
              </div>
              <div className="flex items-center justify-between mt-4">
                <span className="text-xs font-bold text-[var(--accent-3)] bg-[var(--accent-3)]/10 px-3 py-1 rounded-full">인터랙티브 파이썬 실습</span>
                <ChevronRight size={18} className="text-[var(--accent-3)] group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Card 3: SQL Basic */}
            <div 
              onClick={() => {
                setCurrentCategory('sql_basic');
                setActiveSqlLessonIndex(0);
                setSqlQuery(sqlBasicLessons[0].starterQuery);
                setSqlResult(null);
                setSqlSuccess(null);
                setShowSqlHint(false);
              }}
              className="bg-[var(--panel)] border border-[var(--line)] hover:border-[var(--accent)]/50 p-6 rounded-2xl cursor-pointer transition-all duration-300 transform hover:-translate-y-1 hover:shadow-2xl flex flex-col justify-between group"
            >
              <div>
                <div className="bg-[var(--accent)]/10 text-[var(--accent)] p-4 rounded-xl w-14 h-14 flex items-center justify-center mb-5 group-hover:scale-110 transition-transform duration-300">
                  <Database size={28} />
                </div>
                <h3 className="text-xl font-bold text-[var(--accent)] mb-2">SQL 기초</h3>
                <p className="text-sm text-[var(--muted)] leading-relaxed mb-4">
                  데이터베이스의 근간인 SELECT, WHERE, ORDER BY, LIMIT 문을 배우고 실제 학생 데이터를 조회하고 가공해보세요.
                </p>
              </div>
              <div className="flex items-center justify-between mt-4">
                <span className="text-xs font-bold text-[var(--accent)] bg-[var(--accent)]/10 px-3 py-1 rounded-full">인터랙티브 SQL 실습</span>
                <ChevronRight size={18} className="text-[var(--accent)] group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Card 4: SQL Advanced */}
            <div 
              onClick={() => {
                setCurrentCategory('sql_advanced');
                setActiveSqlLessonIndex(0);
                setSqlQuery(sqlAdvancedLessons[0].starterQuery);
                setSqlResult(null);
                setSqlSuccess(null);
                setShowSqlHint(false);
              }}
              className="bg-[var(--panel)] border border-[var(--line)] hover:border-[#b4befe]/50 p-6 rounded-2xl cursor-pointer transition-all duration-300 transform hover:-translate-y-1 hover:shadow-2xl flex flex-col justify-between group"
            >
              <div>
                <div className="bg-[#b4befe]/10 text-[#b4befe] p-4 rounded-xl w-14 h-14 flex items-center justify-center mb-5 group-hover:scale-110 transition-transform duration-300">
                  <Sparkles size={28} />
                </div>
                <h3 className="text-xl font-bold text-[#b4befe] mb-2">SQL 심화</h3>
                <p className="text-sm text-[var(--muted)] leading-relaxed mb-4">
                  그룹화(GROUP BY), 조인(JOIN), 서브쿼리 등 복잡한 데이터 분석 및 집계 처리를 위한 고급 SQL 문법을 학습합니다.
                </p>
              </div>
              <div className="flex items-center justify-between mt-4">
                <span className="text-xs font-bold text-[#b4befe] bg-[#b4befe]/10 px-3 py-1 rounded-full">집계 및 JOIN 마스터</span>
                <ChevronRight size={18} className="text-[#b4befe] group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            {/* Card 5: Algorithm Solving */}
            <div 
              onClick={() => {
                setCurrentCategory('algorithm');
              }}
              className="bg-[var(--panel)] border border-[var(--line)] hover:border-[#f38ba8]/50 p-6 rounded-2xl cursor-pointer transition-all duration-300 transform hover:-translate-y-1 hover:shadow-2xl flex flex-col justify-between group"
            >
              <div>
                <div className="bg-[#f38ba8]/10 text-[#f38ba8] p-4 rounded-xl w-14 h-14 flex items-center justify-center mb-5 group-hover:scale-110 transition-transform duration-300">
                  <Sparkles size={28} />
                </div>
                <h3 className="text-xl font-bold text-[#f38ba8] mb-2">알고리즘 풀기</h3>
                <p className="text-sm text-[var(--muted)] leading-relaxed mb-4">
                  DFS와 BFS를 활용한 시뮬레이션을 통해 복잡한 탐색 알고리즘을 직관적으로 학습합니다.
                </p>
              </div>
              <div className="flex items-center justify-between mt-4">
                <span className="text-xs font-bold text-[#f38ba8] bg-[#f38ba8]/10 px-3 py-1 rounded-full">탐색 알고리즘 실습</span>
                <ChevronRight size={18} className="text-[#f38ba8] group-hover:translate-x-1 transition-transform" />
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* 2. COS PRO OJ VIEW */}
      {/* ========================================================================= */}
      {currentCategory === 'oj' && (
        <>
          {/* Header Bar */}
          <header className="border-b border-[var(--line)] bg-[var(--panel-2)] px-6 py-4 flex items-center justify-between shrink-0">
            <div className="flex items-center gap-3">
              <button 
                onClick={() => setCurrentCategory('home')}
                className="flex items-center gap-1.5 bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] px-3.5 py-2 rounded-xl text-xs font-semibold transition-all duration-200"
              >
                <ArrowLeft size={14} />
                홈으로
              </button>
              <div className="bg-[var(--accent-3)]/20 p-2 rounded-xl text-[var(--accent-3)]">
                <FileCode2 size={20} />
              </div>
              <div>
                <h1 className="text-base font-bold tracking-wide text-[var(--accent-3)] flex items-center gap-2">
                  COS Pro {selectedClass}급 Python Online Judge
                </h1>
                <p className="text-[10px] text-[var(--muted)]">실시간 자동 채점 및 코드 연습 시스템</p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <div className="flex bg-[var(--line)] p-1 rounded-xl border border-[var(--line-hover)]">
                <button
                  onClick={() => {
                    setSelectedClass(3);
                    const class3 = problems.filter(p => (p.classLevel || 3) === 3);
                    if (class3.length > 0) {
                      handleSelectProblemDirect(class3[0]);
                    }
                  }}
                  className={"px-3 py-1 rounded-lg text-xs font-bold transition-all duration-200 " + (
                    selectedClass === 3
                      ? "bg-[var(--accent-3)] text-[var(--bg)]"
                      : "text-[var(--muted)] hover:text-[var(--text)]"
                  )}
                >
                  3급 문제
                </button>
                <button
                  onClick={() => {
                    setSelectedClass(2);
                    const class2 = problems.filter(p => (p.classLevel || 3) === 2);
                    if (class2.length > 0) {
                      handleSelectProblemDirect(class2[0]);
                    }
                  }}
                  className={"px-3 py-1 rounded-lg text-xs font-bold transition-all duration-200 " + (
                    selectedClass === 2
                      ? "bg-[var(--accent-3)] text-[var(--bg)]"
                      : "text-[var(--muted)] hover:text-[var(--text)]"
                  )}
                >
                  2급 문제
                </button>
              </div>

              <button 
                onClick={handleAdminToggle}
                className={"flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold border transition-all duration-200 " + (
                  isAdmin 
                    ? "bg-[var(--accent-2)] text-[var(--bg)] border-[var(--accent-2)]" 
                    : "bg-[var(--line)] text-[var(--muted)] border-[var(--line-hover)] hover:bg-[var(--line-hover)]"
                )}
              >
                <span>{isAdmin ? "관리자 종료" : "관리자 모드"}</span>
              </button>

              <button 
                onClick={toggleTheme}
                className="flex items-center justify-center bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] p-2.5 rounded-xl transition-all duration-200"
                title="테마 변경"
              >
                {theme === 'light' ? <Moon size={14} /> : <Sun size={14} />}
              </button>

              <button 
                onClick={() => setIsAddModalOpen(true)}
                className="flex items-center gap-1.5 bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--accent-2)] px-3 py-1.5 rounded-xl text-xs font-semibold transition-all duration-200"
              >
                <Plus size={14} />
                새 문제 추가
              </button>
            </div>
          </header>

          {/* Main Panel split */}
          <div className="flex-1 flex flex-col lg:flex-row overflow-hidden min-h-0 relative">
            {/* Sidebar Toggle Button (When Collapsed) */}
            {isSidebarCollapsed && (
              <button
                onClick={() => setIsSidebarCollapsed(false)}
                className="absolute left-4 top-4 z-40 bg-[var(--panel-2)] border border-[var(--line)] text-[var(--accent-3)] hover:text-white p-2 rounded-xl shadow-lg transition-all duration-200"
                title="문제 목록 열기"
              >
                <PanelLeftOpen size={20} />
              </button>
            )}

            {/* Left Side: Sidebar Problems List */}
            <aside className={"border-r border-[var(--line)] bg-[var(--panel-2)] flex flex-col shrink-0 overflow-hidden h-full transition-all duration-300 " + (
              isSidebarCollapsed ? "w-0 border-r-0" : "w-full lg:w-80"
            )}>
              <div className="p-4 border-b border-[var(--line)] flex items-center justify-between shrink-0">
                <span className="text-sm font-bold text-[var(--accent-3)] flex items-center gap-1.5">
                  <BookOpen size={16} /> {selectedClass}급 문제 목록
                </span>
                <button
                  onClick={() => setIsSidebarCollapsed(true)}
                  className="text-[var(--muted)] hover:text-white transition-colors"
                  title="문제 목록 접기"
                >
                  <PanelLeftClose size={18} />
                </button>
              </div>

              {/* Search Box */}
              <div className="p-3 border-b border-[var(--line)] shrink-0">
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-[var(--muted-dark)]" size={16} />
                  <input
                    type="text"
                    placeholder="문제 번호 또는 키워드 검색..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full bg-[var(--bg)] border border-[var(--line)] rounded-xl pl-9 pr-4 py-2 text-xs text-[var(--text)] placeholder-[var(--muted-dark)] focus:outline-none focus:border-[var(--accent-3)]"
                  />
                  {searchQuery && (
                    <button
                      onClick={() => setSearchQuery("")}
                      className="absolute right-3 top-1/2 -translate-y-1/2 text-[var(--muted-dark)] hover:text-white text-xs"
                    >
                      초기화
                    </button>
                  )}
                </div>
              </div>

              <div className="flex-1 overflow-y-auto p-2 space-y-1 min-h-0">
                {problems
                  .filter((p) => (p.classLevel || 3) === selectedClass)
                  .filter((p) => {
                    if (!searchQuery.trim()) return true;
                    const query = searchQuery.toLowerCase();
                    return (
                      p.id.toString().includes(query) ||
                      p.title.toLowerCase().includes(query) ||
                      p.description.toLowerCase().includes(query)
                    );
                  })
                  .map((prob) => {
                    const pid = prob.id.toString();
                    const active = currentProblem.id === prob.id;
                    const probStatus = status[pid] || "Unsolved";
                    
                    return (
                      <button
                        key={prob.id}
                        onClick={() => handleSelectProblem(prob)}
                        className={"w-full text-left p-3 rounded-xl flex items-center justify-between transition-all duration-150 " + (
                          active 
                            ? "bg-[var(--line)] border border-[var(--accent-3)]/20 text-[var(--accent-3)]" 
                            : "hover:bg-[var(--panel)] text-[var(--text)]"
                        )}
                      >
                        <div className="flex-1 min-w-0 pr-2">
                          <h3 className="text-sm font-semibold truncate">{prob.title}</h3>
                          <span className="text-[10px] uppercase font-bold text-[var(--muted)] bg-[var(--line)] px-2 py-0.5 rounded-full mt-1 inline-block">
                            {prob.type === "blank" ? "빈칸 채우기" : "소스코드 작성"}
                          </span>
                        </div>

                        <div>
                          {probStatus === "Solved" ? (
                            <CheckCircle2 size={18} className="text-[var(--accent)]" />
                          ) : probStatus === "Attempted" ? (
                            <AlertTriangle size={18} className="text-[#f9e2af]" />
                          ) : (
                            <HelpCircle size={18} className="text-[var(--muted-extra)]" />
                          )}
                        </div>
                      </button>
                    );
                  })}
              </div>
            </aside>

            {/* Right Side: Main Workstation Split */}
            <div className="flex-1 flex flex-col xl:flex-row overflow-hidden min-w-0 h-full">
              
              {/* Left panel: Problem details */}
              <div 
                className="border-b xl:border-b-0 xl:border-r border-[var(--line)] bg-[var(--bg)] overflow-y-auto flex flex-col p-6 min-w-0 shrink-0 h-full"
                style={{ width: isMounted ? leftWidth + "%" : '45%' }}
              >
                <h2 className="text-xl font-bold text-[var(--accent-3)] border-b border-[var(--line)] pb-3 mb-4 shrink-0">
                  {currentProblem.title}
                </h2>

                <div className="space-y-6 text-[var(--text)]">
                  {/* Problem Statement */}
                  <div>
                    <h4 className="text-sm font-bold text-[var(--accent-3)] mb-2 uppercase tracking-wide">■ 문제 설명</h4>
                    <p className="text-sm leading-relaxed whitespace-pre-line text-[var(--muted)]">
                      {currentProblem.description}
                    </p>
                  </div>

                  {/* Input Description */}
                  {currentProblem.input_desc && (
                    <div>
                      <h4 className="text-sm font-bold text-[var(--accent-3)] mb-2 uppercase tracking-wide">■ 입력 설명</h4>
                      <p className="text-sm text-[var(--muted)]">{currentProblem.input_desc}</p>
                    </div>
                  )}

                  {/* Output Description */}
                  {currentProblem.output_desc && (
                    <div>
                      <h4 className="text-sm font-bold text-[var(--accent-3)] mb-2 uppercase tracking-wide">■ 출력 설명</h4>
                      <p className="text-sm text-[var(--muted)]">{currentProblem.output_desc}</p>
                    </div>
                  )}

                  {/* Examples IO */}
                  <div>
                    <h4 className="text-sm font-bold text-[var(--accent-3)] mb-3 uppercase tracking-wide">■ 입출력 예</h4>
                    <div className="space-y-4">
                      {currentProblem.examples.map((ex, index) => {
                        const exId = `ex-${currentProblem.id}-${index}`;
                        return (
                          <div key={index} className="border border-[var(--line)] rounded-xl overflow-hidden bg-[var(--panel-2)]">
                            <div className="bg-[var(--panel)] px-4 py-2 border-b border-[var(--line)] text-xs font-bold text-[var(--accent-3)]">
                              입출력 예 #{index + 1}
                            </div>
                            
                            <div className="grid grid-cols-1 md:grid-cols-2 divide-y md:divide-y-0 md:divide-x divide-[var(--line)]">
                              <div className="p-4">
                                <div className="flex items-center justify-between mb-1">
                                  <span className="text-xs text-[var(--muted)] font-bold">입력</span>
                                  <button 
                                    onClick={() => copyToClipboard(ex.input, exId + "-in")}
                                    className="text-[var(--muted)] hover:text-[var(--accent-3)] transition-colors"
                                  >
                                    {copiedId === exId + "-in" ? <Check size={14} /> : <Copy size={14} />}
                                  </button>
                                </div>
                                <pre className="text-xs font-mono bg-[var(--bg)] p-3 rounded-lg text-[var(--accent)] overflow-x-auto whitespace-pre">
                                  {ex.input}
                                </pre>
                              </div>

                              <div className="p-4">
                                <div className="flex items-center justify-between mb-1">
                                  <span className="text-xs text-[var(--muted)] font-bold">출력</span>
                                  <button 
                                    onClick={() => copyToClipboard(ex.output, exId + "-out")}
                                    className="text-[var(--muted)] hover:text-[var(--accent-3)] transition-colors"
                                  >
                                    {copiedId === exId + "-out" ? <Check size={14} /> : <Copy size={14} />}
                                  </button>
                                </div>
                                <pre className="text-xs font-mono bg-[var(--bg)] p-3 rounded-lg text-[var(--accent-2)] overflow-x-auto whitespace-pre">
                                  {ex.output}
                                </pre>
                              </div>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>

                  {isAdmin && currentProblem.solution_code && (
                    <div className="mt-6 border-t border-[var(--accent-2)]/30 pt-4">
                      <div className="flex items-center justify-between mb-2">
                        <h4 className="text-sm font-bold text-[var(--accent-2)] uppercase tracking-wide">■ 관리자용 정답 및 해설</h4>
                        <button 
                          onClick={() => copyToClipboard(currentProblem.solution_code!, "admin-sol")}
                          className="flex items-center gap-1 text-xs text-[var(--muted)] hover:text-[var(--accent-2)] transition-colors bg-[var(--panel)] px-2.5 py-1.5 rounded-lg border border-[var(--line)]"
                        >
                          {copiedId === "admin-sol" ? <Check size={12} /> : <Copy size={12} />}
                          <span>정답 복사</span>
                        </button>
                      </div>
                      <pre className="text-xs font-mono bg-[var(--panel-2)] border border-[var(--line)] p-4 rounded-xl text-[var(--accent)] overflow-x-auto whitespace-pre leading-relaxed">
                        {currentProblem.solution_code}
                      </pre>
                    </div>
                  )}
                </div>
              </div>

              {/* Horizontal Split Handler (Visible on xl screens only) */}
              <div 
                onMouseDown={startResizingWidth}
                className="hidden xl:flex w-1.5 hover:w-2 bg-[var(--line)] hover:bg-[var(--accent-3)] cursor-col-resize justify-center items-center select-none transition-all duration-150 group shrink-0 h-full"
              >
                <div className="h-12 w-0.5 bg-[var(--muted-extra)] group-hover:bg-[var(--bg)] rounded-full"></div>
              </div>

              {/* Right panel: Code Editor & Console Output */}
              <div className="flex-1 flex flex-col overflow-hidden h-full">
                
                {/* Editor Container */}
                <div className="flex-1 min-h-[200px] border-b border-[var(--line)] relative flex flex-col">
                  <div className="bg-[var(--panel-2)] border-b border-[var(--line)] px-4 py-2.5 flex items-center justify-between text-xs text-[var(--muted)] font-bold shrink-0">
                    <span className="flex items-center gap-1">
                      <Code size={14} /> main.py
                    </span>
                    <div className="flex items-center gap-2">
                      <button 
                        onClick={() => {
                          if (window.confirm("코드를 초기화하시겠습니까?")) {
                            setCode(currentProblem.starter_code);
                            setConsoleLogs([]);
                          }
                        }}
                        className="flex items-center gap-1 bg-[var(--line)] hover:bg-[var(--line-hover)] border border-[var(--line-hover)] text-[var(--text)] px-2.5 py-1 rounded-lg transition-colors"
                      >
                        <RotateCcw size={12} />
                        초기화
                      </button>
                    </div>
                  </div>
                  
                  {/* Monaco Editor Container */}
                  <div className="flex-1 min-h-0">
                    <Editor
                      height="100%"
                      defaultLanguage="python"
                      language="python"
                      theme="light"
                      value={code}
                      onChange={handleCodeChange}
                      options={{
                        fontSize: 14,
                        fontFamily: "var(--font-geist-mono), monospace",
                        minimap: { enabled: false },
                        lineNumbers: "on",
                        scrollbar: {
                          vertical: "auto",
                          horizontal: "auto",
                        },
                        lineHeight: 22,
                        tabSize: 4,
                        automaticLayout: true
                      }}
                    />
                  </div>
                </div>

                {/* Vertical Split Handler */}
                <div 
                  onMouseDown={startResizingConsole}
                  className="h-1.5 hover:h-2 bg-[var(--line)] hover:bg-[var(--accent-3)] cursor-row-resize flex justify-center items-center select-none transition-all duration-150 group shrink-0"
                >
                  <div className="w-12 h-0.5 bg-[var(--muted-extra)] group-hover:bg-[var(--bg)] rounded-full"></div>
                </div>

                {/* Console and Grading Section */}
                <div className="flex flex-col bg-[var(--bg)] shrink-0" style={{ height: consoleHeight + "px" }}>
                  <div className="border-b border-[var(--line)] bg-[var(--panel-2)] px-4 py-3 flex items-center justify-between">
                    <span className="text-sm font-bold text-[var(--muted)] flex items-center gap-1.5">
                      <Terminal size={16} /> 실행 결과 및 콘솔
                    </span>
                    
                    <div className="flex items-center gap-2">
                      <button
                        onClick={handleRunTests}
                        disabled={running}
                        className="flex items-center gap-1.5 bg-[var(--line)] hover:bg-[var(--line-hover)] border border-[var(--line-hover)] disabled:opacity-50 text-sm text-[var(--accent)] px-4 py-2 rounded-xl font-bold transition-colors"
                      >
                        <Play size={14} />
                        테스트 실행
                      </button>

                      <button
                        onClick={handleSubmit}
                        disabled={running}
                        className="flex items-center gap-1.5 bg-[var(--accent)] hover:bg-[#89d587] disabled:opacity-50 text-sm text-[var(--bg)] px-5 py-2 rounded-xl font-bold transition-colors"
                      >
                        <Send size={14} />
                        제출 및 채점
                      </button>
                    </div>
                  </div>

                  {/* Console Logs Output */}
                  <div className="flex-1 overflow-auto p-4 font-mono text-sm space-y-1">
                    {consoleLogs.length === 0 ? (
                      <span className="text-[var(--muted-dark)]">코드를 실행하거나 제출하면 여기에 결과가 표시됩니다.</span>
                    ) : (
                      consoleLogs.map((log, idx) => {
                        if (log.type === "error") {
                          return (
                            <div key={idx} className="bg-[var(--accent-2)]/10 border-l-4 border-[var(--accent-2)] text-[var(--accent-2)] font-bold px-3 py-2.5 my-1.5 rounded-r-xl whitespace-pre-wrap font-mono text-xs flex flex-col gap-1 animate-[fadeIn_0.15s_ease-out]">
                              <div className="flex items-center gap-1.5 text-[9px] uppercase tracking-wider opacity-90 font-bold">
                                <AlertTriangle size={12} />
                                Execution Error / Incorrect Answer
                              </div>
                              <div className="leading-relaxed">
                                {log.text}
                              </div>
                            </div>
                          );
                        }

                        if (log.type === "success") {
                          return (
                            <div key={idx} className="bg-[var(--accent)]/10 border-l-4 border-[var(--accent)] text-[var(--accent)] font-bold px-3 py-2.5 my-1.5 rounded-r-xl whitespace-pre-wrap font-mono text-xs flex flex-col gap-1 animate-[fadeIn_0.15s_ease-out]">
                              <div className="flex items-center gap-1.5 text-[9px] uppercase tracking-wider opacity-90 font-bold">
                                <CheckCircle2 size={12} />
                                Success / All Test Cases Passed
                              </div>
                              <div className="leading-relaxed">
                                {log.text}
                              </div>
                            </div>
                          );
                        }

                        let color = "text-[var(--text)]";
                        if (log.type === "info") color = "text-[var(--accent-3)]";
                        if (log.type === "muted") color = "text-[var(--muted-extra)]";

                        return (
                          <div key={idx} className={color + " whitespace-pre text-xs py-0.5"}>
                            {log.text}
                          </div>
                        );
                      })
                    )}
                  </div>
                </div>

              </div>

            </div>
          </div>
        </>
      )}

      {/* ========================================================================= */}
      {/* 3. COS PRO CONCEPT LEARNING VIEW */}
      {/* ========================================================================= */}
      {currentCategory === 'concept' && (
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Header */}
          <header className="border-b border-[var(--line)] bg-[var(--panel-2)] px-6 py-4 flex items-center justify-between shrink-0">
            <div className="flex items-center gap-3">
              <button 
                onClick={() => setCurrentCategory('home')}
                className="flex items-center gap-1 bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] px-3.5 py-2 rounded-xl text-xs font-semibold transition-all duration-200"
              >
                <ArrowLeft size={14} />
                홈으로
              </button>
              <div className="bg-[var(--accent-2)]/25 p-2 rounded-xl text-[var(--accent-2)]">
                <BookOpen size={20} />
              </div>
              <div>
                <h1 className="text-base font-bold tracking-wide text-[var(--accent-2)]">
                  코스프로 개념 학습
                </h1>
                <p className="text-[10px] text-[var(--muted)]">COS Pro 합격을 위해 꼭 알아야 하는 파이썬 필수 문법 및 이론 총정리</p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <button 
                onClick={toggleTheme}
                className="flex items-center justify-center bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] p-2 rounded-xl transition-all duration-200"
                title="테마 변경"
              >
                {theme === 'light' ? <Moon size={14} /> : <Sun size={14} />}
              </button>
            </div>
          </header>

          <iframe 
            src={`/cospro_python_reference.html?theme=${theme}`} 
            className="w-full flex-1 border-0 bg-[var(--bg)]" 
          />
        </div>
      )}

      {/* ========================================================================= */}
      {/* 3-2. PYTHON BASIC GRAMMAR VIEW */}
      {/* ========================================================================= */}
      {currentCategory === 'python_basic' && (
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Header */}
          <header className="border-b border-[var(--line)] bg-[var(--panel-2)] px-6 py-4 flex items-center justify-between shrink-0">
            <div className="flex items-center gap-3">
              <button 
                onClick={() => setCurrentCategory('home')}
                className="flex items-center gap-1 bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] px-3.5 py-2 rounded-xl text-xs font-semibold transition-all duration-200"
              >
                <ArrowLeft size={14} />
                홈으로
              </button>
              <div className="bg-[var(--accent-3)]/25 p-2 rounded-xl text-[var(--accent-3)]">
                <Code size={20} />
              </div>
              <div>
                <h1 className="text-base font-bold tracking-wide text-[var(--accent-3)]">
                  파이썬 기초 문법
                </h1>
                <p className="text-[10px] text-[var(--muted)]">프로그래밍을 시작하는 분들을 위한 파이썬의 완전 기초 핵심 가이드</p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <div className="flex items-center gap-2 bg-[var(--bg)] p-1 rounded-xl border border-[var(--line)] overflow-x-auto">
                <button
                  onClick={() => setPythonViewType('basic')}
                  className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all duration-200 whitespace-nowrap ${pythonViewType === 'basic' ? 'bg-[var(--accent-3)] text-[var(--bg)] shadow-sm' : 'text-[var(--muted)] hover:text-[var(--text)]'}`}
                >
                  기초 문법
                </button>
                <button
                  onClick={() => setPythonViewType('playground')}
                  className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all duration-200 whitespace-nowrap ${pythonViewType === 'playground' ? 'bg-[var(--accent-3)] text-[var(--bg)] shadow-sm' : 'text-[var(--muted)] hover:text-[var(--text)]'}`}
                >
                  놀이터
                </button>
                <button
                  onClick={() => setPythonViewType('turtle')}
                  className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all duration-200 whitespace-nowrap ${pythonViewType === 'turtle' ? 'bg-[var(--accent-3)] text-[var(--bg)] shadow-sm' : 'text-[var(--muted)] hover:text-[var(--text)]'}`}
                >
                  거북이 교실
                </button>
                <button
                  onClick={() => setPythonViewType('turtle_adv')}
                  className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all duration-200 whitespace-nowrap ${pythonViewType === 'turtle_adv' ? 'bg-[var(--accent-3)] text-[var(--bg)] shadow-sm' : 'text-[var(--muted)] hover:text-[var(--text)]'}`}
                >
                  심화 아트
                </button>
                <button
                  onClick={() => setPythonViewType('pygame')}
                  className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all duration-200 whitespace-nowrap ${pythonViewType === 'pygame' ? 'bg-[var(--accent-3)] text-[var(--bg)] shadow-sm' : 'text-[var(--muted)] hover:text-[var(--text)]'}`}
                >
                  게임 만들기
                </button>
              </div>
              <button 
                onClick={toggleTheme}
                className="flex items-center justify-center bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] p-2 rounded-xl transition-all duration-200"
                title="테마 변경"
              >
                {theme === 'light' ? <Moon size={14} /> : <Sun size={14} />}
              </button>
            </div>
          </header>

          <iframe 
            key={pythonViewType}
            src={pythonViewType === 'basic' ? `/python_basic_reference.html?theme=${theme}` : pythonViewType === 'playground' ? `/python_playground.html?theme=${theme}` : pythonViewType === 'turtle' ? `/python_turtle.html?theme=${theme}` : pythonViewType === 'turtle_adv' ? `/python_turtle_adv.html?theme=${theme}` : `/python_pygame.html?theme=${theme}`} 
            className="w-full flex-1 border-0 bg-[var(--bg)]" 
          />
        </div>
      )}

      {/* ========================================================================= */}
      {/* 4. SQL BASIC VIEW */}
      {/* ========================================================================= */}
      {currentCategory === 'sql_basic' && (
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Header */}
          <header className="border-b border-[var(--line)] bg-[var(--panel-2)] px-6 py-4 flex items-center justify-between shrink-0">
            <div className="flex items-center gap-3">
              <button 
                onClick={() => setCurrentCategory('home')}
                className="flex items-center gap-1 bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] px-3.5 py-2 rounded-xl text-xs font-semibold transition-all duration-200"
              >
                <ArrowLeft size={14} />
                홈으로
              </button>
              <div className="bg-[var(--accent)]/25 p-2 rounded-xl text-[var(--accent)]">
                <Database size={20} />
              </div>
              <div>
                <h1 className="text-base font-bold tracking-wide text-[var(--accent)]">
                  SQL 기초
                </h1>
                <p className="text-[10px] text-[var(--muted)]">SQL의 기초 구조 및 웹 해킹 입문을 위한 SQL Injection 가이드</p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <button 
                onClick={toggleTheme}
                className="flex items-center justify-center bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] p-2 rounded-xl transition-all duration-200"
                title="테마 변경"
              >
                {theme === 'light' ? <Moon size={14} /> : <Sun size={14} />}
              </button>
            </div>
          </header>

          <iframe 
            src={`/sql_injection_easy.html?theme=${theme}`} 
            className="w-full flex-1 border-0 bg-[var(--bg)]" 
          />
        </div>
      )}

      {/* ========================================================================= */}
      {/* 5. SQL ADVANCED VIEW */}
      {/* ========================================================================= */}
      {currentCategory === 'sql_advanced' && (
        <div className="flex-1 flex flex-col overflow-hidden">
          {/* Header */}
          <header className="border-b border-[var(--line)] bg-[var(--panel-2)] px-6 py-4 flex items-center justify-between shrink-0">
            <div className="flex items-center gap-3">
              <button 
                onClick={() => setCurrentCategory('home')}
                className="flex items-center gap-1 bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] px-3.5 py-2 rounded-xl text-xs font-semibold transition-all duration-200"
              >
                <ArrowLeft size={14} />
                홈으로
              </button>
              <div className="bg-[#b4befe]/25 p-2 rounded-xl text-[#b4befe]">
                <Sparkles size={20} />
              </div>
              <div>
                <h1 className="text-base font-bold tracking-wide text-[#b4befe]">
                  SQL 심화
                </h1>
                <p className="text-[10px] text-[var(--muted)]">Blind SQL Injection 및 고급 웹 DB 해킹 기법과 대응 방안 총정리</p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <button 
                onClick={toggleTheme}
                className="flex items-center justify-center bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] p-2 rounded-xl transition-all duration-200"
                title="테마 변경"
              >
                {theme === 'light' ? <Moon size={14} /> : <Sun size={14} />}
              </button>
            </div>
          </header>

          <iframe 
            src={`/sql_injection_reference.html?theme=${theme}`} 
            className="w-full flex-1 border-0 bg-[var(--bg)]" 
          />
        </div>
      )}

      {/* Concept Summary Modal Dialog */}
      {showConceptModal && pendingProblem && (() => {
        const summary = getConceptSummaryForProblem(pendingProblem);
        return (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
            <div className="w-full max-w-lg bg-[var(--panel-2)] border border-[var(--line)] rounded-2xl overflow-hidden flex flex-col shadow-2xl">
              <div className="bg-[var(--panel)] px-6 py-4 flex items-center justify-between border-b border-[var(--line)]">
                <div className="flex items-center gap-2">
                  <div className="bg-[var(--accent-2)]/10 text-[var(--accent-2)] p-1.5 rounded-lg">
                    <BookOpen size={16} />
                  </div>
                  <h3 className="text-base font-bold text-[var(--text)]">💡 핵심 개념 요약 노트</h3>
                </div>
                <button 
                  onClick={() => setShowConceptModal(false)}
                  className="text-[var(--muted)] hover:text-[var(--text)] transition-colors"
                >
                  <X size={18} />
                </button>
              </div>

              <div className="p-6 space-y-5 overflow-y-auto max-h-[70vh]">
                <div>
                  <span className="text-[10px] uppercase font-bold text-[var(--accent-2)] bg-[var(--accent-2)]/10 px-2.5 py-1 rounded-full">
                    {summary.title}
                  </span>
                  <h4 className="text-base font-bold text-[var(--text)] mt-2">
                    {pendingProblem.title}
                  </h4>
                </div>

                <div className="bg-[var(--panel)] p-4 rounded-xl border border-[var(--line)] space-y-2">
                  <h5 className="text-xs font-bold text-[var(--muted)] uppercase tracking-wider mb-2">핵심 체크포인트</h5>
                  <ul className="space-y-1.5 text-xs text-[var(--text)] leading-relaxed">
                    {summary.points.map((pt, idx) => (
                      <li key={idx} className="flex gap-2 items-start">
                        <span className="text-[var(--accent-2)] font-bold mt-0.5">•</span>
                        <span>{pt}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div>
                  <h5 className="text-xs font-bold text-[var(--muted)] uppercase tracking-wider mb-2">참고 코드 스니펫</h5>
                  <pre className="bg-[var(--panel)] p-3 rounded-xl border border-[var(--line)] text-[11px] font-mono text-[var(--text)] overflow-x-auto leading-relaxed">
                    <code>{summary.code}</code>
                  </pre>
                </div>
              </div>

              <div className="px-6 py-4 bg-[var(--panel)] border-t border-[var(--line)] flex justify-end gap-3">
                <button 
                  onClick={() => setShowConceptModal(false)}
                  className="bg-[var(--line)] hover:bg-[var(--line-hover)] text-[var(--text)] px-4 py-2 rounded-xl text-xs font-semibold transition-colors"
                >
                  닫기
                </button>
                <button 
                  onClick={() => {
                    handleSelectProblemDirect(pendingProblem);
                    setShowConceptModal(false);
                  }}
                  className="bg-[var(--accent-3)] hover:bg-[#b4befe] text-[var(--bg)] px-5 py-2 rounded-xl text-xs font-bold transition-colors flex items-center gap-1"
                >
                  <Play size={12} />
                  문제 풀러가기
                </button>
              </div>
            </div>
          </div>
        );
      })()}
      {/* Add Problem Modal Dialog */}
      {isAddModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
          <div className="w-full max-w-2xl bg-[var(--panel-2)] border border-[var(--line)] rounded-2xl overflow-hidden flex flex-col max-h-[90vh]">
            <div className="bg-[var(--panel)] px-6 py-4 flex items-center justify-between border-b border-[var(--line)]">
              <h3 className="text-lg font-bold text-[var(--accent-3)]">새 문제 추가</h3>
              <button 
                onClick={() => setIsAddModalOpen(false)}
                className="text-[var(--muted)] hover:text-white transition-colors"
              >
                <X size={20} />
              </button>
            </div>

            <form onSubmit={handleAddProblem} className="flex-1 overflow-y-auto p-6 space-y-4">
              <div>
                <label className="block text-xs font-bold uppercase text-[var(--muted)] mb-1">문제 제목</label>
                <input 
                  type="text" 
                  placeholder="예: 문제 11 - 제목"
                  value={newTitle}
                  onChange={(e) => setNewTitle(e.target.value)}
                  className="w-full bg-[var(--bg)] border border-[var(--line)] rounded-xl px-4 py-2.5 text-sm text-[var(--text)] focus:outline-none focus:border-[var(--accent-3)]"
                  required
                />
              </div>

              <div className="flex gap-4">
                <div className="flex-1">
                  <label className="block text-xs font-bold uppercase text-[var(--muted)] mb-1">문제 유형</label>
                  <select 
                    value={newType}
                    onChange={(e) => setNewType(e.target.value as "code" | "blank")}
                    className="w-full bg-[var(--bg)] border border-[var(--line)] rounded-xl px-4 py-2.5 text-sm text-[var(--text)] focus:outline-none focus:border-[var(--accent-3)]"
                  >
                    <option value="code">소스코드 작성</option>
                    <option value="blank">빈칸 채우기</option>
                  </select>
                </div>
                <div className="flex-1">
                  <label className="block text-xs font-bold uppercase text-[var(--muted)] mb-1">급수 선택</label>
                  <select 
                    value={newClassLevel}
                    onChange={(e) => setNewClassLevel(Number(e.target.value) as 2 | 3)}
                    className="w-full bg-[var(--bg)] border border-[var(--line)] rounded-xl px-4 py-2.5 text-sm text-[var(--text)] focus:outline-none focus:border-[var(--accent-3)]"
                  >
                    <option value={3}>COS Pro 3급</option>
                    <option value={2}>COS Pro 2급</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase text-[var(--muted)] mb-1">문제 설명</label>
                <textarea 
                  rows={4}
                  value={newDesc}
                  onChange={(e) => setNewDesc(e.target.value)}
                  className="w-full bg-[var(--bg)] border border-[var(--line)] rounded-xl px-4 py-2.5 text-sm text-[var(--text)] focus:outline-none focus:border-[var(--accent-3)] font-sans"
                  required
                />
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-bold uppercase text-[var(--muted)] mb-1">입력 설명</label>
                  <textarea 
                    rows={2}
                    value={newInDesc}
                    onChange={(e) => setNewInDesc(e.target.value)}
                    className="w-full bg-[var(--bg)] border border-[var(--line)] rounded-xl px-4 py-2 text-sm text-[var(--text)] focus:outline-none focus:border-[var(--accent-3)]"
                  />
                </div>
                <div>
                  <label className="block text-xs font-bold uppercase text-[var(--muted)] mb-1">출력 설명</label>
                  <textarea 
                    rows={2}
                    value={newOutDesc}
                    onChange={(e) => setNewOutDesc(e.target.value)}
                    className="w-full bg-[var(--bg)] border border-[var(--line)] rounded-xl px-4 py-2 text-sm text-[var(--text)] focus:outline-none focus:border-[var(--accent-3)]"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase text-[var(--muted)] mb-1">제공 코드 / 기본 템플릿</label>
                <textarea 
                  rows={4}
                  value={newStarter}
                  onChange={(e) => setNewStarter(e.target.value)}
                  className="w-full bg-[var(--bg)] border border-[var(--line)] rounded-xl p-3 text-xs text-[var(--accent)] font-mono focus:outline-none focus:border-[var(--accent-3)]"
                />
              </div>

              <div>
                <label className="block text-xs font-bold uppercase text-[var(--muted)] mb-1">
                  테스트 케이스 JSON 리스트
                </label>
                <textarea 
                  rows={4}
                  value={newTestCases}
                  onChange={(e) => setNewTestCases(e.target.value)}
                  className="w-full bg-[var(--bg)] border border-[var(--line)] rounded-xl p-3 text-xs text-[var(--accent-2)] font-mono focus:outline-none focus:border-[var(--accent-3)]"
                  required
                />
              </div>

              <div className="pt-4 border-t border-[var(--line)] flex justify-end">
                <button 
                  type="submit"
                  className="bg-[var(--accent-3)] hover:bg-[#b4befe] text-[var(--bg)] px-6 py-2.5 rounded-xl text-sm font-bold transition-colors"
                >
                  문제 저장하기
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* ALGORITHM SIMULATION VIEW */}
      {/* ========================================================================= */}
      {currentCategory === 'algorithm' && (
        <div className="flex-1 flex flex-col w-full h-full relative">
          <header className="border-b border-[var(--line)] bg-[var(--panel-2)] px-6 py-4 flex items-center justify-between shrink-0">
            <div className="flex items-center gap-3">
              <button 
                onClick={() => setCurrentCategory('home')}
                className="flex items-center gap-1.5 bg-[var(--line)] border border-[var(--line-hover)] hover:bg-[var(--line-hover)] text-[var(--text)] px-3.5 py-2 rounded-xl text-xs font-semibold transition-all duration-200"
              >
                <ArrowLeft size={14} />
                홈으로
              </button>
              <div className="bg-[#f38ba8]/20 p-2 rounded-xl text-[#f38ba8]">
                <Sparkles size={20} />
              </div>
              <div>
                <h1 className="text-base font-bold tracking-wide text-[#f38ba8] flex items-center gap-2">
                  알고리즘 시뮬레이션
                </h1>
                <p className="text-[10px] text-[var(--muted)]">DFS / BFS 탐색 시뮬레이터</p>
              </div>
            </div>

            <div className="flex items-center gap-2 bg-[var(--bg)] p-1 rounded-xl border border-[var(--line)] overflow-x-auto">
              <button
                onClick={() => setAlgoType('bfs')}
                className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all duration-200 whitespace-nowrap ${algoType === 'bfs' ? 'bg-[#f38ba8] text-[var(--bg)] shadow-sm' : 'text-[var(--muted)] hover:text-[var(--text)]'}`}
              >
                BFS 탐색
              </button>
              <button
                onClick={() => setAlgoType('dfs')}
                className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all duration-200 whitespace-nowrap ${algoType === 'dfs' ? 'bg-[#f38ba8] text-[var(--bg)] shadow-sm' : 'text-[var(--muted)] hover:text-[var(--text)]'}`}
              >
                DFS 탐색
              </button>
              <button
                onClick={() => setAlgoType('minesweeper')}
                className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all duration-200 whitespace-nowrap ${algoType === 'minesweeper' ? 'bg-[#f38ba8] text-[var(--bg)] shadow-sm' : 'text-[var(--muted)] hover:text-[var(--text)]'}`}
              >
                지뢰찾기 확산
              </button>
            </div>
          </header>
          
          <div className="flex-1 bg-[var(--bg)] w-full relative">
            <iframe
              key={algoType}
              src={algoType === 'bfs' ? "/bfs_dfs.html" : algoType === 'dfs' ? "/dfs.html" : "/minesweeper.html"}
              className="absolute inset-0 w-full h-full border-none"
              title="Algorithm Simulation"
            />
          </div>
        </div>
      )}
    </main>
  );
}
