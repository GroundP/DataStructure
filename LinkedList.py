
class Node:
    """링크드 리스트으 ㅣ노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None # 링크드 리스트의 가장 앞 노드
        self.tail = None # 링크드 리스트의 가장 뒤 노드

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""

        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node # 마지막 노드를 추가한 노드로 바꿔준다

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

        if previous_node.next is None:
            self.append(data)
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node

    def deleter_after(self, previous_node):
        """주어진 노드 뒤 노드를 삭제"""

        deleted_data = previous_node.next.data

        if previous_node.next is not None:
            # 지우려는 노드가 tail 노드일 때
            if previous_node.next.next is self.tail:
                previous_node.next = None
                self.tail = previous_node
            # 두 사이 노드를 지울 때
            else:
                previous_node.next = previous_node.next.next

        return deleted_data


List1 = LinkedList()
List1.append(3)
List1.append(4)
List1.append(5)

node3 = List1.GetNode(3)
List1.insert_after(node3, 7)

List1.deleter_after(node3)

List1.printList()