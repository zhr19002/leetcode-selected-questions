class Solution:
    def largestRectangleArea(self, height):
        height.insert(0, 0)
        height.append(0)
        stack = [0]
        result = 0
        
        for i in range(1, len(height)):
            if height[i] > height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while len(stack) != 0 and height[i] < height[stack[-1]]:
                    mid = stack[-1]
                    stack.pop()
                    if len(stack) != 0:
                        right = i
                        left = stack[-1]
                        w = right - left - 1
                        h = height[mid]
                        result = max(result, w * h)
                stack.append(i)
        return result

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
print(s.largestRectangleArea([2,4]))