N = int(input())
numbers = input().split() #빈칸을 기준으로 잘라서 바로 리스트 형태로 저장한다.

M = int(input())
test = input().split()

answer = list()
for i in test:
    if i in numbers:
        answer.append(1)
    elif i not in numbers:
        answer.append(0)

for i in range(M):
    print(answer[i])

'''
N,A = int(input()), {i: 1 for i in map(int,input().split())} #int로 변환하여 있는 수는 1로 매칭 
M = input()
for i in list(map(int,input().split())):
    print(A.get(i,0)) #print(1 if i in A else 0)
'''