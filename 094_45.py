class Solution:   
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        res = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance)
            if i == curDistance:
                if curDistance != len(nums) - 1:
                    res += 1
                    curDistance = nextDistance
                    if nextDistance >= len(nums) - 1:
                        break
        return res

s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([2,2,1,1,4]))