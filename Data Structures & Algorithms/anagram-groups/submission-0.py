class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultMap = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1
            
            if tuple(count) not in resultMap:
                resultMap[tuple(count)] = [ s ]  
            else:
                resultMap[tuple(count)].append(s)
        
        return list(resultMap.values())
            


        