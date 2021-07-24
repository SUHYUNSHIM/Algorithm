from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        a, b, c = q.popleft()
        visit[c][a][b] = 1
        for i in range(6): #상하좌우,윗칸,아래칸
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]

            #범위 조건, 아직 익지 않았는지, 방문하지 않았는지.
            if (0 <= x < n) and (0 <= y < m) and (0 <= z < h) and (s[z][x][y] == 0) and (visit[z][x][y] == 0):
                q.append([x, y, z])
                s[z][x][y] = s[c][a][b] + 1 #기준좌표 +1
                visit[z][x][y] = 1

m, n, h = map(int, input().split()) #가로, 세로 ,상자의 수
s = [[] for _ in range(h)] #익었는지 정보
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)] #방문확인
q = deque() #1 좌표.
isTrue = False #1로 모두 바꿀 수 있는가.


for i in range(h):
    for j in range(n):
        s[i].append(list(map(int, input().split()))) #츷 수, 세로크기만큼 줄 수를 입력. 박스 정보 입력
for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 1:  #1인 것을 골라서 넣는다.
                q.append([x, y, z])
bfs() #탐색
max_num = 0
#모든 좌표 탐색. 0이 있는지 확인.
for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num, s[z][x][y])
if isTrue == True: #다 1로 바꾸지 못했다.
    print(-1)
else:
    print(max_num - 1)
