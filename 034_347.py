import heapq

class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        
        pri_queue = []
        for key,value in freq.items():
            heapq.heappush(pri_queue, (value,key))
            if len(pri_queue) > k:
                heapq.heappop(pri_queue)
            
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_queue)[1]
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))
    print(s.topKFrequent([1], 1))
    print(s.topKFrequent(['a','a','a','a','b','b','b','c','c','d'], 3))
