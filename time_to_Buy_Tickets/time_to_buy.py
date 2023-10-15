#!/usr/bin/python3

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        Calculate the time taken for the person at position k to finish buying tickets.

        Args:
            tickets (list of int): A list of integers representing the number of tickets each person wants.
            k (int): The position of the person you want to measure the time for (0-indexed).

        Returns:
            int: The time taken for the person at position k to finish buying tickets.
        """
        n = len(tickets)
        time = 0

        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                    if i == k and tickets[i] == 0:
                        return time
        return time
