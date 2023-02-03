def my_func(integer, string):
    result = integer
    if string == "следующее":
        result += 1 
    elif string == "предыдущее":
        result -= 1
    else:
        print("Некорректный вызов")
    return result

print(my_func(integer=int(input("Введите число: ")), string=input("Введите строку: ")))