import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        min_heap = []
        heapq.heappush(min_heap,(grid[0][0],0,0))

        cost = [[float('inf')]*COLS for _ in range(ROWS)]
        cost[0][0] = 0

        while min_heap:
            ele = heapq.heappop(min_heap)
            c_cost = ele[0]
            r = ele[1]
            c = ele[2]

            for dir in dirs:
                n_r = r + dir[0]
                n_c = c + dir[1]

                if n_r<0 or n_c<0 or n_r>=ROWS or n_c>=COLS:
                    continue
                
                n_cost = max(c_cost,grid[n_r][n_c])

                if c_cost>=cost[n_r][n_c] or n_cost>=cost[n_r][n_c]:
                    continue
                
                cost[n_r][n_c] = n_cost
                heapq.heappush(min_heap, (n_cost,n_r,n_c))
        
        return cost[ROWS-1][COLS-1]


        