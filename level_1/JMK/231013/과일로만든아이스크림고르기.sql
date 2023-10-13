-- 예상 시간복잡도: O(NlogN)

SELECT I.FLAVOR FROM ICECREAM_INFO AS I
INNER JOIN FIRST_HALF AS F ON I.FLAVOR = F.FLAVOR
WHERE F.TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY F.TOTAL_ORDER DESC;
