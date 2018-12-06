#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 44.

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of
D?

"""
RANGE = 4000

# for easily getting pj and pk
pentlist = [n * (3 * n - 1) // 2 for n in range(1, RANGE)]
# for optmized checking
pentdict = dict.fromkeys(pentlist)

for j in range(0, RANGE // 2):
    for k in range(j + 1, RANGE - 1):
        pj = pentlist[j]
        pk = pentlist[k]
        s = pk + pj
        d = pk - pj
        if s in pentdict and d in pentdict:
            print(d)