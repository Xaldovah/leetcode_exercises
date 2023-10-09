#!/usr/bin/python3
"""This is the Solution class module"""


class Solution(object):
    """The champagneTower method"""
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        current_row = [poured]

        for row in range(query_row):
            next_row = [0.0] * (row + 2)
            for glass in range(len(current_row)):
                overflow = (current_row[glass] - 1.0) / 2.0
                if overflow > 0.0:
                    next_row[glass] += overflow
                    next_row[glass + 1] += overflow

            current_row = next_row

        return min(1.0, current_row[query_glass])
