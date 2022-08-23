class Solution:
    def isAnagram(self, s, t):
        record = 26 * [0]
        for i in range(len(s)):
            record[ord(s[i])-ord('a')] += 1
        for i in range(len(t)):
            record[ord(t[i])-ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
                break
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram('anagram', 'nagaram'))
    print(s.isAnagram('rat', 'car'))
