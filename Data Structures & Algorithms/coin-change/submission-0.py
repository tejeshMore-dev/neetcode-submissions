class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dfs(cnt,sum):
            if (cnt,sum) in mem:
                return mem[(cnt,sum)]

            if sum == amount:
                return cnt            

            min_cnt = pow(2,31)
            for coin in coins:
                if sum+coin > amount:
                    continue
                min_cnt = min(dfs(cnt+1,sum+coin),min_cnt)
            
            mem[(cnt,sum)] = min_cnt
            return min_cnt
        
        ans = dfs(0,0)
        if ans == pow(2,31):
            return -1
        return ans
