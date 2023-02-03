import random

lst = [random.randint(-10-i, 10+i) for i in range(10)]

print(list(set(lst)))