from itertools import permutations

def is_prime(n):
    if n == 0 or n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def pandigital_gen(i = 1):
    a = "9876543210"
    al = len(a)

    for n in range(al, al - i, -1):
        for b in permutations(a[al - n:], n):
            yield ''.join(b)
