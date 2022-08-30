def getNext(s):
    nxt = ['' for i in range(len(s))]
    nxt[0] = 0
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = nxt[j-1]
        if s[i] == s[j]:
            j += 1
        nxt[i] = j
    return nxt    

class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        
        i = j = 0
        nxt = getNext(needle)
        nxt = [-1] + nxt[:-1]
        while i < len(haystack) and j < len(needle):
            if j == -1 or needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                j = nxt[j]
        
        if j == len(needle):
            return i-j
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr('hello', 'll'))
    print(s.strStr('aaaaa', 'bba'))
    print(s.strStr('aabaacaabaaf', 'aabaaf'))
