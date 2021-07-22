N = int(input())
tree = [[] for _ in range(N + 1)]  # 인접 리스트 방식
##
'''
print("트리의 구조는 :", tree)
'''
for _ in range(N - 1):
    a, b = list(map(int,input().split()))
    tree[a].append(b)
    tree[b].append(a)
##
'''
for i in range(N + 1):
    print("트리의 구조는 ", tree[i])
'''
queue = [1]  # 시작노드 넣기
visited = [0] *(N+1)
result = {}  # 부모 노드 딕셔너리

while queue:
    now = queue.pop(0)
    for i in tree[now]:  # 첫번째로는 1의 리스트 요소들을 검색한다. 1은 2와 3이 연결되어 있다.
        if visited[i]==0:  # 2를 방문한 적이 없다면
            result[i] = now  # 2는 키, 2의 value는 부모 값 1이 된다.
            visited[i] =1  # 방문 처리를 한다.
            queue.append(i)  # 큐에 추가
for i in range(2, N+1):
    print(result[i])
print(result)
