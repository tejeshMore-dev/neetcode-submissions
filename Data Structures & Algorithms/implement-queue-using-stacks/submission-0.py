class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            return
        
        ele = self.stack[-1]
        self.stack.pop()
        self.push(x)
        self.stack.append(ele)

    def pop(self) -> int:
        ele = self.stack[-1]
        self.stack.pop()
        return ele

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()