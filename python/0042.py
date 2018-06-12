#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Project Euler - Problem 42.

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?

"""
ts = []
twc = 0

for i in range(1, 21):
    ts.append(i * (i + 1) // 2)

with open('data/p042_words.txt') as f:
    for word in f.read()[1:-1].split('","'):
        v = 0
        for letter in word:
            v += ord(letter) - 64
        if v in ts:
            twc += 1

print(twc)
