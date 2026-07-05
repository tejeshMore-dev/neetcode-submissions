class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not len(self.stack):
            self.stack.append([val, val])
        else:
            min_v = self.getMin()
            min_v = min(min_v, val)
            self.stack.append([val, min_v])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
