class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1,0]]
        m = len(grid)
        n = len(grid[0])
        mem = {}
        MAX = float('inf')

        def helper(r,c):
            if (r,c) in mem:
                return mem[(r,c)]

            if r < 0 or c < 0 or r == m or c == n:
                return MAX
            
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            
            cur_sum = MAX 
            for dr, dc in directions:
                cur_sum = min(cur_sum, helper(dr + r, dc + c) + grid[r][c])
            
            mem[(r,c)] = cur_sum
            return cur_sum

        return helper(0,0)           