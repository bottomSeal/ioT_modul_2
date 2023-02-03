__name__ = "module_1"

def is_integer(number):
    result = True
    if number != int(number):
        result = False
    return result