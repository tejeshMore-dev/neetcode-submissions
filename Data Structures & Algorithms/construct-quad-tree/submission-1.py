"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(r, c, size):
            is_same = True
            first = grid[r][c]

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        is_same = False
                        break

                if not is_same:
                    break


            if is_same:
                return Node(first, True, None, None, None, None)
            

            size = size // 2

            tl = dfs(r, c, size)
            tr = dfs(r, c + size, size)
            bl = dfs(r + size, c, size)
            br = dfs(r + size, c + size, size)

            return Node(True, False, tl, tr, bl, br)
                
        return dfs(0, 0, n)
        