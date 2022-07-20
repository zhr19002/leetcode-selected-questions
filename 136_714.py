class Solution:
    def maxProfit(self, prices, fee):
        if len(prices) == 0:
            return 0
        dp = [[0] * 2 for i in range(len(prices))]
        dp[0][0] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        
        return max(dp[-1][0], dp[-1][1])

s = Solution()
print(s.maxProfit([1,3,2,8,4,9], 2))