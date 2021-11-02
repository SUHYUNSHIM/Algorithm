N = int(input())
data_list = input().split()
data_list.sort()

M = int(input())
test_list = input().split()

def binary_search(data,search):
    if len(data) == 1 and search == data[0]:
        return 1
    if len(data) == 1 and search != data[0]:
        return 0
    if len(data) == 0:
        return 0

    medium = len(data) // 2
    if search == data[medium]:
        return 1
    else:
        if search > data[medium]:
            return binary_search(data[medium+1:],search)
        else:
            return binary_search(data[:medium],search)

answer = list()
for i in range(M):
    answer.append(binary_search(data_list,test_list[i]))

for i in range(M):
    print(answer[i])
