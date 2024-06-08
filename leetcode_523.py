# Process
# Check for special case:
# If k is zero, look for two consecutive zeros in the array. If found, return true.

# Initialize variables:
# Use a variable to keep track of the cumulative sum of elements as you traverse the array.
# Also, use a dictionary to store the remainder of the cumulative sum when divided by k and the corresponding index.

# Traverse the array:
# For each element, add it to the cumulative sum.
# Calculate the remainder when this sum is divided by k.

# Check remainders:
# If this remainder has been seen before and the distance between the current index and the stored index is greater than one, return true (indicating a valid subarray is found).
# Otherwise, store the remainder and index in the dictionary.

# Return result: If no valid subarray is found, return false.

# Solution
class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder_dict = {0: -1}
        cumulative_sum = 0

        for i, num in enumerate(nums):
            cumulative_sum += num
            if k != 0:
                cumulative_sum %= k
            
            if cumulative_sum in remainder_dict:
                if i - remainder_dict[cumulative_sum] > 1:
                    return True
            else:
                remainder_dict[cumulative_sum] = i

        return False