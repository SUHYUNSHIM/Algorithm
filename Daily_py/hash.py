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

#####
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

#충돌 해결

