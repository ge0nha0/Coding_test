# N: 배열의 크기, M: 숫자가 더해지는 횟수, K: 특정 인덱스의 수가 연속해서 더할 수 있는 수
## 가장 큰 수를 k번 더하고 이후 2번째로 큰 수를 한번 더하자
### 가장 먼저 반복되는 수열에 대해서 파악하기

#### 내가 문제 푼 풀이
# N, M, K
n, m, k = map(int, input().split())

# 입력 받기
ipt = list(map(int, input().split()))

ipt.sort()

first = ipt[n-1] # 가장 큰 수
second = ipt[n-2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m ==0:
            break
        result += first
        m -= 1 # 더할 때 마다 1빼기
    if m == 0:
        break
    result += second 
    m -= 1 # 더할 때마다 1빼기

print(result)

## 정답 풀이

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
cnt = int(m / (k+1)) * k
cnt += m %(k+1)

result = 0
result += (cnt) * first # 가장 큰 수 더하기
result += (m-cnt) * second 

print(result)