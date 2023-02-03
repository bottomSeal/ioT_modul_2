def precedence(operator):
    if operator == "+" or operator == "-":
        result = 1
    elif operator == "*" or operator == "/":
        result = 2
    elif operator == "^":
        result = 3
    else:
        result = -1
    return result
        
input_value = input()
if precedence(input_value) == -1:
    print("Невернный ввод")
else:
    print(precedence(input_value))