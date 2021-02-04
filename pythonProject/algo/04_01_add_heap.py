class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        insert_idx = len(self.items) - 1
        while insert_idx > 1:
            parent_index = insert_idx//2
            if self.items[insert_idx] < self.items[parent_index]:
                break
            self.items[insert_idx], self.items[parent_index]=self.items[parent_index],self.items[insert_idx]
            insert_idx = parent_index


max_heap = MaxHeap()
max_heap.insert(3)
print(max_heap.items)
max_heap.insert(4)
print(max_heap.items)
max_heap.insert(2)
print(max_heap.items)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!

#O(log(N))