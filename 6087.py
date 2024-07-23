# 6088 6089 6090 문제

# 등차수열 6088

a, d, n = map(int, input().split())

s = a # 저장할 공간

for i in range(2, n+1):
    s += d # s에는 d씩 커지면서 저장

print(s)

# 등비수열 6089
a, r, n = map(int, input().split())

s = a # 저장할 공간

for i in range(2, n+1):
    s *= r 

print(s)

# -2를 곱한 다음 1를 더해 만든 수열 6090

a, m, d, n = map(int, input().split())

s = a

for i in range(2, n+1):
    s = (s*m) + d

print(s)