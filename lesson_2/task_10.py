import random

lst = [random.randint(-100-i, 100+i) for i in range(10)]
print(lst)

lst[0], lst[-1] = lst[-1], lst[0]

print(lst)