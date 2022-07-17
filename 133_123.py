class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        dp = [[0] * 5 for i in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        
        return dp[-1][4]

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([1]))