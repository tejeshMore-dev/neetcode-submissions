class Solution:
    def totalNQueens(self, n: int) -> int:
        r_set = set()
        c_set = set()
        dig_1 = set()
        dig_2 = set()
        ans = 0

        def helper(r):
            nonlocal ans

            if r >= n:
                ans += 1
                return 
            
            for c in range(n):
                if r not in r_set and c not in c_set and r-c not in dig_1 and r+c not in dig_2:
                    r_set.add(r)
                    c_set.add(c)
                    dig_1.add(r-c)
                    dig_2.add(r+c)

                    helper(r+1)

                    r_set.remove(r)
                    c_set.remove(c)
                    dig_1.remove(r-c)
                    dig_2.remove(r+c)
                
        helper(0)
        return ans