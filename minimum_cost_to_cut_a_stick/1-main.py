#!/usr/bin/python3

from minimum_cost import Solution

n1 = 7
cuts1 = [1, 3, 4, 5]
solution = Solution()
result1 = solution.minCost(n1, cuts1)
print(result1)

n2 = 9
cuts2 = [5, 6, 1, 4, 2]
result2 = solution.minCost(n2, cuts2)
print(result2)
