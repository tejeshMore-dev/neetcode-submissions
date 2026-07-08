class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        ans  = []

        def helper(i, cur_sum):
            if cur_sum == target:
                # ans.add(tuple(sorted(res)))
                ans.append(res.copy())

            # for j, num in enumerate(nums[i:]):
            
            j = i
            while j<len(nums):
                if cur_sum + nums[j] <= target:
                    res.append(nums[j])
                    helper(j, cur_sum + nums[j])
                    res.pop()
                j+=1

        for i, num in enumerate(nums):
            res.append(num)
            helper(i, num)
            res.pop()
        
        return ans