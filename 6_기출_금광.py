# 첫번째 열부터 출발하여 금을 캐기 시작함 
## 맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있음
# 즉, 왼쪽에서의 가장 많은 금을 get 하면 최대 크기를 출력 가능함 -> 열 기준으로 탐색해야됨
## dp[i][j] += max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])


# 참고 https://comlini8-8.tistory.com/110 

import numpy as np
import sys

T = int(sys.stdin.readline()) # 테스트 케이스 개수

for t in range(T):

    n, m = map(int, sys.stdin.readline().split()) # n x m
    golds = list(map(int, sys.stdin.readline().split()))
    golds = (np.array(golds).reshape(n,m)).tolist()

    for j in range(1,m):
        for i in range(n):

            lu, ll, ld = -1, -1, -1

            # 왼쪽 위
            if i-1 >= 0 and j-1 >= 0:
                lu = golds[i][j] + golds[i-1][j-1]

            # 왼쪽
            if j-1 >= 0:
                ll = golds[i][j] + golds[i][j-1]

            # 왼쪽 아래
            if i+1 < n and j-1 >= 0:
                ld = golds[i][j] + golds[i+1][j-1]

            golds[i][j] = max(lu, ll, ld)

    print(max(np.array(golds).T[-1]))