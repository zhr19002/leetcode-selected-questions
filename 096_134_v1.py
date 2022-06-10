class Solution:   
    def canCompleteCircuit(self, gas, cost):
        cur_sum = 0
        min_sum = float('inf')
        
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            min_sum = min(min_sum, cur_sum)
        
        if cur_sum < 0:
            return -1
        if min_sum >= 0:
            return 0
        
        for j in range(len(gas)-1, 0, -1):
            min_sum += gas[j] - cost[j]
            if min_sum >= 0:
                return j
        return -1

s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(s.canCompleteCircuit([2,3,4], [3,4,3]))