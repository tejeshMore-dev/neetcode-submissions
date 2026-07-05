class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []

        digitMap = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        result = []

        def helper(i, combination):
            if len(combination) == len(digits):
                result.append("".join(combination))
                return
            
            for letter in digitMap[digits[i]]:
                combination.append(letter)
                helper(i+1, combination)
                combination.pop()

        helper(0, [])
        return result