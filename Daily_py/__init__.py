class Node:
    def __init__(self,data,next=None): #next를 입력하지 않아도 defatul
        self.data = data
        self.next = next
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
    def add(self,data):
        if self.head=='':
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