# The enumerate function in Python is a built-in function that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object.
# This object can then be used directly in for loops to retrieve both the index and the value of each item in the iterable simultaneously.

# Example of enumerate:

# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")

# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

#Solution
class Solution:
    def searchInsert(self, nums, target):
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)
