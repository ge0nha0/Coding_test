# 1부터 n까지의 정수를 순서대로 계속 더해 합을 만들어가다가, 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력
# 입력 정수(0~1000)

# # 내 풀이
num = int(input())

sum = 0
n = 0

for i in range(1, num+1):
    if sum < num:
        sum += i
        n = i

print(n)

# 정답 풀이
# n = int(input())
# s = 0
# t = 0

# while s<n:
#     t += 1
#     s += t
# print(t)
