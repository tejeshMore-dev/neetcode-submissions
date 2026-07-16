class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [] 
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry

            res.append(total % 10)
            carry = 1 if total // 10 else 0
        
        if carry:
            res.append(1)
        
        res.reverse()
        return res