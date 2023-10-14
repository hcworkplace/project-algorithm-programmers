-- 예상 시간복잡도: O(NKlogN), K:ICECREAM_INFO 행 수
SELECT FLAVOR FROM FIRST_HALF
WHERE TOTAL_ORDER > 3000
    and FLAVOR in (SELECT FLAVOR FROM ICECREAM_INFO 
        WHERE INGREDIENT_TYPE = 'fruit_based')
ORDER BY TOTAL_ORDER desc;

-- 예상 시간복잡도: O(NlogN)
SELECT FIRST_HALF.FLAVOR FROM FIRST_HALF
JOIN ICECREAM_INFO ON FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR
WHERE ICECREAM_INFO.INGREDIENT_TYPE = 'fruit_based'
AND FIRST_HALF.TOTAL_ORDER > 3000
ORDER BY FIRST_HALF.TOTAL_ORDER desc;
