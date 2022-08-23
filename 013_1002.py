class Solution:
    def commonChars(self, words):
        if not words:
            return []
        result = []
        record = 26 * [0]
        
        #Initialization with the first word
        for i in words[0]:
            record[ord(i)-ord('a')] += 1
        #Renewal with other words
        for i in range(1,len(words)):
            record_copy = 26 * [0]
            for j in range(len(words[i])):
                record_copy[ord(words[i][j])-ord('a')] += 1
            for k in range(26):
                record[k] = min(record[k], record_copy[k])

        for i in range(26):
            while record[i]:
                result.extend(chr(i+ord('a')))
                record[i] -= 1
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["bella","label","roller"]))
    print(s.commonChars(["cool","lock","cook"]))
