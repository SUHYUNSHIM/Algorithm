import re
#리스트 문자열 비교
#문자열과 숫자가 나누어짐
def solution(registered_list,new_id):
    list = registered_list
    for id in list:
        if new_id not in list: #아이디가 아얘 새로운 경우
            answer = new_id

        elif new_id in list:
            for i in range(len(list)):
                if new_id == list[i]:
                    numbers = re.sub(r'[^0-9]', '', new_id)
                    if numbers == '':
                        numbers = '0'
                    num = int(numbers)
                    num = num + 1  # 숫자만 추출 후 1을 더하였음
                    words = [i for i in new_id if i.isalpha()]
                    words = ''.join(words)  # 영소문자 문자열
                    # print(words)
                    new_id = words + str(num) #1을 증가시킨 새 단어
                    #print(new_id)
    return answer
list = ["bird99", "bird98", "bird101", "gotoxy"]
list1 = ["cow","cow1","cow2","cow3","cow4","cow9","cow8","cow8","cow7","cow6","cow5"]
list2 = ["card","ace13","ace16","banker","ace17","ace14"]
list3 = ["apple1","orange","banana3"]

check = "bird98"
check1 = "cow"
check2 = "ace15"
check3 = "apple"
print(solution(list,check))
print(solution(list1,check1))
print(solution(list2,check2))
print(solution(list3,check3))


'''
import re
#리스트 문자열 비교
#문자열과 숫자가 나누어짐
def solution(registered_list,new_id):
    #list = []
    list = registered_list
    #print(list)
    for id in range(len(list)):
        if list[id] == new_id: #아이디 중복
            numbers = re.sub(r'[^0-9]', '', new_id) #숫자 분리
            if numbers == '':
                numbers = '0'
            num = int(numbers)
            num = num+1 #숫자만 추출 후 1을 더하였음

            words = [i for i in new_id if i.isalpha()]
            words = ''.join(words) #영소문자 문자열
            new_id = words + str(num) #1을 더한 새 문자열을 만들었음
        elif list[id] != new_id:
            answer = new_id
            return answer
            break;
            #solution(registered_list,new_check)
    #answer=''
    3점짜리 답안.. 예외 3/4 성공

'''