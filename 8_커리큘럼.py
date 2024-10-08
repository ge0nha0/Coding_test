# 위상 정렬 알고리즘 -> 매번 간선 정보를 확인하여 결과 테이블 갱신 
## 리스트의 값을 복제해야 할 때에는 deepcopy()함수를 사용해야됨

from collections import deque 
import copy 

# 노드의 개수
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화 
graph = [[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보를 입력 받기 
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1 
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트 
    q = deque() 

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft() 

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1 

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
            
    # 위상 정렬 수행한 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()