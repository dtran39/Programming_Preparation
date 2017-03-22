'''
Problem:
	- Given a stream of integers and a window size
        , calculate the moving average of all integers in the sliding window.

----------------------------------------------------------------------------------------------------
Examples:
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
----------------------------------------------------------------------------------------------------
Solution:
1. Ideas
	- Use append in python because O(1) complexity
	- Use len in python because O(1) comlexity
	- Don't use insert and delete (because O(n))
2. Solution:
	- Compare length of current arrays with maxSize:
		+ If length of num list is less than maxSize: append, else use ptr
		+ Memory is always optimized (only append memory when needed to)
	- Use curSum, so the sum of the elements besides the added element
		is cached and don't need to compute over and over (really improve performance when size is big)
'''
class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = []
    	self.maxSize = size
    	self.ptr = 0 # ptr to next available position
    	self.curSum = 0
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
    	# Put new elements to list
    	if len(self.nums) < self.maxSize:
    		self.nums.append(val)
    	else:
    		self.curSum -= self.nums[self.ptr] # If there is already an element: subtract its value from curSum
    		self.nums[self.ptr] = val
    	# add new elements to sum
    	self.curSum += val
    	self.ptr = (self.ptr + 1 ) % self.maxSize
    	return self.curSum * 1.0 / len(self.nums)

    # Your MovingAverage object will be instantiated and called as such:
    # obj = MovingAverage(size)
    # param_1 = obj.next(val)
