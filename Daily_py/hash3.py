import hashlib
hash_table = list([0 for i in range(8)])
def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig,16)
