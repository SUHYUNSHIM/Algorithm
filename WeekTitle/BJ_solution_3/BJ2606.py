##그래프를 입력받는다.
##1번 노드와 연결된 노드들의 수를 센다.

from collections import deque

n = int(input())
pair = int(input())
graph = [[0]*(n+1) for _ in range(n+1)] ##인접행렬 방식

for i in range(pair):
    n1,n2 = map(int,input().split())
    graph[n1][n2] = graph[n2][n1] =1

def bfs(start):
    visited =  [start]
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and (i not in visited):
                visited.append(i)
                queue.append(i)
    return visited
print(len(bfs(1))-1)