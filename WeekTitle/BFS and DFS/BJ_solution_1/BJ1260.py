##1260 DFS와 BFS

##graph = dict()
N, M, V = map(int, input().split())
matrix = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_lit = [0]*(N+1)

def dfs(V):
    visit_lit[V] =1
    print(V, end =' ')
    for i in range(1,N+1):
        if(visit_lit[i]==0 and matrix[V][i] ==1):
            dfs(i)
def bfs(V):
    queue =[V]
    visit_lit[V] =0  
    while queue:
        V= queue.pop(0)
        print(V,end= ' ')
        for i in range(1,N+1):
            if(visit_lit[i]==1 and matrix[V][i] ==1):
                queue.append(i)
                visit_lit[i]=0

dfs(V)
print()
bfs(V)