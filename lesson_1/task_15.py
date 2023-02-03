a = int(input())
b = int(input())

result = a
day = 1
while result < b:
    result *= 1.1
    day += 1

print(day - 1)

