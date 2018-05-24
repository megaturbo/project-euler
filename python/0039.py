#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 39.

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""
from math import sqrt

dc = {}

bs = 0
big = 0

for p in range(1, 1001):
    s = 0
    dc[p] = []
    for a in range(1, p // 2):
        for b in range(1, p // 2):
            if a + b + sqrt(a**2 + b**2) == p  and (b, a) not in dc[p]:
                s += 1
                dc[p].append((a, b))
    if s > bs:
        bs, big = s, p
        print(p, dc[p])
print(big)
