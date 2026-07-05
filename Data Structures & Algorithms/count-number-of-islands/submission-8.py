class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]

        def helper(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >=  COLS or grid[r][c] == "#" or grid[r][c] == "0":
                return 

            grid[r][c] = "#"

            for direction in directions:
                new_r = r + direction[0]
                new_c = c + direction[1]
                helper(new_r, new_c)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    helper(r,c)
                    ans += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "#":
                    grid[r][c] = "1"

        return ans
