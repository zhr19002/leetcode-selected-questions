class Solution:   
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):
            if res < len(g) and s[i] >= g[res]:
                res += 1
        return res

s = Solution()
print(s.findContentChildren([1,2,3], [1,1]))
print(s.findContentChildren([1,2], [1,2,3]))
print(s.findContentChildren([1,2,7,10], [1,3,5,9]))