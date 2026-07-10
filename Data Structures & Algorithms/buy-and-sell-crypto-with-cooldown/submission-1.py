class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = {}
        def helper(i, base, bought):
            if (i,base,bought) in mem:
                return mem[(i,base,bought)]
            
            if i>=len(prices):
                return 0

            if bought:
                profit1 = helper(i+2,0,False) + prices[i]-base
            else:
                profit1 = helper(i+1,prices[i],True)
            profit2 = helper(i+1,base,bought)
            
            ans = max(profit1, profit2)
            mem[(i,base,bought)] = ans
            return ans
        
        return helper(0, 0, False)