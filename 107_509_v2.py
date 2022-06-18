class Solution:   
    def fib(self, n):
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)

s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))