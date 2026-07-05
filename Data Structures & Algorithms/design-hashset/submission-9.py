class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        bucket = self.hash(key)

        if key not in self.buckets[bucket]:
            self.buckets[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = self.hash(key)

        if key in self.buckets[bucket]:
            self.buckets[bucket].remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.hash(key)

        return key in self.buckets[bucket]