class Solution:
    def trap(self, height):
        result = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            lHeight = height[i-1]
            rHeight = height[i+1]
            for j in range(i-1):
                if height[j] > lHeight:
                    lHeight = height[j]
            for k in range(i+2, len(height)):
                if height[k] > rHeight:
                    rHeight = height[k]
            h = min(lHeight, rHeight) - height[i]
            if h > 0:
                result += h
        return result

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))