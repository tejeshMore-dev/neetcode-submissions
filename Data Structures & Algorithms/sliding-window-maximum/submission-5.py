class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        n = len(nums)
        ans = []
        l = 0
        cur_max = max(nums[l:k])
        ans.append(cur_max)
        
        if n == k:
            return ans
        

        for r in range(k, n):
            if nums[r] >= cur_max:
                cur_max = nums[r]
            elif cur_max == nums[l]:
                cur_max = max(nums[l+1:r+1])
            
            ans.append(cur_max)
            l += 1

        return ans