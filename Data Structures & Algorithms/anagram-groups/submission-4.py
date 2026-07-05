class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_map = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in key_map:
                key_map[key] = []
            
            key_map[key].append(word)

        return list(key_map.values())