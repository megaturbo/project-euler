#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 21.

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
from math import sqrt


def d(n):
    """Sum alla dee properu divisors."""
    d = 0
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            d += i
            if i != n / i and n != n / i:
                d += n / i
    return d


s = 0
for a in range(1, 10000):
    b = d(a)
    if d(b) == a and a != b:
        s += a
print(s)
