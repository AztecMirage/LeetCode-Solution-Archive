# Process
# Sort the array:
# Create a copy of the array and sort it to get the expected order of heights.

# Compare arrays:
# Compare each element in the original array with the sorted array.

# Count differences:
# Count how many elements in the original array do not match with the sorted array at the same position.

# Return count:
# This count represents the number of students who are out of order.

# Solution
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Step 1: Create the expected array by sorting the heights array
        expected = sorted(heights)
        
        # Step 2: Count the mismatches between heights and expected
        mismatch_count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count += 1
                
        return mismatch_count