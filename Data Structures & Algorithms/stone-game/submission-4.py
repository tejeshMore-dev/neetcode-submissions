class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        total = sum(piles)
        mem = {}

        def helper(start, end):
            if (start, end) in mem:
                return mem[(start, end)]
            if start > end:
                return 0
            
            ans = max( helper(start+1, end) + piles[start], 
                        helper(start, end-1) + piles[end] )
            
            mem[(start, end)] = ans
            return ans
        
        alice = helper(0,len(piles)-1)
        bob = total - alice

        return alice > bob
