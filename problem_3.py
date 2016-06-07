def lpf(n):
    i = 2
    while i ** 2 < n:
        n /= i if n % i == 0 else 1
        i += 1
    return n


print(lpf(600851475143))
