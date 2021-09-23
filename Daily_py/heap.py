class Heap:
    def __init__(self,data):
        self.heap_array =list() #파이썬의 배열은 리스트로
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self,inserted_idx):
        if inserted_idx <= 1: #루트노드
            return False
        parent_idx = inserted_idx//2
        if self.heap_array[inserted_idx]>self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self,data):
        if len(self.heap_array)==0: #루트 노드가 없을 떄
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        #return True

        inserted_idx = len(self.heap_array)-1 #현재 인덱스 값 저장

        while self.move_up(inserted_idx): #부모노드를 바꿔주는 것. 가장 클 때까지
            parent_idx = inserted_idx//2 #몫
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True

#heap = Heap(1)
#print(heap.heap_array)

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
