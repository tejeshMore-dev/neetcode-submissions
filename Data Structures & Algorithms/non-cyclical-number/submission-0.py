class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def helper(n):

            if n==1:
                return True

            if n in visited:
                return False
            
            new_n = 0
            visited.add(n)

            while n!=0:
                mod = n%10
                new_n += pow(mod,2)
                n = n//10
            
            return helper(new_n)
        
        return helper(n)
            
