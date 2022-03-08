class Solution:
    def minSubArrayLen(self, s, nums):
        res = float('inf')
        Sum = 0
        index = 0
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= s:
                res = min(res, i-index+1)
                Sum -= nums[index]
                index += 1
        return 0 if res==float('inf') else res

s1 = Solution()
print(s1.minSubArrayLen(7,[2,3,1,2,4,3]))