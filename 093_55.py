class Solution:   
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        cover = 0
        i = 0
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))