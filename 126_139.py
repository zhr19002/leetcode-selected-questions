class Solution:   
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word):
                    tmp = dp[i - len(word)] and word == s[i - len(word):i]
                    dp[i] = dp[i] or tmp
        
        return dp[len(s)]

s = Solution()
print(s.wordBreak('leetcode', ['leet','code']))
print(s.wordBreak('applepenapple', ['apple','pen']))
print(s.wordBreak('catsandog', ['cats','dog','sand','and','cat']))