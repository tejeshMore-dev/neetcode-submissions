class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = defaultdict(list)
        result = 0

        for i, num in enumerate(nums):
            numMap[num].append(i)
        
        for i , num in enumerate(nums):
            j = i
            currentConsecutivelength = 0
            currentNum = nums[j]

            while currentNum in numMap :
                currentConsecutivelength += 1
                result = max(result, currentConsecutivelength )
                currentNum += 1
        
        return result
        
        