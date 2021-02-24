class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        next_node = self.head
        self.head = Node(value)
        self.head.next = next_node

    def pop(self):
        return_node = self.head
        if self.is_empty():
            print("비었음")
            return
        self.head = return_node.next
        return return_node

    def peek(self):
        if self.is_empty():
            print("비었음")
            return
        return self.head.data

    def isEmpty(self):
        return self.head is None


s = Stack()
s.push("b")
s.push("c")
print(s.peek())
print(s.pop().data)
print(s.peek())
print(s.isEmpty())
print(s.pop().data)
print(s.isEmpty())