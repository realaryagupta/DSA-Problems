"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to a very large value
        min_price = float('inf') 
        # Initialize the maximum profit to 0
        max_profit = 0 
        
        # Iterate through each price in the list
        for price in prices:
            # Update the minimum price if the current price is lower
            min_price = min(min_price, price)
            # Update the maximum profit if selling at the current price yields a higher profit
            max_profit = max(max_profit, price - min_price)
        
        # Return the maximum profit
        return max_profit