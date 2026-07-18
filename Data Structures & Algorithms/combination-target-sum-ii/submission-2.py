class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = set()
        candidates = sorted(candidates)
        res = []

        def helper(start, cur_sum):
        
            if cur_sum > target:
                return
            
            if cur_sum == target:
                ans.add(tuple(res))
                return

            
            for i in range(start, len(candidates)):

                if i>start and candidates[i-1] == candidates[i]:
                    continue

                res.append(candidates[i])
                helper(i+1, cur_sum+candidates[i])
                res.pop()
                    
        helper(0,0)
        return [list(x) for x in ans]
