from DoublyLinkedList4HashTable import LinkedList  # 해시 테이블에서 사용할 링크드 리스트 임포트


class HashTable:
    """해시 테이블 클래스"""

    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이여야 한다.
        """
        return hash(key) % self._capacity

    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        hash_value = self._hash_function(key)
        linked_list = self._table[hash_value]

        return linked_list.find_node_with_key(key).value

        # 코드를 쓰세요

    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다
        """
        hash_value = self._hash_function(key)
        linked_list = self._table[hash_value]
        OrgNode = linked_list.find_node_with_key(key)

        # 리스트에 저장된 pair가 없을 때
        if OrgNode is None:
            linked_list.append(key, value)

        # 있을 때
        else:
            OrgNode.value = value

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]


test_scores = HashTable(50)  # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

print(test_scores)

# key인 이름으로 특정 학생 시험 점수 검색
print(test_scores.look_up_value("현승"))
print(test_scores.look_up_value("태호"))
print(test_scores.look_up_value("영훈"))

# 학생들 시험 점수 수정
test_scores.insert("현승", 10)
test_scores.insert("태호", 20)
test_scores.insert("영훈", 30)

print(test_scores)

from collections import deque


def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    print(f"테스트하는 문자열: {string}")
    stack = deque()  # 사용할 스택 정의

    for i in string:
        stack.append(i)

    leftSyn = []
    rightSyn = []

    for i in range(len(stack)):
        Data = stack[i]
        if Data == ")":
            rightSyn.append((i, Data))

        if Data == "(":
            leftSyn.append((i, Data))

    leftSize = len(leftSyn)
    rightSize = len(rightSyn)

    if leftSize > rightSize:
        Diff = leftSize - rightSize
        while (Diff > 0):
            print("문자열 {} 번째 위치에 있는 괄호가 닫히지 않았습니다".format(leftSyn[Diff - 1][0]))
            Diff = Diff - 1

    if leftSize < rightSize:
        Diff = rightSize - leftSize
        while (Diff > 0):
            print("문자열 {} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다".format(rightSyn[rightSize - (Diff)][0]))
            Diff = Diff - 1


case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)