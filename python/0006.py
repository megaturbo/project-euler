sosq = 0
sqso = 0
for i in range(1, 101):
    sosq += i ** 2
    sqso += i
sqso **= 2
print(sqso - sosq)
