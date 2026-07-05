class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        columnSet = set()
        mainDiagonalSet = set()
        antiDiagonalSet = set()
        defaultBoard = [ ["."] * n for _ in range(n) ]
                
        def helper(r, board):
            if r == n:
                result.append( [ "".join(row) for row in board ] )
                return
            
            for c in range(n):
                if c not in columnSet and (r-c) not in mainDiagonalSet and (r+c) not in antiDiagonalSet:
                    board[r][c] = ("Q")
                    columnSet.add(c)
                    mainDiagonalSet.add(r-c)
                    antiDiagonalSet.add(r+c)

                    helper(r+1, board)
                    board[r][c] = (".")
                    columnSet.remove(c)
                    mainDiagonalSet.remove(r-c)
                    antiDiagonalSet.remove(r+c)

        helper(0,defaultBoard)
        return result

        