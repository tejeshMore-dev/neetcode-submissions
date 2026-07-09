class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        total = sum(piles)
        
        def helper(start, end):
            if start > end:
                return 0
            
            ans = -float('inf')
            if piles[start] >= piles[end]:
                ans = max(ans, helper(start+1, end)+piles[start])
            else:
                ans = max(ans, helper(start, end-1)+piles[end])
            
            return ans
        
        alice = helper(0,len(piles)-1)
        bob = total - alice

        if alice>bob:
            return True
        
        return False
