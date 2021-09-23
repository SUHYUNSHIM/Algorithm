class Heap:
    def __init__(self,data):
        self.heap_array =list() #파이썬의 배열은 리스트로
        self.heap_array.append(None)
        self.heap_array.append(data)

    def insert(self,data):
        if len(self.heap_array)==0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        return True

heap = Heap(1)
print(heap.heap_array)