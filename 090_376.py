class Solution:   
    def wiggleMaxLength(self, nums):
        preC, curC, res = 0, 0, 1
        for i in range(len(nums)-1):
            curC = nums[i+1] - nums[i]
            if curC * preC <= 0 and curC != 0:
                res += 1
                preC = curC
        return res

s = Solution()
print(s.wiggleMaxLength([1,7,4,9,2,5]))
print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))