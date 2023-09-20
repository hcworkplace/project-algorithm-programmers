# 예상 시간복잡도: O(n)

def solution(arr, flag):
    ans = []
    for i in range(len(arr)):
        if flag[i]==True:
            ans += [arr[i]]*(arr[i]*2)
        else:
            ans = ans[:-arr[i]]
    return ans

