class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def helper(i):
            if len(path) == k:
                ans.append(path.copy())
                return

            if i == n + 1:
                return 

            path.append(i)
            helper(i+1)
            path.pop()
            helper(i+1)


        helper(1)
        return ans
