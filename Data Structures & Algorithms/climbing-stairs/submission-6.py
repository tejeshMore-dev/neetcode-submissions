class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dfs(f):
            if f in mem:
                return mem[f]

            if f == n:
                return 1
            
            if f > n:
                return 0

            lf = dfs(f+1)
            rf = dfs(f+2)
            
            mem[f] = lf + rf
            return lf + rf

        return dfs(0)
            