def qsort(data):
    if len(data) <=1:
        return data
    left,right = list(), list()
    pivot = data[0]

    for index in range(1,len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])
    return qsort(left)+[pivot]+qsort(right)

#list comprehension 사용
def qsort(data):
    if len(data)<1:
        return data
    pivot = data[0]
    left = [item for item in data[1:] if pivot>item]
    right = [item for item in data[1:] if pivot<=item]
    return qsort(left)+[pivot] +qsort(right)

#퀵정렬 리스트 자르기
data_list1 = [1,2,3,4,5]
data1 = data_list1[:2]
data2 = data_list1[2:4]
data3 = data_list1[-2:]
print(data1)
print(data2)
print(data3)

#리스트 pop
actor_name = ["Woosung", "Bosung", "Seungbum", "Jihoon", "Joonghoon","Sunggi"]
print (actor_name)
my_favorite = actor_name.pop(1)
print ("My favorite actor is ", my_favorite)
print (actor_name)

#주어진 리스트를 맨 앞에 데이터를 기준으로 작은 데이터는 left 변수에 그렇지 않은 데이터는 right 변수에 넣기
data_list2 = [4,1,2,5,7]
left = []
right = []
stand = data_list2[0]
for num in data_list2:
    if stand > num:
        left.append(num)
    else:
        right.append(num)
print(left+[stand]+right[1:])





