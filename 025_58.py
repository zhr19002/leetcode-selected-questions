class Solution:
    def reverseLeftWords(self, s, n):
        s = list(s)
        s[0:n] = list(reversed(s[0:n]))
        s[n:] = list(reversed(s[n:]))
        s.reverse()
        return ''.join(s)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseLeftWords('abcdefg', 2))
    print(s.reverseLeftWords('lrloseumgh', 6))
