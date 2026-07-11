class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        PAIRS = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        for char in s:
            if char in PAIRS:
                if not stack or stack.pop() != PAIRS[char]:
                    return False
            else:
                stack.append(char)
    
        return not stack