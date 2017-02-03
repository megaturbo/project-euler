"""
Project Euler - Problem 67.

Like problem 18, but not bruteforceable

"""
import copy

a = []
with open('data/p067_triangle.txt') as f:
    for l in f.readlines():
        a.append([])
        for p in l.replace('\n', '').split(' '):
            a[len(a) - 1].append(int(p))

s = [a[0][0]]
for h in range(1, len(a)):
    so = copy.deepcopy(s)
    for i in range(len(a[h])):
        if i == 0:
            s[0] += a[h][0]
        elif i == len(a[h]) - 1:
            s.append(so[i - 1] + a[h][i])
        else:
            s[i] = max(so[i-1], so[i]) + a[h][i]

print(max(s))
