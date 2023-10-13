#!/usr/bin/python3
"""This is the Solution class module"""


class Solution(object):
    """
    This class provides a method to calculate the number of ways to divide the corridor.
    """

    def numberOfWays(self, corridor):
        """
        Calculate the number of ways to divide the corridor.

        Args:
            corridor (str): A string representing the corridor with 'S' for seats and 'P' for plants.
            
            var a = the number of 0 seat
            var b = the number of 1 seat
            var c = the number of 2 seats

        Returns:
            int: The number of ways to divide the corridor.
        """
        MOD = 10**9 + 7

        a, b, c = 1, 0, 0

        for char in corridor:
            if char == 'S':
                a, b, c = 0, a + c, b
            else:
                a, b, c = a + c, b, c

        return c % MOD
