class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        lp = 0 
        rp = lp
        result = 0

        while rp < len(s):
            charMap[s[rp]] = charMap.get(s[rp], 0) + 1

            if charMap.get(s[rp]) > 1:
                while  lp < rp and charMap.get(s[rp]) > 1:
                    charMap[s[lp]] = charMap.get(s[lp]) - 1
                    lp += 1      
            
            rp += 1
            result = max(result, rp - lp)

        return result
        