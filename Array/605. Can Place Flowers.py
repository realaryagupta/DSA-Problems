"""
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
 
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Initialize a counter to track the number of flowers that can be planted
        count = 0
        # Get the length of the flowerbed
        length = len(flowerbed)
        
        # Iterate through each plot in the flowerbed
        for i in range(length):
            # Check if the current plot is empty and its neighbors are also empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1  # Place a flower
                count += 1  # Increment the count of planted flowers
                
            # If the required number of flowers is already planted, return True
            if count >= n:
                return True
        
        # Return whether the required number of flowers can be planted
        return count >= n