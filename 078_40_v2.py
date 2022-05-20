class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.used = []
    
    def combinationSum2(self, candidates, target):
        self.res.clear()
        self.path.clear()
        self.used = [False] * len(candidates)
        candidates.sort()
        self.backtrack(candidates, target, 0, 0)
        return self.res
    
    def backtrack(self, candidates, target, sum_, startIndex):
        if sum_ == target:
            self.res.append(self.path[:])
            return
        for i in range(startIndex, len(candidates)):
            if sum_ + candidates[i] > target:
                return
            if i > 0 and candidates[i] == candidates[i-1] and self.used[i-1] == False:
                continue
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.used[i] = True
            self.backtrack(candidates, target, sum_, i+1)
            self.used[i] = False
            sum_ -= candidates[i]
            self.path.pop()

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
print(s.combinationSum2([2,5,2,1,2], 5))