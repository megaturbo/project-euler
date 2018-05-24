#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 41.

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""
from utils import is_prime
from itertools import permutations

a = "987654321"

for n in range(9, 0, -1):
    for b in permutations(a[9 - n:], n):
        c = int(''.join(b))
        if is_prime(c):
            print(c)
            exit(0)
