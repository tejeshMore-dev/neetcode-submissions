class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i_map = {}
        for i, char in enumerate(s):
            i_map[char] = i
        
        i = 0
        ans = []

        while i<len(s):
            last = i_map[s[i]]

            j = i
            while j<=last:
                if i_map[s[j]] > last:
                    last = i_map[s[j]]
                j+=1
            ans.append(last-i+1)
            i = last+1

        return ans 




