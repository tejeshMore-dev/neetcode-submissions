class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combination = []

        def dfs(o_count, c_count):
            if len(combination) == 2 * n:
                res.append("".join(combination))
                return

            if o_count < n:
                combination.append("(")
                dfs(o_count + 1, c_count)
                combination.pop()

            if o_count > c_count:
                combination.append(")")
                dfs(o_count, c_count + 1)
                combination.pop()

        dfs(0, 0)
        return res

        