class MyHashSet:

    def __init__(self):
        self._bucket = [ False ] * 100000

    def add(self, key: int) -> None:
        self._bucket[key] =True

    def remove(self, key: int) -> None:
        self._bucket[key] = False

    def contains(self, key: int) -> bool:
        return self._bucket[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)