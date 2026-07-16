import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])

        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        
        min_heap = []
        effort = [[float('inf')]*COLS for _ in range(ROWS)]
        effort[0][0] = 0
        heapq.heappush(min_heap,(effort[0][0], 0, 0))

        while min_heap:
            ele = heapq.heappop(min_heap)
            c_effort = ele[0]
            r = ele[1]
            c = ele[2]

            if r==ROWS-1 and c==COLS-1:
                return effort[r][c]
            
            for dir in dirs:
                n_r = r + dir[0]
                n_c = c + dir[1]

                if n_r < 0 or n_c < 0 or n_r >= ROWS or n_c >= COLS:
                    continue

                diff = abs(heights[r][c] - heights[n_r][n_c])
                n_effort = max(c_effort, diff)

                if n_effort<effort[n_r][n_c]:
                    effort[n_r][n_c] = n_effort
                    heapq.heappush(min_heap, (n_effort,n_r,n_c))
        

        