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
Trying to do it without itertools because it'd solve the whole thing.

what:
I use an array to remember how much possibilities I got for every amount. First
loop will check how many 1p possibilities for 1, 2, 3, ..., 200. So it will be
1 for each.

Then second pass will check 
"""
goal = 200
pb = [1, 2, 5, 10, 20, 50, 100, 200]
s = [1] * (goal + 1)  # init at 1 is first pass
for p in pb[1:]:
    for i in range(p, goal + 1):
        s[i] += s[i - p]
print(s[goal])
