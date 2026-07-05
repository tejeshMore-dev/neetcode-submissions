class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in previousMap:
                return [previousMap[diff], i]
            
            previousMap[num] = i
        