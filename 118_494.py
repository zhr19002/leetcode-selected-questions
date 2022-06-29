class Solution:   
    def findTargetSumWays(self, nums, target):
        sumValue = sum(nums)
        if abs(target) > sumValue or (sumValue + target) % 2 == 1:
            return 0
        bag_size = (sumValue + target) // 2
        dp = [0] * (bag_size + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bag_size, nums[i] - 1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[bag_size]

s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))