# 아이디어 -> 중간값에 해당하는 위치의 집에 안테나 설치하면 거리의 총합이 최소가 됨
## 모든 집의 위치 정보를 입력받은 뒤, 이를 정렬해서 중간값을 출력하기 
### 중위수를 구할 때는 리스트 개수는 N-1이기 때문에 (N-1) // 2fh gownrl 

n = int(input())

house = sorted(list(map(int, input().split()))) 

print(house[(n-1)//2]) # 중간값 계산