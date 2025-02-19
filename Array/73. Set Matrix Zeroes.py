"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify the matrix in-place such that if an element is 0,
        its entire row and column are set to 0.
        """
        n = len(matrix)
        m = len(matrix[0])

        # Use flags to determine whether the first row and column should be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(m))
        first_col_zero = any(matrix[i][0] == 0 for i in range(n))

        # Use the first row and column to mark zero rows and columns
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on flags in the first row and column
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row_zero:
            for j in range(m):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col_zero:
            for i in range(n):
                matrix[i][0] = 0
