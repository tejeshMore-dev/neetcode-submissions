class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        def dfs(i,start):
            if (i,start) in mem:
                return mem[(i,start)]

            if i>=len(nums):
                return 0
            
            if i==len(nums)-1:
                if start==0:
                    return 0
            
            ans = max(dfs(i+2,start)+nums[i], dfs(i+1,start))
            mem[(i,start)] = ans
            return ans
        
        if len(nums)<2:
            return nums[0]
        
        return max(dfs(0,0), dfs(1,1))
