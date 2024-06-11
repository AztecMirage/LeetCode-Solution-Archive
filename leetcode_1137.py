# Process
# Base Cases:
# Return 0, 1, or 1 directly for n = 0, 1, or 2.

# Dynamic Programming:
# Use a list to store Tribonacci numbers up to n and calculate each number based on the previous three.

# Solution
def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]
