class Solution:
    def reverseStr(self, s, k):
        p = 0
        while p < len(s):
            p2 = p + k
            s = s[:p] + s[p:p2][::-1] + s[p2:]
            p = p + 2*k
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr('abcdefg', 2))
