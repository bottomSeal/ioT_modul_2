import random

tup = tuple([random.randint(-100-i, 100+i) for i in range(11)])
print(tup)

if len(tup) > 10:
    for i in range(3, 10):
        print(tup[i], end=" ")