import sys
input = sys.stdin.readline
n = int(input())
tree=[[0] for i in range(n+1)]

for i in range(n-1):
    a,b = list(map(int,input().split()))
    tree[a].append(b)
    tree[b].append(a)

queue = [1] ##큐에 1을 넣어줌. 1부터 시작.
visited = [0 for i in range(n+1)]
result ={}

while queue:
    now = queue.pop(0)
    for i in tree[now]:
        if visited[i]==0: #방문한 적이 없다.
            result[i] = now #부모 노드 삽입
            visited[i] = 1
            queue.append(i) #큐에 추가해 탐색을 이어간다.
for i in range(2,n+1):
    print(result[i])