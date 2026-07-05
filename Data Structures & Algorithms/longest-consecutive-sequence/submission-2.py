class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = defaultdict(set)
        result = 0

        for i, num in enumerate(nums):
            numMap[num].add(i)
        
        for i , num in enumerate(nums):
            currentNum = nums[i]

            while currentNum in numMap :
                currentNum += 1
            
            result = max(result, currentNum - nums[i] )

        return result
        
        