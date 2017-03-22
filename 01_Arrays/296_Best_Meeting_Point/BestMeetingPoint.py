# 
'''
- Problem:
A group of two or more people wants to meet and minimize the total travel distance. 
You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. 
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
----------------------------------------------------------------------------------------------------------------------------------
- Examples
For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.
-------------------------------------------------------------------------------------------------------------------------
- Solution: https://discuss.leetcode.com/topic/27762/java-2ms-python-40ms-two-pointers-solution-no-median-no-sort-with-explanation
	- Main idea: must find a point where 
		numeber of people on its left == number people on its right
	and number oe pople on its top == number of people on its bottom
	- Explanation: If there are more people on the left than on the right, 
		then moving left will make the total distance smaller (nearer for left people)
	- Algorithm:
		



Before solving the 2D problem we first consider a 1D case. 
	The solution is quite simple. Just find the median of all the x coordinates and calculate the distance to the median.
	Alternatively, we can also use two pointers to solve the 1D problem. 
		left and right are how many people one left/right side of coordinates i/j. 
		If we have more people on the left we let j decrease otherwise increase i. 
		The time complexity is O(n) and space is O(1).
	To be more clear, a better view is we can think i and j as two meet points. 
		All the people in [0, i] go to meet at i and all the people in [j, n - 1] meet at j. 
		We let left = sum(vec[:i+1]), right = sum(vec[j:]), which are the number of people at each meet point, 
			and d is the total distance for the left people meet at i and right people meet at j.
Our job is to let i == j with minimum d.

If we increase i by 1, the distance will increase by left since there are 'left' people at i and they just move 1 step. The same applies to j, when decrease j by 1, the distance will increase by right. To make sure the total distance d is minimized we certainly want to move the point with less people. And to make sure we do not skip any possible meet point options we need to move one by one.

For the 2D cases we first need to sum the columns and rows into two vectors and call the 1D algorithm.
The answer is the sum of the two. The time is then O(mn) and extra space is O(m+n)
'''
class Solution:
	def minTotalDistance(self, grid):
	    row_sum = map(sum, grid)
	    col_sum = map(sum, zip(*grid)) # syntax sugar learned from stefan :-)

	    def minTotalDistance1D(vec):
	        i, j = -1, len(vec)
	        d = left = right = 0
	        while i != j:
	            if left < right:
	                d += left
	                i += 1
	                left += vec[i]
	            else:
	                d += right
	                j -= 1
	                right += vec[j]
	        return d

	    return minTotalDistance1D(row_sum) + minTotalDistance1D(col_sum)
