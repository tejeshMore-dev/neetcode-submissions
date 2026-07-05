class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)

        prefix_sum = [ 1 ] * nums_len
        sufix_sum = [ 1 ] * nums_len
        
        for i in range (nums_len - 1):
            prefix_sum[i+1] = prefix_sum[i] * nums[i]

        for i in range (nums_len-1, 0, -1):
            sufix_sum[i-1] = sufix_sum[i] * nums[i]

        res = [1] * nums_len
        for i in range(nums_len):
            res[i] = prefix_sum[i] * sufix_sum[i]

        return res