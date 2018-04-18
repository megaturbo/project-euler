#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 32.

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

"""
s = 0
b = set()
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(9999):
    for j in range(9999):
        k = i * j
        l = sorted(str(i) + str(j) + str(k))
        if len(l) > 9:
            break
        if a == l and k not in b:
            b.add(k)
            s += k

print(s)
