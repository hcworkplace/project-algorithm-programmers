# 예상 시간복잡도: O(N)
def solution(arr):
    for i in range(len(arr)):
        if arr[i]%2 == 0 and arr[i]>=50:
            arr[i] //=2
        elif arr[i]%2 == 1 and arr[i]<50:
            arr[i] *= 2
    return arr
