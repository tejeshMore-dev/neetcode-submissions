from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        r_set = set()
        c_set = set()
        dig_1 = set()
        dig_2 = set()

        def dfs(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return 

            for c in range(n):
                if r not in r_set and c not in c_set and r-c not in dig_1 and r+c not in dig_2:
                    r_set.add(r)
                    c_set.add(c)
                    dig_1.add(r-c)
                    dig_2.add(r+c)
                    board[r][c] = "Q"
                    
                    dfs(r + 1)
                    
                    r_set.remove(r)
                    c_set.remove(c)
                    dig_1.remove(r-c)
                    dig_2.remove(r+c)
                    board[r][c] = "."
                    
        dfs(0)
        return ans