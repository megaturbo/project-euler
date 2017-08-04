def p():
    i = 20
    while True:
        b = True
        for x in range(1, 20):
            if i % x != 0:
                b = False
        if b: return i
        if i % 1000000 == 0:
            print(i)
        i += 20

print(p())