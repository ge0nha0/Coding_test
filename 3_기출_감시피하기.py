# https://www.acmicpc.net/problem/18428
# https://velog.io/@bumblebeeda/%EC%9D%B4%EC%BD%94%ED%85%8C-%EC%99%84%EC%A0%84%ED%83%90%EC%83%89-%EA%B0%90%EC%8B%9C%ED%94%BC%ED%95%98%EA%B8%B0

from itertools import combinations

n = int(input())   # 복도의 크기
board = [] # 복도 정보
teachers = []  # 선생님 위치 정보
spaces = [] # 모든 빈공간 위치 

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님 위치 저장
        if board[i][j] == 'T':
            teachers.append((i,j))
            
        # 빈공간 위치 저장 (장애물 설치 예정 )
        if board[i][j] == 'X':
            spaces.append((i,j))
            
# 감시 함수  , 학생 발견 True, 미발견 False
def watch(x,y, direction):
    # 왼쪽
    if direction == 0:
        while y >= 0 :
            if board[x][y] == 'S':  # 학생 발견
                return True
            if board[x][y] == 'O': # 장애물 발견 
                return False
            y -= 1   # 현위치에서 왼쪽으로 탐색할 거니까 
            
    # 오른쪽 탐색
    if direction == 1 :
        while y < n :
            if board[x][y] == 'S' :
                return True
            if board[x][y] == 'O' :
                return False
            y += 1   # 현위치에서 오른쪽으로 탐색
    # 위쪽         
    if direction == 2 :
        while x >= 0 :
            if board[x][y] == 'S' :
                return True
            if board[x][y] == 'O' :
                return False
            x -= 1   # 현위치에서 위쪽으로 탐색
    
    # 아래쪽
    if direction == 3:
        while x<n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O' :
                return False
            x += 1  # 현위치에서 아래쪽으로 탐색
    return False # 모두 탐색했는데, S가 없었으면, 미발견

# 모든 선생님 사방 감시 함수, 사방 중 한곳이라도 나오면 True, 아니면 False
def process():
    for x, y in teachers:
        # 사방 탐색 
        for i in range(4):     # 사방 탐색 중 발견되면 
            if watch(x,y,i):
                return True
    return False   # 발견 안되면 False

## 장애물 설치 후 탐색 
find = False          # 학생을 발견하는 경우 , 원하는 조합을 못찾음 
for data in combinations(spaces, 3):  # 장애물 조합별로, 가능한지 확인 
    # 장애물 설치 
    for x,y in data :
        board[x][y] = 'O'
        
    # 학생 감시
    if not process() :  # 모든 선생님이, 사방으로 검색했을때, 학생이 없었으면
        find = True     # 원하는 발견이다. (선생님이 못찾는 조합 발견)
        break
    # 장애물 다시 치우기
    for x,y in data:
        board[x][y] = 'X'
        
if find :
    print('YES')
else : 
    print('NO')         