#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 40.

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
from functools import reduce

d = "".join(str(i) for i in range(185187))
e = (int(d[10**i]) for i in range(0, 7))
f = reduce(lambda x, y: x*y, e)
print(f)
