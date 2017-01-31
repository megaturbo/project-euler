#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""Euler Project - Problem 15.

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""

n = 20

g = [[1 for x in range(n + 1)] for y in range(n + 1)]

for y in range(n + 1):
    for x in range(n + 1):
        if x != 0 and y != 0:
            g[y][x] = g[y - 1][x] + g[y][x - 1]

print(g[n][n])
