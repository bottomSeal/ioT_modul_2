from random import *

n = int(input())
count = 0
lst = []
for i in range(n):
    lst.append(randint(10, 20))
    if lst[i] > 15:
        count += 1
        
print(count)