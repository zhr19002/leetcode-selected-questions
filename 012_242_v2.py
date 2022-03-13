class Solution:
    def isAnagram(self, s, t):
        dic_s = {}
        dic_t = {}
        for key in s:
            dic_s[key] = dic_s.get(key, 0) + 1
        for key in t:
            dic_t[key] = dic_t.get(key, 0) + 1
        
        if dic_s == dic_t:
            return True
        else:
            return False

s = Solution()
print(s.isAnagram('anagram', 'nagaram'))
print(s.isAnagram('rat', 'car'))