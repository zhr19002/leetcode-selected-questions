class Solution:
    def replaceSpace(self, s):
        n = len(s)
        for e,i in enumerate(s[::-1]):
            if i == ' ':
                s = s[: n-(e+1)] + '%20' + s[n-e :]
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace('We are happy.'))
