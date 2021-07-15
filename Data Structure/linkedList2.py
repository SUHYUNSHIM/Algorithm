##파이썬 객체 지향 프로그래밍으로 링크드 리스트 구현하기
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head =='':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def delete(self,data):
        if self.head=='': ##데이터가 아얘 없는 상황이라면
            print("해당 값을 가진 노드가 없습니다.")
            return
        if self.head.data == data: ##헤더를 삭제
            temp = self.head ##객체를 삭제하기 위해 임시 변수에 옮겨 놓음
            self.head = self.head.next ##지금 헤더를 다음 노드의 주소로 바꿔준다.
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data ==data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
linkedlist1.head
linkedlist1.delete(0)
linkedlist1.head

for data in range(1,10):
    linkedlist1.add(data)
linkedlist1.desc()