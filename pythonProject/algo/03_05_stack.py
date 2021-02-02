from _ast import Not


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # 3->4
    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # 3
    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is Empty!"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Stack is Empty!!!"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stact = Stack()
stact.push(3)
print(stact.peek())
stact.push(4)
print(stact.peek())
print(stact.pop().data)
print(stact.is_empty())
print(stact.pop().data)
print(stact.is_empty())
#파이썬 스택 리스트 이용
print("-------------------------")
py_stack = []
py_stack.append(4)
py_stack.append(3)
top = py_stack.pop()
print(top)

