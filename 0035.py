#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 35.

The number, 197, is called a circular prime because all rotations of the digits:
    197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

def is_prime(n):
    if n == 0 or n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def rotate(l, n):
    return l[-n:] + l[:-n]


sum = 0
for i in range(1000000):
    if is_prime(i):
        p = str(str(i))
        sum += 1 if all(is_prime(int(rotate(p, j)))
                        for j in range(len(p))) else 0


print(sum)
