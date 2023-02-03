import random

lst = [random.randint(-100-i, 100+i) for i in range(10)]

for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

print(lst)