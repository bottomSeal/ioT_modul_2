from random import *

lst_1 = [randint(1, 100) for i in range(10)]
lst_2 = lst_1.copy()
shuffle(lst_2)
count = 0
for i in range(len(lst_1)):
    if lst_1[i] == lst_2[i]:
        count += 1
print(lst_1)
print(lst_2)
print(count)