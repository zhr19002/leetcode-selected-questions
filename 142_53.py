class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            result = max(result, dp[i])
        
        return result

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))