#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 23.

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

"""
from math import sqrt

MAX = 20162  # real maximum


def d(n):
    """Sum alla dee properu divisors."""
    d = 0
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            d += i
            if i != n / i and n != n / i:
                d += n / i
    return d


# create every abundant numbers
abundant = [i for i in range(MAX) if d(i) > i]

# retain every possible sum of two abundant number
canbe = set()
for a in abundant:
    for b in abundant:
        canbe.add(a + b)

# sum every number which is not a sum of two abundant numbers
s = sum([i for i in range(MAX) if i not in canbe])
print(s)
