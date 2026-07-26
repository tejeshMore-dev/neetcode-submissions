class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        ROWS = len(heights)
        COLS = len(heights[0])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def dfs(r, c, ocean):
            if ocean == 1:
                if (r, c) in pacific:
                    return

                pacific.add((r, c))
            else:
                if (r, c) in atlantic:
                    return

                atlantic.add((r, c))

            for dr, dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or heights[nr][nc] < heights[r][c]:
                    continue
                
                dfs(nr, nc, ocean)


        # pacific
        for c in range(COLS):
            dfs(0, c, 1)
        
        for r in range(ROWS):
            dfs(r, 0, 1)

        # atlantic
        for c in range(COLS):
            dfs(ROWS - 1, c, 2)
        
        for r in range(ROWS):
            dfs(r, COLS - 1, 2)
        
        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])
        
        return ans
        


        