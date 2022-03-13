class Solution:
    def twoSum(self, nums, target):
        record = {}
        for index,value in enumerate(nums):
            if target - value not in record:
                record[value] = index
            else:
                return [record[target - value], index]

s = Solution()
print(s.twoSum([2,7,11,15], 9))