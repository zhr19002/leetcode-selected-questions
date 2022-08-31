from collections import deque

class MyStack:
    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()
    
    def push(self, x):
        self.queue_in.append(x)
    
    def pop(self): #Remove the element from the queue and return that element
        if self.empty():
            return None
        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        tmp = self.queue_in
        self.queue_in = self.queue_out
        self.queue_out = tmp
        return self.queue_out.popleft()
        
    def top(self): #Get the front element
        if self.empty():
            return None
        return self.queue_in[-1]
    
    def empty(self):
        if len(self.queue_in) != 0:
            return False
        else:
            return True

if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.empty())
