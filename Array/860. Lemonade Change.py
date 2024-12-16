"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Example 1:
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:
Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
"""

class Solution:    
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Initialize counters for $5 and $10 bills
        five_note_count = 0
        ten_note_count = 0

        # Iterate through each bill received
        for bill in bills:
            # If the bill is $5, simply increment the $5 counter
            if bill == 5:
                five_note_count += 1
                
            # If the bill is $10, check if we have a $5 bill to give change
            elif bill == 10:
                if five_note_count == 0:
                    return False
                five_note_count -= 1
                ten_note_count += 1

            # If the bill is $20, check if we can give change using $10 and $5, or three $5 bills
            elif bill == 20:
                if ten_note_count >= 1 and five_note_count >= 1:
                    ten_note_count -= 1
                    five_note_count -= 1
                elif five_note_count >= 3:
                    five_note_count -= 3
                else:
                    return False

            # Check if any count is negative, which would mean we cannot provide exact change
            if five_note_count < 0 or ten_note_count < 0:
                return False

        # If all transactions are successful, return True
        return True