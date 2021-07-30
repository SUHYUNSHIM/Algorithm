import sys
from collections import deque
read = sys.stdin.readline

dx = [1, -1, 0, 0]  # 동서남북 인접한 곳의 좌표를 구하기 위함
dy = [0, 0, 1, -1]

R, C, N = map(int, read().split()) #가로 칸의 수, 세로 칸의 수, 시간
bomb = deque()

#리스트 입력
board = [list(read()) for _ in range(R)] #step1
N=N-1 #step2 변화없음.

#함수
#폭탄 탐지
def findBomb():
    for i in range(R):
        for j in range(C):
            if board[i][j] =='O':
                bomb.append((i,j))
#모두 설치-step3
def addBomb():
    for i in range(R):
        for j in range(C):
            if board[i][j] != 'O':
                board[i][j] ='O'
#폭발-step4
def bombbomb():
    while bomb:
        x, y = bomb.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx <R and 0 <=ny<C:
                if board[nx][ny] == 'O':
                    board[x][y] ='.'

while N:
    findBomb()
    addBomb()
    N = N-1
    if N ==0:
        break
    bombbomb()
    N = N-1
for i in range(R):
    for j in range(C):
        print(board[i][j], end='')
    print()


