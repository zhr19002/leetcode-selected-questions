def calculate_happy(n):
    sum_ = 0
    while n:
        sum_ += (n%10) ** 2
        n = n // 10
    return sum_

class Solution:
    def isHappy(self, n):
        record = set()
        while True:
            n = calculate_happy(n)
            if n == 1:
                return True
            if n in record:
                return False
            else:
                record.add(n)

s = Solution()
print(s.isHappy(19))