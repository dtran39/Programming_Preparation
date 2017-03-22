'''
Problem:
    -
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
----------------------------------------------------------------------------------------------------
Examples: 
Example:
    X..X
    ...X
    ...X
In the above board there are 2 battleships.
----------------------------------------------------------------------------------------------------
Solution: 
    - Loop through each cell:
        + If found a cell with 'X': increase count
        + If cell on the left or above has 'X': -> already count -> decrease count
'''
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    count += 1
                    # Track up and left (if has X -> this ship is already counted)
                    if (r > 0 and board[r - 1][c] == 'X') or (c > 0 and board[r][c - 1] == 'X'):
                        count -= 1
        return count