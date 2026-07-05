from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.seen = set()
        result = 0

        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == "1" and (r, c) not in self.seen:
                    result += 1
                    self.markIsland(r, c)
        
        return result
    
    def markIsland(self, r: int, c: int):
        # Check bounds and if already visited
        if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]) or (r, c) in self.seen or self.grid[r][c] == "0":
            return
        
        self.seen.add((r, c))
        # Explore all adjacent cells
        self.markIsland(r, c + 1)
        self.markIsland(r, c - 1)
        self.markIsland(r + 1, c)
        self.markIsland(r - 1, c)
