class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        wp = 0
        rp = 0

        while rp < len(nums):
            nums[wp] = nums[rp]
            
            while rp < len(nums) and nums[rp] == nums[wp]:
                rp += 1
            
            wp += 1

        return wp