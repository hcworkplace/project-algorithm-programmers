# 예상 시간복잡도: O(n)
def solution(my_string, n):
    answer = ''
    for i in range (0, n,1):
        answer = answer + my_string[i]
    return answer

