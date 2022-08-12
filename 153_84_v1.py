class Solution:
    def largestRectangleArea(self, height):
        result = 0
        for i in range(len(height)):
            left = i
            right = i
            for j in range(left, -1, -1):
                if height[left] < height[i]:
                    break
                left -= 1
            for k in range(right, len(height)):
                if height[right] < height[i]:
                    break
                right += 1
            w = right - left - 1
            h = height[i]
            result = max(result, w * h)
        return result

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
print(s.largestRectangleArea([2,4]))