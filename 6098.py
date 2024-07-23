# 성실한 개미

grid = [list(map(int, input().split())) for _ in range(10)]
i = 1
j = 1
grid[i][j] = 9
while grid[i][j] != 2:
    if grid[i][j + 1] != 1:
        if grid[i][j + 1] == 2:
            grid[i][j + 1] = 9
            break
        grid[i][j + 1] = 9
        j += 1
        continue
    if grid[i + 1][j] != 1:
        if grid[i + 1][j] == 2:
            grid[i + 1][j] = 9
            break
        grid[i + 1][j] = 9
        i += 1
    else:
        break

for i in range(10):
    print(*grid[i])