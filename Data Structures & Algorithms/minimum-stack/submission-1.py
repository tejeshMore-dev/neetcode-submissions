class MinStack:

    def __init__(self):
        self._stack = []
        self._minStack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._minStack.append(val if not self._minStack else min(val, self._minStack[-1]))

    def pop(self) -> None:
        if self._stack:
            self._stack.pop()
            self._minStack.pop()

    def top(self) -> int:
        return self._stack[-1] if self._stack else None        

    def getMin(self) -> int:
        return self._minStack[-1] if self._minStack else None        

        
