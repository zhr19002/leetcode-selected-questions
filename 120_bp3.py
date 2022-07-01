class Solution:   
    def complete_pack(self, bag_size, weight, val):
        dp = [0] * (bag_size + 1)
        
        for i in range(len(weight)):
            for j in range(weight[i], bag_size + 1):
                dp[j] = max(dp[j], dp[j-weight[i]] + val[i])
        
        return dp

s = Solution()
print(s.complete_pack(4, [1,3,4], [15,20,30]))