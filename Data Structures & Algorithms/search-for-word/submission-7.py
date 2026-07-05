class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def wordExist(r, c, i):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True
            
            temp = board[r][c]
            board[r][c] = "#"

            found = wordExist(r, c+1, i+1) or wordExist(r, c-1, i+1) or wordExist(r+1, c, i+1) or wordExist(r-1, c, i+1)
            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if wordExist(r, c, 0):
                        return True

        return False
