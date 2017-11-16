#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 31.

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?


note:
Trying to do it with itertools because it'd solve the whole thing.
"""

GOAL = 2.0
# odered by size, hence we can break the for-loop when we found one
pb = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0]

def do(old_sum=0.0):
    s = 0
    for p in pb:
        new_sum = old_sum + p
        if new_sum < GOAL:
            s += do(new_sum)
        elif new_sum >= GOAL:
            return s
    return s

print(do())
