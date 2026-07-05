class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        frequencyMap = [ [] for _ in range(len(nums) + 1) ]
        result = []

        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        
        for num, count in countMap.items():
            frequencyMap[count].append(num)
        
        for i in range(len(frequencyMap) - 1, -1, -1):
            for num in frequencyMap[i]:
                result.append(num)

                if len(result) == k:
                    return result
            
