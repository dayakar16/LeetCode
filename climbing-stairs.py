class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(dp,n):
            if n == 0: 
                return 1 
            if n == 1: 
                return 1
            if dp[n] != -1: 
                return dp[n]
            else: 
                dp[n] = climb(dp,n-1) + climb(dp,n-2)
            return dp[n]
        
        dp = [-1 for _ in range(n+2)]
        return climb(dp,n)
