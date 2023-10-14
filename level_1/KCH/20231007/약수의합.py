# 예상 시간복잡도: O(logN)
def solution(n):
    answer = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            answer += i
            answer += n//i
    return answer
