class Solution:   
    def canPartition(self, nums):
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2
        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return target == dp[target]

s = Solution()
print(s.canPartition([1,5,11,5]))
print(s.canPartition([1,2,3,5]))