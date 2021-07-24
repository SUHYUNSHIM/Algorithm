from collections import deque
m, n = map(int, input().split())
s = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(map(int, input().split())))
def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and s[x][y] == 0: #가능 범위
                s[x][y] = s[a][b] + 1
                queue.append([x, y])
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j])
bfs()
isTrue = False
result = -2
for i in s:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)

'''
우선 토마토의 위치를 queue에 저장을 해준다.
그리고 저장된 토마토 위치를 기준으로 bfs를 사용하여 상, 하, 좌, 우를 검사해주어 0인값을 찾아 나간다.
찾아 나가는 과정에서 기준이 되는 숫자에 +1을 해주어 더해나간다.
만약 bfs함수를 실행하고나서도 0이 있다면 -1을 출력해주고, 가장 큰 값이 -1이면 0을 출력해주고
둘다 아니라면 제일 큰 값에 -1을 한 값을 출력해준다.
'''