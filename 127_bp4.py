class Solution:   
    def multi_pack(self, bag_size, weight, val, nums):
        for i in range(len(nums)):
            while nums[i] > 1:
                weight.append(weight[i])
                val.append(val[i])
                nums[i] -= 1
        
        dp = [0] * (bag_size + 1)
        
        for i in range(len(weight)):
            for j in range(bag_size, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-weight[i]] + val[i])
        
        return ' '.join(map(str, dp))

s = Solution()
print(s.multi_pack(10, [1,3,4], [15,20,30], [2,3,2]))