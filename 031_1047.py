class Solution:
    def removeDuplicates(self, s):
        stack = []
        for item in s:
            if stack and stack[-1] == item:
                stack.pop()
            else:
                stack.append(item)
        return ''.join(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates('abbaca'))
