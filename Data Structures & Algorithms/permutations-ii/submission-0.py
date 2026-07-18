class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        visited = set()
        res = []
        nums = sorted(nums)

        def helper():
            if len(res) == len(nums):
                ans.add(tuple(res))
                return
            
            for i, num in enumerate(nums):
                if i not in visited:
                    visited.add(i)
                    res.append(num)
                    helper()
                    res.pop()
                    visited.remove(i)
        
        helper()
        return list(ans)
