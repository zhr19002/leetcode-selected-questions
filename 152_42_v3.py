class Solution:
    def trap(self, height):
        stack = [0]
        result = 0
        
        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while len(stack) != 0 and height[i] > height[stack[-1]]:
                    mHeight = height[stack[-1]]
                    stack.pop()
                    if len(stack) != 0:
                        rHeight = height[i]
                        lHeight = height[stack[-1]]
                        h = min(lHeight, rHeight) - mHeight
                        w = i - stack[-1] - 1
                        result += h * w
                stack.append(i)
        return result

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))