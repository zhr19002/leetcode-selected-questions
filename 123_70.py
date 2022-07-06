class Solution:   
    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        m = 2
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i >= j:
                    dp[i] += dp[i - j]
        
        return dp[n]

s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))