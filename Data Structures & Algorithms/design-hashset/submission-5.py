class MyHashSet:

    def __init__(self):
        self._size = 1000
        self._buckets = [[] for _ in range(self._size)]

    def _hash(self, key):
        return key // self._size

    def add(self, key: int) -> None:
        bucket = self._buckets[self._hash(key)]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self._buckets[self._hash(key)]
        
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self._buckets[self._hash(key)]

        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)