class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 1:
            return cost[0]
        
        if n == 2:
            return min(cost[0], sum(cost))
        
        i = 0
        res = [0]*n
        res[n-1] = cost[n-1]
        res[n-2] = cost[n-2]

        for i in range(n-3,-1,-1):
            res[i] = min(res[i+1],res[i+2])+cost[i]
        
        return min(res[0],res[1])
            