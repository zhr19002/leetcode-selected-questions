class MyQueue:
    def __init__(self):
        self.queue = []
        
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)
        
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    
    def front(self):
        return self.queue[0]
    
class Solution:
    def maxSlidingWindow(self, nums, k):
        queue = MyQueue()
        result = []
        for i in range(k):
            queue.push(nums[i])
        result.append(queue.front())
        for i in range(k, len(nums)):
            queue.pop(nums[i-k])
            queue.push(nums[i])
            result.append(queue.front())
        return result

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))