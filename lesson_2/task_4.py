import random

lst = [random.randint(-100-i, 100+i) for i in range(10)]

max_elem = lst[0]
pos = 0

for i in range(len(lst)):
    if lst[i] > max_elem:
        max_elem = lst[i]
        pos = i

print(f"Максимальный элемент: {max_elem}, его позиция: {pos + 1}")
print(lst)