class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.targetSum = 0
    
    def combinationSum3(self, k, n):
        self.res.clear()
        self.path.clear()
        self.backtrack(k, n, 1)
        return self.res
    
    def backtrack(self, k, n, startIndex):
        if self.targetSum > n:
            return
        if len(self.path) == k:
            if self.targetSum == n:
                self.res.append(self.path[:])
            return
        for i in range(startIndex, 10-(k-len(self.path))+1):
            self.path.append(i)
            self.targetSum += i
            self.backtrack(k, n, i+1)
            self.path.pop()
            self.targetSum -= i

s = Solution()
print(s.combinationSum3(3, 9))