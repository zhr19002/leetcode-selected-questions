class Solution:
    def maxUncrossedLines(self, A, B):
        dp = [[0] * (len(B)+1) for i in range(len(A)+1)]
        
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

s = Solution()
print(s.maxUncrossedLines([1,4,2], [1,2,4]))
print(s.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))
print(s.maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]))