graph = []
n = int(input())
answer = []
dx = [1,-1,0,0] #동서남북 인접한 곳의 좌표를 구하기 위함
dy = [0,0,1,-1]
cnt = 0
for _ in range(n):
    x = list(map(int,input()))
    graph.append(x)
def dfs(x,y):
    global cnt
    graph[x][y] = '#'
    cnt += 1 #단지의 개수 증가
    for k in range(4): #인접한 house 탐색.
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] ==1: #인접한 곳의 좌표가 범위 내이고, ==1이라면
            graph[nx][ny] = '#' #방문한 곳으로 처리해준다
            dfs(nx,ny) #조건을 만족하는 지점에서 다시 탐색을 시작한다
    return cnt
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            answer.append(dfs(i,j)) #현재 위치에서 DFS 수행.count 반환 받음.
print(len(answer))
answer.sort()
for i in answer:
    print(i)