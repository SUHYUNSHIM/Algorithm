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
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if 0 <= x < n and 0 <= y < m and 0 <= z < h and s[z][x][y] == 0 and visit[z][x][y] == 0:
                q.append([x, y, z])
                s[z][x][y] = s[c][a][b] + 1
                visit[z][x][y] = 1
m, n, h = map(int, input().split())
s = [[] for i in range(h)]
visit = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]
q = deque()
isTrue = False
st = False
for i in range(h):
    for j in range(n):
        s[i].append(list(map(int, input().split())))
for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 1:
                q.append([x, y, z])
bfs()
max_num = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num, s[z][x][y])
if isTrue == True:
    print(-1)
else:
    print(max_num - 1)

'''
bfs로 구현을 해준다.
토마토가 있는 위치를 저장해서 bfs를 실행시켜준다.
만약 0이 존재하면 -1을 출력해주고 그게 아니라면 제일 큰 값에 -1을 해준 값을 출력해준다.
'''