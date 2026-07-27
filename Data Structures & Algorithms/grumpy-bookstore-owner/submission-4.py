class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        mem = {}

        def helper(i, powerUsed):
            if (i, powerUsed) in mem:
                return mem[(i, powerUsed)]

            if i >= n :
                return 0
            
            # not grumpy
            if grumpy[i] == 0:
                ans = customers[i] + helper(i+1, powerUsed)
                
                mem[(i, powerUsed)] = ans
                return ans
            else:
                # grumpy
                ans = helper(i + 1, powerUsed)
                if not powerUsed:
                    j = i
                    c_sum = 0
                    while j < i + minutes and j < n:
                        c_sum += customers[j]
                        j += 1
                    
                    ans = max(ans, c_sum + helper(i + minutes, True))
                
                mem[(i, powerUsed)] = ans
                return ans
            
        
        return helper(0, False)
                


        