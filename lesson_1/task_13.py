input_value = int(input())

num_divisors = 0
for i in range (1, int(input_value**0.5)+1):
    if input_value % i == 0:
        print(input_value // i, i)
        num_divisors += 2
print(num_divisors)