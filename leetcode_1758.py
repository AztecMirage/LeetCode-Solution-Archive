# Process
# Two Patterns:
# Create two patterns: "010101..." and "101010..." based on the length of s.

# Count Mismatches:
# Count the number of mismatches for each pattern.

# Return Minimum Mismatches:
# Return the minimum count of mismatches from the two patterns.

# Solution
def minOperations(s):
    n = len(s)
    
    pattern1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(n)])
    pattern2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(n)])
    
    mismatch1 = sum(1 for i in range(n) if s[i] != pattern1[i])
    mismatch2 = sum(1 for i in range(n) if s[i] != pattern2[i])
    
    return min(mismatch1, mismatch2)
