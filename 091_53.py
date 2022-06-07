class Solution:   
    def maxSubArray(self, nums):
        res = -float('inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > res:
                res = count
            if count <= 0:
                count = 0
        return res

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))