# Process
# Initialize variables:
# Use a variable to keep the cumulative sum and a dictionary to store how many times each remainder (cumulative sum divided by k) has appeared.
# Initialize the dictionary with {0: 1} because a sum of zero is trivially divisible by k.

# Traverse the array:
# For each element, add it to the cumulative sum. Calculate the remainder when this sum is divided by k.
# Adjust the remainder to be positive.

# Check remainders:
# If this remainder has been seen before in the dictionary, it means there are subarrays that have a sum divisible by k.
# Increase the count by the number of times this remainder has been seen. Then, update the dictionary to include the current remainder.

# Return count:
# After processing the entire array, return the count of subarrays that have sums divisible by k.

# Solution
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        map = {0: 1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k
            if remainder in map:
                count += map[remainder]
                map[remainder] += 1
            else:
                map[remainder] = 1
        return count