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
    def repeatedSubstringPattern(self, s):
        if len(s) == 0:
            return False
        nxt = getNext(s)
        if nxt[-1] != 0 and len(s) % (len(s) - (nxt[-1])) == 0: 
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern('abab'))
    print(s.repeatedSubstringPattern('aba'))
    print(s.repeatedSubstringPattern('abcabcabcabc'))
