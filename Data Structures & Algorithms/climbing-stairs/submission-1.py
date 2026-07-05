class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i):
            if (i >= n):
                if i == n:
                    return 1
                else:
                    return 0
                         
            return helper(i+1) + helper(i+2)
        
        return helper(0)