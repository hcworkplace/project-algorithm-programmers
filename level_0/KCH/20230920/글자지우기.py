# 예상 시간복잡도: O(N)
def solution(my_string, indices):
    my_string = list(my_string)
    for idx in indices:
        my_string[idx] = ''
    
    return ''.join(my_string)
