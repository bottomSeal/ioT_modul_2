numeral_dict = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть",
                7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать"}


def my_function(value):
    if value in numeral_dict.keys():
        return numeral_dict[value]
    else:
        return "Такого значения в словаре нет."

print(my_function(13))