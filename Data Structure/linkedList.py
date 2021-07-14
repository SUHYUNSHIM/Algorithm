class Node1:
    def __init__(self,data):
        self.data = data
        self.next = None
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1
##노드 연결하기 


