# 예상 시간복잡도: O(1)
def solution(my_string, num1, num2):
    answer = ''.join([my_string[0:num1],my_string[num2],my_string[num1+1:num2],my_string[num1],my_string[num2+1:]])
    return answer
