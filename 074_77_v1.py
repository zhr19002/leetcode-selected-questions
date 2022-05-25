class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def combine(self, n, k):
        self.res.clear()
        self.path.clear()
        self.backtrack(n, k, 1)
        return self.res
        
    def backtrack(self, n, k, startIndex):
        if len(self.path) == k:
            self.res.append(self.path[:])
            return
        for i in range(startIndex, n+1):
            self.path.append(i)
            self.backtrack(n, k, i+1)
            self.path.pop()

s = Solution()
print(s.combine(4, 2))