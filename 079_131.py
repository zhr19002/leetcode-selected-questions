class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    
    def partition(self, s):
        self.res.clear()
        self.path.clear()
        self.backtrack(s, 0)
        return self.res
    
    def backtrack(self, s, startIndex):
        if startIndex >= len(s):
            self.res.append(self.path[:])
            return
        for i in range(startIndex, len(s)):
            temp = s[startIndex:i+1]
            if temp == temp[::-1]:
                self.path.append(temp)
                self.backtrack(s, i+1)
                self.path.pop()
            else:
                continue

s = Solution()
print(s.partition('aab'))