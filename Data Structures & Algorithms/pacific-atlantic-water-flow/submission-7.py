class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c, ocean):
            ocean.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in ocean and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, ocean)

        # Pacific
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(0, c, pacific)

        # Atlantic
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result