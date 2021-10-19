def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1,0,-1):
            if data[index2] < data[index2-1]:
                data[index2],data[index2-1] = data[index2-1],data[index2]
            else:
                break
    return data

import random
data_list = random.sample(range(100),50)
print(insertion_sort(data_list))

list1=[19,2,1,23,10]
for index in range(len(list1)-1):
    for index2 in range(index+1,0,-1):
        if list1[index2] < list1[index2-1]:
            list1[index2],list1[index2-1] = list1[index2-1],list1[index2]
        else:
            break #for문 break의 의미. 이번 index 번째에서는 앞의 것이 뒤의 것보다 큰 경우가 없으므로 pass하고 현재+1번째의 인덱스로
            #탐색하러 간다.
print(list1)
