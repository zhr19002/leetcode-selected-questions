class Solution:   
    def uniquePaths(self, m, n):
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]

s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(2, 3))
print(s.uniquePaths(7, 3))
print(s.uniquePaths(3, 3))