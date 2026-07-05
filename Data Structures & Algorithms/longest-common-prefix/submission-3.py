class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        common_length = len(strs[0])

        for s in strs:
            current_common_length = 0

            for i, char in enumerate(s):
                if i >= len(ans) or char != ans[i]:
                    break
                
                current_common_length += 1

            common_length = min(current_common_length, common_length)

        return "".join(ans[:common_length])
