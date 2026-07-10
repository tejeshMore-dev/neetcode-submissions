class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = {}
        def helper(i, cur_sum):
            if (i,cur_sum) in mem:
                return mem[(i,cur_sum)]

            if i>=len(coins) or cur_sum>amount:
                return 0
            
            if cur_sum == amount:
                return 1
            
            ans = helper(i, cur_sum+coins[i]) + helper(i+1, cur_sum)
            mem[(i, cur_sum)] = ans
            return ans
        
        return helper(0, 0)