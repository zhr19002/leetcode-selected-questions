class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def permuteUnique(self, nums):
        self.res.clear()
        self.path.clear()
        nums.sort()
        used = [False] * len(nums)
        self.backtrack(nums, used)
        return self.res
    
    def backtrack(self, nums, used):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return
        uset = set()
        for i in range(0, len(nums)):
            if used[i] == True:
                continue
            if nums[i] in uset:
                continue
            uset.add(nums[i])
            used[i] = True
            self.path.append(nums[i])
            self.backtrack(nums, used)
            self.path.pop()
            used[i] = False

s = Solution()
print(s.permuteUnique([1,1,2]))
print(s.permuteUnique([1,2,3]))