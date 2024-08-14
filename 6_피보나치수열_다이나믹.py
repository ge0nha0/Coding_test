# Memoization하기 위한 리스트 초기화 ## Top-Down방식
## 다이나믹 프로그래밍이란 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘

d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# Bottom-Up방식 # 반복문
## 앞선 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

d[1] = 1 
d[2] = 1
n = 99

# 반복문으로 구현 # Bottom-Up 다이나믹 프로그래밍
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])