# 아이디어
## 주변 상,하,좌,우 살핀 후 0이면서 아직 방문하지 않은 지점이 있다면 방문하기
## 연결된 모든 지점 발문 => 모든 노드 반복하며 방문하지 않은 지점의 수 세기 

n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = [] 
for i in range(n):
    graph.append(list(map(int,input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들로 방문
def dfs(x,y):
        if x <= -1 or x >= n or y <= -1 or y >= m:
              return False
        # 현재 노드를 아직 방문 하지 않았다면
        if graph[x][y] ==0:
              graph[x][y] = 1
            # 상하좌우 위치 재귀 호출
              dfs(x-1, y) # 상
              dfs(x, y-1) # 좌 
              dfs(x+1, y) # 하
              dfs(x, y+1) # 우
              
              return True
        return False 

# 모든 노드에 대하여 음료수 채우기 
result = 0
for i in range(n):
      for j in range(m):
            if dfs(i,j) == True:
                  result += 1 

print(result)