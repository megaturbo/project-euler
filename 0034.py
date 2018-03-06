#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 34.

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""
from math import factorial as f

for i in range(3, 100000):
    s = 0
    for j in str(i):
        s += f(int(j))
    if s == i:
        print(s)
