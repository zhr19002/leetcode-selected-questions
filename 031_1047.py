class Solution:
    def removeDuplicates(self, s):
        stack = []
        for item in s:
            if stack and stack[-1] == item:
                stack.pop()
            else:
                stack.append(item)
        return ''.join(stack)
    
s = Solution()
print(s.removeDuplicates('abbaca'))