class Solution:   
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
        
        return dp[amount] if dp[amount] < amount + 1 else -1

s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))
print(s.coinChange([1], 1))
print(s.coinChange([1], 2))