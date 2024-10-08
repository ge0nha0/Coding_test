# 점화식을 어떻게 세울까? -> 인접한 창고는 털 수 없다는 점에서 경우의 수를 어떻게 나눌 수 있는지가 포인트
## i번째 창고를 털기 위해서는? 식량창고를 털지 안털지를 결정하는 경우 + 
# # i-1번째를 털었을 경우 / i-2번재를 털었을 경우 2가지 -> 이 중 최댓값을 서치
# 점화식 -> a_i = max(a_i-1, a_i-2 + k_i)

n = int(input()) # 창고 개수
array = list(map(int, input().split())) # n개의 색량 개수

# DP 테이블 초기화
d = [0] * 100

# Bottom-Up 다이나믹 프로그래밍
d[0] = array[0]
d[1] = max(array[0], array[1]) # 둘 중 최대값 

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i]) # array[i]: 현재의 위치에 대한 식량의 값

print(d[n-1])

# d[i-3]는 d[i-1]과 d[i-2]을 구하는 과정에서 이미 고려되었기 때문에, d[i]의 값을 구할 때는 d[-1]과 d[-2]만 고려하면 됨
# 한 칸 이상 떨어진 식량창고는 항상 털 수 있으므로 고려 X