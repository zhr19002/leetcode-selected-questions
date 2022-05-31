class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def permute(self, nums):
        self.res.clear()
        self.path.clear()
        self.backtrack(nums)
        return self.res
    
    def backtrack(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return 
        for i in range(0, len(nums)):
            if nums[i] in self.path:
                continue
            self.path.append(nums[i])
            self.backtrack(nums)
            self.path.pop()

s = Solution()
print(s.permute([1,2,3]))