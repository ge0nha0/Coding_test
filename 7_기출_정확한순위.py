# 최단 경로 문제
## A -> B 도달 가능 and B -> A 도달 가능하면 성적 비교 ㅇㅋ
### 플로이드 워셜 알고리즘 수행

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1 

print(result)
