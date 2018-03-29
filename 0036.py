#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 36.

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""


def is_palindome(s):
    ls = len(s)
    return all(s[i] is s[ls - i - 1] for i in range(ls // 2))


print(sum(a for a in range(1000000) if is_palindome(str(a)) and is_palindome(str(bin(a))[2:])))
