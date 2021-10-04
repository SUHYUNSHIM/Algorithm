def selection_sort(data):
    for stand in range(len(data)-1):
        lowest = stand
        for index in range(stand+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest],data[stand] = data[stand],data[lowest]
    return data

data_list = [9,3,2,1]
print(selection_sort(data_list))