class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[0,-1], [0, 1], [-1, 0], [1, 0]]
        visited = set()

        def found_word(r, c, i):
            if i >= len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or board[r][c] != word[i]:
                return False

            res = False
            visited.add((r,c))
            for direction in directions:
                if found_word(r + direction[0], c + direction[1], i+1): 
                    res = True
            
            visited.remove((r,c))
            return res    

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if found_word(row, col, 0):
                        return True   

        
        return False