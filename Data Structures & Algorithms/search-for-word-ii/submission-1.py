class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        dirs = [[0,1], [0,-1], [-1,0], [1,0]]

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            
            node.word = word
        
        ROWS = len(board)
        COLS = len(board[0])
        ans = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node.children:
                return

            nxt = node.children[ch]

            if nxt.word:
                ans.append(nxt.word)
                nxt.word = None
                        
            board[r][c] = '#'
            for a_r, a_c in dirs:
                n_r = r + a_r
                n_c = c + a_c

                if n_r < 0 or n_c < 0 or n_r >= ROWS or n_c >= COLS or board[n_r][n_c]=='#':
                    continue

                dfs(n_r, n_c, nxt)
            
            board[r][c] = ch

            if not nxt.children:
                del node.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
            
        return ans
