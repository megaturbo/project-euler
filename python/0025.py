#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 25.

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?

"""
from math import log, ceil


def f(i):
    """Fibonacci dis shit. yieldaru index, fib(index)."""
    a = 1
    b = 0
    for x in range(i):
        yield x + 1, a
        a, b = b + a, a


for x, i in f(100000):
    if ceil(log(i, 10)) == 1000:
        break
print(x)
