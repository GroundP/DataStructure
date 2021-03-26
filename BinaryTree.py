class Node:
    """이진 트리 노드 클래스"""

    def __init__(self, data):
        """데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left = None
        self.right = None



"""노드 인스턴스 생성"""
node_root = Node(2)
node_B = Node(3)
node_C = Node(4)
node_D = Node(7)
node_E = Node(9)

# Test
# Temp Test
# B와 C를 root 노드의 자식으로 지정
node_root.left = node_B
node_root.right = node_C

# D와 E를 B노드의 자식으로 지정
node_B.left = node_D
node_B.right = node_E

# root 노드의 왼쪽자식 받아오기
node_test = node_root.left

print(node_test.data)
