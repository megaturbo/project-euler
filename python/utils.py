"""A few tools to facilitate project euler solving."""

from itertools import permutations


def is_prime(n):
    """
    Check if an integer is prime or not.

    :param n:   The integer to check
    :return:    True if n is prime
    """
    if n == 0 or n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def smaller_prime(n):
    """Give the biggest prime smaller than n."""
    for i in range(n, 0, -2):
        if is_prime(i):
            return i


def primes(n):
    """
    Return a generator of prime numbers.

    :param n:   The count of prime it will generate before ending
    """
    return filter(is_prime, range(1, n))


def pandigital_gen(i=1):
    """
    Return a pandigital generator.

    :param i:   The number of iteration
    :return:    An iterable pandigital generator
    """
    a = "9876543210"
    al = len(a)

    for n in range(al, al - i, -1):
        for b in permutations(a[al - n:], n):
            yield ''.join(b)
