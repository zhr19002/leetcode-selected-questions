class Solution:
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]
        
        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

s = Solution()
print(s.longestCommonSubsequence('abcde', 'ace'))
print(s.longestCommonSubsequence('abc', 'abc'))
print(s.longestCommonSubsequence('abc', 'def'))