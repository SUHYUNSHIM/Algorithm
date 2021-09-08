hash_table = list([i for i in range(10)])
print(hash_table)

day1 = 'Andy'
day2 = 'Dave'
day3 = 'Trump'
print(ord(day1[0]), ord(day2[0]),ord(day3[0]))

def hash_func(key):
    return key % 5
def storage_data(data,value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] =value

storage_data('Andy','01012123434')
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
    return hash(data)
def hash_function(key):
    return key % 8
def save_data(data,value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave','01034345656')
save_data('Andy','01012123434')
print(read_data('Dave'))

