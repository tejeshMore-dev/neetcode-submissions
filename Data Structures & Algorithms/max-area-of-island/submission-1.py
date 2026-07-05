class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.ROWS = len(self.grid)
        self.COLS = len(self.grid[0])
        self.seen = set()
        maxArea = 0

        for r in range(self.ROWS):
            for c in range(self.COLS):
                print(r,c)
                if self.grid[r][c] == 1 and (r,c) not in self.seen:
                    maxArea = max(maxArea, self.findArea(r,c))
        
        return maxArea
    
    def findArea(self, r,c):
        if r < 0 or r >= self.ROWS  or c < 0 or c >= self.COLS or (r,c) in self.seen or self.grid[r][c] == 0:
            return 0
        
        self.seen.add((r,c))
        return 1 + self.findArea(r+1,c) + self.findArea(r-1,c) + self.findArea(r,c+1) + self.findArea(r,c-1)

        