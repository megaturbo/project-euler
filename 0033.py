#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 33.

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.

"""
from functools import reduce
from fractions import Fraction

f = [1, 1]
for a in range(10, 100):
    # ignore trivial cases
    if a % 10 is 0:
        continue
    for b in range(a + 1, 100):
        sa, sb = str(a), str(b)
        if sa[-1:] == sb[:1] and sb[1:] != "0" and a / b == int(sa[:1]) / int(sb[-1:]):
            f[0] *= a
            f[1] *= b


print(Fraction(f[0], f[1]).denominator)
