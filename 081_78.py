class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def subsets(self, nums):
        self.res.clear()
        self.path.clear()
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, startIndex):
        self.res.append(self.path[:])
        if startIndex == len(nums):
            return
        for i in range(startIndex, len(nums)):
            self.path.append(nums[i])
            self.backtrack(nums, i+1)
            self.path.pop()

s = Solution()
print(s.subsets([1,2,3]))