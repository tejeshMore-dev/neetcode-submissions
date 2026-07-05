class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s_map = {}
        r_map = {}
        c_map = {}

        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                cur = board[i][j]

                if cur==".":
                    continue 

                if i in r_map:
                    if cur in r_map[i]:
                        return False
                else:
                    r_map[i] = set()
                r_map[i].add(cur)

                if j in c_map:
                    if cur in c_map[j]:
                        return False
                else:
                    c_map[j] = set()
                c_map[j].add(cur)

                s_i = i // 3
                s_j = j // 3

                if (s_i, s_j) in s_map:
                    if cur in s_map[(s_i, s_j)]:
                        return False
                else:
                    s_map[(s_i, s_j)] = set()
                s_map[(s_i, s_j)].add(cur)
        
        return True
