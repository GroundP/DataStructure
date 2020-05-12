
class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""

        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            new_node.prev = self.tail  # 새로운 노드의 앞은 현재 tail Node
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def GetNode(self, data):
        iterator = self.head

        while(iterator is not None):
            if iterator.data == data:
                return  iterator
            else:
                iterator = iterator.next

        return iterator

    def printList(self):
        """에라 모르겠다 프린트"""
        print_node = self.head

        while(print_node is not None):
            print(print_node.data)
            print_node = print_node.next

    def insert_after(self, previous_node, data):
        """주어진 노드 뒤 삽입 연산 메소드"""

        new_node = Node(data)

        # 데이터가 하나밖에 없고, 그 뒤에 추가하는 경우
        if previous_node.next is None:
            self.append(data)

        # 데이터가 여러개 있는 경우
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node
            previous_node.next.prev = new_node
            new_node.prev = previous_node

    def delete(self, node):
        """주어진 노드 뒤 노드를 삭제"""

        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        return node.data





List1 = LinkedList()
List1.append(2)
List1.append(3)
List1.append(5)
List1.append(7)

Node3 = List1.GetNode(3)
List1.delete(Node3)
List1.printList()

print("")

Node2 = List1.GetNode(2)
List1.delete(Node2)
List1.printList()

print("")

Node7 = List1.GetNode(7)
List1.delete(Node7)
List1.printList()