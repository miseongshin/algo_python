#[3]->[4]
#data, next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(4)
node.next = first_node

print(node.next.data)
