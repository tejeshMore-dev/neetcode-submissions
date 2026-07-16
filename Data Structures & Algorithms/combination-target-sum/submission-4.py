class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        ans  = []

        def helper(i, cur_sum):
            if cur_sum == target:
                ans.append(res.copy())
                return
            
            j = i
            while j<len(nums):
                if nums[j] > target:
                    break

                if cur_sum + nums[j] <= target:
                    res.append(nums[j])
                    helper(j, cur_sum + nums[j])
                    res.pop()
                j+=1
        
        helper(0,0)        
        return ans