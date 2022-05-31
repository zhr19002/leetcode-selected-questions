class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def permute(self, nums):
        self.res.clear()
        self.path.clear()
        used = [False] * len(nums)
        self.backtrack(nums, used)
        return self.res
    
    def backtrack(self, nums, used):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return 
        for i in range(0, len(nums)):
            if used[i] == True:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtrack(nums, used)
            self.path.pop()
            used[i] = False

s = Solution()
print(s.permute([1,2,3]))