import random

lst = [random.randint(-100-i, 100+i) for i in range(10)]

number_of_elements = 0
for i in range(1, len(lst)):
    if lst[i] < lst[i-1]:
        number_of_elements += 1

print(lst)
print(number_of_elements)