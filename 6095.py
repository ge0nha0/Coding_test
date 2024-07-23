# 바둑판에 흰 돌 놓기
# 19 x 19 바둑판임
# List Comprehension

n = int(input())

d = [[0 for i in range(20)] for j in range(20)]

for i in range(n):
    x,y = map(int, input().split())
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1,20):
        print(d[i][j], end=' ')
    print()