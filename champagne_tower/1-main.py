#!/usr/bin/python3

from champagne_tower import Solution

# Create an instance of the Solution class
solution = Solution()

poured = 1
query_row = 1
query_glass = 1
result = solution.champagneTower(poured, query_row, query_glass)
print(f"Champagne in glass ({query_row}, {query_glass}): {result}")

poured = 2
query_row = 1
query_glass = 1
result = solution.champagneTower(poured, query_row, query_glass)
print(f"Champagne in glass ({query_row}, {query_glass}): {result}")

poured = 100000009
query_row = 33
query_glass = 17
result = solution.champagneTower(poured, query_row, query_glass)
print(f"Champagne in glass ({query_row}, {query_glass}): {result}")
