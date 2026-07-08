class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = set()

        nums = sorted(nums)

        def dfs(i):
            if i >= len(nums):
                ans.add(tuple(res.copy()))
                return
            
            res.append(nums[i])
            dfs(i+1)
            res.pop()

            dfs(i+1)
        
        dfs(0)
        return list(ans)
