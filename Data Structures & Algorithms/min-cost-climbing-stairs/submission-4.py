import sys

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)

        def helper(i, currentCost):
            if i >= len(cost):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            return cost[i] + min(helper(i+1, currentCost + cost[i]),helper(i+2, currentCost + cost[i]))

        return min(helper(0, 0), helper(1, 0))