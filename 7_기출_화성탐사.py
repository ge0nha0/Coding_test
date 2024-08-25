# 다익스트라 최단 경로 알고리즘

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 전체 Case만큼 반복
for tc in range(int(input())):
    n = int(input())

    graph = [] # 전체 맵 정보 입력 받기 
    for i in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]

    x, y = 0,0
    # 시작 노드로 가기 위한 비용은 (0,0) 위치의 값으로 설정하여, 큐에 삽입
    q = [(graph[x][y], x,y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue 
            
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost 
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])