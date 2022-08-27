class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.reverseString(['h','e','l','l','o']))
    print(s.reverseString(['H','a','n','n','a','h']))
