class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        rows = len(grid)
        cols = len(grid[0])

        ans = 0

        def helper(r,c):
            nonlocal ans

            if r<0 or c<0 or r>=rows or c>=cols :
                return 0
            
            if grid[r][c] == 0 or grid[r][c] == -1:
                return 0

            grid[r][c] = -1

            cur_area = 0
            for dir in directions:
                new_r = r + dir[0]
                new_c = c + dir[1]
                cur_area += helper(new_r,new_c)
            
            return cur_area + 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = helper(r,c)
                    ans = max(ans,area)
        
        return ans