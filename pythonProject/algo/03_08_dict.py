class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        self.items[hash(key) % len(self.items)] = value
        #key

    def get(self, key):
        return self.items[hash(key) % len(self.items)]


d = Dict()
d.put("test", 3)
print(d.get("test"))



#충돌발생
#1) 링크드 리스트
