house = []
danji = []
n = int(input())
dx = [1,-1,0,0] #동서남북 인접한 곳의 좌표를 구하기 위함
dy = [0,0,1,-1]
cnt = 0
for _ in range(n):
    house.append(list(map(int,input())))
def dfs(x,y):
    global cnt
    house[x][y] = '0' #방문표시. 문자열 0
    cnt += 1 #탐색을 시작할 때마다 카운트를 더해준다
    for k in range(4): #동서남북 인접한 네 방향에 대해서
        next_x = x + dx[k]
        next_y = y + dy[k]
        if 0<=next_x<n and 0<=next_y<n and house[next_x][next_y] ==1: #인접한 곳의 좌표가 범위 내이고, ==1이라면
            house[next_x][next_y] = '0' #방문한 곳으로 처리해준다
            dfs(next_x,next_y) #조건을 만족하는 지점에서 다시 탐색을 시작한다
    return cnt
for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            cnt = 0
            danji.append(dfs(i,j))
print(len(danji))
danji.sort()
for i in danji:
    print(i)