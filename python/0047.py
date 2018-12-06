#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 47.

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?

"""
from math import sqrt

def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True

c = 0
for n in range(644, 650):
    c = c + 1 if is_prime(n) else 0
    if c == 3:
        print('shoot: {}'.format(n))
