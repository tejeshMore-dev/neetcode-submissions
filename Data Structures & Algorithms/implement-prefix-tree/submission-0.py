class TrieNode:
    def __init__(self, key=None):
        self.key = key
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children.keys():
                child_node = TrieNode(char)
                cur.children[char] = child_node
                cur = child_node
            else:
                cur = cur.children[char]
        
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children.keys():
                return False
            else:
                cur = cur.children[char]
        
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.children.keys():
                return False
            else:
                cur = cur.children[char]
        
        return True
        
        