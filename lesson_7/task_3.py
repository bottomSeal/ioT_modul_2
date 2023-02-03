input_value = input()
start_from_black = ['a', 'c', 'e', 'g']
if input_value[0] in start_from_black:
    ceil = int(input_value[1]) % 2
else:
    ceil = (int(input_value[1]) + 1) % 2

if ceil == 1:
    print("black")
else:
    print("white")