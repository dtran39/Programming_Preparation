'''
Problem:
    -

----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution: 
1. One value stack, one min stack
    push:
        If new <= minStack.peek(): minStack.push(new)
    pop:
        if popped <= minStack.peek(): minStack.pop()
2. If keep track of a min value
    if new < min: 
        push min, push new
        update min = new    
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxint
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        popped = self.stack.pop()
        # if popped is current min, restore old min
        if popped == self.min:
            self.min = self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()