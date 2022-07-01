class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        for str in strs:
            zeros = str.count('0')
            ones = str.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        
        return dp[m][n]

s = Solution()
print(s.findMaxForm(['10','0001','111001','1','0'], 5, 3))
print(s.findMaxForm(['10','0','1'], 1, 1))