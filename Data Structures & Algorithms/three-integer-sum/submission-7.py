class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = set()
        for i in range(len(nums)):
            seen = set()
            target = 0 - nums[i]
            for num in nums[i+1:]:
                if target-num in seen:
                    ans.add((nums[i],target-num,num))
                else:
                    seen.add(num)

        return [list(x) for x in ans]
                     

