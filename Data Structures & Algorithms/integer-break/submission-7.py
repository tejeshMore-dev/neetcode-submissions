class Solution:
    def integerBreak(self, n: int) -> int:
        mem = {}
        
        def helper(i, sum):
            if (i, sum) in mem:
                return mem[(i, sum)]

            if sum == n:
                return 1
            
            if sum > n:
                return 0

            if i > n - 1:
                return 0

            ans = 0 
            # using
            ans = max (ans, i * helper(i, i + sum))
            # not using
            ans = max (ans, helper(i + 1, sum))
            
            mem[(i, sum)] = ans
            return ans
        
        return helper(1, 0)