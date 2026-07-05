class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def helper(ans, openedB, closedB):
            if len(ans) == 2 * n:
                result.append("".join(ans.copy()))
                return
            
            if openedB < n:
                ans.append("(")
                helper(ans, openedB + 1, closedB)
                ans.pop()
            
            if closedB < openedB:
                ans.append(")")
                helper(ans, openedB, closedB + 1)
                ans.pop()

        helper([], 0, 0)
        return result
        
