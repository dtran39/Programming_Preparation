'''
Problem:
	- You are given an n x n 2D matrix representing an image.
	Rotate the image by 90 degrees (anti-clockwise).

----------------------------------------------------------------------------------------------------
Examples: 
	1 2 3  	3 6 9
	4 5 6 	2 5 8
	7 8 9 	1 4 7


	1  2  3  4  	4 8 12 16
	5  6  7  8 		3 7 11 15
	9 10 11 12 		2 6 10 14
	13 14 15 16 	1 5 9  13

----------------------------------------------------------------------------------------------------
Solution: 
	for each square cycle, 
		we swap the elements involved with the corresponding cell in the matrix 
			in anti-clockwise direction i.e. f
		rom top to left, left to bottom, bottom to right and from right to top one at a time. 
		We use nothing but a temporary variable to achieve this.
'''
def swap(matrix, r1, c1, r2, c2):
	temp = matrix[r1][c1]
	matrix[r1][c1] = matrix[r2][c2]
	matrix[r2][c2] = temp
def rotate(matrix):
	size = len(matrix)
	for r in range(size):
		for c in range(r, size - r - 1):
			# Store cur
			temp = matrix[r][c]
			# Move values from right to top
			matrix[r][c] = matrix[c][size - r - 1] 
            # move values from bottom to right
			matrix[c][size - r - 1] = matrix[size - r - 1][size - c - 1]
			# move values from left to bottom
			matrix[size - r - 1][size - c - 1] = matrix[size - c - 1][r] 
			# move values from top to left
			matrix[size - 1 - c][r] = temp;
	return matrix
print rotate([[1, 2, 3], [4, 5, 6 ], [7, 8, 9]])
print rotate([[1, 2, 3, 4], [5, 6, 7, 8 ], [9, 10, 11, 12], [13, 14, 15, 16]])