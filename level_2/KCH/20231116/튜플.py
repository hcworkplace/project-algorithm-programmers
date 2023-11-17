# 예상 시간복잡도: O(N)
def solution(s):
    res = []
    ex = {}
    for s in sorted(s[2:-2].split('},{'), key=lambda x:len(x)):
        now = set(s.split(','))
        res.append(int((now - set(ex))))
        ex = now
    return res
