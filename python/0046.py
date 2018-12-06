#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 46.

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?

"""
from utils import is_prime
from math import sqrt


def _is_cool(ocn, k):
    return is_prime(k) and sqrt((ocn - k) / 2).is_integer()


RANGE = 150

for i in range(3, RANGE, 2):
    for j in range(i, RANGE, 2):
        ocn = i * j
        if not any(_is_cool(ocn, k) for k in range(ocn - 2, 0, -2)):
            print("fuck at {}".format(ocn))
