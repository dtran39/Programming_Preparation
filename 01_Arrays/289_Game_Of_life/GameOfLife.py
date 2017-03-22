'''
Problem:
    -


Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
    Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
        using the following four rules (taken from the above Wikipedia article):
            Any live cell with fewer than two live neighbors dies, as if caused by under-population.
            Any live cell with two or three live neighbors lives on to the next generation.
            Any live cell with more than three live neighbors dies, as if by over-population..
            Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: 
    You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution: 
    Using 2 bits:
        Least significant bit represent current state
        Most significant bit represent next state
    When check to count live neighbors: 
        Check board[neighbor_r][neighbor_c] % 1 == 1
    WHen update: check next state:
        Check board[r][c] / 2 = 1

    How to find neighbors in 2d:
        Set boundary: left, right, up down
        2 nested loop: exclue board[r][c]
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # First pass: check and mark
        height, width = len(board), len(board[0])
        for r in range(height):
            for c in range(width):
                self.check_and_mark(board, r, c)
        # Second pass: check and update
        for r in range(height):
            for c in range(width):
                board[r][c] = board[r][c] / 2
    def check_and_mark(self, board, r, c):
        height, width = len(board), len(board[0])
        # Check how many live neighbors
        live_neighbors = 0
        up = r - 1 if r > 0 else r
        down = r + 1 if r < height - 1 else r
        left = c - 1 if c > 0 else c
        right = c + 1 if c < width - 1 else c
        for neighbor_r in range(up, down + 1):
            for neighbor_c in range(left, right + 1):
                if board[neighbor_r][neighbor_c] % 2 == 1 and (neighbor_r != r or neighbor_c != c):
                    live_neighbors += 1
        # Check if continue to live (2 or three live neighbors)
        if board[r][c] == 0 and live_neighbors == 3:
            board[r][c] = 2
        if board[r][c] == 1 and live_neighbors >= 2 and live_neighbors <= 3:
            board[r][c] = 3
    