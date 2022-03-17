def trim_head_space(s):
    p = 0
    while p < len(s) and s[p] == ' ':
        p += 1
    return s[p:]

class Solution:
    def reverseWords(self, s):
        # Trim the head and tail space
        s = trim_head_space(s)
        s = trim_head_space(s[::-1])[::-1]
        
        # Reverse the string
        fast = 0
        slow = 0
        s = s[::-1]
        while fast < len(s):
            if s[fast] == ' ':
                if s[fast] == s[fast+1]:
                    s = s[:fast] + s[fast+1:]
                    continue
                else:
                    s = s[:slow] + s[slow:fast][::-1] + s[fast:]
                    slow = fast + 1
                    fast = fast + 2
            else:
                fast += 1
        
        return s[:slow] + s[slow:][::-1]

s = Solution()
print(s.reverseWords('the sky is blue'))
print(s.reverseWords(' hello world!'))
print(s.reverseWords('a good  example'))