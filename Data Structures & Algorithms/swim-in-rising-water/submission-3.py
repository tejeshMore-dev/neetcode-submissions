from collections import deque
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        INF = float('inf')
        ans_grid = [ [INF] * COLS for _ in range(ROWS) ]

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], 0, 0))


        while min_heap:
            v, r, c = heapq.heappop(min_heap)

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue

                nw = max(grid[nr][nc], v)

                if ans_grid[nr][nc] > nw:
                    ans_grid[nr][nc] = nw
                else:
                    continue

                heapq.heappush(min_heap, (nw , nr, nc))
        
        return ans_grid[ROWS-1][COLS-1]


            

        