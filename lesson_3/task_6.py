def is_primary(value):
    num_of_div = 0
    result = False
    for _ in range(1, int(value**0.5)+1):
        if value % _ == 0:
            num_of_div += 1
    if num_of_div == 1:
        result = True
    return result


n = int(input())
primary_list = []
n_numbers = 0
i = 0
while n_numbers < n:
    if is_primary(i):
        primary_list.append(i)
        n_numbers += 1
    i += 1
print(primary_list)