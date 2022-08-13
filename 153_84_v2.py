class Solution:
    def largestRectangleArea(self, height):
        left, right = [0] * len(height), [0] * len(height)
        
        left[0] = -1
        for i in range(1, len(height)):
            temp = i - 1
            while temp >= 0 and height[temp] >= height[i]:
                temp = left[temp]
            left[i] = temp
        
        right[-1] = len(height)
        for i in range(len(height)-2, -1, -1):
            temp = i + 1
            while temp < len(height) and height[temp] >= height[i]:
                temp = right[temp]
            right[i] = temp
        
        result = 0
        for i in range(len(height)):
            w = right[i] - left[i] - 1
            h = height[i]
            result = max(result, w * h)
        return result

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
print(s.largestRectangleArea([2,4]))