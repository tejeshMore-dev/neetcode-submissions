from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue = deque([(r,c)])
                    level = 0
                    visited = set()

                    while queue:
                        q_len = len(queue)

                        for i in range(q_len):
                            c_r, c_c = queue.popleft()
                            visited.add((c_r, c_c))

                            for d_r, d_c in directions:
                                n_r = c_r + d_r
                                n_c = c_c + d_c

                                if n_r < 0 or n_c < 0 or n_r >= ROWS or n_c >= COLS or (n_r, n_c) in visited:
                                    continue
                                
                                if grid[n_r][n_c] <= 0:
                                    continue
                        
                                grid[n_r][n_c] = min(1 + level, grid[n_r][n_c])

                                queue.append((n_r, n_c))
                        
                        level += 1




