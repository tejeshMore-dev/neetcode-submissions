class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        lp = 0
        rp = len(matrix) * len(matrix[0]) -1
        result = False

        while lp <= rp:
            mid = (rp+lp) // 2
            row = mid // COLS
            col = mid % COLS

            midVal = matrix[row][col]

            if midVal == target:
                result = True
                break
            elif target < midVal:
                rp = mid - 1
            else:
                lp = mid + 1
        
        return result


