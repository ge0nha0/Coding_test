# https://www.acmicpc.net/problem 
## https://hgk5722.tistory.com/32 
## BFS 문제 -> 큐

from collections import deque

n, m, k, x = map(int, input().split())

# 그래프로 노드의 개수 정해줌
graph = [ [] for _ in range(n + 1) ]

# 연결된 노드를 저장하는 방법
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) 

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0

# bfs 수행
queue = deque([x]) # 리스트니까 [x]로 시작
while queue:
    now = queue.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        # bfs는 너비 우선 탐색이라 가까운것부터 탐색 따라서 처음에 방문이 최단거리를 보장
        if distance[next_node] == -1: 
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            queue.append(next_node) 
# 여기까지 했으면 갈 수 있는 모든 노드의 최단거리 지정완료

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i) # 한 줄에 하나씩 오름차순으로 출력해야 하니까
        check = True
# 만약 최단 거리가 k인 도시가 없다면, -1 출력
if check == False:
    print(-1)