#어떤 데이터리스트가 있을 때 리스트를 앞뒤로 짜르는 코드 작성
def split_func(data):
    medium = int(len(data)/2)
    left = data[:medium]
    right = data[medium:]
    print(left,right)
#split_func([1,5,3,2,4])

#재귀 함수1
def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point: #while문은 한번들어오면 조건이 맞을 때까지 반복한다.
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else: #둘다 1인 경우가 있다. 그럼 일단 왼쪽부터 넣는다.
            merged.append(left[left_point])
            left_point += 1

    # case2 - left 데이터가 없을 때  --> 아님 오른쪽이 없을 때임
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3 - right 데이터가 없을 때 --> 아님 왼쪽이 없을 때임 
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def mergesplit(data):

    if len(data) <= 1:
        return data
    print(len(data))
    print("입력된 데이터")
    print(data)
    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    print("left 값")
    print(left)
    right = mergesplit(data[medium:])
    print("right 값")
    print(right)
    return merge(left, right)

import random

data_list = [17, 73, 37, 3, 41, 5, 14, 6, 26, 60]
print(mergesplit(data_list))

#연습 코드
#두 리스트가 주어졌을 때 합치기
#병합 정렬 시 두 리스트의 합치는 순서에 따라 먼저 다 사용된
#리스트가 존재하므로, 각 리스트의 데이터가 존재하는지가 while의 조건이 될 것이다.
left1 = [0,2]
right1 = [3,1]

#def split()


def msort(left,right):
    m_list= list()
    l_point ,r_point = 0,0 #포인트는 작은 값으로 우선 m_list에 들어갔을 때, 증가되는 것으로 탐색되는 위치를 가리킨다.
    while len(left) > l_point and len(right) > r_point: #둘다 탐색이 끝나지 않았을 때 탐색이 끝났다면 point의 값이 len과 같기 때문
        if left[l_point] > right[r_point]:
            m_list.append(right[l_point])
            r_point += 1
        else:
            m_list.append(left[r_point])
            l_point += 1
    while len(left) > l_point:  #왼쪽 리스트만 남았을 경우, 왼쪽의 모든 잔여 값들을 더해야 하기 때문에 while을 썼다.
        m_list.append(left[l_point])
        l_point += 1

    while len(right) > r_point:
        m_list.append(right[r_point])
        r_point += 1

    return m_list

print(msort([left1[0]],[left1[1]]))
print (msort([right1[0]],[right1[1]]))
m_list1 = list()
for i in range(len(left1)-1):
    result = msort([left1[i]],[left1[i+1]])
m_list1.append(result)
for j in range(len(right1)-1):
    result2 = msort([right1[j]],[right1[j+1]])
m_list1.append(result2)
print(m_list1)  ##안의 값들을 잘라서 비교하고 합치는 것에 있어서 재귀의 사용이 필수적임을 알 수 있다.

print(mergesplit(left1+right1))




