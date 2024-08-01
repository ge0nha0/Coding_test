# 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 구하기 
# input a1 -> output 2
## 나이트의 8가지 경로를 하나씩 확인 + 8가지 방향에 대한 방향 벡터 정의 

now = input()
row, col = now[1], now[0]

col_lst = [0,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col = col_lst.index(col)
row = int(row)

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

result = 0

for i in range(len(dx)):
    x = row + dx[i]
    y = col + dy[i] 

    if 1 <= x <= 8 and 1 <= y <= 8:
        result += 1 

print(result)

