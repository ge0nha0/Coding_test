# 참고 https://wooono.tistory.com/570 
# 모든 공유기들의 간격을 공평하게 설치하자 -> 이진 탐색

import sys

n, c = map(int, sys.stdin.readline().rstrip().split())  # 집의 개수(N), 공유기의 개수(C)

array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort() 

# 공유기를 설치할 수 있는 최소 간격
start = 1

# 공유기를 설치할 수 있는 최대 간격
end = array[-1] - array[0]

def binary_search(array, start, end):
    global result 

    if (start > end):
        return result
    
    # 가장 처음으로 공유기를 설치하는 집의 위치
    recent_dist = array[0]
    # 공유기 설치 개수
    cnt = 1
    # 공유기 설치 간격
    mid = (start + end) // 2 

    # 현재 Mid 값을 이용해 공유기를 설치
    for i in range(1, n):
        if (array[i] - recent_dist >= mid):
            recent_dist = array[i]
            cnt += 1 

    # 설치된 공유기의 개수가 C개 이상이라면, 해당 간격을 저장하고 간격을 더 늘리기
    if (cnt >= c):
        result = mid # 최적의 결과 저장
        return binary_search(array, mid+1, end)
    
    # 설치된 공유기의 개수가 C개 미만이라면, 간격을 더 줄이기
    else:
        return binary_search(array, start, mid-1)

print(binary_search(array, start, end))

