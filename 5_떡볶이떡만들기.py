# 아이디어 -> 적절한 높이를 찾을 때까지 절단기의 높이를 반복해서 조정하기
# 이후 조건 확인 -> 만족 여부 확인 -> 이진 탐색 범위 좁히기

# 떡의 개수(n)와 요청한 떡의 길의(m)을 입력 받기
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력 받기
array = list(map(int, input().split()))

# 이진탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 -> 반복문
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid 

    # 떡의 양이 부족한 경우 -> 왼쪽 파트 탐색
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 -> 오른쪽 파트 탐색
    else:
        result = mid 
        start = mid + 1

print(result)
