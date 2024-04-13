#!/usr/bin/env python3
"""Returns the largest string x such that x divides both str1 and str2
"""

class Solution:
    """Solution class
    """

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        For two strings s and t, we say 't divides s' if and only if
        s = t + t + t + ... + t + t (i.e., t is concatenated with itself
        one or more times).
        """
        if str1 + str2 != str2 + str1:
            return ""
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]

# Test cases
solution = Solution()

str1 = "ABCABC"
str2 = "ABC"
print(solution.gcdOfStrings(str1, str2))  # Output: "ABC"

str1 = "ABABAB"
str2 = "ABAB"
print(solution.gcdOfStrings(str1, str2))  # Output: "AB"

str1 = "LEET"
str2 = "CODE"
print(solution.gcdOfStrings(str1, str2))  # Output: ""
