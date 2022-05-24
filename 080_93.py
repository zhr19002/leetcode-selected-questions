class Solution:
    def __init__(self):
        self.res = []
    
    def restoreIpAddresses(self, s):
        self.res.clear()
        if len(s) > 12:
            return []
        self.backtrack(s, 0, 0)
        return self.res
    
    def backtrack(self, s, startIndex, pointNum):
        if pointNum == 3:
            if self.isValid(s, startIndex, len(s)-1):
                self.res.append(s[:])
            return
        for i in range(startIndex, len(s)):
            if self.isValid(s, startIndex, i):
                s = s[:i+1] + '.' + s[i+1:]
                self.backtrack(s, i+2, pointNum+1)
                s = s[:i+1] + s[i+2:]
            else:
                break
    
    def isValid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        return True

s = Solution()
print(s.restoreIpAddresses('25525511135'))
print(s.restoreIpAddresses('0000'))
print(s.restoreIpAddresses('1111'))
print(s.restoreIpAddresses('010010'))
print(s.restoreIpAddresses('101023'))