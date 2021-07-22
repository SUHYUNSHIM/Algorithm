##저장하는 공간과 뒤에 나올 데이터가 나올 공간을 가리키는 주소를 가리키는 값을 저장한다.
##노드, 포인터
##node 구현, 클래스가 객체를 만들 때마다 노드 생성.
'''''
class Node1:
    def __init(self,data):
        self.data = data
        self.next = None
'''''
##노드 값, 다음 노드 인자를 가리키는 주소를 넣는다.
class Node:
    def __init__(self,data,next=None):
        self.data= data
        self.next = next

node1 = Node(1)
node2 = Node(2)
##객체를 두 개 만든 셈.
node1.next = node2
head = node1

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)
    ##현재 노드는 마지막 노드
    ##현재 노드의 next는 none인 상태
    ##여기에 새로운 객체를 생성하면
    ##인자로 받는 data로
    ##마지막 노드의 주소에 지금 생성한 노드가 늘 가리키게 한다.
