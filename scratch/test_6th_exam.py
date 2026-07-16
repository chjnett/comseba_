# Verification script for 6th Mock Exam problems

def test_problem_1():
    # 기온이 높았던 날 구하기
    def solution(temperature, A, B):
        answer = 0
        for i in range(A+1, B):
            if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
                answer += 1
        return answer
    
    # Test cases
    assert solution([3, 2, 1, 5, 4, 3, 3, 2], 1, 6) == 2
    # Case 2: [10, 20, 30, 40, 50] with A=0, B=4 should yield 0 since B (50) is max
    print("Problem 1: case 1 passed")
    try:
        assert solution([10, 20, 30, 40, 50], 0, 4) == 3
    except AssertionError:
        print("Problem 1: case 2 FAILED (expected 3 but got", solution([10, 20, 30, 40, 50], 0, 4), ")")

def test_problem_6():
    # 비밀번호 조건 검사
    def solution(password):
        capital_count, small_count, digit_count = 0, 0, 0
        for p in password:
            if p >= 'A' and p <= 'Z':
                capital_count += 1
            elif p >= 'a' and p <= 'z':
                small_count += 1
            elif p >= '0' and p <= '9':
                digit_count += 1
        if capital_count >= 1 and small_count >= 2 and digit_count >= 2:
            answer = True
        else:
            answer = False
        return answer
    
    print("Problem 6: Ab12c returns", solution("Ab12c"))
    print("Problem 6: Pass12ord returns", solution("Pass12ord"))
    print("Problem 6: Aab12 returns", solution("Aab12"))

def test_problem_10():
    # 불량 사과 박스
    def solution(weight, boxes):
        answer = 0
        for x in boxes:
            if x < weight * 9 / 10 or x > weight * 11 / 10:
                answer += 1
        return answer
    
    # Case 3: 200, boxes = [200, 190, 210, 180, 220]
    print("Problem 10: case 3 returns", solution(200, [200, 190, 210, 180, 220]))

if __name__ == "__main__":
    test_problem_1()
    test_problem_6()
    test_problem_10()
