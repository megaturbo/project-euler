#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 30.

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

"""
from itertools import product

s = 0   # sum
p = 5   # power
for numbers in product('0123456789', repeat=p+1): # i don't know the exact limit
    a = sum(int(n)**p for n in numbers)
    if a == int("".join(numbers)) and a > 1:
        s += a
print(s)
