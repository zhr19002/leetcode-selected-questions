class Solution:
    def canConstruct(self, ransomNote, magazine):
        record = {}
        for i in ransomNote:
            record[i] = record.get(i, 0) + 1
        for i in magazine:
            if i in record:
                record[i] -= 1
        for key in record:
            if record[key] > 0:
                return False
        return True

s = Solution()
print(s.canConstruct('a', 'b'))
print(s.canConstruct('aa', 'ab'))
print(s.canConstruct('aa', 'aab'))
