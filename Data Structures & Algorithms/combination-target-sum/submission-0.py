class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def helper(i, currentSum):
            if currentSum >= target or i >= len(nums):
                if currentSum == target:
                    result.append(subset.copy())
                return
            
            subset.append(nums[i])
            helper(i, currentSum + nums[i])
            subset.pop()
            helper(i+1, currentSum)
        helper(0, 0)

        return result