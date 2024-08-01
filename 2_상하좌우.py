## L, R, U, D에 대해 정의를 하고 돌리자
n = int(input())
lst = list(map(str,input().split()))

now = [1,1]

for i in lst:
    if i == 'L':
        if now[1] > 1:
            now[1] -= 1
    elif i == 'R':
        if now[1] < n:
            now[1] += 1
    elif i == 'U':
        if now[0] > 1:
            now[0] -= 1
    elif i == 'D':
        if now[0] < n:
            now[0] += 1 

print(now[0], now[1])

## 해설 풀이
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)