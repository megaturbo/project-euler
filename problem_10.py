"""Project Euler - Problem 10.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from problem_7 import is_prime

sum = 0
for i in range(2000000):
    if is_prime(i):
        sum += i
print(sum)
