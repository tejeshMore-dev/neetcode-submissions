import sys

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = sys.maxsize

        def helper(i, currentCost):
            nonlocal result

            if i >= len(cost):
                result = min(currentCost, result)
                return
            
            helper(i+1, currentCost + cost[i])
            helper(i+2, currentCost + cost[i])

        helper(0, 0)
        helper(1, 0)

        return result
