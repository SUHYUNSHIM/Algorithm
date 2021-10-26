#heapq 라이브러리
import heapq

queue = list()
graph_data = [[2,'A'],[5,'B'],[3,'C']]

for edge in graph_data:
    heapq.heappush(queue,edge) #리스트를 넣는다.

for index in range(len(queue)):
    print(heapq.heappop(queue)) #작은 가중치를 가진 값부터 뽑는다
# [2, 'A']
# [3, 'C']
# [5, 'B']

heapq.heapify(graph_data) #힙 구조로 변환. 리스트 데이터를 heap 형태로 한 번에 변환

for index in range(len(graph_data)):
    print(heapq.heappop(graph_data))
#[2, 'A']
#[3, 'C']
#[5, 'B']

##collections 라이브러리의 defaultdict 함수 활용
from collections import defaultdict
from heapq import *
list_dict = defaultdict(list) #초기값에 대한 데이터 타입 . int, float. 초기값을 넣어주지 않아도 된다.
print(list_dict['key'])

##########################################
myedges = [
    (7,'A','B'),(5,'A','D'),
    (8,'B','C'),(9,'B','D'),(7,'B','E'),
    (5,'C','E'),
    (7,'D','E'),(6,'D','F'),
    (8,'E','F'),(9,'E','G'),
    (11,'F','G')
]

def prim(start_node,edges):
    mst = list()
    #각각의 노드가 갖고 있는 간선 정보를 관리
    adjacent_edges = defaultdict(list)
    for weight, n1,n2 in edges:
        adjacent_edges[n1].append((weight,n1,n2))
        adjacent_edges[n2].append((weight, n2, n1)) #초기화 코드

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node] #선택된 노드에 대한 간선 정보를 list로 받는다.
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight,n1,n2)) #0 ,1, 2

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list,edge)
    return mst

print(prim('A',myedges))

#[(5, 'A', 'D'), (6, 'D', 'F'), (7, 'A', 'B'), (7, 'B', 'E'), (5, 'E', 'C'), (9, 'E', 'G')]