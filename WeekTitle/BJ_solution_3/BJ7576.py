import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]  # 동서남북 인접한 곳의 좌표를 구하기 위함
dy = [0, 0, 1, -1]

M, N = map(int, input().split()) #가로 칸의 수, 세로 칸의 수
box = []
ripe = deque()

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1: #시간을 줄이기 위해 입력과 동시에 1인 것을 판별하여 리스트에 넣었음.
            ripe.append([i, j])
    box.append(row)

'''
for _ in range(N):
    temp = list(map(int, input().split()))
    
for i in range(N):
    for j in range(M):
        if temp[i][j] == 1: ##1인 것만 골라담기
            box.append([i,j])
'''
#주변 탐색. BFS
def bfs(M, N, box):
    days = -1

    while ripe: #ripe 큐가 비어있을 때까지.
        days += 1
        for _ in range(len(ripe)):
            x, y = ripe.popleft() #큐에 쌓인 좌표값을 읽기 위해 pop 했다.

            for i in range(4):
                next_x = x + dx[i] #1인 것의 주변을 탐색
                next_y = y + dy[i]

                if 0<= next_x <N and 0<= next_y <M and box[next_x][next_y] == 0:
                    box[next_x][next_y] = box[x][y] + 1 #현재 1인 것보다 +1일이 소요된 것이므로.
                    ripe.append([next_x, next_y])

    for b in box:
        if 0 in b:  #모든 토마토를 1로 만들지 못했으므로 -1을 반환한다.
            return -1
    return days


print(bfs(M, N, box))

