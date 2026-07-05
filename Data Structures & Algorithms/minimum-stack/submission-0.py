class MinStack:

    def __init__(self):
        self.__stack = []
        self.__minStack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        self.__minStack.append(val if not self.__minStack else min(val, self.__minStack[-1]))

    def pop(self) -> None:
        if self.__stack:
            self.__stack.pop()
        
        if self.__minStack:
            self.__minStack.pop()

    def top(self) -> int:
        return self.__stack[-1] if self.__stack else None        

    def getMin(self) -> int:
        return self.__minStack[-1] if self.__minStack else None        

        
