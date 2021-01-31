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
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        cur = self.head

        if len(linked_list) - k < 1:
            return cur

        for idx in range(len(linked_list) - k):
            cur = cur.next
        return cur


linked_list = LinkedList(6)
#print(len(linked_list))
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
#print(linked_list.get_kth_node_from_last(1).data)  # 7이 나와야 합니다!