# https://www.acmicpc.net/problem/18353 
# 참고 https://wooono.tistory.com/575 

# 최장 증가 부분 수열(LIS) 알고리즘 
## 하나의 수열이 주어졌을 때, 값들이 증가하는 형태의 가장 긴 부분 수열을 찿는 문제임 
### 점화식 dp[i] = max(dp[i], dp[j]+1) if array[j] < array[i]

# dp[i]: i번째 수를 마지막 원소로 가지는 부분 수열의 최대 길이
# 0 ~ i-1번째 원소들 중에서, i번째 원소보다 작은 원소들의 dp값들 중 가장 큰 값 + 1을 dp[i]로 기록

import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split())
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 반환
array.reverse()
# DP 테이블 초기화
dp = [1] * n 

# LIS 알고리즘 수행
for i in range(1,n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] +1)

# 열외해야 하는 병사의 최소 수를 출력
print(n-max(dp))