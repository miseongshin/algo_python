class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            print("비었음")
            return
        delete_head = self.head
        self.head = delete_head.next
        return delete_head

    def peek(self):
        if self.isEmpty():
            print("비었음")
            return
        return self.head.data


q = Queue()
q.enqueue(3)
print(q.peek())
q.enqueue(4)
print(q.peek())
print(q.dequeue().data)
print(q.peek())

