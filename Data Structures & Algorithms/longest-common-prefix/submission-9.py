class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        r_string = strs[0]
        min_common_len = len(r_string)


        for word in strs[1:]:
            for i, char in enumerate(r_string):
                if len(word) <= i or char != word[i]:
                    min_common_len = min(min_common_len, i)
                    break
            
        return r_string[:min_common_len]
