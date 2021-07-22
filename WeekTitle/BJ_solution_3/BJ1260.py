import sys
read = sys.stdin.readline
N,M,V = map(int,read().split())

graph =[[0] *(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(V):
    visited[V] = True
    print(V, end=" ")
    for i in range(1,N+1):
        if not visited[i] and graph[V][i] ==1:
            dfs(i)
def bfs(V):
    visited[V]= False
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V,end=" ")
        for i in range(1,N+1):
            if visited[i] and graph[V][i] == 1:
                queue.append(i)
                visited[i] = False
dfs(V)
print()
bfs(V)