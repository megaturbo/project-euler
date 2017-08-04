#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 26.

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

"""

def cycle(d):
    r = 10
    i = 0
    while True:
        r = r % d * 10
        i += 1
        if r == 10:
            return i

a = 0
for d in range(2, 1000):
    # 2 and 5 multiples are never periodic
    if d % 2 != 0 and d % 5 != 0:
        b = cycle(d)
        # remember longest one and print it
        if b > a:
            a = b
            print(d)
