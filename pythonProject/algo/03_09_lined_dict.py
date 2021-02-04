class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key,value))

    def get(self, key):
        for k,v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self,key,value):
        index = hash(key)%len(self.items)
        #LinkedTuple
        self.items[index].add(key,value)

    def get(self,key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

#hash("사") %8   >>1
#hash("다") %8   >>1
l = LinkedDict();
a ="바"
b ="자"
print(a,b,(hash(a) %8)==(hash(b) %8))
l.put(a,"사자")
l.put(b,"다리미")
print(l.get(a))
print(l.get(b))