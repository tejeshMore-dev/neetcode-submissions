class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: int(a / b),
        }
        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                res = operations[token](a, b)
                stack.append(res)
        
        return stack[-1]