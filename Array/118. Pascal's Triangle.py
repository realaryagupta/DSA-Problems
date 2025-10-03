'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''
# solved on 10 June 2025

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        
        # init res array with just top layer of 1
        res = [[1]]

        # 
        for i in range(numRows - 1):
            prev_row = res[-1]

            # clever trick to put 0 at the first and last location of the temp (see neetcode)
            temp = [0] + prev_row + [0]

            new_row = []

            for j in range(len(prev_row) + 1):
                new_row.append(temp[j] + temp[j + 1])
            res.append(new_row)
            
        return res
