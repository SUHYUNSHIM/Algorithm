def selection_sort(data):
    for stand in range(len(data)-1):
        lowest = stand #기준이 되는 값
        for index in range(stand+1, len(data)): #range의 경우 (a,b)일때 b-1까지의 범위를 갖기 때문에 len(data)로 했을 때 리스트의 인덱스와 일치한다.
            if data[lowest] > data[index]:
                lowest = index #가장 작은 값 업데이트
        data[lowest],data[stand] = data[stand],data[lowest]
    return data

data_list = [9,3,2,1]
print(selection_sort(data_list))

#처음 위치의 값과 나머지 값들을 비교해서 가장 작은 값과 비교한다.

list = [9,1,7,3]
for i in range(len(list)):
    min = i #최초로 작은 값, 그 기준은 첫 인덱스이다.
    for j in range(i+1,len(list)):
        if list[min] > list[j]:
            min = j #반복문으로 비교해나가면서 최소 인덱스를 찾는다. min의 값이 업데이트 되고
        list[i],list[min] = list[min],list[i]
print(list)