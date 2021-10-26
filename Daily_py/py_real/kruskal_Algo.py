mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent =dict()  #키는 노드이름, 값은 부모 노드
rank = dict()  #어떤 높이를 가지고 있는지. 키는 노드, 값이 rank

#해당 노드의 root 노드를 리턴한다.
def find(node):
    #path compression 기법.(중간 노드들을 모두 root 노드에 연결시켜서 부모 노드를 탐색하는 시간을 줄인다. )
    if parent[node] != node: #자신이 루트 노드가 아니라면
        parent[node] = find(parent[node]) #부모 노드 대입. 재귀를 사용해서 루트 노드를 찾았다.
    return parent[node]

#각 집합 트리 합치기
def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    #union-by-rank 기법
    if rank[root1] > rank[root2]:  #둘 중 루트 노드의 rank가 더 큰 것이 parent가 되어, 다른 노드들을 붙인다.
        parent[root2] = root1
    else: #높이가 같을 때.
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] +=1

#초기화. 분리된 개별 집합.
def make_set(node):
    parent[node] = node #parent['A'] = 'A'
    rank[node] = 0      #rank['A'] = 'A'
def kruskal(graph):
    mst = list() #선택된 간선 정보

    #1.초기화
    for node in graph['vertices']:
        make_set(node)
    #2.간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()   #제일 앞에 있는 숫자 7 A B. A와 B 사이의 거리는 7이다. 간선의 거리, 두번째 알파벳의 정렬 순으로 sort된다. 오름차순.
    print("edges: ",edges)

    #3.간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v , node_u = edge
        if find(node_v) != find(node_u): #root 노드가 다른 것을 확인했다.
            union(node_v, node_u) #합치기
            mst.append(edge)
    return mst

print(kruskal(mygraph))