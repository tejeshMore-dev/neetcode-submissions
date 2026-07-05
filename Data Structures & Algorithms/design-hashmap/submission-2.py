class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [ [] for _ in range(self.size + 1) ]

    def hash (self, key):
        return key // self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.hash(key)

        for i, (k, v) in enumerate(self.buckets[bucket]):
            if k == key:
                self.buckets[bucket][i] = (key, value)
                return
        
        self.buckets[bucket].append((key, value))

    def get(self, key: int) -> int:
        bucket = self.hash(key)

        for i, (k, v) in enumerate(self.buckets[bucket]):
            if k == key:
                return v        

        return -1

    def remove(self, key: int) -> None:
        bucket = self.hash(key)
        for i, (k, v) in enumerate(self.buckets[bucket]):
            if k == key:
                self.buckets[bucket].pop(i)




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)