class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

def get_single_sum(linked_list):
    sum = 0
    cur = linked_list.head
    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next
    return sum

def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = get_single_sum(linked_list_1)
    sum_2 = get_single_sum(linked_list_2)
    return sum_1 + sum_2

def josephus_problem(n, k):
    # first setting
    link = LinkedList(1)
    for i in range(2, n+1):
        link.append(i)

    # 꼬리 잇기
    result_list = []
    tail = link.get_node(n - 1)
    tail.next = link.head

    # head change
    while n > 0:
        # k번째 노드 연결 삭제
        result_list.append(link.get_node(k-1).data)
        link.delete_node(k-1)

        # head 바꾸기
        k_node = link.get_node(k-1)
        link.head = k_node

        # 노드 갯수 감소
        n -= 1

        # 노드 없으면 종료
        if n == 0:
            break

    print("<", ", ".join(map(str, result_list)), ">", sep='')

def solution(n, k):
    circle_list = [i for i in range(1, n+1)]
    result_list = []
    next_index = k-1

    while circle_list:
        result = circle_list.pop(next_index)
        result_list.append(result)
        if len(circle_list) != 0:
            next_index = (next_index + k-1) % len(circle_list)

    return f"<{', '.join(map(str,result_list))}>"


if __name__ == '__main__':
    import sys
    # sys.stdin = open('input.txt')
    n, k = map(int, input().split())
    print(solution(n, k))
