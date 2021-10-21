str_list = ['1ahello','1chello','1bhello']
print(sorted(str_list, key=lambda x:x[1])) #기준이 두번째 문자이다.

num_list = [15,22,8,79,10]
num_list.sort(reverse= True) ##내림차순 배열
print(num_list)

num_list = sorted(num_list) #sorted의 기본은 오름차순
print(num_list)

abc_list = ['apple','zero','coke','bill']
abc_list.sort(reverse=True) #아얘 원본을 바꾸는 것. 내림차순
print(abc_list)

print(sorted(abc_list)) #리스트 자체 #오름차순으로 . 원본을 바꾸지 않는다.
print(abc_list)


