class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_by_value = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_by_value:
                return [index_by_value[complement], i]
            
            index_by_value[num] = i

        return [-1, -1]
    