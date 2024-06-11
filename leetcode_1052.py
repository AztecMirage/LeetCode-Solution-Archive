# Process
# Credits: https://leetcode.com/u/Hai_dee/

# The first involves counting how many customers are already satisfied, i.e. those where the shopkeeper is not grumpy. I also set any slots with already satisfied customers to 0, so that we will be left with only the currently unsatisfied customers in the list.
# For the second part, the array now only contains customers who will not be satisfied.
# We are able to make X adjacent times “happy”, so we want to find the subarray of length X that has the most customers.
# We can just keep a rolling sum of the last X customers in the array, and then the best solution is the max the rolling sum ever was.
# Finally we return the sum of the 2 parts: the customers who were already satisfied, and the maximum number who can be made satisfied by stopping the shop keeper from being grumpy for X time.
# Note that both parts can be combined into a single loop, but I felt this way was probably easier for understanding, and both are still O(n) time.

# Solution
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        already_satisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
                customers[i] = 0
        we_can = 0
        current = 0
        for i, totalcus in enumerate(customers):
            current += totalcus
            if i >= X:
                current -= customers[i - X]
            we_can = max(we_can, current)
        
        return already_satisfied + we_can