class Solution:
    def maxProfit(self, k, prices):
        if len(prices) == 0:
            return 0
        dp = [[0] * (2*k+1) for i in range(len(prices))]
        for j in range(1, 2*k, 2):
            dp[0][j] = -prices[0]
        
        for i in range(1, len(prices)):
            for j in range(0, 2*k-1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])
        
        return dp[-1][2*k]

s = Solution()
print(s.maxProfit(2, [2,4,1]))
print(s.maxProfit(2, [3,2,6,5,0,3]))