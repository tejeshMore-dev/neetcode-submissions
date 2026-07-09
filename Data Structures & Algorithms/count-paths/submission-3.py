class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[0, 1], [1,0]]
        mem = {}

        def helper(r,c):
            if (r,c) in mem:
                return mem[(r,c)]

            if r < 0 or c < 0 or r == m or c == n:
                return 0
            
            if r == m - 1 and c == n - 1:
                return 1
            
            ways = 0 
            for dr, dc in directions:
                ways += helper(dr + r, dc + c)
            
            mem[(r,c)] = ways
            return ways

        return helper(0,0)    