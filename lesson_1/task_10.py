input_value = int(input())

high_bit = input_value // 100 + input_value // 10 % 10
low_bit = input_value // 10 % 10 + input_value % 10

if high_bit > low_bit:
    print(str(high_bit) + str(low_bit))
else:
    print(str(low_bit) + str(high_bit))