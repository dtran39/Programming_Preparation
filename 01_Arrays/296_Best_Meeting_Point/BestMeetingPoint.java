/*
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
- Solution: https://discuss.leetcode.com/topic/27762/java-2ms-python-40ms-two-pointers-solution-no-median-no-sort-with-explanation
	- Main idea: must find a point where 
		numeber of people on its left == number people on its right
	and number oe pople on its top == number of people on its bottom
	- Explanation: 
		If we increase i by 1, the distance will increase by left 
			since there are 'left' people at i and they just move 1 step. 
		The same applies to j, when decrease j by 1, 
			the distance will increase by right. 
		To make sure the total distance d is minimized 
			we certainly want to move the point with less people.
		And to make sure we do not skip any possible meet point options we need to move one by one.
	- Algorithm:
		sum the columns and rows into two vectors
		use two pointers: 
		left and right are how many people one left/right side of coordinates i/j. 
		 	If we have more people on the left we let j decrease otherwise increase 
*/

public class Solution {
	public int minTotalDistance(int[][] grid) {
		int height = grid.length, width = grid[0].length;
		int[] num_of_people_each_row = new int[height], num_of_people_each_col = new int[width];
		// Adding to get the number of people in each row and in each col
		for (int r = 0 ; r < height; r++) {
			for (int c = 0; c < width; c++) {
				num_of_people_each_row[r] += grid[r][c];
				num_of_people_each_col[c] += grid[r][c];
			}
		}
		return minDistance(num_of_people_each_row) + minDistance(num_of_people_each_col);
	}
	private int minDistance(int[] vector) {
		int left_bound = -1, right_bound = vector.length;
		int num_left_people = 0, num_right_people = 0, total_distance = 0;
		while (left_bound != right_bound) {
			if (num_left_people < num_right_people) {
				total_distance += num_left_people;
				num_left_people += vector[++left_bound];
			} else {
				total_distance += num_right_people;
				num_right_people += vector[--right_bound];				
			}
		}
		return total_distance;
	}

}
// Runtime: 2ms