import random
def binary_search(data,search):
    #print(data)
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = len(data)//2 #정수 몫을 구하고 싶으면 /가 아니라 //을 써라
    if search == data[medium]:
        return True
    else:
        if data[medium] > search:
            return binary_search(data[:medium],search)
        else:
            return binary_search(data[medium:],search)


data_list = random.sample(range(100),10)
data_list.sort()
print(data_list)
print(binary_search(data_list,27))