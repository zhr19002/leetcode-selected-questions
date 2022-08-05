class Solution:
    def nextGreaterElements(self, nums):
        result = [-1] * len(nums)
        stack = []
        for i in range(len(nums)*2):
            while len(stack) != 0 and nums[i%len(nums)] > nums[stack[-1]]:
                result[stack[-1]] = nums[i%len(nums)]
                stack.pop()
            stack.append(i%len(nums))
        return result

s = Solution()
print(s.nextGreaterElements([1,2,1]))