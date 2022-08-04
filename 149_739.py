class Solution:
    def dailyTemperatures(self, temp):
        result = [0] * len(temp)
        stack = [0]
        for i in range(1, len(temp)):
            if temp[i] <= temp[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and temp[i] > temp[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return result

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))