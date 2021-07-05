graph = dict() ##파이썬은 딕셔너리와 리스트 자료 구조를 사용하여 그래프를 표현한다.

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

##print(graph)

def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

print(bfs(graph,'A'))

##시간 복잡도
## BFS는 노드 수+ 간선 수 만큼 while 문을 수행한다.

def bfs(graph, start_node):  ## 그래프 정보와 시작노드를 받는다.
    visited = list()
    need_visit = list()

    need_visit.append(start_node)
    count =0
    while need_visit:
        count +=1
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print(count)
    return visited

print(bfs(graph,'A'))

