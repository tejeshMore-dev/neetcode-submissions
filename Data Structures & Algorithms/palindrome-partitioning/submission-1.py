class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        ans = [] 

        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True

        def helper(j, i):
            if i >= len(s):
                if i == j:
                    ans.append(res.copy())

                return
            
            #checking for palindrome /breaking
            if is_palindrome(j, i):
                res.append(s[j: i+1])
                helper(i+1, i+1)
                res.pop()

            # waiting for bigger substring/ non breaking
            helper(j, i+1)    

        
        helper(0,0)
        return ans 