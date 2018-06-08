from utils import is_prime

c = 1
i = 1
while c != 10001:
    c += int(is_prime(i))
    i += 2
print(i - 2)
