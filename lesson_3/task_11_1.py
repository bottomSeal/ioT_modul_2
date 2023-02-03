def int_func(string):
    return string[0].upper() + string[1:]  ## string.title()


value = input().split(" ")
for i in range(len(value)):
    value[i] = int_func(value[i])

print(" ".join(value))