class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        def dfs(r,c):
            nonlocal perimeter

            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] != 1 or (r,c) in visited:
                return

            visited.add((r,c))
            
            for direction in directions:
                new_row = r + direction[0]
                new_col = c + direction[1]

                if new_row >= rows or new_col >= cols or new_row < 0 or new_col < 0 or grid[new_row][new_col] == 0:
                    perimeter += 1

                dfs(new_row, new_col)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row,col)
                    break

        return perimeter

