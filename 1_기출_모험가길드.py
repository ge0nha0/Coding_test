# 오름차순 정렬 -> 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면, 그룹 결정

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수 
cnt = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    cnt += 1 # 현재 그룹에 해당 모험가를 포함
    if cnt >= i: # 현재 그룹에 포함된 모험가의 수 >= 현재의 공포도 -> 그룹 결정
        result += 1
        cnt = 0 # 초기화 

print(result)