'''
Problem:
	-

----------------------------------------------------------------------------------------------------
Examples: 
 	1     2     3     4
    5     6     7     8
    9    10    11    12
   13    14    15    16
   17    18    19    20
    1
    5     2
    9     6     3
   13    10     7     4
   17    14    11     8
   18    15    12
   19    16
   20
----------------------------------------------------------------------------------------------------
Solution: 
	Fact: number of diagonals = height + width - 1
	- First: print diagonal from i =  0 to height - 1:
		+ starts with r = i, c = 0
		while r >= 0 and c < width
		+ print mat[r][c]
		+ r--, i++
	- Second: print diagonal from i = 1 to width - 1:
		+ starts with r = height - 1, c = i
		while r >= 0 and c < width:
			print mat[r][c]
			r--, i++
	- Time: O(mn)
	- Space: O(1)
'''
def traverse(matrix):
	height, width = len(matrix), len(matrix[0])
	traversal = []
	# left side: depends on row
	for row_end in range(height):
		r, c = row_end, 0
		while r >= 0 and c < width:
			traversal.append(matrix[r][c])
			r, c = r - 1, c + 1
	# right side: depends on columns	
	for col_begin in range(1, width): # because first column is covered in row
		r, c = height - 1, col_begin
		while r >= 0 and c < width:
			traversal.append(matrix[r][c])
			r, c = r - 1, c + 1
	return traversal
print traverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]])