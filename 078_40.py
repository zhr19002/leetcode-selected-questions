class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def combinationSum2(self, candidates, target):
        self.res.clear()
        self.path.clear()
        candidates.sort()
        self.backtrack(candidates, target, 0, 0)
        return self.res
    
    def backtrack(self, candidates, target, sum_, startIndex):
        if sum_ == target:
            self.res.append(self.path[:])
            return
        uset = set()
        for i in range(startIndex, len(candidates)):
            if sum_ + candidates[i] > target:
                return
            if i > 0 and candidates[i] == candidates[i-1] and (candidates[i] in uset):
                continue
            uset.add(candidates[i])
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtrack(candidates, target, sum_, i+1)
            sum_ -= candidates[i]
            self.path.pop()

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
print(s.combinationSum2([2,5,2,1,2], 5))