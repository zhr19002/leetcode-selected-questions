class Solution:   
    def maxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))