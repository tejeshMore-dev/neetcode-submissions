class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [1,0]]
        rows = len(grid)
        cols = len(grid[0])
        INF = float('inf')
        mem = {}

        def helper(r,c):
            if (r,c) in mem:
                return mem[(r,c)]

            if r<0 or c<0 or r>=rows or c>=cols:
                return INF
            
            if r==rows-1 and c==cols-1:
                return grid[r][c]
            
            ans = INF
            for dir in directions:
                new_r = r + dir[0]
                new_c = c + dir[1]
                ans = min(ans, helper(new_r, new_c)+grid[r][c])
            
            mem[(r,c)] = ans
            return ans

        return helper(0,0) 