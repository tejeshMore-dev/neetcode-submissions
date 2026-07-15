class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        res = []
        
        while columnNumber>0:
            num = columnNumber - 1
            mod = num % 26
            ch = chr(ord('A') + mod)
            res.append(ch)
            columnNumber = num // 26
        
        return "".join(res[::-1])