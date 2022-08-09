class Solution:
    def trap(self, height):
        lHeight, rHeight = [0] * len(height), [0] * len(height)
        
        lHeight[0] = height[0]
        for i in range(1, len(height)):
            lHeight[i] = max(lHeight[i-1], height[i])
        rHeight[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            rHeight[i] = max(rHeight[i+1], height[i])
        
        result = 0
        for i in range(len(height)):
            h = min(lHeight[i], rHeight[i]) - height[i]
            if h > 0:
                result += h
        return result

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))