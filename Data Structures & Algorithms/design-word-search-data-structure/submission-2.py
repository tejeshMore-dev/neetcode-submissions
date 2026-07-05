class TrieNode:
    def __init__(self, key=None):
        self.key = key
        self.childrens = {}
        self.isWordEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root

        for char in word:
            if char not in cur_node.childrens.keys():
                child_node = TrieNode()
                cur_node.childrens[char] = child_node
                cur_node = child_node
            else:
                cur_node = cur_node.childrens[char]
            
        cur_node.isWordEnd = True
    
    def search_from_node(self, word: str, node: TrieNode):
        for i, char in enumerate(word):
            if char == ".":
                for child in node.childrens.keys():
                    if self.search_from_node(word[i+1:], node.childrens[child]):
                        return True
                return False
            elif char not in node.childrens.keys():
                return False
            else:
                node = node.childrens[char]
        
        return node.isWordEnd

    def search(self, word: str) -> bool:
        return self.search_from_node(word, self.root)
        
            
