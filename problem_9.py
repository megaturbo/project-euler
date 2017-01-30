#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""Project Euler - Problem 9.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for a in range(0, 500):
    for b in range(a, 500):
        for c in range(b, 500):
            if a**2 + b**2 == c**2:
                if(a + b + c == 1000):
                    print("a = {}, b = {}, c = {}".format(a, b, c))
                    print("total: {}".format(a + b + c))
                    print("product: {}".format(a*b*c))
