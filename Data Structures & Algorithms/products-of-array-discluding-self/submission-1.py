class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [ 1 ] * len(nums)
        lefProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
               lefProduct[i] = 1
            else:
                lefProduct[i] =  lefProduct[i-1] * nums[i-1]

        for i in range(len(nums)-1,-1, -1):
            if i == len(nums) - 1:
               rightProduct[i] = 1
            else:
                rightProduct[i] =  rightProduct[i+1] * nums[i+1]
        
        # print(lefProduct, rightProduct)
        for i in range(len(nums)):
            result[i] = lefProduct[i] * rightProduct[i]
        
        return result
