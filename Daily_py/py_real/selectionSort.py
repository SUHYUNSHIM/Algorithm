def selection_sort(data):
    for stand in range(len(data)-1):
        lowest = stand #기준이 되는 값
        for index in range(stand+1, len(data)): #range의 경우 (a,b)일때 b-1까지의 범위를 갖기 때문에 len(data)로 했을 때 리스트의 인덱스와 일치한다.
            if data[lowest] > data[index]:
                lowest = index
        data[lowest],data[stand] = data[stand],data[lowest]
    return data

data_list = [9,3,2,1]
print(selection_sort(data_list))