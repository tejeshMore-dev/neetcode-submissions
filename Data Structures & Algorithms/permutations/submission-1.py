class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        
        def helper(ans):
            if len(ans) == len(nums):
                result.append(ans[:])
                return

            for num in nums:
                if num not in seen:
                    seen.add(num)
                    ans.append(num)
                    helper(ans)
                    seen.remove(num)
                    ans.pop()

        helper([])
        return result        