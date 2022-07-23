class Solution:
    def findLengthOfLCIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        result = 0
        
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                dp[i+1] = dp[i] + 1
            result = max(result, dp[i+1])
        
        return result

s = Solution()
print(s.findLengthOfLCIS([1,3,5,4,7]))
print(s.findLengthOfLCIS([2,2,2,2,2]))