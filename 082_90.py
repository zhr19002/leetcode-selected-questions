class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def subsetsWithDup(self, nums):
        self.res.clear()
        self.path.clear()
        nums.sort()
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, startIndex):
        self.res.append(self.path[:])
        if startIndex == len(nums):
            return
        uset = set()
        for i in range(startIndex, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and (nums[i] in uset):
                continue
            uset.add(nums[i])
            self.path.append(nums[i])
            self.backtrack(nums, i+1)
            self.path.pop()

s = Solution()
print(s.subsetsWithDup([1,2,2]))