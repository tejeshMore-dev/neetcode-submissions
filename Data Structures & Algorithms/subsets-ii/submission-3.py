class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []

        nums = sorted(nums)

        def dfs(i):
            ans.append(res.copy())

            for j in range(i, len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                res.append(nums[j])
                dfs(j+1)
                res.pop()
        
        dfs(0)
        return ans
