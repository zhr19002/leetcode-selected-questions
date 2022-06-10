class Solution:   
    def canCompleteCircuit(self, gas, cost):
        start = 0
        cur_sum = 0
        total_sum = 0
        
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if cur_sum < 0:
                cur_sum = 0
                start = i + 1
        if total_sum < 0:
            return -1
        return start

s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(s.canCompleteCircuit([2,3,4], [3,4,3]))