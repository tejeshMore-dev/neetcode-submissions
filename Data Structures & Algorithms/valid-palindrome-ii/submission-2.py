class Solution:
    def validPalindrome(self, s: str) -> bool:
        combination = []
        del_cnt = 0

        def check(l,r, del_cnt):
            if del_cnt>1:
                return False

            if l>=r:
                return True
            
            if s[l]==s[r]:
                l+=1
                r-=1
                return check(l,r, del_cnt)
            else:
                return check(l,r-1,del_cnt+1) or check(l+1,r, del_cnt+1)
        
        return check(0,len(s)-1,del_cnt=0)

        