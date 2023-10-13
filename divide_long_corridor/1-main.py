#!/usr/bin/python3

from divide import Solution

# Example 1
corridor1 = "SSPPSPS"
solution = Solution()
result1 = solution.numberOfWays(corridor1)
print(result1)  # Output: 3

# Example 2
corridor2 = "PPSPSP"
result2 = solution.numberOfWays(corridor2)
print(result2)  # Output: 1

# Example 3
corridor3 = "SPSPS"
result3 = solution.numberOfWays(corridor3)
print(result3)  # Output: 0
