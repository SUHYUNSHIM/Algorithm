str_list = ['1ahello','1chello','1bhello']
print(sorted(str_list, key=lambda x:x[1])) #기준이 두번째 문자이다.
print("sorted는 원본 리스트의 값을 바꾸지 않는다.")
print(str_list)

#############################################################################
num_list = [15,22,8,79,10]
num_list.sort(reverse= True) ##내림차순 배열
print(num_list)
print("출력 방식 변경-sort ")
print(num_list.sort(reverse=True)) # None 출력. 리스트 이름.sort(내림 or 오름 선택)로 정렬 후 print (리스트 이름) 이렇게 해야 출력된다.
                                   #sort는 그렇고, sorted(리스트명)은 print로 그 자체를 출력해도 된다.

###############################################################################
num_list = sorted(num_list) #sorted의 기본은 오름차순
print(num_list)
print("출력 방식 변경-sorted")
print(sorted(num_list, reverse=True)) # 내림 차순으로 출력

abc_list = ['apple','zero','coke','bill']
abc_list.sort(reverse=True) #아얘 원본을 바꾸는 것. 내림차순
print("내림차순 sort 출력")
print(abc_list)

print(sorted(abc_list)) #리스트 자체 #오름차순으로 . 원본을 바꾸지 않는다.
print(abc_list)

###########
'''
*요약* 
리스트명.sort(reverse기준)는 원본을 바꾸고, 출력 방식이 print(리스트명이다)
sorted(리스트명,reverse 기준)은 원본을 바꾸지 않는다. 그리고 출력 방식은 print(sorted(리스트명)) 이다.
'''


