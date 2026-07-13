class ListNode:

    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.c_map = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        next1 = node.next

        prev.next = next1
        next1.prev = prev

    def insert(self, node):
        prev = self.tail.prev

        node.prev = prev
        node.next = self.tail
        prev.next = node

        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.c_map:
            return -1
        
        cur = self.c_map[key]
        self.remove(cur)
        self.insert(cur)   

        return cur.val

    def put(self, key: int, value: int) -> None:

        if key in self.c_map:
            node = self.c_map[key]
            node.val = value

            self.remove(node)
            self.insert(node)
            
            return
        
        new_node = ListNode(key, value)
        self.insert(new_node)
        self.size += 1

        self.c_map[key] = new_node

        if self.size > self.capacity:
            lru = self.head.next

            self.remove(lru)
            del self.c_map[lru.key]

            self.size -= 1
        