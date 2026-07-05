class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        prefix_length = len(strs[0])

        for s in strs:
            match_length = 0

            for i, char in enumerate(s):
                if i >= len(prefix) or char != prefix[i]:
                    break
                
                match_length += 1

            prefix_length = min(match_length, prefix_length)

        return prefix[:prefix_length]
