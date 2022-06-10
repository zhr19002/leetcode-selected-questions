class Solution:   
    def largestSumAfterKNegations(self, A, K):
        A = sorted(A, key=abs, reverse=True)
        for i in range(len(A)):
            if K > 0 and A[i] < 0:
                A[i] *= -1
                K -= 1
        if K > 0:
            A[-1] *= (-1)**K
        return sum(A)

s = Solution()
print(s.largestSumAfterKNegations([4,2,3], 1))
print(s.largestSumAfterKNegations([3,-1,0,2], 3))
print(s.largestSumAfterKNegations([2,-3,-1,5,-4], 2))