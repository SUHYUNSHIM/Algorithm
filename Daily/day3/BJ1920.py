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