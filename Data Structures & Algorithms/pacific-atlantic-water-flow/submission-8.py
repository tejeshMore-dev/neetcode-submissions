class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        visited = set()
        rows = len(heights)
        cols = len(heights[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]] 
        
        def dfs(r, c, ocean):
            ocean.add((r,c))
            for dir in directions:
                new_r = r + dir[0]
                new_c = c + dir[1]

                if new_r>=0 and new_c>=0 and new_r<rows and new_c<cols and heights[new_r][new_c] >= heights[r][c] and (new_r, new_c) not in ocean:
                    dfs(new_r, new_c, ocean)

        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(0, c, pacific)

        for c in range(cols):
            dfs(rows-1, c, atlantic)
        
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        results = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    results.append([r,c])

        return results        
