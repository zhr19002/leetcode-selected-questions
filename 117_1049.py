class Solution:   
    def lastStoneWeightII(self, stones):
        sumWeight = sum(stones)
        target = sumWeight // 2
        dp = [0] * 15001
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return sumWeight - 2 * dp[target]

s = Solution()
print(s.lastStoneWeightII([2,7,4,1,8,1]))
print(s.lastStoneWeightII([2,4,1,1]))