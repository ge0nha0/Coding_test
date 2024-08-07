# 문제 접근 -> 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체!!
## A -> 오름차순 정렬 // B -> 내림차순 정렬 
### 두 배열의 원소를 첫 번째 인덱스부터 차례로 확인하면서 A의 원소가 B의 원소보다 작을 때만 교체 수행
#### 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 0(NlogN) 보장하는 알고리즘 구성

n,k= map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

# 첫번째 인덱스부터 확인하며 두 배열의 원소를 최대 k번 비교
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break 

print(sum(a))