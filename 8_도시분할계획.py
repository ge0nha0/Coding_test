# 크루스칼 알고리즘 -> 최소 신장 트리 -> 구성하는 간선 중에서 가장 비용이 큰 간선 제거 
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a 
    else:
        parent[a] = b 

v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화 

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = [] 
result = 0 

for _ in range(1, v+1):
    parent[i] = i 

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort() 
last = 0 

for edge in edges:
    cost, a, b = edge 
    # 사이클이 발생하지 않는 경우에만 집합에 포함 
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost 
        last = cost 

print(result - last)