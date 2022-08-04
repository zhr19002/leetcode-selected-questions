class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = [-1] * len(nums1)
        stack = [0]
        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        result[index] = nums2[i]
                    stack.pop()
                stack.append(i)
        return result

s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
print(s.nextGreaterElement([2,4], [1,2,3,4]))