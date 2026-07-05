class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def helper(i, combination, currentTarget):
            if currentTarget == target:
                result.append(combination[:])
                
            if i == len(candidates) or currentTarget >= target :
                return 

            combination.append(candidates[i])
            helper(i+1, combination, currentTarget + candidates[i] )
            combination.pop()

            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1

            helper(i+1, combination, currentTarget)

        helper(0, [], 0)
        return result
            


