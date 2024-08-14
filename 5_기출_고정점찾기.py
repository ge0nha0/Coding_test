# 수열의 원소 중에서 그 값이 인덱스와 동일한 원소 

import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진 탐색 -> 재귀함수
def binary_search(array, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2

    # 고정점을 발견한 경우 고정점 반환
    if array[mid] == mid:
        return mid 
    elif array[mid] < mid:
        return binary_search(array, mid+1, end)
    else:
        return binary_search(array, start, mid-1)
    
check = binary_search(array, 0, n-1)

if (check == 0):
    print(-1)
else:
    print(check)