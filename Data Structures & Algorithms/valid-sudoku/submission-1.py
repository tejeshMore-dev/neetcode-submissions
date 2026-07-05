class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        subBoxSet = defaultdict(set)
        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                digit = board[r][c]
                subBox = (r//3, c//3)
                if digit != ".":
                    if digit in rowSet[r] or digit in colSet[c] or digit in subBoxSet[subBox]:
                        return False
                    else:
                        rowSet[r].add(digit)
                        colSet[c].add(digit)
                        subBoxSet[subBox].add(digit)
                     
        
        return True