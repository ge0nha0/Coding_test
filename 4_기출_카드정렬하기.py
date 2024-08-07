# 그리디..? 정렬?? 
## 우선순위 큐 문제 (Heap)
## https://gammistory.tistory.com/27 

# 아이디어 -> 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해 보장 -> 우선순위 큐 -> 완전이진트리형태 자료구조(오른쪽 leaf 제거)

N = int(input())
card = [int(input()) for _ in range(N)]

import heapq 
heapq.heapify(card) # 기존 리스트를 힙으로 변환
result = 0

while len(card) != 1:
    n1 = heapq.heappop(card) # 힙 원소 삭제 (가장 작은 항목 반한)
    n2 = heapq.heappop(card)
    sum_n = n1+n2
    result += sum_n 
    heapq.heappush (card, sum_n) # 힙 원소 삽입

print (result)