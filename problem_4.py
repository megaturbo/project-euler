def p():
    q = []
    i = 999
    while i > 0:
        j = 999
        while j > 0:
            s = i * j
            if str(s) == str(s)[::-1]:
                q.append(s)
            j -= 1
        i -= 1
    return max(q)
print(p())