def is_prime(n):
    if n == 0 or n == 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


c = 1
i = 1
while c != 10001:
    c += int(is_prime(i))
    i += 2
print(i - 2)
