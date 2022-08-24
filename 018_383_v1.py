class Solution:
    def canConstruct(self, ransomNote, magazine):
        record = 26 * [0]
        for i in magazine:
            record[ord(i) - ord('a')] += 1
        for i in ransomNote:
            if record[ord(i) - ord('a')]:
                record[ord(i) - ord('a')] -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct('a', 'b'))
    print(s.canConstruct('aa', 'ab'))
    print(s.canConstruct('aa', 'aab'))
