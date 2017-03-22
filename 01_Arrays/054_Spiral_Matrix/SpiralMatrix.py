'''
Problem:
	-

----------------------------------------------------------------------------------------------------
Examples: 
Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 


Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output: 
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
----------------------------------------------------------------------------------------------------
Solution: 
	Traverse right -> down -> left (if still have row) -> up (if still have columns)
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
    	traversal = []
    	if len(matrix) == 0: return traversal
    	# Initialization
    	height, width = len(matrix), len(matrix[0])
    	up, down, left, right = 0, height - 1, 0, width - 1
    	#
    	while up <= down and left <= right: # <= because we can traverse in one row/col
    		# Traverse right: up[left : right + 1]
    		if up <= down:
    			for i in range(left, right + 1):
    				traversal.append(matrix[up][i])
    			up += 1
    		# Traverse down: right[up : down + 1]
    		if left <= right:
    			for i in range(up, down + 1):
    				traversal.append(matrix[i][right])
    			right -= 1
    		# Traverse left if possible
    		if up <= down:
    			for i in range(right, left - 1, -1):
    				traversal.append(matrix[down][i])
    		# Traverse up if possible
    		down -= 1
    		if left <= right:
    			for i in range(down, up - 1, -1):
    				traversal.append(matrix[i][left])
    		left += 1
    	return traversal
print traverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])