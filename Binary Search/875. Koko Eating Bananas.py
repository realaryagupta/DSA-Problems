"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours. 

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Helper function to determine if a given speed is feasible
        def feasible(speed) -> bool:
            # Calculate the total number of hours required to eat all piles at the given speed
            # Using (pile - 1) // speed + 1 is a faster way to compute ceil(pile / speed)
            return sum((pile - 1) // speed + 1 for pile in piles) <= H

        # Initialize the search range for the eating speed
        # Left boundary: minimum possible speed (1 banana per hour)
        # Right boundary: maximum possible speed (eat the largest pile in one hour)
        left, right = 1, max(piles)

        # Perform binary search to find the minimum feasible speed
        while left < right:
            # Calculate the middle point of the current range
            mid = left + (right - left) // 2

            # Check if the current speed is feasible
            if feasible(mid):
                # If feasible, try a smaller speed (move the right boundary)
                right = mid
            else:
                # If not feasible, try a larger speed (move the left boundary)
                left = mid + 1

        # The smallest feasible speed is found when left == right
        return left