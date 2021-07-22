'''
def dfs(graph, start_node):
    visited =list()
    need_visit=list()
    need_visit.append(start_node)

    while need_visit:
        node =need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(grpah[node])
            
def bfs(graph, start_node):
    visited= list()
    need_visit = list()
    need_visit.append(start_node)
----------------------------------
def dfs(graph,i,visited):
    visited[v] =True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
visited =[False] *9

dfs(graph,1,visited)

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] =True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True
visited =[False] *9
bfs(graph, 1, visited)
'''
    
