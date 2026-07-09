class TrieNode:
    
    def __init__(self,val=None):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        temp = self.root
        for i, char in enumerate(word):
            if char not in temp.children:
                temp.children[char] = TrieNode(char)
            temp = temp.children[char]
            
        temp.isEnd = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        mem = {}

        def search(i, cur_trie):

            if i == len(s):
                return cur_trie.isEnd
            
            if cur_trie == trie.root and i in mem:
                return mem[i]

            if s[i] not in cur_trie.children:
                return False

            next_node = cur_trie.children[s[i]]

            ans = search(i+1, next_node)
            
            if next_node.isEnd:
                ans = ans or search(i+1, trie.root)

            if cur_trie == trie.root:
                mem[i] = ans

            return ans

        for word in wordDict:
            trie.add(word)
        
        return search(0, trie.root)
        

            
