'''
Problem:
	- Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

----------------------------------------------------------------------------------------------------
Examples: 
n = 3: You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
----------------------------------------------------------------------------------------------------
Solution: 
	Traverse: right -> down -> left -> up, until fill all
'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1: return []
        matrix = [[0] * n for i in range(n)]
        counter = 1
    	up, down, left, right = 0, n - 1, 0, n - 1
    	#
    	while up <= down and left <= right: # <= because we can traverse in one row/col
    		# Traverse right: up[left : right + 1]
    		if up <= down:
    			for i in range(left, right + 1):
    				matrix[up][i] = counter
    				counter += 1
    			up += 1
    		# Traverse down: right[up : down + 1]
    		if left <= right:
    			for i in range(up, down + 1):
    				matrix[i][right] = counter
    				counter += 1
    			right -= 1
    		# Traverse left if possible
    		if up <= down:
    			for i in range(right, left - 1, -1):
    				matrix[down][i] = counter
    				counter += 1
    		# Traverse up if possible
    		down -= 1
    		if left <= right:
    			for i in range(down, up - 1, -1):
    				matrix[i][left] = counter
    				counter += 1
    		left += 1
    	return matrix