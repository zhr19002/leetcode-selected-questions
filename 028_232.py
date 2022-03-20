class MyQueue:
    def __init__(self):
        self.stack_in = [] #For push operation
        self.stack_out = [] # For pop operation
    
    def push(self, x):
        self.stack_in.append(x)
    
    def pop(self): #Remove the element from the queue and return that element
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        
    def peek(self): #Get the front element
        ans = self.pop()
        self.stack_out.append(ans)
        return ans
    
    def empty(self):
        if self.stack_in or self.stack_out:
            return False
        else:
            return True

queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())