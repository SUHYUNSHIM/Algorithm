import random

def bubblesort(data):
    for index in range(len(data)-1):
        swap = False #swap이라는 장치를 추가
        for index2 in range(len(data)-index-1):
            if data[index2] > data[index2+1]:
                data[index2],data[index2+1] = data[index2+1], data[index2]
                swap = True #크기 순이 바뀌는 경우, True로 바꿔준다.
        if swap == False: # for문을 다 빠져나왔을 때, 아직도 false면 이미 정렬된 상태라는 것.
            break
    return data
data_list = random.sample(range(100),50)
print(data_list)
print(bubblesort(data_list))

#데이터가 두 개일 때 버블 정렬 알고리즘 방식으로 정렬해보세요
def bubblesort2(data):
    for i in range(len(data)-1):
        swap = False
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                swap= True
        if swap == False:
            break
    return data
data_list2 = [57,23]
print(bubblesort2(data_list2))

#데이터가 세 개일 때 버블 정렬 알고리즘 방식으로 정렬해보세요
data_list3 = [21,19,14]
print(bubblesort2(data_list3))
#데이터가 네 개일 때 버블 정렬 알고리즘 방식으로 정렿해보세요
data_list4 = [66,71,27,12]
for i in range(len(data_list4)-1):
    for j in range(len(data_list4)-i-1):
        if data_list4[j]>data_list4[j+1]:
            data_list4[j],data_list4[j+1] = data_list4[j+1],data_list4[j]
print(data_list4)
