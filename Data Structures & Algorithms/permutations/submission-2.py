class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []

        def helper():
            if len(res)>=len(nums):
                ans.append(res.copy())

            for num in nums:
                if num not in res:
                    res.append(num)
                    helper()
                    res.pop()
        
        helper()
        return ans