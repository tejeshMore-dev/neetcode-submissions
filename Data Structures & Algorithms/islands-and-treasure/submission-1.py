from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        INF = 2147483647
        queue = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            q_len = len(queue)

            for i in range(q_len):
                c_r, c_c = queue.popleft()

                for d_r, d_c in directions:
                    n_r = c_r + d_r
                    n_c = c_c + d_c

                    if n_r < 0 or n_c < 0 or n_r >= ROWS or n_c >= COLS or grid[n_r][n_c] != INF:
                        continue
                    
                    grid[n_r][n_c] = 1 + grid[c_r][c_c]
                    queue.append((n_r, n_c))
            



