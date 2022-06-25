class Solution:   
    def bag_problem_2d(self, bag_size, weight, val):
        dp = [[0 for j in range(bag_size + 1)] for i in range(len(weight))]
        
        for i in range(len(weight)):
            dp[i][0] = 0
        for j in range(1, bag_size + 1):
            if j >= weight[0]:
                dp[0][j] = val[0]
                
        for i in range(1, len(weight)):
            for j in range(1, bag_size + 1):
                if j < weight[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + val[i])
        
        return dp

s = Solution()
print(s.bag_problem_2d(4, [1,3,4], [15,20,30]))