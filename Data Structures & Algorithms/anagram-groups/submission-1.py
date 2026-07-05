class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            hash = "".join(sorted(s))

            if hash not in groups:
                groups[hash] = []

            groups[hash].append(s)
        
        ans = []
        for key, value in groups.items():
            ans.append(value)
            
        return ans