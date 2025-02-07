/*
SELECT 문제로 특정 열의 값을 이진수로 변환하여 2번째 자리가 1이면 안되고 1번째 or 3번째 자리가 1인
열들을 COUNT해서 COUNT로 출력

*/
--제출 정답--
SELECT COUNT(*) COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0
AND ((GENOTYPE & 1) = 1 OR (GENOTYPE & 4) = 4);

--실패했던던 정답--
SELECT COUNT(*) COUNT
FROM ECOLI_DATA
WHERE BIN(GENOTYPE) LIKE '%1__'
AND BIN(GENOTYPE) LIKE '%1'
OR BIN(GENOTYPE) NOT LIKE '%1_';

--이유--
/*
1번째와 3번째가 1이면 되고 2번째만 1이 아니면 되기에 처음부터 칸을 정해놓고 계산해내면 되리라 생각했지만
1번째와 3번째가 OR로 묶이고 그리고 2가 1이 아닌 상황이 AND로 묶여야 했는데 각각의 상황이 되어 실패
*/