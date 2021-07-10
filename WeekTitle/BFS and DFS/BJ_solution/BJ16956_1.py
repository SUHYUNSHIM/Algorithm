from collections import deque
##BFS, 양과 늑대가 인접해있으면 막을 수가 없으므로 0을 출력해주고,
##인접한 경우가 없다면 늑대를 가둬버리고 결과를 출력해주면 된다.
def bfs(y, x):
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < R) and (0 <= X < C):
            if graph[Y][X] == 'S':
                return False
            if graph[Y][X] == '.':
                graph[Y][X] = 'D'
    return True

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(R):
    for j in range(C):
        t = True
        if graph[i][j] == 'W':
            t = bfs(i, j)
            if t == False:
                print(0)
                break
if t:
    print(1)
    for line in graph:
        print(''.join(line))