class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            for i in range(len(ans)):
                new = ans[i].copy()
                new.append(num)
                ans.append(new)
        
        return ans