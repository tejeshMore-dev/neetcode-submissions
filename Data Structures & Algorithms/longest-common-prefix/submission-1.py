class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = list(strs[0])
        common_length = len(strs[0])

        for s in strs:
            current_length = 0

            for i, char in enumerate(s):
                if i < len(ans) and char == ans[i]:
                    current_length += 1
                else:
                    break

            common_length = min(current_length, common_length)

        return "".join(ans[:common_length])
