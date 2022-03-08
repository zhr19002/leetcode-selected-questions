class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        i = 0
        j = n-1
        k = n-1
        ans = [-1] * n
        while i <= j:
            lm = nums[i] ** 2
            rm = nums[j] ** 2
            if lm > rm:
                ans[k] = lm
                i += 1
            else:
                ans[k] = rm
                j -= 1
            k -= 1
        return ans

s1 = Solution()
print(s1.sortedSquares([-4,-1,0,3,10]))
s2 = Solution()
print(s2.sortedSquares([-7,-3,2,3,11]))