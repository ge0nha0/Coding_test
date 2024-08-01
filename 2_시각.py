# 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하라
# 접근 방식 -> 3중 for + int -> str + 3이 있는지 찾기 
## 완전 탐색 알고리즘 -> Brute Forcing -> 100만 개 이하일 때 사용하면 적절
### input 5 -> output 11475

n = int(input())

cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in (str(i) + str(j) + str(k)):
                cnt += 1

print(cnt)