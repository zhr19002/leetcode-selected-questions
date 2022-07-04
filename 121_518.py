class Solution:   
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        
        return dp[amount]

s = Solution()
print(s.change(5, [1,2,5]))
print(s.change(3, [2]))
print(s.change(10, [10]))