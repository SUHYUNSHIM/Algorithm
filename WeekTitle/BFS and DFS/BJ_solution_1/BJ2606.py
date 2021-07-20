n = int(input())
m = int(input())
dic={}

for i in range(n):
    dic[i+1] = set() ##노드번호 - {1,2,3,}
for j in range(m):
    a,b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

    def dfs(start,dic):
        for i in dic[start]:
            if i not in visited:
                visited.append(i)
                dfs(i,dic)
visited = []
dfs(1,dic)
print(len(visited)-1)


##BFS
from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
visited = []
bfs(1, dic)
print(len(visited)-1)