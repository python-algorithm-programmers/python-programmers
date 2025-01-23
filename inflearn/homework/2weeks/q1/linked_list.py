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

    def get_node(self, index):
        cur_idx = 0
        cur = self.head

        if index == 0:
            return cur.data

        while cur.next is not None:
            cur_idx += 1
            cur = cur.next

            if cur_idx == index:
                return cur.data

    def get_kth_node_from_last(self, k):
        # 마지막 node의 인덱스 찾기
        cur = self.head
        last_idx = 0

        while cur.next is not None:
            last_idx += 1
            cur = cur.next

        return self.get_node(last_idx+1-k)


if __name__ == "__main__":
    import sys
    sys.stdin = open("input.txt")
    n = int(input())

    # 초기 세팅
    link = LinkedList(6)
    link.append(7)
    link.append(8)
    print(link.get_kth_node_from_last(n))