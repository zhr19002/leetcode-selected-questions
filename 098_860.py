class Solution:   
    def lemonadeChange(self, bills):
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True

s = Solution()
print(s.lemonadeChange([5,5,5,10,20]))
print(s.lemonadeChange([5,5,10]))
print(s.lemonadeChange([10,10]))
print(s.lemonadeChange([5,5,10,10,20]))