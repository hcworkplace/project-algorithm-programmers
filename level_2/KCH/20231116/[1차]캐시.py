# 맞왜틀? ㅜㅜ 
def solution(cacheSize, cities):
    op = lambda x: x.lower()
    cities_dict = {k:0 for k in set(map(op, cities))}
    res = 0
    window = 0
    
    for i in range(len(cities)):
        city = cities[i].lower()
        if cities_dict[city] == 0 or cities_dict[city] + cacheSize + window < i+1 : # cache miss
            cities_dict[city] = i+1 # latest used
            res += 5
            window = 0
            
        else: #cache hit
            cities_dict[city] = i+1
            res += 1
            window += 1
        
    return res