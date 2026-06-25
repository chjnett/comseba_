"use client";

import React, { useState, useEffect, useRef } from "react";
import Script from "next/script";
import Editor from "@monaco-editor/react";
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
  FileCode2
} from "lucide-react";
import { problems as initialProblems, Problem, Example } from "@/data/problems";

// Helper to sanitize python inputs for builtin.input mock
function preparePythonRunner(code: string, inputLines: string[]): string {
  const jsonInputs = JSON.stringify(inputLines);
  return `
import builtins
import json

inputs = json.loads('''${jsonInputs}''')
input_idx = 0

def mock_input(prompt=''):
    global input_idx
    if input_idx < len(inputs):
        val = inputs[input_idx]
        input_idx += 1
        return val
    raise EOFError("EOF when reading a line")

builtins.input = mock_input

# User code follows
${code}
`;
}

export default function Home() {
  const [isMounted, setIsMounted] = useState(false);
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

  // New Problem Form States
  const [newTitle, setNewTitle] = useState("");
  const [newType, setNewType] = useState<"code" | "blank">("code");
  const [newClassLevel, setNewClassLevel] = useState<2 | 3>(3);
  const [newDesc, setNewDesc] = useState("");
  const [newInDesc, setNewInDesc] = useState("");
  const [newOutDesc, setNewOutDesc] = useState("");
  const [newStarter, setNewStarter] = useState("");
  const [newTestCases, setNewTestCases] = useState("[\n  {\n    \"input\": \"입력값\",\n    \"output\": \"출력값\"\n  }\n]");
  
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

  // Update editor code when current problem changes
  const handleSelectProblem = (prob: Problem) => {
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

    // Setup stdout capture in Pyodide
    let stdout = "";
    py.setStdout({
      batched: (text: string) => {
        stdout += text + "\n";
      }
    });

    try {
      await py.runPythonAsync(prepCode);
      return { stdout, stderr: "" };
    } catch (err: any) {
      return { stdout, stderr: err.message };
    }
  };

  // Compare actual vs expected
  const checkMatch = (actual: string, expected: string): boolean => {
    const actualLines = actual.trim().split("\n").map(l => l.trim()).filter(Boolean);
    const expectedLines = expected.trim().split("\n").map(l => l.trim()).filter(Boolean);
    
    if (actualLines.length >= expectedLines.length) {
      const sliced = actualLines.slice(-expectedLines.length);
      return sliced.every((val, idx) => val === expectedLines[idx]);
    }
    return false;
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

  return (
    <main className="min-h-screen bg-[#11121d] text-[#cdd6f4] font-sans flex flex-col">
      <Script 
        src="https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js" 
        strategy="afterInteractive"
        onLoad={initPyodide}
      />

      {/* Header Bar */}
      <header className="border-b border-[#25283c] bg-[#161725] px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="bg-[#89b4fa] p-2 rounded-xl text-[#11121d]">
            <FileCode2 size={24} />
          </div>
          <div>
            <h1 className="text-lg font-bold tracking-wide text-[#89b4fa]">
              COS Pro {selectedClass}급 Python Online Judge
            </h1>
            <p className="text-xs text-[#a6adc8]">Pure Web Online Judge - No DB Connection Required</p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          {/* Class Level Selector */}
          <div className="flex bg-[#25283c] p-1 rounded-xl border border-[#313552]">
            <button
              onClick={() => {
                setSelectedClass(3);
                const class3 = problems.filter(p => (p.classLevel || 3) === 3);
                if (class3.length > 0) {
                  handleSelectProblem(class3[0]);
                }
              }}
              className={"px-4 py-1.5 rounded-lg text-sm font-bold transition-all duration-200 " + (
                selectedClass === 3
                  ? "bg-[#89b4fa] text-[#11121d]"
                  : "text-[#a6adc8] hover:text-[#cdd6f4]"
              )}
            >
              COS Pro 3급
            </button>
            <button
              onClick={() => {
                setSelectedClass(2);
                const class2 = problems.filter(p => (p.classLevel || 3) === 2);
                if (class2.length > 0) {
                  handleSelectProblem(class2[0]);
                }
              }}
              className={"px-4 py-1.5 rounded-lg text-sm font-bold transition-all duration-200 " + (
                selectedClass === 2
                  ? "bg-[#89b4fa] text-[#11121d]"
                  : "text-[#a6adc8] hover:text-[#cdd6f4]"
              )}
            >
              COS Pro 2급
            </button>
          </div>

          <button 
            onClick={handleAdminToggle}
            className={"flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-semibold border transition-all duration-200 " + (
              isAdmin 
                ? "bg-[#f5c2e7] text-[#11121d] border-[#f5c2e7] hover:bg-[#f2cdcd] hover:border-[#f2cdcd]" 
                : "bg-[#25283c] text-[#a6adc8] border-[#313552] hover:bg-[#313552] hover:text-white"
            )}
          >
            <span>{isAdmin ? "관리자 로그아웃" : "관리자 로그인"}</span>
          </button>

          <button 
            onClick={() => setIsAddModalOpen(true)}
            className="flex items-center gap-2 bg-[#25283c] border border-[#313552] hover:bg-[#313552] text-[#f5c2e7] px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-200"
          >
            <Plus size={16} />
            새 문제 추가
          </button>
        </div>
      </header>

      {/* Main Panel split */}
      <div className="flex-1 flex flex-col lg:flex-row overflow-hidden">
        {/* Left Side: Sidebar Problems List */}
        <aside className="w-full lg:w-80 border-r border-[#25283c] bg-[#161725] flex flex-col shrink-0">
          <div className="p-4 border-b border-[#25283c] flex items-center justify-between">
            <span className="text-sm font-bold text-[#89b4fa] flex items-center gap-1.5">
              <BookOpen size={16} /> {selectedClass}급 문제 목록 ({problems.filter(p => (p.classLevel || 3) === selectedClass).length})
            </span>
          </div>

          <div className="flex-1 overflow-y-auto p-2 space-y-1 max-h-[250px] lg:max-h-none">
            {problems
              .filter((p) => (p.classLevel || 3) === selectedClass)
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
                        ? "bg-[#25283c] border border-[#89b4fa]/20 text-[#89b4fa]" 
                        : "hover:bg-[#1e1f2f] text-[#cdd6f4]"
                    )}
                  >
                    <div className="flex-1 min-w-0 pr-2">
                      <h3 className="text-sm font-semibold truncate">{prob.title}</h3>
                      <span className="text-[10px] uppercase font-bold text-[#a6adc8] bg-[#25283c] px-2 py-0.5 rounded-full mt-1 inline-block">
                        {prob.type === "blank" ? "빈칸 채우기" : "소스코드 작성"}
                      </span>
                    </div>

                    <div>
                      {probStatus === "Solved" ? (
                        <CheckCircle2 size={18} className="text-[#a6e3a1]" />
                      ) : probStatus === "Attempted" ? (
                        <AlertTriangle size={18} className="text-[#f9e2af]" />
                      ) : (
                        <HelpCircle size={18} className="text-[#6c7086]" />
                      )}
                    </div>
                  </button>
                );
              })}
          </div>
        </aside>

        {/* Right Side: Main Workstation Split */}
        <div className="flex-1 flex flex-col xl:flex-row overflow-hidden min-w-0">
          
          {/* Left panel: Problem details */}
          <div 
            className="border-b xl:border-b-0 xl:border-r border-[#25283c] bg-[#11121d] overflow-y-auto flex flex-col p-6 min-w-0 shrink-0"
            style={{ width: isMounted ? leftWidth + "%" : '45%' }}
          >
            <h2 className="text-xl font-bold text-[#89b4fa] border-b border-[#25283c] pb-3 mb-4">
              {currentProblem.title}
            </h2>

            <div className="space-y-6 text-[#cdd6f4]">
              {/* Problem Statement */}
              <div>
                <h4 className="text-sm font-bold text-[#89b4fa] mb-2 uppercase tracking-wide">■ 문제 설명</h4>
                <p className="text-sm leading-relaxed whitespace-pre-line text-[#a6adc8]">
                  {currentProblem.description}
                </p>
              </div>

              {/* Input Description */}
              {currentProblem.input_desc && (
                <div>
                  <h4 className="text-sm font-bold text-[#89b4fa] mb-2 uppercase tracking-wide">■ 입력 설명</h4>
                  <p className="text-sm text-[#a6adc8]">{currentProblem.input_desc}</p>
                </div>
              )}

              {/* Output Description */}
              {currentProblem.output_desc && (
                <div>
                  <h4 className="text-sm font-bold text-[#89b4fa] mb-2 uppercase tracking-wide">■ 출력 설명</h4>
                  <p className="text-sm text-[#a6adc8]">{currentProblem.output_desc}</p>
                </div>
              )}

              {/* Examples IO */}
              <div>
                <h4 className="text-sm font-bold text-[#89b4fa] mb-3 uppercase tracking-wide">■ 입출력 예</h4>
                <div className="space-y-4">
                  {currentProblem.examples.map((ex, index) => {
                    const exId = `ex-${currentProblem.id}-${index}`;
                    return (
                      <div key={index} className="bg-[#161725] border border-[#25283c] rounded-xl overflow-hidden">
                        <div className="bg-[#1e1f2f] px-4 py-2 text-xs font-semibold text-[#a6adc8] flex items-center justify-between border-b border-[#25283c]">
                          <span>예제 {index + 1}</span>
                        </div>
                        
                        <div className="grid grid-cols-1 md:grid-cols-2 divide-y md:divide-y-0 md:divide-x divide-[#25283c]">
                          <div className="p-4">
                            <div className="flex items-center justify-between mb-1">
                              <span className="text-xs text-[#a6adc8] font-bold">입력</span>
                              <button 
                                onClick={() => copyToClipboard(ex.input, exId + "-in")}
                                className="text-[#a6adc8] hover:text-[#89b4fa] transition-colors"
                              >
                                {copiedId === exId + "-in" ? <Check size={14} /> : <Copy size={14} />}
                              </button>
                            </div>
                            <pre className="text-xs font-mono bg-[#11121d] p-3 rounded-lg text-[#a6e3a1] overflow-x-auto whitespace-pre-wrap">
                              {ex.input}
                            </pre>
                          </div>

                          <div className="p-4">
                            <div className="flex items-center justify-between mb-1">
                              <span className="text-xs text-[#a6adc8] font-bold">출력</span>
                              <button 
                                onClick={() => copyToClipboard(ex.output, exId + "-out")}
                                className="text-[#a6adc8] hover:text-[#89b4fa] transition-colors"
                              >
                                {copiedId === exId + "-out" ? <Check size={14} /> : <Copy size={14} />}
                              </button>
                            </div>
                            <pre className="text-xs font-mono bg-[#11121d] p-3 rounded-lg text-[#f5c2e7] overflow-x-auto whitespace-pre-wrap">
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
                <div className="mt-6 border-t border-[#f5c2e7]/30 pt-4">
                  <div className="flex items-center justify-between mb-2">
                    <h4 className="text-sm font-bold text-[#f5c2e7] uppercase tracking-wide">■ 관리자용 정답 및 해설</h4>
                    <button 
                      onClick={() => copyToClipboard(currentProblem.solution_code!, "admin-sol")}
                      className="flex items-center gap-1 text-xs text-[#a6adc8] hover:text-[#f5c2e7] transition-colors bg-[#1e1f2f] px-2.5 py-1.5 rounded-lg border border-[#25283c]"
                    >
                      {copiedId === "admin-sol" ? <Check size={12} /> : <Copy size={12} />}
                      <span>정답 복사</span>
                    </button>
                  </div>
                  <pre className="text-xs font-mono bg-[#161725] border border-[#25283c] p-4 rounded-xl text-[#a6e3a1] overflow-x-auto whitespace-pre-wrap leading-relaxed">
                    {currentProblem.solution_code}
                  </pre>
                </div>
              )}
            </div>
          </div>

          {/* Horizontal Split Handler (Visible on xl screens only) */}
          <div 
            onMouseDown={startResizingWidth}
            className="hidden xl:flex w-1.5 hover:w-2 bg-[#25283c] hover:bg-[#89b4fa] cursor-col-resize justify-center items-center select-none transition-all duration-150 group shrink-0"
          >
            <div className="w-0.5 h-8 bg-[#6c7086] group-hover:bg-[#11121d] rounded-full"></div>
          </div>

          {/* Right panel: Code Editor & Console Output */}
          <div className="flex-1 flex flex-col bg-[#161725] min-w-0">
            {/* Editor Header */}
            <div className="border-b border-[#25283c] px-4 py-3 flex items-center justify-between">
              <span className="text-sm font-bold text-[#89b4fa] flex items-center gap-1.5">
                <Code size={16} /> Python 코드 편집기
              </span>
              <button
                onClick={handleReset}
                className="flex items-center gap-1 bg-[#25283c] hover:bg-[#313552] border border-[#313552] text-xs text-[#cdd6f4] px-3 py-1.5 rounded-lg transition-colors"
              >
                <RotateCcw size={12} />
                초기화
              </button>
            </div>

            {/* Monaco Editor Container */}
            <div className="flex-1 min-h-[200px] border-b border-[#25283c]">
              <Editor
                height="100%"
                language="python"
                theme="vs-dark"
                value={code}
                onChange={handleCodeChange}
                options={{
                  fontFamily: "Menlo, Monaco, Consolas, 'Courier New', monospace",
                  fontSize: 14,
                  minimap: { enabled: false },
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

            {/* Vertical Split Handler */}
            <div 
              onMouseDown={startResizingConsole}
              className="h-1.5 hover:h-2 bg-[#25283c] hover:bg-[#89b4fa] cursor-row-resize flex justify-center items-center select-none transition-all duration-150 group shrink-0"
            >
              <div className="w-12 h-0.5 bg-[#6c7086] group-hover:bg-[#11121d] rounded-full"></div>
            </div>

            {/* Console and Grading Section */}
            <div className="flex flex-col bg-[#11121d] shrink-0" style={{ height: consoleHeight + "px" }}>
              <div className="border-b border-[#25283c] bg-[#161725] px-4 py-3 flex items-center justify-between">
                <span className="text-sm font-bold text-[#a6adc8] flex items-center gap-1.5">
                  <Terminal size={16} /> 실행 결과 및 콘솔
                </span>
                
                <div className="flex items-center gap-2">
                  <button
                    onClick={handleRunTests}
                    disabled={running}
                    className="flex items-center gap-1.5 bg-[#25283c] hover:bg-[#313552] border border-[#313552] disabled:opacity-50 text-sm text-[#a6e3a1] px-4 py-2 rounded-xl font-bold transition-colors"
                  >
                    <Play size={14} />
                    테스트 실행
                  </button>

                  <button
                    onClick={handleSubmit}
                    disabled={running}
                    className="flex items-center gap-1.5 bg-[#a6e3a1] hover:bg-[#89d587] disabled:opacity-50 text-sm text-[#11121d] px-5 py-2 rounded-xl font-bold transition-colors"
                  >
                    <Send size={14} />
                    제출 및 채점
                  </button>
                </div>
              </div>

              {/* Console Logs Output */}
              <div className="flex-1 overflow-y-auto p-4 font-mono text-sm space-y-1">
                {consoleLogs.length === 0 ? (
                  <span className="text-[#585b70]">코드를 실행하거나 제출하면 여기에 결과가 표시됩니다.</span>
                ) : (
                  consoleLogs.map((log, idx) => {
                    let color = "text-[#cdd6f4]";
                    if (log.type === "success") color = "text-[#a6e3a1] font-bold";
                    if (log.type === "error") color = "text-[#f38ba8]";
                    if (log.type === "info") color = "text-[#89b4fa]";
                    if (log.type === "muted") color = "text-[#6c7086]";

                    return (
                      <div key={idx} className={color + " whitespace-pre-wrap"}>
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

      {/* Add Problem Modal Dialog */}
      {isAddModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
          <div className="w-full max-w-2xl bg-[#161725] border border-[#25283c] rounded-2xl overflow-hidden flex flex-col max-h-[90vh]">
            <div className="bg-[#1e1f2f] px-6 py-4 flex items-center justify-between border-b border-[#25283c]">
              <h3 className="text-lg font-bold text-[#89b4fa]">새 문제 추가</h3>
              <button 
                onClick={() => setIsAddModalOpen(false)}
                className="text-[#a6adc8] hover:text-white transition-colors"
              >
                <X size={20} />
              </button>
            </div>

            <form onSubmit={handleAddProblem} className="flex-1 overflow-y-auto p-6 space-y-4">
              <div>
                <label className="block text-xs font-bold uppercase text-[#a6adc8] mb-1">문제 제목</label>
                <input 
                  type="text" 
                  placeholder="예: 문제 11 - 제목"
                  value={newTitle}
                  onChange={(e) => setNewTitle(e.target.value)}
                  className="w-full bg-[#11121d] border border-[#25283c] rounded-xl px-4 py-2.5 text-sm text-[#cdd6f4] focus:outline-none focus:border-[#89b4fa]"
                  required
                />
              </div>

              <div className="flex gap-4">
                <div className="flex-1">
                  <label className="block text-xs font-bold uppercase text-[#a6adc8] mb-1">문제 유형</label>
                  <select 
                    value={newType}
                    onChange={(e) => setNewType(e.target.value as "code" | "blank")}
                    className="w-full bg-[#11121d] border border-[#25283c] rounded-xl px-4 py-2.5 text-sm text-[#cdd6f4] focus:outline-none focus:border-[#89b4fa]"
                  >
                    <option value="code">소스코드 작성</option>
                    <option value="blank">빈칸 채우기</option>
                  </select>
                </div>
                <div className="flex-1">
                  <label className="block text-xs font-bold uppercase text-[#a6adc8] mb-1">급수 선택</label>
                  <select 
                    value={newClassLevel}
                    onChange={(e) => setNewClassLevel(Number(e.target.value) as 2 | 3)}
                    className="w-full bg-[#11121d] border border-[#25283c] rounded-xl px-4 py-2.5 text-sm text-[#cdd6f4] focus:outline-none focus:border-[#89b4fa]"
                  >
                    <option value={3}>COS Pro 3급</option>
                    <option value={2}>COS Pro 2급</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase text-[#a6adc8] mb-1">문제 설명</label>
                <textarea 
                  rows={4}
                  value={newDesc}
                  onChange={(e) => setNewDesc(e.target.value)}
                  className="w-full bg-[#11121d] border border-[#25283c] rounded-xl px-4 py-2.5 text-sm text-[#cdd6f4] focus:outline-none focus:border-[#89b4fa] font-sans"
                  required
                />
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-bold uppercase text-[#a6adc8] mb-1">입력 설명</label>
                  <textarea 
                    rows={2}
                    value={newInDesc}
                    onChange={(e) => setNewInDesc(e.target.value)}
                    className="w-full bg-[#11121d] border border-[#25283c] rounded-xl px-4 py-2 text-sm text-[#cdd6f4] focus:outline-none focus:border-[#89b4fa]"
                  />
                </div>
                <div>
                  <label className="block text-xs font-bold uppercase text-[#a6adc8] mb-1">출력 설명</label>
                  <textarea 
                    rows={2}
                    value={newOutDesc}
                    onChange={(e) => setNewOutDesc(e.target.value)}
                    className="w-full bg-[#11121d] border border-[#25283c] rounded-xl px-4 py-2 text-sm text-[#cdd6f4] focus:outline-none focus:border-[#89b4fa]"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase text-[#a6adc8] mb-1">제공 코드 / 기본 템플릿</label>
                <textarea 
                  rows={4}
                  value={newStarter}
                  onChange={(e) => setNewStarter(e.target.value)}
                  className="w-full bg-[#11121d] border border-[#25283c] rounded-xl p-3 text-xs text-[#a6e3a1] font-mono focus:outline-none focus:border-[#89b4fa]"
                />
              </div>

              <div>
                <label className="block text-xs font-bold uppercase text-[#a6adc8] mb-1">
                  테스트 케이스 JSON 리스트
                </label>
                <textarea 
                  rows={4}
                  value={newTestCases}
                  onChange={(e) => setNewTestCases(e.target.value)}
                  className="w-full bg-[#11121d] border border-[#25283c] rounded-xl p-3 text-xs text-[#f5c2e7] font-mono focus:outline-none focus:border-[#89b4fa]"
                  required
                />
              </div>

              <div className="pt-4 border-t border-[#25283c] flex justify-end">
                <button 
                  type="submit"
                  className="bg-[#89b4fa] hover:bg-[#b4befe] text-[#11121d] px-6 py-2.5 rounded-xl text-sm font-bold transition-colors"
                >
                  문제 저장하기
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </main>
  );
}
