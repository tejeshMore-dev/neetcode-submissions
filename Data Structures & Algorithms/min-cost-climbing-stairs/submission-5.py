class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c_map = {}

        def dfs(i):
            if i in c_map:
                return c_map[i]

            if i>=len(cost):
                return 0

            c1 = dfs(i+1) + cost[i]
            c2 = dfs(i+2) + cost[i]

            c_min = min(c1,c2)

            c_map[i] = c_min
            return c_min
        
        return min(dfs(0), dfs(1))
            

