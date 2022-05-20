class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def combinationSum(self, candidates, target):
        self.res.clear()
        self.path.clear()
        self.backtrack(candidates, target, 0, 0)
        return self.res
    
    def backtrack(self, candidates, target, sum_, startIndex):
        if sum_ == target:
            self.res.append(self.path[:])
            return
        if sum_ > target:
            return
        for i in range(startIndex, len(candidates)):
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtrack(candidates, target, sum_, i)
            sum_ -= candidates[i]
            self.path.pop()

s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))