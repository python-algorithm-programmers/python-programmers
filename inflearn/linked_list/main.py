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



if __name__ == "__main__":
    first_node = LinkedList(5)
    first_node.append(2)
    first_node.append(4)
    first_node.append(6)
    first_node.print_all()



