class Solution:
    def integerBreak(self, n: int) -> int:
        
        mem = {}

        def dfs(i, cur_sum):
            if cur_sum in mem:
                return mem[cur_sum]

            if i>=n:
                return 0

            if cur_sum == n:
                return 1
            
            if cur_sum>n:
                return 0
            
            ans = max(i*dfs(i, cur_sum+i), dfs(i+1, cur_sum))
            mem[cur_sum] = ans
            return ans

        return dfs(1,0)