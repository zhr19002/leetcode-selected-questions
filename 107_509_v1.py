class Solution:   
    def fib(self, n):
        if n < 2:
            return n
        a, b, c = 0, 1, 0
        for i in range(1, n):
            c = a + b
            a, b = b, c
        return c

s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))