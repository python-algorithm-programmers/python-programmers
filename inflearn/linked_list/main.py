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
        cur = self.head
        cur_idx = 0

        while cur_idx != index:
            cur = cur.next
            cur_idx += 1

        return cur

    def add_node(self, index, value):
        if index < 0:
            return 0

        # 인덱스가 0일 때 문제
        elif index == 0:
            new_node = Node(value)

            # 링크드 리스트는 첫번째 head만 갖고 있는 형태
            new_node.next = self.head
            self.head = new_node

        else:
            # 이전꺼 까지만 이동
            # 이전꺼 노드에 붙이기
            past_node = self.get_node(index-1)
            next_node = past_node.next

            input_node = Node(value)
            past_node.next = input_node

            # 입력시킨 것에 다음꺼 연결
            input_node.next = next_node

    def delete_node(self, index):
        if index < 0:
            return 0

        elif index == 0:
            self.head = self.get_node(index+1)

        else:
            past_node = self.get_node(index-1)
            next_node = self.get_node(index+1)
            past_node.next = next_node


if __name__ == "__main__":
    linked_list = LinkedList(5)
    linked_list.append(2)
    linked_list.append(4)
    linked_list.append(6)
    linked_list.delete_node(2)
    linked_list.print_all()
    # print(linked_list.get_node(0).data)




