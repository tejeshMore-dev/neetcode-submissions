class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mem = {}
        
        def helper(i, bought, val=0):
            if (i,bought,val) in mem:
                return mem[(i,bought,val)]
            
            if i>=len(prices):
                return 0
            
            if not bought:
                a = helper(i+1, False, 0)
                b = helper(i+1, True, prices[i])
                profit = max(a,b)
            else:
                a = helper(i+1, bought, val)
                b = helper(i+1, True, prices[i]) + prices[i] - val
                c = helper(i+1, False, 0) + prices[i] - val
                profit = max(a,b,c)
            
            mem[(i,bought,val)] = profit
            
            return profit
        
        return helper(0,False)
