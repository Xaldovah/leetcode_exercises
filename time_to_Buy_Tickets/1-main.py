#!/usr/bin/python3

from time_to_buy import *

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    tickets1 = [2, 3, 2]
    k1 = 2
    time1 = solution.timeRequiredToBuy(tickets1, k1)
    print(f"Time for person at position {k1} to finish buying tickets: {time1}")

    # Example 2:
    tickets2 = [5, 1, 1, 1]
    k2 = 0
    time2 = solution.timeRequiredToBuy(tickets2, k2)
    print(f"Time for person at position {k2} to finish buying tickets: {time2}")
