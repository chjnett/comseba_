def solution(weight, boxes):
    answer = 0
    for x in boxes:
        if x < weight * 9 / 10 or x > weight * 11 / 10:
            answer += 1
    return answer

print("Test Case 1:")
print("Result:", solution(100, [90, 91, 89, 110, 111]))

print("Test Case 2:")
print("Result:", solution(50, [45, 55, 44, 56]))

print("Test Case 3:")
print("Result:", solution(200, [200, 190, 210, 179, 221]))
