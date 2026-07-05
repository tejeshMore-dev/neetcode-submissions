class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0

        def helper(i):
            nonlocal result
            
            if i >= n:
                if i == n:
                    result += 1
                return            

            helper(i+1)
            helper(i+2)
        
        helper(0)
        return result