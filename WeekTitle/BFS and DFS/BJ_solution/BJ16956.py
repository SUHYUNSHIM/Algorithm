import sys

r,c=map(int,input().split())
maps=[list([p for p in sys.stdin.readline().strip()]) for _ in range(r)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]
flag=False
for i in range(r):
    for j in range(c):
        #늑대
        if maps[i][j]=='W':
            for z in range(4):
                nx,ny=i+dx[z],j+dy[z]
                if nx<0 or nx>=r or ny<0 or ny>=c:
                    continue
                #양이 늑대와 인접해있으면 flag 변경
                if maps[nx][ny]=='S':
                    flag=True
                    break
        #양이면 그대로 놔둠
        elif maps[i][j]=='S':
            continue
        #.이면 모두 울타리채움
        else:
            maps[i][j]='D'

if flag:
    print(0)
else:
    print(1)
    for i in maps:
        print(''.join(i))

https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-16956%EB%B2%88-%EB%8A%91%EB%8C%80%EC%99%80-%EC%96%91-%EC%B4%88%EC%BD%94%EB%8D%94