a= [1,2,3,4,5,5,5]
remove_set = {3,5}

result =[]
for i in a:
    if i not in remove_set:
        result.append(i)
##인접 행렬_2차원 배열로 그래프의 연결 관계를 표현하는 방식. 파이썬에서는 2차원 리스트로 구현한다.
#[[0,0,0,0],[0,0,0,0],[0,0,0,0]] -->2차원 리스트를 활용해 인접 행렬을 표현할 수 있다.
n=3
m=4
array3 =[[0]*m for _ in range(n)]

graph= [[0,7,5],[7,0,999999],[5,999999,0]] #연결되어 있지 않은 노드끼리는 무한 비용.
##노드 1과 노드 7이 연결되어 있는가. graph[1][7] 확인.ㅏㅑ
#인덱스 순서대로 비용 저장된 것.


##인접 리스트 방식
#[[(1,7),(2,5)],[(0,7)],[(0,5)]] #노드, 거리
graph = [[] for _ in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))



