from collections import deque

n = int(input())
pair = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(pair):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] =1

def bfs(start_node):
    visited = [start_node]
    queue = deque()
    queue.append(start_node)

    while queue:
        v = queue.popleft()
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and (i not in visited):
                visited.append(i)
                queue.append(i)
    return visited
print(len(bfs(1))-1)