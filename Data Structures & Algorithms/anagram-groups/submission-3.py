class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            group_key = "".join(sorted(word))

            if group_key not in groups:
                groups[group_key] = []

            groups[group_key].append(word)
        
        return list(groups.values())