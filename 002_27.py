class Solution:
    def removeElement(self, nums, val):
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

s1 = Solution()
print(s1.removeElement([3,2,2,3], 3))
s2 = Solution()
print(s2.removeElement([0,1,2,2,3,0,4,2], 2))