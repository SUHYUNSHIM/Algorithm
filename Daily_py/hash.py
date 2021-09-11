hash_table = list([i for i in range(10)])
print(hash_table)

day1 = 'Andy'
day2 = 'Dave'
day3 = 'Trump'
print(ord(day1[0]), ord(day2[0]),ord(day3[0])) #문자의 아스키 코드 리턴

def hash_func(key):
    return key % 5 #5로 나눈 나머지
print(ord(day1[0]),hash_func(ord(day1[0]))) #데이터, 키값 출력

def storage_data(data,value):
    key = ord(data[0]) #단어의 첫글자.
    hash_address = hash_func(key) #해시 함수에 의해 키값 생성.
    hash_table[hash_address] =value #키 번째 인덱스에 값을 넣는다.

storage_data('Andy','01012123434')  #data, value
storage_data('Dave','01034345656')
storage_data('Trump','0109998989')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))

########################################################################
hash_table = list([0 for i in range(8)])
def get_key(data):
    return hash(data) #hash 함수, 이것은 내장 함수이다.
def hash_function(key):
    return key % 8

def save_data(data,value):
    hash_address = hash_function(get_key(data)) #key로 변환하고 그 안에 넣는다.
    hash_table[hash_address] = value
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave','01034345656')
save_data('Andy','01012123434')
print(read_data('Dave'))

#충돌 해결#
hash_table = list([0 for i in range(8)]) ##[0,0,0,0,0,0,0,0]
def get_key(data):
    return hash(data) #hash 함수, 이것은 내장 함수이다.
def hash_function(key):
    return key % 8

def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key) #key로 변환하고 그 안에 넣는다.
    if hash_table[hash_address] !=0: #value가 0이 아니다. 이미 하나가 들어가 있다.
        for index in range(len(hash_table[hash_address])): #현재 해시 테이블 탐색
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key,value]) #테이블 밖에 추가.for문을 빠져나오고 나서.
    else:
        hash_table[hash_address] = [[index_key,value]] #비어있다면 그냥 넣는다.
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] !=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key: #index_key로 찾았다면
                return hash_table[hash_address][index][1] #그 value를 가져온다.
            return None #None 없다.
    else:
        return None

print(hash('Dd')%8)
print(hash('Data')%8)
save_data('Dd','1201023010')
save_data('Data','3301023010')
print("충돌해결 " + read_data('Dd'))
print(hash_table)

#####linear probling
hash_table = list([0 for i in range(8)]) ##[0,0,0,0,0,0,0,0]
def get_key(data):
    return hash(data) #hash 함수, 이것은 내장 함수이다.
def hash_function(key):
    return key % 8

def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key) #key로 변환하고 그 안에 넣는다.

    if hash_table[hash_address] !=0: #value가 0이 아니다. 이미 하나가 들어가 있다.
        for index in range(hash_address,len(hash_table)): # 시작점,8. 데이터 순회
            if hash_table[index] == 0: #비어있는 다음 곳에 넣는다
                hash_table[index] = [index_key,value]
                return
            elif hash_table[index][0] == index_key: #키가 동일하면 해당 값만 업데이트 한다. 11,21
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key,value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] !=0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None
print(hash('dk')%8)
print(hash('da')%8)
print(hash('dc')%8)

save_data('dk','01200123123')
save_data('da','33333333333')
read_data('dc')

######
