class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for opr in operations:
            if opr.lstrip("-").isdigit():
                stack.append(opr)
            elif opr == "+":
                num1 = int(stack[-1])
                num2 = int(stack[-2])
                num1 = num1+num2
                stack.append(str(num1))
            elif opr == "D":
                num1 = 2*int(stack[-1])
                stack.append(str(num1))
            elif opr == "C":
                stack.pop()
        
        ans = 0
        while stack:
            ans = ans + int(stack[-1])
            stack.pop()
        return ans