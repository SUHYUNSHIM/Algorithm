#다익스트라 알고리즘. 시작점과 노드까지의 최소 거리를 구한다.
#우선순위 큐를 사용하여 가지고 있는 거리값이 작은 노드를 계산한다.
#최소거리를 갱신, 최소거리보다 큰 값이 들어오면 pass --> continue
import heapq

def dijkstra(graph, start):
    distances = {node: float('int') for node in graph} #dictionary 형태. inf 무한대 값으로 초기화, node는 키를 의미.
    distances[start] = 0 #자신에서 자신에게로
    queue =[]
    heapq.heappush(queue,[distances[start],start]) #초기화



    