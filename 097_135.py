class Solution:   
    def candy(self, ratings):
        candyVec = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candyVec[i] = candyVec[i-1] + 1
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                candyVec[j] = max(candyVec[j], candyVec[j+1] + 1)
        return candyVec, sum(candyVec)

s = Solution()
print(s.candy([1,0,2]))
print(s.candy([1,2,2]))
print(s.candy([1,2,2,5,4,3,2]))