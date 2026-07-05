class Solution:
    PAIRS = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in self.PAIRS:
                if not stack or stack.pop() != self.PAIRS[char]:
                    return False
            else:
                stack.append(char)
    
        return not stack