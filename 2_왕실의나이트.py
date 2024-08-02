# 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 구하기 
# input a1 -> output 2
## 나이트의 8가지 경로를 하나씩 확인 + 8가지 방향에 대한 방향 벡터 정의 

# now = input()
# row, col = now[1], now[0]

# col_lst = [0,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# col = col_lst.index(col)
# row = int(row)

# dx = [2, 2, -2, -2, 1, -1, 1, -1]
# dy = [1, -1, 1, -1, 2, 2, -2, -2]

# result = 0

# for i in range(len(dx)):
#     x = row + dx[i]
#     y = col + dy[i] 

#     if 1 <= x <= 8 and 1 <= y <= 8:
#         result += 1 

# print(result)

# 정답 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의 
steps = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        result += 1

print(result)