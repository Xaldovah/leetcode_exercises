#!/usr/bin/python3
"""
This is the Solution class module which has the method to
solve the min cost of making cuts in a wooden stick
"""


class Solution(object):
    """The minCost method that solves this problem"""
    def minCost(self, n, cuts):
        """
        Calculate the minimum total cost of making cuts in a wooden stick.

        Args:
            n (int): The length of the wooden stick.
            cuts (List[int]): A list of cut positions.

        Returns:
            int: The minimum total cost of making the cuts.
        """

        """Sort the cuts so that they are in ascending order"""
        cuts.sort()

        """Add the start and end points to the cuts list"""
        cuts = [0] + cuts + [n]
        m = len(cuts)

        """Initialize a 2D array to store the minimum cost"""
        dp = [[0] * m for _ in range(m)]

        """Iterate over the possible cut lengths"""
        for length in range(2, m):
            for start in range(m - length):
                end = start + length
                dp[start][end] = float('inf')
                for k in range(start + 1, end):
                    dp[start][end] = min(dp[start][end], cuts[end] - cuts[
                        start] + dp[start][k] + dp[k][end])

        """The minimum cost of cutting the stick from 0 to n"""
        return dp[0][-1]
