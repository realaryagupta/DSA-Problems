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


# Method - 2

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n is number of rows in matrix
        # m is number of colm in matrix
        n = len(matrix)
        m = len(matrix[0])

        # we will check that does the first row consist of 0 in matrix
        first_row_zero = False
        for j in range(m):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # check does the first colm consist of 0 or not
        first_col_zero = False
        for i in range(n):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # checking does the first colm contain 0 or not
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # if we get 0 from row 1 onwards or colm 1 onwards then we will replace that entire row and col with 0's
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # change for first row as well
        if first_row_zero:
            for j in range(m):
                matrix[0][j] = 0
                
        # change for first colm as well
        if first_col_zero:
            for i in range(n):
                matrix[i][0] = 0 

        return matrix
    
        