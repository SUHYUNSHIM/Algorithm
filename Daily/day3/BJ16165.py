N, M = map(int,input().split())
member_table = [[] for i in range(N)] #그룹 수만큼 빈 리스트 생성
quiz = list()
group= {}

for i in range(N):
    group_name = input()
    member_num = int(input())
    for j in range(member_num):
        member_name = input()
        member_table[i].append(member_name)
    group[group_name] = member_table[i]

'''
for i in range(N):
    print(member_table[i])
'''
#print(group['twice'])
'''
for i in range(M):
    quiz.append(input())
    int(input())
'''
for i in range(M):
    question = input()
    kind = int(input())

    if kind == 0: #멤버 이름
        quiz.extend(sorted(group[question]))
    elif kind == 1: #속한 그룹의 이름
        for g, members in group.items():
            if question in members:
                quiz.append(g)
                #print(g)

for answer in quiz:
    print(answer)

print(group) #{'twice': ['jihyo', 'dahyeon', 'mina', 'momo', 'chaeyoung', 'jeongyeon', 'tzuyu', 'sana', 'nayeon'], 'blackpink': ['jisu', 'lisa', 'rose', 'jenny'], 'redvelvet': ['wendy', 'irene', 'seulgi', 'yeri', 'joy']}