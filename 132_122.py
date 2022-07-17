class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        dp = [[0] * 2 for i in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        return dp[-1][1]

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))