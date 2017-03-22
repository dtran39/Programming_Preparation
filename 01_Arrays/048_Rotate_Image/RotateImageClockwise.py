'''
Problem:
	-
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
----------------------------------------------------------------------------------------------------
Examples: 
Input 			Output:
 1  2  3 		 3  6  9 
 4  5  6		 2  5  8 
 7  8  9 		 1  4  7 

Input: 			Output:
 1  2  3  4  	 4  8 12 16 
 5  6  7  8  	 3  7 11 15 
 9 10 11 12  	 2  6 10 14 
13 14 15 16  	 1  5  9 13



----------------------------------------------------------------------------------------------------
Solution: 
http://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
	An N x N matrix will have floor(N/2) square cycles
	For example, a 4 X 4 matrix will have 2 cycles. 
		The first cycle is formed by its 1st row, last column, last row and 1st column. 
		The second cycle is formed by 2nd row, second-last column, second-last row and 2nd column.
	The idea is for each square cycle, we swap the elements 
		involved with the corresponding cell in the matrix 
			in anti-clockwise direction r.e. 
				from top to left, left to bottom, bottom to right and from right to top one at a time. 

Solution 2:  
	- Antidiagonal mirror: [r][c] swap with [n - 1 - c][n - 1 - r]
	- Horizontal mirror: [r][c] swap with [n - 1 - r], [c]
Solution 3:
    - reverse row, then swap the symmetry
* clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def swap(matrix, r1, c1, r2, c2):
            temp = matrix[r1][c1]
            matrix[r1][c1] = matrix[r2][c2]
            matrix[r2][c2] = temp
            size = len(matrix)
        height, width = len(matrix), len(matrix[0])
        # reverse rows
        for r in range(height / 2):
            for c in range(width):
                swap(matrix, r, c, height - r - 1, c)   
        # Swap the symmetry
        for r in range(height):
            for c in range(r):
                swap(matrix, r, c, c, r)
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        
        # anti-diagonal mirror
        for r in xrange(n):
            for c in xrange(n - r):
                matrix[r][c], matrix[n-1-c][n-1-r] = matrix[n-1-c][n-1-r], matrix[r][c]
        
        # horizontal mirror
        for r in xrange(n / 2):
            for c in xrange(n):
                matrix[r][c], matrix[n-1-r][c] = matrix[n-1-r][c], matrix[r][c]
                
        return matrix
# Time:  O(n^2)
# Space: O(n^2)
class Solution2:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]
    
if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print Solution().rotate(matrix)


'''
Problem:
    - Given a matrix, clockwise rotate elements in it. (rotate by ring)
----------------------------------------------------------------------------------------------------
Examples: 
Input
1    2    3
4    5    6
7    8    9

Output:
4    1    2
7    5    3
8    9    6

For 4*4 matrix
Input:
1    2    3    4    
5    6    7    8
9    10   11   12
13   14   15   16

Output:
5    1    2    3
9    10   6    4
13   11   7    8
14   15   16   12
----------------------------------------------------------------------------------------------------

'''
# Python program to rotate a matrix
 
# Function to rotate a matrix
def rotateMatrix(mat):
 
    if not len(mat):
        return
     
    """
        top : starting row index
        bottom : ending row index
        left : starting column index
        right : ending column index
    """
 
    top = 0
    bottom = len(mat)-1
 
    left = 0
    right = len(mat[0])-1
 
    while left < right and top < bottom:
 
        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top+1][left]
 
        # Move elements of top row one step right
        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
 
        top += 1
 
        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
 
        right -= 1
 
        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
 
        bottom -= 1
 
        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
 
        left += 1
 
    return mat