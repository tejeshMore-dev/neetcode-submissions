class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * 30
        def helper(i):
            if (i >= n):
                return  i == n

                if cache[i] != -1:
                    return cache[i]

            cache[i] = helper(i+1) + helper(i+2)
            return cache[i]
        
        return helper(0)