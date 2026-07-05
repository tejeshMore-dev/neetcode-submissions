class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_r = 0
        cnt_w = 0
        cnt_b = 0

        for num in nums:
            if num == 0:
                cnt_r+=1
            elif num == 1:
                cnt_w += 1
            else:
                cnt_b += 1
        i = 0
        while cnt_r>0:
            nums[i] = 0
            cnt_r -= 1
            i += 1
        
        while cnt_w>0:
            nums[i] = 1
            cnt_w -= 1
            i += 1
        
        while cnt_b>0:
            nums[i] = 2
            cnt_b -= 1
            i += 1
        