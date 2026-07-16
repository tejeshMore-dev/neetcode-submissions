class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {
            0:0,
            1:1,
            2:1
        }


        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        

        # if n<3:
        #     return dp[n]
        
        # if n in dp:
        #     return dp[n]
        
        # dp[n] = dp[n-1]+dp[n-2]+dp[n-3]
        return dp[n]

        