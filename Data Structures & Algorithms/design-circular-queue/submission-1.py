class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.limit = k
        self.head = None
        self.end = self.head

    def enQueue(self, value: int) -> bool:
        new_node = ListNode(value)
        if self.size == 0:
            self.head = new_node
            self.end = new_node
            self.head.next = self.end
            self.size += 1
            return True
        elif self.size < self.limit:
            self.end.next = new_node
            self.end = new_node
            self.end.next = self.head
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.size == 1:
            self.end = None
            self.head = None
            self.size -= 1
            return True
        elif self.size > 1:
            self.end.next = self.head.next
            self.head = self.head.next
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.size > 0:
            return self.head.val
        else: 
            return -1

    def Rear(self) -> int:
        if self.size > 0:
            return self.end.val
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.limit:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.end()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()