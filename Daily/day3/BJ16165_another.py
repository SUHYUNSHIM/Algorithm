N, M = map(int, input().split())
team_mem , mem_team = {},{}

for i in range(N):
    team_name, mem_num = input(), int(input())
    team_mem[team_name] = [] #리스트 형태로 받을 것
    for j in range(mem_num):
        name = input() #멤버의 이름을 입력받는다.
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name, q = input() , int(input())
    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)

print(mem_team) #{'jihyo': 'twice', 'dahyeon': 'twice', 'mina': 'twice', 'momo': 'twice', 'chaeyoung': 'twice', 'jeongyeon': 'twice', 'tzuyu': 'twice', 'sana': 'twice', 'nayeon': 'twice', 'jisu': 'blackpink', 'lisa': 'blackpink', 'rose': 'blackpink', 'jenny': 'blackpink', 'wendy': 'redvelvet', 'irene': 'redvelvet', 'seulgi': 'redvelvet', 'yeri': 'redvelvet', 'joy': 'redvelvet'}
print(team_mem) #{'twice': ['jihyo', 'dahyeon', 'mina', 'momo', 'chaeyoung', 'jeongyeon', 'tzuyu', 'sana', 'nayeon'], 'blackpink': ['jisu', 'lisa', 'rose', 'jenny'], 'redvelvet': ['wendy', 'irene', 'seulgi', 'yeri', 'joy']}

