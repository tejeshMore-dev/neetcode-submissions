class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        directions = [[1,0], [0,1], [0,-1], [-1,0]]
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            visited.add((r,c))
            
            for dir in directions:
                new_r = r + dir[0]
                new_c = c + dir[1]

                if new_r>=0 and new_c>=0 and new_r<rows and new_c<cols and board[new_r][new_c] == "O" and (new_r,new_c) not in visited:
                    dfs(new_r, new_c)
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
        
        for c in range(cols):
            if board[rows-1][c] == "O":
                dfs(rows-1, c)
        
        for r in range(rows):
            if board[r][cols-1] == "O":
                dfs(r, cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"



