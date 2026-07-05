class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l_map = {
            "1":[],
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        results = []
        combination = []
        def dfs(index):
            if index>=len(digits):
                results.append("".join(combination))
                return
            
            for char in l_map[digits[index]]:
                combination.append(char)
                dfs(index+1)
                combination.pop()
        if not digits:
            return []
        dfs(0)
        return results
            
        
