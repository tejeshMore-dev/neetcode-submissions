class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = nums[0]
        max_prod = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            candidate = (nums[i], nums[i] * min_prod, nums[i] * max_prod)
            min_prod = min(candidate)
            max_prod = max(candidate)
            ans = max(ans, max_prod)


        return ans