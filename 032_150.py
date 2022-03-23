class Solution:
    def evalRPN(self, tokens):
        stack = []
        for item in tokens:
            if item not in ['+','-','*','/']:
                stack.append(item)
            else:
                first_num = stack.pop()
                second_num = stack.pop()
                stack.append(int(eval(f'{second_num}{item}{first_num}')))
        return int(stack.pop())
    
s = Solution()
print(s.evalRPN(['2','1','+','3','*']))
print(s.evalRPN(['4','13','5','/','+']))
print(s.evalRPN(['10','6','9','3','+','-11','*','/','*','17','+','5','+']))