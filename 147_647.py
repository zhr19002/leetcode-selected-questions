class Solution:
    def countSubstrings(self, s):
        dp = [[False] * len(s) for i in range(len(s))]
        result = 0
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    result += 1
                    dp[i][j] = True
        
        return result

s = Solution()
print(s.countSubstrings('abc'))
print(s.countSubstrings('aaa'))