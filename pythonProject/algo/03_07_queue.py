class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head : 4 -> tail 2
    # new node 3 > head 4 -> 2 -> tail 3
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty!!(dequeue)"
        delete_head = self.head
        self.head=self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Queue is Empty!!(peek)"
        return self.head.data

    def is_empty(self):
        return self.head is None

q = Queue()
q.enqueue(3)
print(q.peek())
q.enqueue(4)
print(q.peek())
q.enqueue(5)
print(q.peek())
q.dequeue()
print(q.peek())
print(q.is_empty())
print(q.peek())
q.dequeue()
print(q.is_empty())
print(q.peek())
print(q.dequeue())
print(q.is_empty())
print(q.peek())
print(q.dequeue())
