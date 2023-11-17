# 예상 시간복잡도: O(N)
def solution(clothes):
    closet = dict()
    for _, cloth_type in clothes:
        if cloth_type in closet:
            closet[cloth_type] += 1
        else:
            closet[cloth_type] =1
        
    res = 1
    for v in closet.values():
        res *= (v+1)
    return res-1
