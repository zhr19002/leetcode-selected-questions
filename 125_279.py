class Solution:   
    def numSquares(self, n):
        nums = [i**2 for i in range(1, n+1) if i**2 <= n]
        dp = [10**4] * (n + 1)
        dp[0] = 0
        
        for i in nums:
            for j in range(i, n + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
        
        return dp[n]

s = Solution()
print(s.numSquares(12))
print(s.numSquares(13))