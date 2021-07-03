##리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현
queue_list = list()
def enqueue(data):
    queue_list.append(data) ##append로 리스트에 더하기
def dequeue():
    data = queue_list[0]
    del queue_list[0] ##뺀 후에는 아얘 리스트에서 삭제해야 한다.
    return data

for index in range(10):
    print(enqueue(index))

print(len(queue_list))
print(dequeue())
