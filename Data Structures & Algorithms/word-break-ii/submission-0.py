class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set()

        for word in wordDict:
            words.add(word)
        
        ans = []
        res = []

        def helper(l, r):
            if l >= len(s):
                ans.append(" ".join(res))
                return

            if r>=len(s):
                return

            cur_word = s[l:r+1]
            if cur_word in words:
                res.append(cur_word)
                helper(r+1, r+1)
                res.pop()
            
            helper(l,r+1)
        
        helper(0,0)
        return ans
            
            
