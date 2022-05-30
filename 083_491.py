class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def findSubsequences(self, nums):
        self.res.clear()
        self.path.clear()
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, startIndex):
        if len(self.path) >= 2:
            self.res.append(self.path[:])
        if startIndex == len(nums):
            return
        uset = set()
        for i in range(startIndex, len(nums)):
            if (self.path and nums[i] < self.path[-1]) or (nums[i] in uset):
                continue
            uset.add(nums[i])
            self.path.append(nums[i])
            self.backtrack(nums, i+1)
            self.path.pop()

s = Solution()
print(s.findSubsequences([4,7,6,7]))