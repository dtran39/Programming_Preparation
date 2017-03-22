'''
Problem:
	-

----------------------------------------------------------------------------------------------------
Examples: 
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
----------------------------------------------------------------------------------------------------
Solution: 
	Do DFS with visited list:
		+ If found a number 1 unvisited: we found one more island
		+ Increment counter
		+ Explore all of the cell in that island, add to visited list
'''
class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
    	# Invalid case
        if not grid: return 0
		# Initialization
        height, width = len(grid), len(grid[0])    
        visited = [[False for c in xrange(width)] for r in xrange(height)]
        numOfIslands = 0
        # Looping
        for r in xrange(height):
            for c in xrange(width):
                if grid[r][c] == '1' and not visited[r][c]:
                    self.dfs(grid, visited, r, c)
                    numOfIslands += 1
        return numOfIslands
    def dfs(self, grid, visited, r, c):
        def checkIsOutOfBound(grid, r, c):
        	height, width = len(grid), len(grid[0])
         	return r < 0 or r >= height or c < 0 or c >= width
    	# If the cell is not a valid cell with value 1: skip
    	if checkIsOutOfBound(grid, r, c) or grid[r][c] == '0' or visited[r][c]:
    		return
    	visited[r][c] = True
    	# Call its neighbor
     	self.dfs(grid, visited, r - 1, c)
    	self.dfs(grid, visited, r + 1, c)
    	self.dfs(grid, visited, r, c - 1)
        self.dfs(grid, visited, r, c + 1)    	    	
