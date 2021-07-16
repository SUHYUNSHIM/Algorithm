#인접 행렬 방식
INF =999999999

#2차원 리스트를 이용해 인접 행렬 표현
#노드 0,1,2
#노드 1과 노드7이 연결되어 있는가.
#graph[1][7]확인

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

#인접리스트 방식
graph =[[] for _ in range(3)]
#노드에 연결된 노드 정보 저장(노드,거리)
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))

print(graph)
