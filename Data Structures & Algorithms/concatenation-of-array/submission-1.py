class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * 2 * length

        for i in range(len(nums)):
            result[i], result[i + length ] = nums[i], nums[i]

        return result
        