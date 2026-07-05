from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        minutes = 0

        queue = deque([])
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
        minutes = 0
        while queue:
            length = len(queue)
        
            for _ in range(length):
                ele = queue.popleft()
                for dir in directions:
                    new_r = ele[0] + dir[0]
                    new_c = ele[1] + dir[1]
                    
                    if new_r>=0 and new_c>=0 and new_r<rows and new_c<cols:
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
                            queue.append((new_r, new_c))
            if queue:      
                minutes += 1

        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cnt+=1
        
        if cnt > 0:
            return -1

        return minutes