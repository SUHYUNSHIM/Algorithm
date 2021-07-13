##큐 -> 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
##put, get
import queue
data_queue = queue.Queue()
data_queue.put("hello_future")
data_queue.put(127)

print(data_queue.get())
print(data_queue.qsize())

print(data_queue.get())
print(data_queue.qsize())

##우선순위를 부여한 Queue도 만들 수 있다.
data_queue = queue.PriorityQueue()
data_queue.put((10, "korea")) ##데이터가 튜플로 들어가기 때문에 괄호를 두개 쓴다.
data_queue.put((5, 1)) ##우선순위, 들어가는 데이터
data_queue.put((15, "canada"))

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())

