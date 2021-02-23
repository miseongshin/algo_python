class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def __len__(self):
        cur = self.head
        list_len = 1
        while cur.next is not None:
            list_len += 1
            cur = cur.next
        return list_len

    def append(self, value):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(value)

    def print_all(self):
        current_node = self.head
        print_text = current_node.data
        while current_node.next is not None:
            current_node = current_node.next
            print_text += ", " + current_node.data
        print(print_text)

    def get_node(self, index):
        current_node = self.head
        for i in range(0, index):
            if current_node.next is None:
                print("데이터가 존재하지 않습니다.")
                return None
            current_node = current_node.next
        return current_node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        before_node = self.get_node(index - 1)
        if before_node is None:
            print("추가할수가 없습니다.")
            return
        new_node.next = before_node.next
        before_node.next = new_node

    def delete_node(self, index):

        if index == 0:
            self.head = self.head.next
            return
        before_node = self.get_node(index - 1)
        if before_node is None:
            print("삭제할수가 없습니다.")
            return
        before_node.next = before_node.next.next


linked_list = LinkedList("a")
print(linked_list.head.data)
linked_list.append("b")
linked_list.print_all()
print(linked_list.get_node(1).data)
linked_list.add_node(0, "first")
linked_list.print_all()
linked_list.add_node(1, "2th")
linked_list.add_node(2, "3th")
linked_list.add_node(3, "4th")
linked_list.add_node(3, "4th")
linked_list.print_all()
linked_list.add_node(10, "4th")
linked_list.delete_node(10)
linked_list.delete_node(0)
linked_list.print_all()
linked_list.delete_node(3)
linked_list.print_all()