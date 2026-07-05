class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lp, rp = i+1, len(nums) - 1         
            while lp < rp:
                currentSum = nums[i] + nums[lp] + nums[rp]
                if currentSum == 0:
                    result.append([nums[i], nums[lp], nums[rp]])
                
                    while lp < rp and nums [lp] == nums[lp+1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp-1]:
                        rp -= 1
                    
                    lp += 1
                    rp -= 1
                elif currentSum < 0:
                    lp += 1
                else:
                    rp -= 1
 
        return result        