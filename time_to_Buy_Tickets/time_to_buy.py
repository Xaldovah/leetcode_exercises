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
        queue = [(tickets[i], i) for i in range(n)]
        time = 0

        while True:
            max_tickets, max_pos = max(queue)
            if max_pos == k and max_tickets == 0:
                return time
            time += 1

            if max_tickets > 0:
                queue.remove((max_tickets, max_pos))
                queue.append((max_tickets - 1, max_pos))
            else:
                queue.remove((0, max_pos))
