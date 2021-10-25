#조건 comprehension
#[출력표현식 for 요소 in 입력sequence if조건식]
dataset=['aa',11,'12755',12]
int_data = [num for num in dataset if type(num) == int]
#print(int_data)

int_data1 = [num*num for num in dataset if type(num)==int]
#print(int_data1)

#dictionary
#{key:value for 요소 in sequence if조건식}
dic = {'a':12 , 'b':13 , 'c':14}
distances = {node : float('inf') for node in dic}
#print(distances.values()) #dict_values([inf, inf, inf])
#print(distances.items()) #dict_items([('a', inf), ('b', inf), ('c', inf)])

dic1= {1:'a' , 2:'bb',3:'ccc'}
trans = {key: val for key,val in dic1.items() if key>=2}
#print(trans) #{2:'bb',3:'ccc'}

'''
for i in dic1.keys(): #key의 목록을 뽑아내는 것. 딕셔너리.keys()
    print(dic1[i])
'''
#a bb ccc 출력
#입력받을 때 0으로 초기화된 리스트
num = int(input())
cache = [0 for index in range(num+1)]
print(cache)