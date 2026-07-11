class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        lp = 0 
        rp = ROWS * COLS -1

        while lp <= rp:
            mid = lp + (rp - lp) // 2

            r = mid // COLS
            c = mid % COLS

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                rp = mid - 1
            else:
                lp = mid + 1
        
        return False
            