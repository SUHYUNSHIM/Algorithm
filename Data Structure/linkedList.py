class Node1:
    def __init__(self,data):
        self.data = data
        self.next = None
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
##노드 연결하기
node1 = Node(1) ##객체 생성 . data에 1을 넣음
node2 = Node(2) ##객체 생성. data에 2를 넣음
node1.next = node2
head = node1

##데이터 추가하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1
for index in range(2,10):
    add(index)
##데이터 검색, 출력하기
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

##링크드 리스트 데이터 사이에 데이터를 추가
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

node3 = Node(1.5)
node = head
search = True
while search:
    if node.data ==1:
        search = False
    else:
        node= node.next
node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

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

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()




