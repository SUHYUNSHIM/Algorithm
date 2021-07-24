n = int(input())
s = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []
for i in range(n):
    s.append(list(input()))
def bfs(i, j):
    queue = [[i, j]]
    s[i][j] = "0"
    count = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and s[x][y] == "1":
                s[x][y] = "0"
                queue.append([x, y])
                count += 1
    cnt.append(count)
for i in range(n):
    for j in range(n):
        if s[i][j] == "1":
            bfs(i, j)
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)

#"1"인 값을 찾고 bfs를 이용해 하나 하나씩 "0"으로 바꿔주고 count(집의 수)를 증가시켜 저장해주고
#cnt(단지수)에 집의 수를 추가해준다.
'''
그래프 탐색 문제로, 동서남북으로 인접한 곳에 집이 있으면(= 1이라면) 집이 연결되어 있다고 하고, 연결된 집의 모임을 단지라고 한다. 여기서 단지의 개수, 각 단지내 집의 수를 출력해야 한다.

 

1. 어느 한 점에 대해서 인접한 곳에 1이 있는지를 탐색하고

2. 1이 있다면 그 점에서 다시 인접한 곳을 탐색하길 반복하고

3. 탐색을 할 때마다 카운트를 세다가

4. 탐색이 끝나면 카운트를 정답에 저장해준다 '''