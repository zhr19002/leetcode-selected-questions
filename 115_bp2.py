class Solution:   
    def bag_problem_1d(self, bag_size, weight, val):
        dp = [0] * (bag_size + 1)
        
        for i in range(len(weight)):
            for j in range(bag_size, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-weight[i]] + val[i])
        
        return dp

s = Solution()
print(s.bag_problem_1d(4, [1,3,4], [15,20,30]))