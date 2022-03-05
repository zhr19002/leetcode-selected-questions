class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

s1 = Solution()
print(s1.search([-1,0,3,5,9,12], 9))
s2 = Solution()
print(s2.search([-1,0,3,5,9,12], 2))